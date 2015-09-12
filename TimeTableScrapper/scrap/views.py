from django.shortcuts import render
from django.http import HttpResponse
import requests , json
import sys,os,shutil
import cookielib 
from django.conf import settings
from BeautifulSoup import BeautifulSoup
from requests.cookies import RequestsCookieJar, create_cookie
import time

#BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def getcaptcha(request):
    
    captcha_url = "https://academics.vit.ac.in/parent/captcha.asp"
    url = "https://academics.vit.ac.in/parent/parent_login.asp"
    BASE_DIR = "/home/ashish/Desktop/scrapper/TimeTableScrapper"

    ids = request.GET.get('id',None)
    if ids is None:
        return HttpResponse("No Id provided.")
    regno = request.GET.get('regno',None)
    dob = request.GET.get('dob',None)
    mobile = request.GET.get('mobile',None)
    captcha = request.GET.get('captcha',None)
    captaddr= os.path.join(BASE_DIR, "captchas",(ids))
    cookieaddr= os.path.join(BASE_DIR, "cookies",(ids))
    print cookieaddr
    if not(regno or dob or mobile or captcha):
        try:
            session = requests.Session()
            jar = cookielib.LWPCookieJar(filename=cookieaddr)
            
            session.cookies=jar
            
            response = session.get(url,timeout=60)

            response = session.get(captcha_url,stream=True,timeout=60)
            for c in response.cookies:
                print c
                jar.set_cookie(c)
            jar.save(ignore_discard=True,ignore_expires=True)

            with open(captaddr, 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)


        except requests.exceptions.ConnectionError:
            raise requests.exceptions.ConnectionError("A Connection error occurred.")
        except requests.exceptions.HTTPError:
            raise requests.exceptions.HTTPError("A HTTP error occurred.")
        except requests.exceptions.URLRequired:
            raise requests.exceptions.URLRequired("a valid URL required")
        except requests.exceptions.ConnectTimeout:
            raise requests.exceptions.ConnectTimeout("The request timed out while trying to connect to the remote server.")
        except requests.exceptions.ReadTimeout:
            raise requests.exceptions.ReadTimeout("The server did not send any data in the allotted amount of time.")
        except requests.exceptions.Timeout:
            raise requests.exceptions.Timeout("The request timed out.")
        except:
            raise requests.exceptions.RequestException("There was an ambiguous exception that occurred while handling your request")

        return HttpResponse("OK.Now enter captcha along with login details")
    else:
        try:

            jar = cookielib.LWPCookieJar()
            try:
                jar.load(cookieaddr,ignore_expires=True,ignore_discard=True)
            except:
                print "ERRO COOKIE"
            print jar
            session = requests.Session()
            session.cookies=jar

            dicr = {}
            dicr['wdregno'] = regno
            dicr['wdpswd'] = dob
            dicr['wdmobno'] = mobile
            dicr['vrfcd'] = captcha
            data = json.dumps(dicr)
            headers = {'content-type': 'application/x-www-form-urlencoded'}
            post_url = "https://academics.vit.ac.in/parent/parent_login_submit.asp"
            response = session.post(post_url,data=data,headers=headers,cookies=session.cookies,allow_redirects=True,verify=True)

            home_url = "https://academics.vit.ac.in/parent/home.asp"
            #response = session.get(home_url)
       

        except requests.exceptions.ConnectionError:
            raise requests.exceptions.ConnectionError("A Connection error occurred.")
        except requests.exceptions.HTTPError:
            raise requests.exceptions.HTTPError("A HTTP error occurred.")
        except requests.exceptions.URLRequired:
            raise requests.exceptions.URLRequired("a valid URL required")
        except requests.exceptions.ConnectTimeout:
            raise requests.exceptions.ConnectTimeout("The request timed out while trying to connect to the remote server.")
        except requests.exceptions.ReadTimeout:
            raise requests.exceptions.ReadTimeout("The server did not send any data in the allotted amount of time.")
        except requests.exceptions.Timeout:
            raise requests.exceptions.Timeout("The request timed out.")
        except:
            raise requests.exceptions.RequestException("There was an ambiguous exception that occurred while handling your request")

        html = response.content 
        return HttpResponse(html)



