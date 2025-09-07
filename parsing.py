from bs4 import BeautifulSoup
import pandas as pd
import requests
import lxml
import json
import time
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
import atexit


class Parsingweb:
    # url address
    # data parsed info with slovar
    # soup soup object
    # html_content content parsed   
    # selectors slovar to save css selectors

        


    def __init__(self, url, selectors):
            self.url = url
            self.selectors = selectors
            self.data = []
            service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service)
            atexit.register(self.close_driver)  # Автоматическое закрытие драйвера
            self.driver.get(url)
            time.sleep(3)
            parameter = "578"
            select_element = self.driver.find_element(By.ID, "dnn_ctr1300_TimeTableView_ClassesList")
            select = Select(select_element)
            select.select_by_value(parameter)


            time.sleep(5)
            self.driver.execute_script(f"setTimeout('__doPostBack(\"dnn$ctr1300$TimeTableView$btnChangesTable\", \"\")',0)")
            time.sleep(5)

            

    def parsetable(self):
        try:
            table = self.driver.find_element(By.CSS_SELECTOR, self.selectors['table'])
            rows = table.find_elements(By.CSS_SELECTOR, self.selectors['rows'])

            for row in rows:
                cells = row.find_elements(By.CSS_SELECTOR, self.selectors['cells'])
                self.data.append([cell.text for cell in cells])  # Сохраняем текст ячеек

            self.data = json.dumps(self.data)
            self.data = json.loads(self.data)

        except Exception as e:
            print(f"Ошибка при парсинге таблицы: {e}")

    def close_driver(self):
        if self.driver:
            self.driver.quit()
    

    
    @staticmethod
    def parse_school_csv(file_path):
        try:
            # Load the CSV file
            data = pd.read_csv(file_path, header=None)

            # Extract relevant rows and columns
            month_row = data.iloc[0]  # Month is in the first row
            day_row = data.iloc[4]    # Days are in row E (fifth row, index 4)

            # Extract month and propagate downward
            months = month_row.fillna(method="ffill")

            # Create a DataFrame for the dates and events
            events_data = data.iloc[5:]  # Events start from row F onwards
            events_data.columns = ["Month", "Day"] + list(data.columns[2:])  # Add headers

            # Combine month and day information
            events_data["Month"] = months
            events_data["Day"] = day_row

            # Filter holidays and exams based on your needs
            holidays = events_data[~events_data.iloc[:, -1].isna()]  # Assuming holidays are in the last column
            exams = events_data[~events_data.iloc[:, -2].isna()]     # Assuming exams are in the second-to-last column

            # Convert to dictionaries
            holidays_dict = holidays.to_dict(orient="records")
            exams_dict = exams.to_dict(orient="records")

            # Print results
            print("Holidays:")
            print(holidays_dict)
            print("\nExam Dates:")
            print(exams_dict)

            return holidays_dict, exams_dict

        except Exception as e:
            print(f"Error processing the CSV file: {e}")
            return None, None













if __name__ == '__main__':
    selectors = {'table': ".TTTable", 'rows': "tr", 'cells': ".TTCell"}
    url = "https://amalb.iscool.co.il/default.aspx"
    parsingweb = Parsingweb(url, selectors)
    
    parsingweb.parsetable()
    print(parsingweb.data)

    # Parse the table from the webpage
    
    
    # Parse data from a CSV file
    #holidays, exams = Parsingweb.parse_school_csv(file_path='school.csv')
