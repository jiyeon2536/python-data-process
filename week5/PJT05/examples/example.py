import requests
from bs4 import BeautifulSoup

def crawling_basic():
    # 가져올 웹 페이지 url
    url = 'https://quotes.toscrape.com/tag/love/'
    
    response = requests.get(url)
    
    # 우리가 얻고자하는 html 내용이 담김
    html_text = response.text
    
    # html을 파싱이 가능한 정리된 형태로 변환
    soup = BeautifulSoup(html_text, 'html.parser')
    
    print(soup.prettify())
    
    # 1. 태그로 검색하기
    # 1.1 가장 첫번째 태그에 해당하는 요소
    # 크롤링할 때는 항상 페이지 분석 -> 검색
    title = soup.find('a')
    print(f'제목: {title.text}')
    
    # 1.2 해당 태그 모든 요소
    a_tags = soup.find_all('a')
    for a_tag in a_tags:
        print(f'링크: {a_tag}')
        
    print(f'a 태그들 = {a_tags}')
    # 2. CSS 선택자로 검색하기
    # 2.1 css 선택자와 일치하는 첫번째 요소
    word = soup.select_one('.text')
    print(f'첫 번째 글 = {word.text}')
    
    # 2.2 css 선택자와 일치하는 모든 요소
    words = soup.select('.text')
    for w in words:
        print(f'글: {w.text}')
        
        
    with open('soup.txt', 'w', encoding='uft-8') as file:
        file.write(soup.prettify())
    
crawling_basic()