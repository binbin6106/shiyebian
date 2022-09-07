import requests
import re
from bs4 import BeautifulSoup as bs
import io
import sys
import datetime

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

def getData(src):
    html = requests.get(src).content
    soup = bs(html, 'lxml')

    global ws
    infoList = []
    LS = soup.find_all('ul', class_="lie1")

    for i in LS:
        LS = i.find_all("li")

    for info in LS:
        tmpText = '[' + info.a.string + ']' + '(' + info.a['href'] + ')'
        infoList.append(tmpText)

    push(infoList)

def push(text):
    pushText = ""
    i = 1
    for item in text:
        pushText = pushText + str(i) + '. ' + item + '\n'
        i = i + 1

    yue = datetime.datetime.now().strftime("%m")
    ri = datetime.datetime.now().strftime("%d")
    title = yue + '月' + ri + '日' + '山东事业单位招聘推送'
    pushPara = {'title': title,'desp': pushText}

    r1 = requests.post("https://sctapi.ftqq.com/SCT57577TXrQ38vB3fZnfZE9xbeW9fDmG.send", data=pushPara)

def Find(string):
    url = re.findall(r'href="http://www.shiyebian.net/xinxi/(.*?)"', string)
    url.remove('')
    url1 = []
    for i in url:
        url = 'http://www.shiyebian.net/xinxi/' + i
        url1.append(url)
    return url1

if __name__ == '__main__':
    src = 'http://www.shiyebian.net/shandong/'
    getData(src)