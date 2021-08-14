from django.http.response import HttpResponseNotAllowed, HttpResponseRedirect
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from .models import Job,Interest_url,Non_Interest_url
import json

# Create your views here.
def internshala(request):
    url = "https://internshala.com/"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    r= requests.get(url,headers=headers)
    htmlcontent =r.content
    
    soup = BeautifulSoup(htmlcontent,"html.parser")
    flink=soup.find('a',attrs={'class':"nav-link",})
    link=flink.get('href')
    url="https://internshala.com/{}".format(link)
    

    # headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    r= requests.get(url,headers=headers)
    htmlcontent =r.content
    
    soup = BeautifulSoup(htmlcontent,"html.parser")
    jobs=[]

    
    lists=soup.find_all('div', attrs={'class':"heading_4_5 profile"})
    for link in lists[:10]:
        link=link.find('a')
        jobs.append(link.get('href')) 
    # print(len(jobs))
    json_jobs=[]
    urls=[]
    for job in jobs:
        url="https://internshala.com/{}".format(job)
        # print (url)  
        # headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        r= requests.get(url,headers=headers)
        htmlcontent =r.content 
        soup = BeautifulSoup(htmlcontent,"html.parser")
        detail=soup.find('body')
        name=json.loads("".join(detail.find("script", {"type":"application/ld+json"}).contents))
        (json_jobs.append(name))
        urls.append(url)
    count=0    
    for job in json_jobs:
        print("-----------------------------------------------------------------------------------")
        print(job)
        if job:
            title=job["title"]
            validity=job[ "validThrough"]
            company=job['hiringOrganization']['name']
            type=str(job["employmentType"])
            urltype="intersting url"
            print("title : ",title)
            print("validity:",validity)
            print(urltype)
            pro_data = Job(title=title,validity=validity,company=company,type=type)
            pro_data.save()
            u=Interest_url(url=urls[count])
            u.save()
        
        else:
            urltype="not_intersting url"
            u=Non_Interest_url(url=urls[count])
            u.save()
        count+=1
        





    return  render (request,'job_data/internshala.html')
    
        