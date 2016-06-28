
# coding: utf-8

# In[42]:

import requests
res = requests.get("http://163.32.98.3/KHHCVS/Main/ClassList.aspx?new=1")
res.close()
res.encoding = res.apparent_encoding


# In[43]:

from bs4 import BeautifulSoup
soup = BeautifulSoup(res.text, "lxml")
#print(soup.prettify())


# In[44]:

table = soup.select('#DataRow')
from crawlerApi import crawerAPI
#print(table)


# In[45]:

import uuid
text= ""
href = 'http://163.32.98.3'
city = "高雄市"
figure = ""
for item in table:
    detail_href1 = 'empty'
    detail_href2 = 'empty'
    
    uniqid = str(uuid.uuid4())[24:]
    text += uniqid + ',' + city + ','
    
    charge = ''
    for idx, cell in enumerate(item.select('td')):
        if idx == 1:
            continue
        elif idx == 3:
            course_name = cell.text.strip().replace(' ','')
            category = crawerAPI.courseClassify(course_name.upper())
            text += course_name + ',' + category + ','
        elif idx == 4:
            try:
                link = cell.find('a').get('href')
                if link[-2:] == '/.':
                    detail_href1 =''
                else:
                    detail_href1 = href + link
            except:
                pass
        elif idx == 5:
            try:
                link = cell.find('a').get('href')
                #判斷網址是否有效
                if link[-2:] == '/.':
                    detail_href2 =''
                else:
                    detail_href2 = href + link
            except:
                pass
        elif idx == 6:
            text += cell.text.strip().replace('/','-')+','
        elif idx == 7:
            weekday = cell.text.strip()
        elif idx == 8:
            text += '每周' + weekday + ' ' +cell.text.strip()+','
        elif idx == 11:
            charge = cell.text.strip()
        elif idx == 12:            
            if cell.text.strip() == '0':
                text += charge + ','
            else:
                text += charge + '  另收雜費:' + cell.text.strip() +','
        elif idx == 13:
            if cell.text.strip() != '':
                text += cell.text.strip().replace('\r\n',' ')+','
            else:
                text += "note_empty,"
        else:
            text += cell.text.strip()+','

    text += detail_href1 + ',' + detail_href2 + ',' + figure
    text += '\n'
print(text)


# In[46]:

title = "ID,city,serial_number,organizer,course_name,category,start_date,classtime,num_of_people,總節數,charge,note,teacher_website,relate_website,figure"


# In[47]:

with open('./output_file/' + 'kh_hcvs.csv','w', encoding ='utf8') as outputfile:
    outputfile.write(title+'\n')
    outputfile.write(text)


# In[48]:

crawerAPI.csvtojson('kh_hcvs.csv', 'kh_hcvs.json')

