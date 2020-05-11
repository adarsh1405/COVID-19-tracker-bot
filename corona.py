from bs4 import BeautifulSoup
import requests
import json
html_doc=requests.get('https://www.mohfw.gov.in/').text
soup=BeautifulSoup(html_doc,'lxml')
div_tag=soup.find('div',class_="data-table table-responsive")
out1=[]
for trtag in div_tag.find_all('tr'):
	inp1=[]
	for tdtag in trtag.find_all('td'):
		inp1.append(tdtag.text.strip())
	out1.append('|'.join(inp1))
# print(out1)
for item in out1:
	print(item.split("|"))


