from bs4 import BeautifulSoup
import requests 


job_category = input("Enter Your Job Category:").lower()
print(f"Searching {job_category} Job for you !!\n")

location = input("Enter Job Location to be Search :")
print(f"Searching Job in {location} \n")

fimilar_skill = input("Enter Your Key skill:").lower()
print(f"Filtering Out your {fimilar_skill} \n")

f = open('job.txt','w')

def find_job(url,x=1):
    
    r = requests.get(url)

    html_content = r.content 

    soup = BeautifulSoup(html_content,'html.parser')


    jobs = soup.find_all('li',class_="clearfix job-bx wht-shd-bx")


    for job in jobs:
    
        posted = job.find('span', class_="sim-posted").text
        if ("few" in posted) or ("1" in posted) or ("2" in posted) or ("3" in posted) or ("4" in posted) or ("5" in posted):
            company_name = job.find('h3',class_="joblist-comp-name").text.replace("  ","")
            skill = job.find('span' , class_= "srp-skills").text.replace("  ","")
            if fimilar_skill in skill.lower():
                link = job.find('a')['href']          # OR   link = job.header.h2.a['href']  or you can also use this 
                c = "\nCompany Name :"+company_name.strip()
                s = "\nSkills :"+ skill.replace('\n','')
                p = "\nPosted on :"+posted.replace('\n','')
                l = "\nMore info :"+link+"\n\n\n\n"
                f.write(c.replace('\r',""))
                f.write(s.replace('\r',""))
                f.write(p.replace('\r',""))
                f.write(l)

    
    x =x + 1
    if x<=5:
        find_job(url=f"https://www.timesjobs.com/candidate/job-search.html?from=submit&actualTxtKeywords={job_category}&searchBy=0&rdoOperator=OR&searchType=personalizedSearch&txtLocation={location}&luceneResultSize=25&postWeek=60&txtKeywords={job_category}&pDate=I&sequence={x}&startPage=1",x=x)      
    else:
        print("File has Been Created !!")    
        f.close()


if __name__ == "__main__":

    url = f"https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords={job_category}&txtLocation={location}"

    find_job(url)
    