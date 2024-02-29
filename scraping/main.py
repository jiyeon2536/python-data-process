import requests
import bs4

# 현재 백준에 제출 현황을 스크래핑...!

cookies = {
    'OnlineJudge': 'jqul8h206b024qbl000pucs6t8',
    '_ga': 'GA1.1.1024011840.1697153802',
    '_fbp': 'fb.1.1697153802046.139122367',
    'bojautologin': '8abeec681de9e76140744dd275343520e9a78715',
    '_ga_C81GGQEMJZ': 'GS1.1.1697173614.2.1.1697174005.0.0.0',
    '__gads': 'ID=85ffe0a5c3e36ee5-22376883e3e4009f:T=1697153918:RT=1697174005:S=ALNI_MZvnFcu0wlRn-9OKlRHbJNCBDeyWA',
    '__gpi': 'UID=00000c5df026a4e5:T=1697153918:RT=1697174005:S=ALNI_MaabE7k1-6TGb051_DRBnFsr_Mkvw',
}


headers = {
    # 크롬 브라우저라 안내를 해줄 수 있는 메시지
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/117.0.0.0 Safari/537.36',
}

response = requests.get('https://www.acmicpc.net/status',
                        cookies=cookies, headers=headers)

# html 파싱을 위해 bs4 라이브러리 사용
soup = bs4.BeautifulSoup(response.text, 'html.parser')

# 테이블을 파싱
table = soup.select_one('#status-table')

# 테이블의 헤더들 출력
headers = table.find_all('th')
for header in headers:
    print(header.text, end=',')
print()

# 테이블의 데이터 출력
rows = table.find_all('tr')
for row in rows:
    tds = row.find_all('td')
    for td in tds:
        print(td.text, end=', ')
    print()
        