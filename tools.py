import requests
import telnetlib
from bs4 import BeautifulSoup

# 爬取整个HTML页面
def getHtml(url):
    return requests.get(url).text

# 解析爬取到的HTML页的关键数据
def parseHtml(html, result):
    soup = BeautifulSoup(html)
    ele = soup.find_all("td")
    for index in range(0, len(ele)):
        if index % 7 == 0:
            result += "\n" + ele[index].string + ','
        elif index % 7 == 6:
            result += ele[index].string
        else:
            result += ele[index].string + ','
    return result

# 爬取指定页，通过getHtml()函数和parseHtml函数
def spider():
    result = []
    results = []
    usingList = []
    url = "https://www.kuaidaili.com/free/inha/"
    for index in range(1, 4):
        results = parseHtml(getHtml(url + str(index)), '').split("\n")
        del results[0]
        for res in range(0, len(results)):
            result = results[res].split(',')
            if checkIP(result[0], result[1]):
                print(result[0] + ':' + result[1])
                usingList.insert(0, result[0] + ':' + result[1])
        results.clear()
        result.clear()
    return usingList

# 检查爬取到的IP是否可用
def checkIP(ip, port):
    try:
        telnetlib.Telnet(ip, port = port, timeout = 3)
    except:
        return False
    else:
        return True

if __name__ == '__main__':
    print(spider())
