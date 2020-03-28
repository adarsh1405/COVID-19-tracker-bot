from telegram.ext import Updater,MessageHandler,Filters,CommandHandler
import requests
from bs4 import BeautifulSoup

updater=Updater("1135837651:AAHqrZnyXoG1ADS4NDBuEA2XzEC0VlUEpPE")

html_doc=requests.get('https://www.worldometers.info/coronavirus/').text
soup=BeautifulSoup(html_doc,'lxml')
tag_info=soup.find_all('tbody' , class_="table table-bordered table-hover main_table_countries dataTable no-footer")
out=[]
for trtag in soup.find_all('tr'):
	inp=[]
	for tdtag in trtag.find_all('td'):
		inp.append(tdtag.text.strip())
	out.append('|'.join(inp))
res=out
t_case=res[-1]
top5=res[1:6]
symp="1.Fever\n2.Tiredness\n3.Cough\n4.Difficulty in breathing\n5.In severe cases, it can cause pneumonia and respiratory failure sometimes leading to death"
prevn1="1.Maintain personal hygiene, hand washing, avoiding touching the eyes, nose or mouth with unwashed hands, coughing/sneezing into a tissue and putting the tissue directly into a dustbin.\n 2.Those who may already have the infection have been advised to wear a surgical mask in public."
prevn2="3.Physical distancing\nwhich includes infection control actions intended to slow the spread of disease by minimizing close contact between individuals."
prevn3="4.Self-isolation\nThose who may have been exposed to someone with COVID-19 and those who have recently travelled to a country with widespread transmission have been advised to self-quarantine for 14 days from the time of last possible exposure"
prevn=prevn1+prevn2+prevn3;
rule1="/start - sends a welcome message and link to the APP\n /country - to know the country present situation\n /total - to know the stats of total world "
rule2="/top - gives data of top 5 countries affected\n /symptoms - to know about the symptoms\n /tips - see to get aware"
rule=rule1+rule2

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
			return ret
	return "No Such Country Found !!"

def country(bot,update):
	update.message.reply_text(text="Enter the country")

def reply(bot,update):
	item=update.message.text
	detail=find_country(item)
	update.message.reply_text(detail)

def top(bot,update):
	for i in top5:
		top=i.split("|")
		smsg1=top[0]+"-"+top[1]+"\nNew Cases:-"+top[2]+"\nTotal Deaths:-"+top[3]+"\nTotal Recover:-"+top[4]
		update.message.reply_text(smsg1)

def grettings(bot,update):
	update.message.reply_text("Welcome to the COVID-19 Tracker")
	update.message.reply_text("GO TO https://tiny.cc/covid-19india to download the App")
	

def total(bot,update):
	sen=t_case.split("|")
	smsg=sen[0]+"-"+sen[1]+"\nNew Cases:-"+sen[2]+"\nTotal Deaths:-"+sen[3]+"\nTotal Recover:-"+sen[4]
	update.message.reply_text(smsg)
	#print(smsg)

def symptoms(bot,update):
	update.message.reply_text(symp)

def tips(bot,update):
	update.message.reply_text(prevn)

def rules(bot,update):
	upda.message.reply_text(rule)


def main():
	dispatcher=updater.dispatcher
	dispatcher.add_handler(CommandHandler("start",grettings))
	dispatcher.add_handler(CommandHandler("country", country))
	dispatcher.add_handler(CommandHandler("total", total))
	dispatcher.add_handler(CommandHandler("top",top))
	dispatcher.add_handler(CommandHandler("symptoms",symptoms))
	dispatcher.add_handler(CommandHandler("tips",prevn))
	dispatcher.add_handler(CommandHandler("rules",rules))
	dispatcher.add_handler(MessageHandler(Filters.text, reply))
	
	
	updater.start_polling()
	updater.idle()

if __name__=='__main__':
	main()