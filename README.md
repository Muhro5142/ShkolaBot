# ShkolaBot
**Школа Бот** позволяет нам узнать расписание уроков и экзаменов прямиком из сайта школы(с помощью **парсинга**)
https://pb.amalnet.k12.il/%d7%9e%d7%a2%d7%a8%d7%9b%d7%95%d7%aa-%d7%95%d7%a9%d7%99%d7%a0%d7%95%d7%99%d7%99%d7%9d/
<option selected="selected" value="578">יא5</option>
<a id="dnn_ctr1300_TimeTableView_btnChangesTable" class="HeaderTitle" href="javascript:__doPostBack('dnn$ctr1300$TimeTableView$btnChangesTable','')">מערכת ושינויים</a>
<td class="TTCell" nowrap="">
				<table width="100%"></table><div class="TTLesson"><b>מדעי המחשב ב' - תכנות מונחה עצמים</b>&nbsp;&nbsp;(A27 מ.ב.מחשבים)<br>סטפ טובי</div><div class="TTLesson"><b>מדעי המחשב ב' - תכנות מונחה עצמים</b>&nbsp;&nbsp;(A26 מ.א.מחשבים)<br>מור גולן</div>
			</td>

   
## Инструменты для реализации
bs4
csv
telebot
matplotlib
numpy

# Архитектура Проекта 
Class parsing(csv+bs4)
Class Info2Table(info from parsing to table)
Class Telebot(schedule+Bot Architecture)
