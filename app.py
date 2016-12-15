from bs4 import BeautifulSoup
from datetime import datetime
import subprocess
import urllib2
import time

bashCommand = "cd /home/user/nodejs_apps/portfolio-website && git pull origin master && pm2 restart portfolio-site"
latest_time = ""

while True:
    response = urllib2.urlopen('https://github.com/JamesDaniel/portfolio-website/commits/master')
    html_doc = response.read()
    soup = BeautifulSoup(html_doc, 'html.parser')
    for tim in soup.find_all('relative-time'):
        tim = tim.get('datetime')
        year = tim[0:4]
        month = str(tim)[5:7]
        day = tim[8:10]
        hour = tim[11:13]
        minute = tim[14:16]
        second = tim[17:19]
        date = datetime.strptime(year+month+day+hour+minute+second,'%Y%m%d%H%M%S')
        if latest_time == "":
            process = subprocess.call(bashCommand, shell=True)
            latest_time = date
        elif latest_time < date:
            process = subprocess.call(bashCommand, shell=True)
            latest_time = date

    print(latest_time.strftime("%A, %d. %B %Y %I:%M%p"))
    time.sleep(30)
