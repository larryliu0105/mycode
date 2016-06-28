import csv
import json


def csvtojson(inputname, outputname):
    """
    csv檔轉json檔
    agr1: 轉檔名(勿加副檔名)
    agr2: 轉出檔名(勿加副檔名)
    """
    f = open('./output_file/' + inputname, 'r', encoding='utf8')
    title = tuple(f.readline().replace('\n', '').split(','))
    reader = csv.DictReader(f, fieldnames=title)
    out = json.dumps(
        [row for row in reader], indent=4, separators=(',', ': '), ensure_ascii=False)
    f = open('./output_file/' + outputname, 'w', encoding='utf8')
    f.write(out)
    f.close()


def convertDateForm(date, form):
    """
    民國日期轉西洋日期
    date = xxxooxx, xxx/oo/xx, xxx-oo-xx
    form1 = xxxxooxx
    form2 = xxxx/oo/xx
    form3 = xxxx-oo-xx
    """
    symbol = ''
    if form == 2:
        symbol = '/'
    elif form == 3:
        symbol = '-'
    rtndate = str(int(date.replace('/', '').replace('-', '')) + 19110000)
    rtndate = rtndate[0:4] + symbol + rtndate[4:6] + symbol + rtndate[6:]
    return rtndate


def courseClassify(text):
    datalist = []
    exercise = {'name': '運動健身',
                'content': ['有氧', '瑜珈', '氣功', '體適能', '太極拳', '舒活', '芭蕾', '肚皮舞', '國標舞', '單人舞', '排舞', '佛拉明哥', '桌球', '皮拉提斯', '拳擊', '塑身', '運動', '舞蹈', '詠春', '武術', '肢體', '社交舞', '羽球', '籃球', '撞球', '網球', '韻律有氧', '標準舞', '敦煌舞', '潛水', '太極'
                            ]}
    arts = {'name': '美術繪畫',
            'content': ['水墨畫', '水彩畫', '禪繞畫', '世界名畫', '繪畫', '油畫', '國畫', '水墨', '彩墨', '燒烙畫', '歐洲彩繪', '粉彩', '美術', '篆刻', '陶土', '押花', '花鳥畫', '素描', '棉紙撕畫', '水彩', '工筆']}
    hobbs = {'name': '興趣才藝',
             'content': ['圍棋', '攝影', '旅遊', '茶藝', '咖啡', '製酒', '釀造', '塔羅', '書法', '詩詞', '作文', '花園', '桌遊', '視覺傳達', '公關', '漫畫', '文化遺產', '戲劇']}
    language = {'name': '語言學習',
                'content': ['英語', '英文', '日本語', '日語', '日文', '手語', '韓文', '韓語', '美語', '華語', '文學']}
    handmade = {'name': '創意手作',
                'content': ['縫紉', '手藝', '製作', '手作', '剪髮', '配飾', '時裝', '花藝', '中國結', '手工', '盆栽', '馬賽克', '毛線', '編織', '機縫', 'DIY', '拼布', '園藝', '陶瓷', '工藝', '裝置藝術', '創作', '金工', '花飾', '珠寶', '皮革', '配件', '陶藝', '產品設計']}
    computerSkills = {'name': '電腦技能',
                      'content': ['FACEBOOK', 'LINE', 'PHOTOSHOP', 'WORD', 'EXCEL', 'OFFICE', 'AUTO CAD', '2D', '3D', 'DREAMWEAVER', 'APP', '會聲會影', '工程製圖', '電腦', '剪輯', '軟體', '影像', '平板', '剪接', '手機', '文書', '視覺設計', 'ILLUSTRATOR', 'AUTODESK', '網路行銷', '網站', '網拍', '數位', '行動裝置']}
    science = {'name': '科學實驗',
               'content': ['生活科技', '創思', '科學', '實驗']}
    instruments = {'name': '樂器音樂',
                   'content': ['古琴', '演奏', '烏克麗麗', '小提琴', '吉他', '二胡', '口琴', '古箏', '音樂', '教唱', '電子琴', '薩克斯風', '太鼓', '南胡', '琴韻', '胡琴', '韻律', '中國笛', '歡唱', '歌唱']}
    healthcare = {'name': '健康養生',
                  'content': ['經絡穴道', '養生', '鬆筋', '紫微', '情感療癒', '生活', '心靈']}
    religion = {'name': '宗教信仰',
                'content': ['易經', '法輪功', '風水', '姓名學', '禪', '佛', '華嚴經', '大乘']}

    food = {'name': '餐飲美食',
            'content': ['西餐', '中餐', '地方小吃', '家常料理', '蛋糕', '點心', '麵包', '料理', '烹飪', '烘培', '日本料理', '日式料理']}

    beauty = {'name': '美容彩妝',
              'content': ['美容', '護膚', '彩妝', '美睫', '指甲', '美甲', '造型', '美髮', '新娘秘書']}

    finance = {'name': '財務規劃',
              'content': ['會計', '期貨', '選股', '企業經營']}

    datalist.append(exercise)
    datalist.append(arts)
    datalist.append(hobbs)
    datalist.append(language)
    datalist.append(handmade)
    datalist.append(computerSkills)
    datalist.append(science)
    datalist.append(instruments)
    datalist.append(healthcare)
    datalist.append(finance)
    datalist.append(religion)
    datalist.append(food)
    datalist.append(beauty)

    rtnstr = '其他'
    for lst in datalist:
        for i in lst['content']:
            if i in text:
                rtnstr = lst['name']
                break
    return rtnstr


# print(courseClassify('有氧'))
