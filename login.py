#!/usr/bin/env python3
import os, sys, cgi
from templates import login_page, secret_page, after_login_incorrect
import secret

form = cgi.FieldStorage()
username = form.getvalue("username")
password = form.getvalue("password")

if (username == secret.username and password == secret.password):
    print(f"Set-Cookie:username = {username}")
    print(f"Set-Cookie:password = {password}")
    print("Content-Type: text/html\r\n")
else:
    print(after_login_incorrect())
