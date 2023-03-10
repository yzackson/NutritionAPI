from selenium import webdriver
import pandas as pd
from pathlib import Path
import logging
import time

csv = pd.read_csv("./food_list.csv")

logging.basicConfig(filename='logs.log', encoding='utf-8', level=logging.INFO)
logging.info("Program started")

browser = webdriver.Chrome(f'C:\Dev\Drivers\chromedriver111.exe')

food_data_file_path = Path('./food_data/')


def getTableData(browser_table):
    t_heads = browser_table.find_elements_by_tag_name('th')
    for e in t_heads:
        table[0].append(e.text)

    body = browser_table.find_element_by_tag_name('tbody')
    bodyRows = body.find_elements_by_tag_name('tr')
    for row in bodyRows:
        new_row = []
        for element in row.find_elements_by_tag_name('td'):
            new_row.append(element.text)
        table[1].append(new_row)


for item in csv["Código"]:
    url = "http://www.tbca.net.br/base-dados/int_composicao_alimentos.php?cod_produto=" + item
    browser.get(url)
    logging.info("Accesing URL=%s" % (url))
    table= ([],[])
    browser_table = browser.find_element_by_tag_name('table')
    try:
        logging.info("Getting food data... FoodCode=%s" % (item))
        start = time.time()
        getTableData(browser_table)
        end = time.time()
        logging.info("Getting food data succesfuly! Food Code=%s" % (item))
        logging.info("Time elapsed: %f" % (end-start))
    except:
        logging.error("Get food data failed! FoodCode=%s" % (item))
    df = pd.DataFrame(table[1],columns=table[0])
    file_name = item + ".csv"
    logging.info("Saving food data to file...")
    df.to_csv(food_data_file_path.joinpath(file_name), index=False)
    logging.info("Food data saved to file: %s" % (file_name))

logging.info("Total program time elapsed: %fs" % (time.perf_counter))

webdriver.quit()