#DEfault values
def postdata(request):
    
    captcha_url = "https://academics.vit.ac.in/parent/captcha.asp"
    url = "https://academics.vit.ac.in/parent/parent_login.asp"
    BASE_DIR = "/home/ashish/Desktop/scrapper/TimeTableScrapper"
    ids = request.GET.get('id',None)
    if ids is None:
        return HttpResponse("No Id provided.")
    regno = '13BCE0019'
    dob = '12101995'
    mobile = '9845150445'
    captcha = request.GET.get('cap',None)
    captaddr= os.path.join(BASE_DIR, "captchas",ids)
    cookieaddr= os.path.join(BASE_DIR, "cookies",ids)

    if not(captcha):
        try:
            session = requests.Session()
            jar = cookielib.LWPCookieJar(filename=cookieaddr)
            
            session.cookies=jar
            
            response = session.get(url,timeout=60)

            response = session.get(captcha_url,stream=True,timeout=60)
            for c in response.cookies:
                print c
                jar.set_cookie(c)
            jar.save(ignore_discard=True,ignore_expires=True)

            with open(captaddr, 'wb') as out_file:
                shutil.copyfileobj(response.raw, out_file)


        except requests.exceptions.ConnectionError:
            raise requests.exceptions.ConnectionError("A Connection error occurred.")
        except requests.exceptions.HTTPError:
            raise requests.exceptions.HTTPError("A HTTP error occurred.")
        except requests.exceptions.URLRequired:
            raise requests.exceptions.URLRequired("a valid URL required")
        except requests.exceptions.ConnectTimeout:
            raise requests.exceptions.ConnectTimeout("The request timed out while trying to connect to the remote server.")
        except requests.exceptions.ReadTimeout:
            raise requests.exceptions.ReadTimeout("The server did not send any data in the allotted amount of time.")
        except requests.exceptions.Timeout:
            raise requests.exceptions.Timeout("The request timed out.")
        except:
            raise requests.exceptions.RequestException("There was an ambiguous exception that occurred while handling your request")

        return HttpResponse("OK.Now enter captcha along with login details")
    else:
        try:

            jar = cookielib.LWPCookieJar()
            try:
                jar.load(cookieaddr,ignore_expires=True,ignore_discard=True)
            except:
                print "ERRO COOKIE"
            print jar
            session = requests.Session()
            session.cookies=jar

            dicr = {}
            dicr['wdregno'] = regno
            dicr['wdpswd'] = dob
            dicr['wdmobno'] = mobile
            dicr['vrfcd'] = captcha
            data = json.dumps(dicr)
            headers = {'content-type': 'application/x-www-form-urlencoded'}
            post_url = "https://academics.vit.ac.in/parent/parent_login_submit.asp"
            response = session.post(post_url,data=data,headers=headers,cookies=session.cookies,allow_redirects=True)

            home_url = "https://academics.vit.ac.in/parent/home.asp"
            #response = session.get(home_url)
       

        except requests.exceptions.ConnectionError:
            raise requests.exceptions.ConnectionError("A Connection error occurred.")
        except requests.exceptions.HTTPError:
            raise requests.exceptions.HTTPError("A HTTP error occurred.")
        except requests.exceptions.URLRequired:
            raise requests.exceptions.URLRequired("a valid URL required")
        except requests.exceptions.ConnectTimeout:
            raise requests.exceptions.ConnectTimeout("The request timed out while trying to connect to the remote server.")
        except requests.exceptions.ReadTimeout:
            raise requests.exceptions.ReadTimeout("The server did not send any data in the allotted amount of time.")
        except requests.exceptions.Timeout:
            raise requests.exceptions.Timeout("The request timed out.")
        except:
            raise requests.exceptions.RequestException("There was an ambiguous exception that occurred while handling your request")

        html = response.content 
        return HttpResponse(html)