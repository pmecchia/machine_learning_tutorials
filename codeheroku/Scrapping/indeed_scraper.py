import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import unidecode
##We need to get these columns: Jobs Title,Location, Salary, Sponsored/organic,Summary

#Step1: send a get request to URL; get the contents and parse it

querry=['fpga','asic','vhdl']



for word in querry:
    print(word)
    df=pd.DataFrame(columns=['Title','Location','Company','Salary_per_year','Summary'])
    for start in range(0,500,10):

        URL="https://www.indeed.fr/jobs?q={}&l=France&start={}".format(word,start)

        page = requests.get(url=URL)
        content=page.content
        soup=BeautifulSoup(content,'html.parser')

        section=soup.find('td',attrs={'id':'resultsCol'})
        all_jobs=section.find_all('div',attrs={'class':'jobsearch-SerpJobCard unifiedRow row result'})

        for jobs in all_jobs:
            #print(jobs)
            try:
                title=jobs.find('a',attrs={'class':'jobtitle turnstileLink '})['title']
            except:
                title='None'


            try:
                location=jobs.find('div',class_='recJobLoc')['data-rc-loc']
            except:
                location='None'


            try:
                company=jobs.find('span',attrs={'class':'company'}).text.strip()
            except:
                company='None'

            try:
                salary=jobs.find('span',attrs={'class':'salaryText'}).text.strip()
                salary=re.sub(r'\s', '', salary)
                by=salary.find("mois")
                salary=min(re.findall(r"\d{1,10}(?:\.\d{1,10})?", salary))
                if by!= -1:
                    salary=str(int(salary)*12)

            except:
                salary='None'

            try:
                summary=jobs.find('div',attrs={'class':'summary'})
                summary=summary.find('li').text.strip()
            except:
                summary='None'

            df=df.append({'Title':title,'Location':location,'Company':company,'Salary_per_year':salary,'Summary':summary},ignore_index=True)

    print(df.shape)
    file_path='datasets/dataset_{}.csv'.format(word)
    df.to_csv(file_path,index=False)
