from urllib.request import urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup
import re
import datetime
import random
import requests

class Content:
	
	def __init__(self, url, title, body):
		self.url = url
		self.title = title
		self.body = body

	def printar(self):
		print(f"URL: {self.url}")
		print(f"TITLE: {self.title}")
		print(f"BODY: {self.body}")

class Website:
	def __init__(self, name, url, titleTag, bodyTag):
		self.name = name
		self.url = url
		self.titleTag = titleTag
		self.bodyTag = bodyTag

class Crawler:
	def getPage(self, url):
		try:
			req = requests.get(url)
		except requests.exceptions.RequestException:
			return None
		return BeautifulSoup(req.text, 'html.parser')

	def safeGet(self, pageObj, selector):
		selectedElemens = pageObj.select(selector)
		if selectedElemens is not None and len(selectedElemens) > 0:
			return '\n'.join( [elem.get_text() for elem in selectedElemens])
		return ''

	def parse(self, site, url):
		bs = self.getPage(url)
		if bs is not None:
			title = self.safeGet(bs, site.titleTag)
			body = self.safeGet(bs, site.bodyTag)
			if title != '' and body != '':
				content = Content(url, title, body)
				content.printar()

crawler = Crawler()
siteData = [['O\'Reilly Media','http://oreilly.com','h1','section#product-description'],['Reuters', 'http://reuters.com', 'h1','div.StandardArticleBody_body_1gnLA'],['Brookings','http://www.brookings.edu', 'h1', 'div.post-body'],['New York Times', 'http://nytimes.com', 'h1', 'p.story-content']]
websites = []

for row in siteData:
	websites.append(Website(row[0], row[1], row[2], row[3]))
	crawler.parse(websites[0], 'http://shop.oreilly.com/product/0636920028154.do')
	crawler.parse(websites[1], 'http://www.reuters.com/article/us-usa-epa-pruitt-idUSKBN19W2D0')
	crawler.parse(websites[2], 'https://www.brookings.edu/blog/techtank/2016/03/01/idea-to-retire-old-methods-of-policy-education/')
	crawler.parse(websites[3], 'https://www.nytimes.com/2018/01/28/business/energy-environment/oil-boom.html')



		
# pages = set()
# random.seed(datetime.datetime.now())

# #Obtém uma lista de todos os links
# def getInternalLinks(bs, includeUrl):
# 	includeUrl = '{}://{}'.format(urlparse(includeUrl).scheme, urlparse(includeUrl).netloc)
# 	internalLinks = []
# 	#Encontra todos os lins que começam com "/"
# 	for link in bs.find_all('a', href=re.compile('^(/|.*'+includeUrl+')')):
# 		if link.attrs['href'] is not None:
# 			if link.attrs['href'] not in internalLinks:
# 				if(link.attrs['href'].startswith('/')):
# 					internalLinks.append(includeUrl+link.attrs['href'])
# 				else:
# 					internalLinks.append(link.attrs['href'])
# 	return internalLinks

# #Obtém uma lista de todos links externos
# def getExternalLinks(bs, excludeUrl):
# 	externalLinks = []
# 	#Encontra todos os links que começam com "HTTP" e que não contem URL atual
# 	for link in bs.find_all('a', href=re.compile('^(http|www)((?!'+excludeUrl+').)*$')):
# 		if link.attrs['href'] is not None:
# 			if link.attrs['href'] not in externalLinks:
# 				externalLinks.append(link.attrs['href'])
# 	return externalLinks

# def getRandomExternalLinks(startingPage):
# 	html = urlopen(startingPage)
# 	bs = BeautifulSoup(html, 'html.parser')
# 	externalLinks = getExternalLinks(bs, urlparse(startingPage).netloc)
# 	if len(externalLinks) == 0:
# 		print('No external links')
# 		domain = '{}://{}'.format(urlparse(startingPage).scheme, urlparse(startingPage).netloc)
# 		internalLinks = getInternalLinks(bs, domain)
# 		return getRandomExternalLinks(internalLinks[random.randint(0, len(internalLinks)-1)])
# 	else:
# 		return externalLinks[random.randint(0, len(externalLinks)-1)]

# def followExternalOnly(startingSite):
# 	externalLink = getRandomExternalLinks(startingSite)
# 	print(f"Random external link is: {externalLink}")
# 	followExternalOnly(externalLink)

# followExternalOnly('http://oreilly.com')
			
