import datetime
from ..helpers import CollectionAppointment
from collections import OrderedDict
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
import urllib.parse
import re
import arrow


DESCRIPTION = "Schedule from Hadeland og Ringerike Avfallsselskap AS - hra.no"
URL = "https://hra.no"
TEST_CASES = OrderedDict([("Biliberget", 
{"agreement":"aa6f7f45-d88e-400b-882f-b02050db1735",
"address":"Biliberget 7, 3530 RØYSE"
})])

class Source:
    def __init__(self, agreement=None, address=None):
        self._agreement = agreement
        self._address = address

    def fetch(self):
        rooturl='https://hra.no/tommekalender/'

        enc_params = urllib.parse.urlencode({'agreement': self._agreement, 'query': self._address})

        req = Request(rooturl+'?'+enc_params)

        fp = urlopen(req).read()
        page = fp.decode("utf8")

        soup = BeautifulSoup(page, features="html.parser")
        soup.prettify()
        calendar = soup.find("div", {"id" : "calendar-content"});

        today=arrow.now().floor('day')

        entries = []

        for retr_div in calendar.findAll("div", {"class" : "garbage-retrieval-row"}):
            typesrow=retr_div.find('div',{'class' : 'types'});
            for div in typesrow.findAll("div",recursive=False):
              try:
                rawdate=div.strong.find("span",{"class" : "date"}).text.strip();
                adate=arrow.get(rawdate,'D. MMM',locale='nb_NO').replace(year=today.year).floor('day')
                if adate < today:
                    adate.shift(year=1)
                date=adate.date()
              except:
                bintype=re.search('.*/(.+?)-.*',div.img['src']).group(1)

                entries.append(
                    CollectionAppointment(
                        date,
                        bintype,
                    )
                )

        return entries
