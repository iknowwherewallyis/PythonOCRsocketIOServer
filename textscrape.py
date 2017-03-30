# import libraries
import re
import urllib2
from bs4 import BeautifulSoup

def parse_string(el):
   text = ''.join(el.findAll(text=True))
   return text.strip()

def scrape_text(page, day, time):

    quote_page = page
    searchday = day
    searchtime = time
    print searchtime
    error = 'There are no classes in this room at this time.'
    #quote_page = 'http://timetable.ait.ie/reporting/textspreadsheet;location;id;X107%0D%0A?t=location+textspreadsheet&days=1-5&weeks=&periods=3-20&template=location+textspreadsheet'
# query the website and return the html to the variable 'page'
    page = urllib2.urlopen(quote_page)
# parse the html using beautiful soap and store in variable `soup`
    soup = BeautifulSoup(page, 'html.parser')
        #print(soup('table')[4].prettify())
    cells = []
    cells1 = []
    i = 0
    final = 0
    if (searchday == 1):
        tables = soup.find_all('table')[8]
        for tr in tables.find_all('tr')[1:]:
            for result in tr.find_all('td')[2]:
                cells = result[:2]
                print cells
                for result1 in tr.find_all('td')[3]:
                    cells1 = result1[:2]
                print cells1
                if (searchtime > int(cells) and searchtime < int(cells1)):
                    final = tr

    if (searchday == 2):
        tables = soup.find_all('table')[9]
        for tr in tables.find_all('tr')[1:]:
            for result in tr.find_all('td')[2]:
                cells = result[:2]
                print cells
                for result1 in tr.find_all('td')[3]:
                    cells1 = result1[:2]
                print cells1
                if (searchtime > int(cells) and searchtime < int(cells1)):
                    final = tr

    if (searchday == 3):
        tables = soup.find_all('table')[10]
        for tr in tables.find_all('tr')[1:]:
            for result in tr.find_all('td')[2]:
                cells = result[:2]
                print cells
                for result1 in tr.find_all('td')[3]:
                    cells1 = result1[:2]
                print cells1
                if (searchtime > int(cells) and searchtime < int(cells1)):
                    final = tr

    if (searchday ==4):
        tables = soup.find_all('table')[11]
        for tr in tables.find_all('tr')[1:]:
            for result in tr.find_all('td')[2]:
                cells = result[:2]
                print cells
                for result1 in tr.find_all('td')[3]:
                    cells1 = result1[:2]
                print cells1
                if (searchtime > int(cells) and searchtime < int(cells1)):
                    final = tr

    if (searchday == 5):
        tables = soup.find_all('table')[12]
        for tr in tables.find_all('tr')[1:]:
            for result in tr.find_all('td')[2]:
                cells = result[:2]
                print cells
                for result1 in tr.find_all('td')[3]:
                    cells1 = result1[:2]
                print cells1
                if (searchtime > int(cells) and searchtime < int(cells1)):
                    final = tr

        # print [cell.get_text(strip=True) for cell in cells]
        #8 = monday
        #9 = tuesday
        #10 = wednesday
        #11 = thursday
        #12 = friday
        #print(tables[8])

    if final:
        return final.text
    else: return error
#print scrape_text('http://timetable.ait.ie/reporting/textspreadsheet;location;id;X107%0D%0A?t=location+textspreadsheet&days=1-5&weeks=&periods=3-20&template=location+textspreadsheet', 2, 17)

