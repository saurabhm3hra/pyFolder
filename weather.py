#!/usr/bin/env python3
import requests
import bs4
import re
import sys
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    )
city = sys.argv[1]
logging.debug('City Name: ' + city)
#res = requests.get('https://www.google.com.tw/search?site=&source=hp&q=site%3Aaccuweather.com+mumbai')
logging.debug('Starting Google Search (site Accuweather) for ' + city)
res = requests.get('https://www.google.com.tw/search?site=&source=hp&q=site%3Aaccuweather.com+' + city)
print(res.status_code)
soup = bs4.BeautifulSoup(res.text, 'html.parser')
logging.debug('Searching Accuweather URL for ' + city)
sss = soup.select("div#search a")
result = re.search('url\?q=(.*)&amp;sa', str(sss[0]))
url1 = result.group(1)
url2 = url1.replace('weather-forecast', 'current-weather')
logging.debug('Visit Accuweather ' + city)
res = requests.get(url2)
soup = bs4.BeautifulSoup(res.text, 'html.parser')
logging.debug('Getting Weather Data for ' + city)
sss = soup.select("div .forecast")
print(sss[0].getText().replace('\n', ' ').encode('ascii', 'ignore'))
