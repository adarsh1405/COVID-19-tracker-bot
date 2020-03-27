from telegram.ext import Updater,MessageHandler,Filters,CommandHandler
import requests
from bs4 import BeautifulSoup

updater=Updater("1135837651:AAHqrZnyXoG1ADS4NDBuEA2XzEC0VlUEpPE")

#item="India"
#driver=webdriver.Chrome(executable_path=r'C:\chromedriver\chromedriver.exe')
html_doc=requests.get('https://www.worldometers.info/coronavirus/').text
#html_doc=driver.page_source
soup=BeautifulSoup(html_doc,'lxml')
tag_info=soup.find_all('tbody' , class_="table table-bordered table-hover main_table_countries dataTable no-footer")
out=[]
for trtag in soup.find_all('tr'):
	inp=[]
	for tdtag in trtag.find_all('td'):
		inp.append(tdtag.text.strip())
	out.append('|'.join(inp))
res=out
#print('\n'.join(res))
#driver.quit()
t_case=res[-1]

def find_country(country="India"):

	fields={"Country":None,"Total cases":None,"New Cases":None,"Total Deaths":None,"New Deaths":None,"Total Recover":None,"Active Cases":None,"Serious Cases":None}
	for i in range(len(res)):
		x=res[i]
		res1=x.split('|')
		if country in res1:
			ret=""
			for j,key in enumerate(fields):
				if res1[j]!='':
					ret+=key+":- "+res1[j]+"\n"
			#sen="Country:-"+res1[0]+"\n"+"Total cases:-"+res1[1]+"\n"+			"New Cases:-"+res1[2]+"\n"+"Total Deaths:-"+res1[3]+"\n"+"New Deaths:-"+res1[4]+"\n"+"Total Recover:-"+res1[5]+"\n"+"Active Cases:-"+res1[6]+"\n"+"Serious Cases:-"+res1[7]
			return ret
	return "No Such Country Found !!"

def country(bot,update):
	update.message.reply_text(text="Enter the country")

def reply(bot,update):
	item=update.message.text
	#print(item)
	detail=find_country(item)
	update.message.reply_text(detail)

def grettings(bot,update):
	update.message.reply_text("Welcome to the COVID-19 Tracker")
	update.message.reply_text("Type /country /total inorder to get the result")
	#print("Call request")
	

def total(bot,update):
	sen=t_case.split("|")
	smsg=sen[0]+"-"+sen[1]+"\nNew Cases:-"+sen[2]+"\nTotal Deaths:-"+sen[3]+"\nTotal Recover:-"+sen[4]
	update.message.reply_text(smsg)
	#print(smsg)


def main():
	dispatcher=updater.dispatcher
	dispatcher.add_handler(CommandHandler("start",grettings))
	dispatcher.add_handler(CommandHandler("country", country))
	dispatcher.add_handler(CommandHandler("total", total))
	dispatcher.add_handler(MessageHandler(Filters.text, reply))
	updater.start_polling()
	updater.idle()

if __name__=='__main__':
	main()