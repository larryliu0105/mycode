
# coding: utf-8

import requests
import uuid
from bs4 import BeautifulSoup
from crawlerApi import crawerAPI
res = requests.get("http://www.kmseh.gov.tw/07_class/online.php")
res.close()
res.encoding = res.apparent_encoding
soup = BeautifulSoup(res.text, "lxml")
# print(soup.prettify())


table = soup.find('table', {"summary": "硬體設備"})
output_text = ""
city = "高雄市"
district = "小港區"
location = "高雄市小港區學府路115號"
organizer = "高雄社教館-教育推廣班"
figure = ""


def detailCrawler(link, class_weekday, text):
    rtntext = ""
    res = requests.get(link)
    res.close()
    res.encoding = res.apparent_encoding
    soup = BeautifulSoup(res.text, "lxml")
    table = soup.find('table', {"bgcolor": "#F2A3B9"})

    # 加上ID,PLACE,organizer
    uniqid = str(uuid.uuid4())[24:]
    rtntext += uniqid + ',' + city + ',' + district + \
        ',' + location + ',' + organizer + ','

    for idx, row in enumerate(table.findAll('td', {"bgcolor": "#FFFFFF"})):
        if idx == 1:
            className = row.text.strip().upper()
            category = crawerAPI.courseClassify(className)
            rtntext += className + ',' + category + ','
        elif idx == 2:
            rtntext += '每周' + class_weekday + ' ' + row.text + ','
        elif idx == 4:
            date = row.text.strip().replace(' ', '').split('~')
            rtntext += crawerAPI.convertDateForm(
                date[0], 3) + ',' + crawerAPI.convertDateForm(date[1], 3) + ','
        elif idx in (9, 10):
            rtntext += '\"' + row.text + '\"' + ','
        else:
            rtntext += row.text + ','

    rtntext += text
    return rtntext

for row in table.findAll("tr"):
    text = ""
    rowdata = row.findAll("td")
    href = "http://www.kmseh.gov.tw/07_class/"
    uniqid = str(uuid.uuid4())[24:]
    class_weekday = ""
    if len(rowdata) == 10:
        for idx, i in enumerate(rowdata):
            if idx == 2:
                detail_href = href + i.find('a').get('href')
            elif idx == 3:
                class_weekday = i.text.strip()
            elif idx == 8:
                singup_list_href = href + i.find('a').get('href')
            elif idx == 9:
                try:
                    singup_href = href + i.find('a').get('href')
                except:
                    singup_href = "尚未開始報名"
        text += detail_href + ","
        text += singup_href + ","
        text += figure + ","
        text += singup_list_href + "\n"
        output_text += detailCrawler(detail_href, class_weekday, text)
print(output_text)


with open('./output_file/' + 'kh_mseh.csv', 'w', encoding='utf8') as outputfile:
    # title
    outputfile.write(
        'ID,city,district,location,organizer,serial_number,course_name,category,classtime,classroom,start_date,end_date,teacher,charge,num_of_people,num_of_applied,intro,note,relate_website,signup,figure,apply_list' + '\n')
    outputfile.write(output_text)

crawerAPI.csvtojson('kh_mseh.csv', 'kh_mseh.json')
