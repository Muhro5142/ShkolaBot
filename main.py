import parsing
import info2table
import telebot


TOKEN = "YOUR TOKEN HERE"


bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    parsingweb = parsing.Parsingweb(url, selectors)
    parsingweb.parsetable()
    #info2table.create_table_from_data(parsingweb.data)
    for i in range(len(parsingweb.data)):
        if not any(parsingweb.data[i]):
            continue
        text = str(parsingweb.data[i]).replace('\\', '     |      ')
        bot.reply_to(message,i)
        bot.reply_to(message, text,parse_mode='HTML')



selectors = {'table': ".TTTable", 'rows': "tr", 'cells': ".TTCell"}
url = "https://amalb.iscool.co.il/default.aspx"
bot.polling(non_stop=1)
