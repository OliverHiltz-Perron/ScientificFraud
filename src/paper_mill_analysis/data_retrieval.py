# src/paper_mill_analysis/data_retrieval.py

import urllib.request
from bs4 import BeautifulSoup
import pandas as pd

def fetch_data(contract_number: int, author_position: int) -> BeautifulSoup:
    """Fetch and parse HTML from paper mill contract URL."""
    url = f'https://web.archive.org/web/20210617233318/http://123mi.ru/1/contract.php?r=1&n={contract_number}&m={author_position}'
    html = urllib.request.urlopen(url)
    return BeautifulSoup(html, 'html.parser')

def extract_contract_number(parsed_html: BeautifulSoup) -> str:
    """Extract contract number from parsed HTML."""
    h1_tag = parsed_html.find("h1")
    if h1_tag and (font_tag := h1_tag.find("font")):
        return font_tag.get_text().split('.')[0]
    return None

def extract_titles_and_scopus(parsed_html: BeautifulSoup) -> tuple:
    """Extract Russian and English titles, and Scopus data."""
    para = parsed_html.find_all("p")[1]
    scopus_russian_title = para.get_text()
    russian_title_all = scopus_russian_title.split('«')[1].split('»')[0]
    
    russian_title, english_title = (russian_title_all.split('\n') 
                                  if '\n' in russian_title_all 
                                  else (russian_title_all, 'no suspected english title'))
    
    try:
        scopus = scopus_russian_title.split('(')[2].split(')')[0]
    except IndexError:
        scopus = scopus_russian_title
        
    return russian_title, english_title, scopus

def extract_web_of_science(parsed_html: BeautifulSoup) -> str:
    """Extract Web of Science data from parsed HTML."""
    para = parsed_html.find_all("p")[1]
    if 'Web of Science' in para.get_text():
        try:
            return para.get_text().split('(')[3].split(')')[0]
        except IndexError:
            return para.get_text()
    return False

def extract_price(parsed_html: BeautifulSoup) -> str:
    """Extract price data from parsed HTML."""
    para = parsed_html.find_all("p")[6]
    return para.get_text().split('Общая стоимость услуг, выполняемых Исполнителем в рамках настоящего Договора, составляет ')[1].split(' (')[0]

def retrieve_paper_data(max_contracts: int = 1009, max_authors: int = 8) -> pd.DataFrame:
    """Retrieve all paper data from paper mill website."""
    df_paper = pd.DataFrame()
    
    for contract_number in range(1, max_contracts):
        for author_position in range(1, max_authors):
            parsed_html = fetch_data(contract_number, author_position)
            
            contract_num = extract_contract_number(parsed_html)
            russian_title, english_title, scopus = extract_titles_and_scopus(parsed_html)
            web_of_science = extract_web_of_science(parsed_html)
            price = extract_price(parsed_html)
            
            df = pd.DataFrame({
                'contract_link': [f'http://123mi.ru/1/contract.php?r=1&n={contract_number}&m={author_position}'],
                'Contract_number': contract_num,
                'Base_title': [russian_title],
                'First_title': [russian_title],
                'Suspected_second_title': [english_title],
                'Price_Ruble': price,
                'contract_number': f"{contract_num}.{author_position}",
                'Scopus': scopus,
                'Web_of_science': web_of_science
            })
            
            df_paper = pd.concat([df_paper, df])
    
    return df_paper.reset_index(drop=True)