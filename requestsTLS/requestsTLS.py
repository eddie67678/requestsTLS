import requests
import os
from threading import Thread
import requestsTLS.exceptions as exceptions
import time

def intializeServer():

    def runServer():
       os.system("cmd /k go run requestsTLS/proxy.go")

    print("Initializing Server...")
    Thread(target=runServer()).start()
    while True:

        time.sleep(10)
        print("What He Said ^^^")
        print("Also consider starring the requestsTLS repo @ htps://github.com/eddie67678/requestsTLS")
        return

def get(url, **kwargs):
    if kwargs:
        #checking if URL passed is http or https
        if url.startswith("http://"):
            urlType = "http"
        elif url.startswith("https://"):
            urlType = "https"
        else:
            raise exceptions.InvalidURL

        #checking if headers are passed and adding url to headers as poptls-url
        try:
            headers = kwargs["headers"]
            headers["poptls-url"] = url
        
        except KeyError:
            headers = {"poptls-url" : url}

        #checking if proxies are passed and if so adding them to headers as poptls-proxy
        try:
            if urlType == "http":
                headers["poptls-proxy"] = kwargs["proxies"]["http"]
            elif urlType == "https":
                headers["poptls-proxy"] = kwargs["proxies"]["https"]
        except KeyError:
            pass
        
        #checking if cookies are passed
        try:
            cookies = kwargs["cookies"]
        except KeyError:
            cookies = None

        #sending request via proxy server    
        try:

            response = requests.get("http://localhost:8082", headers=headers, cookies=cookies)
            return response

        except Exception as e:
            raise e

    else:
        #setting poptls-url header as passed URL
        headers = {"poptls-url" : url}

        #sending request via proxy server    
        try:

            response = requests.get("http://localhost:8082", headers=headers)
            return response

        except Exception as e:
            raise e

def post(url, **kwargs):

    if kwargs:
        #checking if URL passed is http or https
        if url.startswith("http://"):
            urlType = "http"
        elif url.startswith("https://"):
            urlType = "https"
        else:
            return "Invalid URL Passed. Must Start with http:// OR https://"

        #checking if headers are passed and adding url to headers as poptls-url
        try:
            headers = kwargs["headers"]
            headers["poptls-url"] = url
        
        except KeyError:
            headers = {"poptls-url" : url}

        #checking if proxies are passed and if so adding them to headers as poptls-proxy
        try:
            if urlType == "http":
                headers["poptls-proxy"] = kwargs["proxies"]["http"]
            elif urlType == "https":
                headers["poptls-proxy"] = kwargs["proxies"]["https"]
        except KeyError:
            pass
        
        #checking if cookies are passed
        try:
            cookies = kwargs["cookies"]
        except KeyError:
            cookies = None

        #checking if a body is passed
        try:
            data = kwargs["data"]
        
        except KeyError:
            data = None
        
        #checking if a json is passed
        try:
            json = kwargs["json"]
        
        except KeyError:
            json = None
        
        #sending request via proxy server
        try:

            response = requests.post("http://localhost:8082", headers=headers, data=data, json=json, cookies=cookies)
            return response

        except Exception as e:
            return e
    
    else:
        #setting poptls-url header as passed URL
        headers = {"poptls-url" : url}
        
        #sending request via proxy server    
        try:

            response = requests.post("http://localhost:8082", headers=headers)
            return response

        except Exception as e:
            raise e
