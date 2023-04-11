from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random

pages = set()

def getLinks(pageUrl):
	global pages
	html = urlopen(f"http://en.wikipedia.org{pageUrl}")
	print(html)
	bs = BeautifulSoup(html, 'html.parser')
	
	try:
		print(bs.h1.get_text())
		print(bs.find(id='mw-content-text').find_all('p')[0])
		print(bs.find(id='ca-edit').find('span').find('a').attrs['href'])

	except AttributeError:
		print('This page is missing something! Continuing...')

	for link in bs.find_all('a', href=re.compile('^(/wiki/)')):
		if 'href' in link.attrs:
			if link.atrrs['href'] not in pages:
				newPage = link. attrs['href']
				print('-'*20)
				print(newPage)
				pages.add(newPage)
				getLinks(newPage)
getLinks('')
	
# Rastreamento de links
# random.seed(datetime.datetime.now())

# def getLinks(articleUrl):
# 	html = urlopen(f"http://en.wikipedia.org{articleUrl}")
# 	bs = BeautifulSoup(html, 'html.parser')
# 	return bs.find('div', {'id':'bodyContent'}).find_all('a', href=re.compile('^(/wiki/)((?!:).)*$'))

# links = getLinks('/wiki/Kevin_Bacon')
# while len(links) > 0:
# 	newArticle = links[random.randint(0, len(links)-1)].attrs['href']
# 	print(newArticle)
# 	links = getLinks(newArticle)

# Recursividade
	
# html = urlopen('http://www.pythonscraping.com/pages/page3.html')
# bs = BeautifulSoup(html, 'html.parser')

# images = bs.find_all('img', {'src':re.compile('\.\.\/img\/gifts\/img.*\.jpg')})

# for image in images:
# 	print(bs.find('img', {'src':image['src']}).parent.previous_sibling.get_text())
# 	print(image['src'])

# print(bs.find('img', {'src':re.compile('\.\.\/img\/gifts\/img.*\.jpg')}).parent.previous_sibling.get_text())