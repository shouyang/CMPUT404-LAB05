#!/usr/bin/env python3
import os

import cgi
import cgitb
cgitb.enable()

import templates
from secret import username,password

print("Content-Type: text/html")
if os.environs.get("REQUEST_METHOD", "GET") != "GET":
    form = cgi.FieldStorage()
    f_username = form.getfirst("username", "")
    f_password = form.getfirst("password", "")

    if f_username == username and f_password == password:
        print("Set-Cookie: username={};".format(f_username))
        print("Set-Cookie: password={}".format(f_password))

        print()
        print()
        print(templates.secret_page(f_username,f_password))
    else:
        print()
        print()
        print(templates.after_login_incorrect())

else:
    print()
    print()
    print(templates.login_page())






