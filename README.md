Clone the project
```
git clone https://github.com/yash1th/billboard-songs-chart-scraping.git <optional-directory-name>
```

Go to the directory that you just created and create a virtual environment (Highly recommended!!)

```
python3 -m venv .
```

Activate the environment and install the requirements.txt file using the following command

```
pip install -r requirements.txt
```

Go to the folder `billboard` and then run the spider `spider_1`

```
scrapy crawl spider_1
```

A csv file will be created with appropriate file name. You can scrap more than one chart at at time. Simply add the urls to the list `start_urls` object in the following file
```
/billboard/billboard/spiders/songs_chart_spider.py
```