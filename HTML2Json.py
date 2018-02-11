import urllib
import sys
from BeautifulSoup import BeautifulSoup
from bs4 import BeautifulSoup
import json

DIV_SELECTOR = "outer-cell mdl-cell mdl-cell--12-col mdl-shadow--2dp"
EVENT_SELECTOR = "content-cell mdl-cell mdl-cell--6-col mdl-typography--body-1"
META_SELECTOR = "content-cell mdl-cell mdl-cell--12-col mdl-typography--caption"



def isVisit(text):
	return text.find('http') == 0
# content-cell mdl-cell mdl-cell--6-col mdl-typography--body-1
# content-cell mdl-cell mdl-cell--12-col mdl-typography--caption

def parseHTML(page, output_f):
	array = [] 
	soup = BeautifulSoup(page,'html.parser')
	for div in soup.find_all('div',class_ = DIV_SELECTOR):
		try:
			event = div.find('div',class_ = EVENT_SELECTOR)
			if event:
				elt ={}
				link = event.find('a')
				text = link.get_text()
				if isVisit(text):
					elt['visit'] = text
				else :
					elt['query_text'] = text
				elt['link'] = link["href"]
				elt['date'] = event.find('br').get_text()
				meta = div.find('div',class_ =META_SELECTOR)
				if meta :
					elt['meta'] = meta.get_text()
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
