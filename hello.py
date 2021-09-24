#!/usr/bin/env python3
import os
import json
from templates import login_page, secret_page, after_login_incorrect
import sys, cgi
import secret

print("Content-type:text/html\r\n\r\n")
print("<title>Test CGI</title>")
print("<p>Hello World!</p>")

#Question 1
#print(os.environ)

#Question 2 & Question 3
json_object = json.dumps(dict(os.environ), indent=4)
print(json_object)

info_query = dict(os.environ)
print("<p>QUERY_STRING : ", info_query["QUERY_STRING"], "</p>")
print("<p>Browser : ",info_query["HTTP_USER_AGENT"],"</p>")

#Question 4
print("<p>Cookie : ", info_query["HTTP_COOKIE"], "</p>")

if len(info_query["HTTP_COOKIE"]) > 1:
    cookies = info_query["HTTP_COOKIE"].split(";")
    username = cookies[0][cookies[0].find('=')+1:]
    password = cookies[1][cookies[1].find('=')+1:]
    print(secret_page(username, password))
else:
    print(login_page())





