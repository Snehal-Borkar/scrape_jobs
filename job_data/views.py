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
    
        


def talentrack(request):
    url = "https://www.talentrack.in/"
    print(url)
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    r= requests.get(url,headers=headers)
    htmlcontent =r.content
    
    soup = BeautifulSoup(htmlcontent,"html.parser")
    tag=soup.find('a',attrs={"href":"/all-job-in-india"})
    link=tag.get('href')
    url="https://www.talentrack.in{}".format(link)
    print(url)
    r= requests.get(url,headers=headers)
    htmlcontent =r.content
    
    soup = BeautifulSoup(htmlcontent,"html.parser")
    jobs=[]
    flinks=[]
    links=soup.find_all('a', attrs={'class':"new-job-link"})
    for link in links:
        c=link.get('class')
        if len(c)==1:
            flinks.append(link)
    for link in flinks[:10]:
        jobs.append(link.get('href'))
    json_jobs=[]
    urls=[]
    for job in jobs[:10]:
        url="https://www.talentrack.in{}".format(job)  
        # headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
        
        r= requests.get(url,headers=headers)
        htmlcontent =r.content 
        soup = BeautifulSoup(htmlcontent,"html.parser")
        detail= (''.join(soup.find('script',attrs={'type':'application/ld+json'}).contents))
        # for c in detail:
        # detail=detail.replace('<br />','')
        detail=detail.replace('\r\n','')
        data=json.loads(detail)
        json_jobs.append(data)
        urls.append((url))
    # for data in json_jobs: 
    #     print(data)
        
    count=0    
    for job in json_jobs:
        print("--------------------------------------------------------------------------------------------")
        print("--------------------------------------------------------------------------------------------")
        # print(job)
        if job:
            title=job["title"]
            validity=job["validThrough"]
            company=job['hiringOrganization']['name']
            type=str(job["employmentType"])
            urltype="intersting url"
            print("title : ",title)
            print("validity:",validity)
            print("company: ",company)
            print("type:",type)
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
    



def iimjob(request):
    url = "https://www.iimjobs.com/c/banking--finance-jobs-13.html"

    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    r= requests.get(url,headers=headers)
    htmlcontent =r.content
    
    soup = BeautifulSoup(htmlcontent,"html.parser")
    b_tag=soup.find('body')
    all_tag=b_tag.find_all("a",attrs={"class":"mrmob5 hidden-xs"})[3:12]
    links=[]
    json_data=[]
    urlss=[]
    for a in all_tag:
        link=a.get('href')
        links.append(link)
    for link in links:
        url=link
        r= requests.get(url,headers=headers)
        htmlcontent =r.content 
        soup = BeautifulSoup(htmlcontent,"html.parser")
        detail= (''.join(soup.find('script',attrs={'type':'application/ld+json'}).contents)) 
        # detail=json.dumps(detail)
        # detail=detail.replace('<br />','')
        detail=detail.replace('\\','') 
        # d=json.loads(detail)
        job=json.loads(detail)
        json_data.append(job)
        urlss.append(link)
    count=0
    for job in json_data:
        if job:
            print("---------------------------------------------------------------------------------")
            print("---------------------------------------------------------------------------------")
            
            title=job["title"]
            validity=job["validThrough"]
            company=job['hiringOrganization']
            type=str(job["employmentType"])
            urltype="intersting url"
            pro_data = Job(title=title,validity=validity,company=company,type=type)
            pro_data.save()
            u=Interest_url(url=urlss[count])
            u.save()
            print(job)
     
        else:
            u=Non_Interest_url(url=urlss[count])
            u.save()
        count+=1
    return  render (request,'job_data/internshala.html')