import pymongo
import schedule, time

from parsers.DE import fetch_DE
from parsers.DK import fetch_DK
from parsers.ES import fetch_ES
from parsers.FI import fetch_FI
from parsers.FR import fetch_FR
from parsers.NO import fetch_NO
from parsers.SE import fetch_SE
from parsers.UK import fetch_UK

INTERVAL_SECONDS = 60

parsers = [
    fetch_DE,
    fetch_DK,
    fetch_ES,
    fetch_FI,
    fetch_FR,
    fetch_NO,
    fetch_SE,
    fetch_UK
]

client = pymongo.MongoClient('mongodb://localhost:27017')
db = client['electricity']
col = db['realtime']

def fetch_all():
    for parser in parsers: 
        obj = parser()
        print 'INSERT %s' % obj
        col.insert_one(obj)

schedule.every(INTERVAL_SECONDS).seconds.do(fetch_all)
fetch_all()

while True:
    schedule.run_pending()
    time.sleep(INTERVAL_SECONDS)