from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from updating.updating.spiders.skuAmazon import SkuamazonSpider
from updating.updating.spiders.dataAmazon import DataamazonSpider

import pandas as pd, os, logging
base = os.getcwd()
log = logging.getLogger("scraper log")
print(base + r"/skus.csv")

listado = pd.read_excel(base + r"/skus.xlsx")
listadosku = set(listado['asin'].to_list())

print(len(listadosku))

process = CrawlerProcess(get_project_settings())

process.crawl(DataamazonSpider, skus = listadosku)

process.start()

# if __name__ == "__main__":
#     print("____________________________________________")
#     print("Menu de inicio para scraping datos de amazon")
#     print("____________________________________________\n\n")
#     print("""Opciones:
#             1. raspar sku.
#             2. raspar datos.
#             3. actualizar datos.
#         """)

#     op = int(input("ingrese la opcion:"))

#     if op == 1:
#         log.info("Inicia de scraping de sku de amazon")
#         process.crawl(SkuamazonSpider, link = listadosku)

#         process.start()

#     elif op == 2:
#         pass
#     elif op == 3:
#         pass
#     else:
#         pass