import bs4
import requests
import re

url = "https://www.indeed.com/jobs?q=python&l=Chicago%2C+IL, https://www.indeed.com/jobs?q=java&l=Chicago%2C+IL, https://www.indeed.com/jobs?q=javascript&l=Chicago%2C+IL, https://www.indeed.com/jobs?q=c%23&l=Chicago%2C+IL, https://www.indeed.com/jobs?q=php&l=Chicago%2C+IL, https://www.indeed.com/jobs?q=c%2B%2B&l=Chicago%2C+IL, https://www.indeed.com/jobs?q=sql&l=Chicago%2C+IL, https://www.indeed.com/jobs?q=ruby&l=Chicago%2C+IL, https://www.indeed.com/jobs?q=perl&l=Chicago%2C+IL, https://www.indeed.com/jobs?q=visual+basic&l=Chicago%2C+IL, https://www.indeed.com/jobs?q=.net&l=Chicago%2C+IL, https://www.indeed.com/jobs?q=python&l=Chicago%2C+IL, https://www.indeed.com/jobs?q=r&l=Chicago%2C+IL, https://www.indeed.com/jobs?q=swift&l=Chicago%2C+IL"

url = url.split()


while len(url) >0:
    htmltext = requests.get(url[0])
    text = "".join(url[0])
    name = re.search('s?q=(.+?)&l=C', text)
    if name:
        found = name.group(1)
    if found == ('c%23'):
        print ('c#')
    elif found == ('c%2B%2B'):
        print ('c++')
    else:
        print(found)
    #where = url[0].split('https://www.indeed.com/jobs?q=')
    #result = where.split('&l=Chicago%2C+IL')
    tags = bs4.BeautifulSoup(htmltext.content, 'lxml')
    url.pop(0)
    tag = tags.select('#searchCount')
    text_r = (str(tag[0].getText()))
    text_r = text_r.split()
    text_r = text_r[5]
    print(text_r)
