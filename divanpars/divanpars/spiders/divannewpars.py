import csv
import scrapy
from openpyxl import Workbook
import pandas as pd
import matplotlib.pyplot as plt

class DivannewparsSpider(scrapy.Spider):
    name = "divannewpars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/category/divany-i-kresla"]
    custom_settings = {
        'FEEDS': {
            'output.json': {
                'format': 'json',
                'encoding': 'utf8',
                'store_empty': False,
                'fields': None,
                'indent': 4,
            },
        }
    }

    def __init__(self):
        self.workbook = Workbook()
        self.sheet = self.workbook.active
        self.sheet.append(["Name", "Price", "URL"])

    def parse(self, response):
        try:
            links = []
            link = response.css('div.ui-jDl24')
            for i in link.css('a::attr(href)'):
                if len(links) == 0:
                    links.append(i)
                else:
                    flag = True
                    for j in links:
                        if i == j:
                            flag = False
                        else:
                            continue
                    if flag:
                        links.append(i)
                    else:
                        continue
            l = links[:-1]

        except IndexError:
            return 0
        with open('light.csv', 'w', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow(['Название', 'Цена', 'Ссылка'])
        for i in l:
            response.follow(i)
            lights = response.css('div.lsooF')

            for light in lights:
                name = light.css('span::text').get()
                price = light.css('div.q5Uds span::text').get()
                url = response.urljoin(light.css('a').attrib['href'])
                if ' ' in price:
                    price = price.replace(" ", "")

                # Сохраняем данные в XLSX
                self.sheet.append([name, int(price), url])
                with open('light.csv', 'a', newline='', encoding='utf-8') as file:
                    writer = csv.writer(file)
                    writer.writerow([name, price, url])

                # Возвращаем данные для экспорта в JSON
                yield {
                    "name": name,
                    "price": price,
                    "url": url
                }

        data = pd.read_csv('C:/PyCh/new_matplotlib/divanpars/divanpars/spiders/light.csv')
        a = data['Цена'].mean()

        plt.hist(data['Цена'], bins=6)
        plt.xlabel('x ось')
        plt.ylabel('y ось')
        plt.title(f'Гистограмма для цен на диваны.\nСредняя цена дивана {a} руб.')

        plt.show()


    def closed(self, reason):
        self.workbook.save("output.xlsx")

