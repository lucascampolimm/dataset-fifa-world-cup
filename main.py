from bs4 import BeautifulSoup
import requests
import csv
import json

url = 'https://pt.wikipedia.org/wiki/Copa_do_Mundo_FIFA'

html = requests.get(url).content

soup = BeautifulSoup(html, 'html.parser')

tabela = soup.find('table', class_='wikitable')

dados_copas = []

# Encontrando os elementos.
linhas = tabela.find_all('tr')
for linha in linhas:
    colunas = linha.find_all('td')
    if len(colunas) > 0:
        ano = colunas[0].get_text(strip=True)
        pais_sede = colunas[1].get_text(strip=True)
        campeao = colunas[2].get_text(strip=True)
        vice_campeao = colunas[3].get_text(strip=True)
        
        copa = {
            'ano': ano,
            'pais_sede': pais_sede,
            'campeao': campeao,
            'vice_campeao': vice_campeao
        }
        
        dados_copas.append(copa)

with open('dataset.csv', 'w', newline='', encoding='utf-8-sig') as arquivo_csv:
    campos = ['ano', 'pais_sede', 'campeao', 'vice_campeao']
    escritor_csv = csv.DictWriter(arquivo_csv, fieldnames=campos)
    escritor_csv.writeheader()
    escritor_csv.writerows(dados_copas)

with open('dataset.json', 'w', encoding='utf-8-sig') as arquivo_json:
    json.dump(dados_copas, arquivo_json, ensure_ascii=False, indent=4)

print('')
print('Dataset salvo com sucesso!')