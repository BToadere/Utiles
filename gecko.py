#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 15:25:50 2023

@author: btoadere
"""

import json
import requests
from bs4 import BeautifulSoup

url = 'https://www.coingecko.com/en/coins/camelot-token'

def pagina(url):
    
    res = []
    a = requests.get(url) 
    aa = BeautifulSoup(a.text,'html.parser')
    #print(aa)

    name = aa.find('span',{'class':'tw-font-bold tw-text-gray-900 dark:tw-text-white dark:tw-text-opacity-87 md:tw-text-xl tw-text-lg tw-ml-2 tw-mr-1'}).text
    price = aa.find('span',{'class':'no-wrap'}).text
    percent = aa.find_all('span',{'class': 'text-danger', 'data-json': True})
#    json_str = percent['data-json']
    print(percent, type(percent))
# =============================================================================
#     json_obj = json.loads(json_str)
#     aed_value = json_obj['aed']
# =============================================================================
    
    
    res = [name, price]
    print(res)

# =============================================================================
#         # precio, vol24h, cap, noseke
#         k1 = aa[i].find_all('span',{'data-target':'price.price'})
#         
#         # cosas verdes v1h, v24h, v7d
#         k2 = aa[i].find_all('span',{'data-up-class':'text-green'})
#         
#         print("NAME: ", name, [ki.text for ki in k1+k2],"\n")
#         
#         res.append([name, [ki.text for ki in k1+k2]])
#         
# =============================================================================



# descomenta para scrapear todo
#for pag in range(1,113):
#    print("PAGINA: ", pag)
#    url = 'https://www.coingecko.com/es?page='+str(pag)
#    pagina(url)
    

# solo la principal
pagina(url)




# =============================================================================
#     with open('variable_aa2.txt', 'w') as file:    
#         for element in aa:
#             file.write(str(element) + '\n')
# =============================================================================

    