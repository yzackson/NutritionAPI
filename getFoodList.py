from selenium import webdriver
import pandas as pd
from pathlib import Path


browser = webdriver.Chrome(f'C:\Dev\Drivers\chromedriver111.exe')

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

    



for i in range(1,55,1):
    table= ([],[])
    url = 'http://www.tbca.net.br/base-dados/composicao_alimentos.php?pagina=' + str(i) + '&atuald=6'
    browser.get(url)
    browser_table = browser.find_element_by_tag_name('table')
    getTableData(browser_table)
    df = pd.DataFrame(table[1],columns=table[0])
    path = Path('./food_list.csv')
    if path.is_file():
        df.to_csv('./food_list.csv', mode='a', index=False, header=False)
    else:
        df.to_csv('./food_list.csv')

browser.quit()