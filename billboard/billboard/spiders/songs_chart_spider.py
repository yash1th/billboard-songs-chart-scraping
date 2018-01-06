import scrapy
from pprint import pprint as pp
from scrapy.selector import Selector
from itertools import count, zip_longest
import csv

class hot100Spider(scrapy.Spider):
    name = 'spider_1'
    start_urls = [
        'https://www.billboard.com/charts/greatest-adult-pop-songs',
        ]

    def parse(self, response):
        filename = response.url.split('/')[-1]+'.csv'
        with open(filename, 'w') as outcsv:
            writer = csv.writer(outcsv, delimiter=',')
            writer.writerow(['chart_position','artist_name','song_name'])
            sel = Selector(text=response.body)
            sequence = count(1)
            for i in zip_longest(sel.css('.chart-row__song::text').extract(), sel.css('.chart-row__artist::text').extract()):
                line = [str(next(sequence)),i[0].strip(),i[1].strip()]
                writer.writerow(line)
        
        #file writing
        # with open('charts.txt', 'w') as f:
        #     sel = Selector(text=response.body)
        #     sequence = count(1)
        #     for i in zip_longest(sel.css('.chart-row__song::text').extract(), sel.css('.chart-row__artist::text').extract()):
        #         line = str(next(sequence))+'. '+ i[0]+ ' - '+ i[1].strip()
        #         f.write(line)
        #         f.write('\n')
        