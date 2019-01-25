#!/usr/bin/env python3
import cgi
import cgitb
cgitb.enable()

import json
import os
import urllib.parse import parse_qs

qs = os.environ.get("QUERY_STRING", None)

print(qs)
