# requires pip install requests for bs4 and response 
import requests
from bs4 import BeautifulSoup

# get news from some source; i.e. BBC  
url = 'https://www.bbc.com/news'
response = requests.get(url)

# parse the html using beautiful soup and keep headlines only (of type h3))  
soup = BeautifulSoup(response.text, 'html.parser')
headlines = soup.find('body').find_all('h3')
# extract repetitive text from headlines
unwanted = ['BBC World News TV', 'BBC World Service Radio',
            'News daily newsletter', 'Mobile app', 'Get in touch']

# print headlines
print("TODAY'S HEADLINES FROM BBC NEWS")  
for x in list(dict.fromkeys(headlines)):
    # exclude single words and unwanted text
    if x.text.strip() not in unwanted and len(x.text.split()) > 1:
        # print only if headline is not a question
        if x.text.strip()[-1] != '?':
            print(x.text.strip())
