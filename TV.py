from bs4 import BeautifulSoup
from urllib2 import urlopen
import pynotify
import time

#the most interesting channels currently on my TV at home..
discov = "http://www.tvinfo.in/discovery-channel.html?i=49"
natgeo = "http://www.tvinfo.in/national-geographic.html?i=79"

def get_schedule(url):
	html = urlopen(url).read()
	soup = BeautifulSoup(html)

	h2 = soup.findAll('h2', {'class' : 'ch-name'})
	links = soup.findAll('p', {'class' : 'pg-desc'})
	times = soup.findAll('h5', {'class' : 'pg-time'})

	pynotify.init("Basic")

	n = pynotify.Notification( h2[0].get_text(),
		"currently : " + links[0].get_text() + '\n'+"up next : " + links[1].get_text()
	)

	n.show()

while(True):
	get_schedule(discov)
	get_schedule(natgeo)
	time.sleep(30)
