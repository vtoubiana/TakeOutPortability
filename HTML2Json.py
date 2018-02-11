import urllib
import sys
from BeautifulSoup import BeautifulSoup
from bs4 import BeautifulSoup
import json

array = [] 

def isVisit(text):
	return text.find('http') == 0


def parseHTML(page, output_f):
	soup = BeautifulSoup(page,'html.parser')
	for div in soup.find_all('div',class_ ="content-cell mdl-cell mdl-cell--6-col mdl-typography--body-1"):
		try:
			elt ={}
			link = div.find('a')
			text = link.get_text()
			if isVisit(text):
				elt['visit'] = text
			else :
				elt['query_text'] = text
			date = div.find('br').get_text()
			elt['link'] = link["href"]
			elt['date'] = date
			array.append(elt)
		except:
			print "Failed to parse elt"	

  
	print array	
	print output_f
	with open(output_f, 'w') as outfile:
		json.dump(array, outfile)	


def main(argv):
	input_f = argv[1]
	output_f = argv[2]
	page =urllib.urlopen(input_f).read()
	parseHTML(page, output_f)




if __name__ == "__main__":
    main(sys.argv)
