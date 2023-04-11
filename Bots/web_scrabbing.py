import requests
from bs4 import BeautifulSoup

url = 'https://educacao.araras.cc/AzhTOQZwVnNROwZxAyRXbQRjVDpQYA18!@5e7558c44525f09fd97ef617434bff78!&/AycDZgRmADAGdl0bAyJRYQRvBWhXYw==!@5e7558c44525f09fd97ef617434bff78!&/VzcGMgE2A2E=!@5e7558c44525f09fd97ef617434bff78!&/XDsAMlNkAmQ=!@5e7558c44525f09fd97ef617434bff78!&'
response = requests.get(url)
raw_html = response.text
parsed_html = BeautifulSoup(raw_html, 'html.parser')

name_school = parsed_html.select_one('#container > div > div.ui-widget-content > div > p')

if name_school is not None:
	print(name_school.parent)
