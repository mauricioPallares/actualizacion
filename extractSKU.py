from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
# from updating.updating.spiders.dataAmazon import dataAmazon
from updating.updating.spiders.dataAmazon import DataamazonSpider



import pandas as pd
import os
import logging
import math
base = os.getcwd()

log = logging.getLogger("scraper log")


listado = pd.read_excel(base + r"/skus.xlsx")
listadosku = set(listado['asin'].to_list())

lista = []

for x in listadosku:
    lista.append(x)

incremento = math.ceil(len(lista)/10)

i, aux = 1, 0

listaAux, listaUrls = [], []
while i <= len(lista):
    i += incremento
    listaAux = lista[int(aux):int(i)]
    aux = i

    listaUrls.append(listaAux)

skus1 = listaUrls[0]
skus2 = listaUrls[1]
skus3 = listaUrls[2]
skus4 = listaUrls[3]
skus5 = listaUrls[4]
skus6   = listaUrls[5]
skus7   = listaUrls[6]
skus8   = listaUrls[7]
skus9   = listaUrls[8]
skus10  = listaUrls[9]
# skus11  = listaUrls[10]
# skus12  = listaUrls[11]
# skus13  = listaUrls[12]
# skus14  = listaUrls[13]
# skus15  = listaUrls[14]

print(len(listaUrls))
print("____________________________________________")
for lis in listaUrls:
    print(len(lis))


process = CrawlerProcess(get_project_settings())

# process.crawl(DataamazonSpider, skus = skus)

process.crawl(DataamazonSpider, skus=skus1)
process.crawl(DataamazonSpider, skus=skus2)
process.crawl(DataamazonSpider, skus=skus3)
process.crawl(DataamazonSpider, skus=skus4)
process.crawl(DataamazonSpider, skus=skus5)
process.crawl(DataamazonSpider, skus= skus6)
process.crawl(DataamazonSpider, skus= skus7)
process.crawl(DataamazonSpider, skus= skus8)
process.crawl(DataamazonSpider, skus= skus9)
process.crawl(DataamazonSpider, skus= skus10)
# process.crawl(DataamazonSpider, skus= skus11)
# process.crawl(DataamazonSpider, skus= skus12)
# process.crawl(DataamazonSpider, skus= skus13)
# process.crawl(DataamazonSpider, skus= skus14)
# process.crawl(DataamazonSpider, skus= skus15)

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
