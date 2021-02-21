#!/usr/bin/env python3

# NOTE: this script was written hastly thus it sucks so beware 

import requests
import sys
from bs4 import BeautifulSoup
from termcolor import colored #TODO: switch to colorama



u = sys.argv[1] 
if u[:1] == '/':
	u = u[:-1]
n_pages = int(sys.argv[2])
if not n_pages:
	print("[WARNING][!]Missing argument: default setting for number of pages is 100")
	n_pages = 100
print("%s" % (n_pages))
parameter = sys.argv[3]

for i in range(n_pages):
	print("-"*50, end='\r')
	n_u = (u + "/" + "?" + parameter + "=" + str(i))
	print(colored("[*]Currently trying: ", "blue") + u + "/" + "?"+ parameter+ "=" + str(i), end='\r')
	r = requests.get(n_u)
	r_unicode = r.text
	title = r_unicode[r_unicode.find('<title>') + 7 : r_unicode.find('</title>')]
	if r.status_code < 300:
		print(colored(f"[{title}][{r.status_code}]", "green") + colored("This site might exists: ", "cyan")
		 + colored(f"{n_u}", "white"))
	r.close


