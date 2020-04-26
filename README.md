# Data Playground

Welcome to my data playground, a repository where I explore and learn to use new tools and technologies for dealing with a variety of data problems.
I've decided to publish my projects to this repository so that I can share what I've learned, and hopefully help others who are new to these topics.

I'll use real-world examples as much as possible, because I realize that often there is a significant gap going from toy examples in tutorials/training courses to dealing with real-world data problems.

I'll primarily use python for my examples, but may explore other tools/languages in the future.

## Projects
**1. [Wrangling COVID-19 data](https://github.com/rtm010/data-playground/tree/master/covid-19-data-wrangling)**  
In this project I dive into _web scraping_ and _data wrangling_ techniques. 
- I'll use the python libraries [Requests](https://requests.readthedocs.io/en/master/) and [Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) to automatically download PDFs from the [WHO website](https://www.who.int/emergencies/diseases/novel-coronavirus-2019/situation-reports/) containing daily COVID-19 data. 
- A second implementation uses [Selenium](https://selenium-python.readthedocs.io/index.html), which is essential when you're dealing with dynamic websites that only build up the HTML page once opened in your browser. Think of websites built using frameworks like React, Angular, and Vue.
- Once downloaded, I'll read the table from the PDF using [tabula-py](https://tabula-py.readthedocs.io/en/latest/) and clean up the data using [pandas](https://pandas.pydata.org/).

## Contact
**Got any questions?**  
[Reach out to me here](https://twitter.com/rtm010) or open an issue. Happy to have a chat! :smiley:
