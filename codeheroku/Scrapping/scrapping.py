import requests
from bs4 import BeautifulSoup

#EXERCISE 1
comment='''URL="https://www.codeheroku.com/blog.html"

page = requests.get(url=URL)
content=page.content

soup=BeautifulSoup(content,'html.parser')
section=soup.find('section',attrs={'class':'card-group-2'})
all_cards=section.find_all('div',attrs={'class':'card'})

data=[]
for card in all_cards:
    blog={}
    title=card.find('h2',class_='card-title')
    title=title.text.strip()
    date=card.find('p',class_='card-date')
    date=date.text.strip()
    blog['title']=title
    blog['date_posted']=date
    data.append(blog)

print(data)'''

#EXERCISE 2

#Step1: get request on login page to get the form key
session_request = requests.session()
URL2="https://www.codeheroku.com/login"
page=session_request.get(url=URL2)
content=page.content
soup=BeautifulSoup(content,'html.parser')
key=soup.find('input',attrs={'name':'_formkey'})

print(key['value'])

#Step2: parse the form key and add it to the payload
payload={
    'email':'test123@codeheroku.com',
    'password' : 'test123',
    '_formname' : 'login',
    '_formkey' : key['value']
}
#Step3: post request
response=session_request.post(url=URL2,data=payload)

soup=BeautifulSoup(response.content,'html.parser')

print(soup)
