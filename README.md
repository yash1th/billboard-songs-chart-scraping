This project scraps different **_SONG CHARTS_** from the billboard 

1. clone the project
```
git clone https://github.com/yash1th/billboard-songs-chart-scraping.git
```

2. navigate to the directory that you just created and create a virtual environment (Highly recommended!!)
```
cd billboard-songs-chart-scraping/
```

3. activate the virtual environment

```
python3 -m venv .
```

4. install the requirements.txt file using the following command

```
pip install -r requirements.txt
```

5. Navigate to the folder `billboard`
```
cd billboard/
```

6. run the spider `spider_1`
```
scrapy crawl spider_1
```

7. A csv file will be created with an appropriate file name. Examples are 

```
* greatest-adult-pop-songs.csv
* hot-100.csv
```

**Note:** You can scrap more than one chart at at time. Simply add the urls to the list `start_urls` object in the following file
```
billboard/spiders/songs_chart_spider.py
```