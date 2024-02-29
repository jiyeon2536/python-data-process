# 01 PJT

- 날짜 : 2023년 7월 21일
- 주제 : [도전] 금융 데이터 수집
- 목표 : 금융기관 API를 통해 데이터를 수집하고, 필요한 정보를 추출 및 가공하여 정리한다.

## 1️⃣ API 활용하기

- api key 를 발급 받고 데이터를 끌어 온다
- 난이도 : 3 / 5 (어려울수록 5에 가깝다)
- 느낀 점 :  
  공식 문서를 참고하면서 진행했음에도 오류가 나는 경우가 다수 있었다.  
  api 사용 예제에 나와있는 코드를 그대로 받아 적었는데 없었으면 못했을 것 같다.  
  url의 일부를 직접 수정하는 과정도 약간은 혼란스러웠는데 점점 익숙해져야 할듯.

## 2️⃣ 데이터 추출 - json으로 변환하기

- 받아온 데이터를 json으로 변환한다.
- 난이도 : 2 / 5
- 느낀 점 :  
  정확하게 코드만 쓰면 된다. 하지만 내가 직접 쓸 수 있었을까하는 의문은 남는다.

## 3️⃣ 데이터 추출 - 필요한 정보만 리스트로 각각 추출하기

- json으로 받은 데이터를 필요한 부분만 출력한다.
- 난이도 : 2 / 5
- 느낀 점:  
  처음에는 조금 헤매는데, 데이터의 타입 - 리스트인지 딕셔너리인지,  
  그래서 어떻게 접근해야 하는지만 익히면 어렵지 않게 가져올 수 있었다.

## 4️⃣ python dictionary 데이터 추가하기

- 딕셔너리를 생성해서 키와 밸류를 넣어 새로운 데이터를 추가한다.
- 난이도 : 3 / 5
- 느낀 점 :  
  딕셔너리에 값을 넣어 본 것이 처음이라 헤맸는데 여러번 반복학습을 하는 것이 큰 도움이 되었다.  
  정확한 이유는 모르겠지만 이번 도전과제에서 가장 재미있는 과정이었다.

```
# 딕셔너리에 키 값에 따라 데이터 생성하는 방법
my_dict = {} # 새로운 딕셔너리를 생성한다
my_dict['key1'] = "value1"
print(my_dict) # { 'key1' : 'value1' }
```

## 5️⃣ 데이터 가공 - 옵션 리스트 키 값 변경하기

- 변수 형식의 키 값을 이해하기 쉽게 한글로 변경하는 과정
- 난이도 : 4 / 5
- 느낀 점:  
  여러 겹으로 중첩된 데이터에 접근하는 것이 이리도 어려운 일임을 알게 되었다.  
  리스트에 접근하는 방법과 딕셔너리에 접근하는 법,  
  그 안에서도 키와 밸류에 각각 들어가고 수정하는 과정이 뒤섞여 혼란스러웠다.  
  정확한 개념 파악과 방법 습득이 절실히 필요하다 느꼈다.

## 6️⃣ 데이터 가공 - 새로운 값을 만들어 반환

- 추출한 데이터들을 연결하여 필요한 부분만 출력하고, 보기 좋은 데이터로 만든다.
- 난이도: 5 / 5
- 느낀 점:  
  원하는 데이터 생성을 위해 정확한 코드를 짜는 것이 정말 중요한 과정이었다.  
  역시나 여러 겹의 리스트와 딕셔너리로 만들어진 데이터의 요소 내에 접근하는 것이 어려웠다.  
  특히 중첩 반복문에서 어디에서 정보값을 초기화하고 새로 리스트를 생성해야 하는지나,  
  어디에서 리스트를 업데이트 해야하는지 등에서 큰 어려움을 겪었다.  
  논리적으로 차근차근 처리 과정을 프로그램하고 이해하는 능력이 부족함을 느꼈다.

## ✅ 요약

- 개선할 점

  - 전체적으로 난도가 높게 느껴졌던 도전과제였다.
  - 이는 아직 프로그래밍 실력, 특히 사고력이 부족함에 있다고 생각한다.
  - 원하는 결과에 이르기까지 소요한 시간이 다른 사람에 비해 현저히 길었다.
  - 내 코드가 가독성이 좋고 잘 쓰인 코드인지에 대한 의문이 남는다.
  - 동료들에게 도움을 청하는 것이 어려웠는데 더 적극적으로 질문하는 능력을 키우고 싶다.

- 배운 점
  - 도움을 받을 때 코드를 직접 다 넘겨받지 않고 논리적 오류가 있는 부분의 피드백을 받았다.
  - 이 과정에서 스스로 논리적으로 정확한 사고를 하는 방법을 익혔다.
  - 데이터 타입, 데이터 구조 등 파이썬의 기초 문법의 학습을 더욱 철저히 해야 겠다는 배움이 있었다.

---

# 02 PJT

- 날짜 : 2023년 7월 28일
- 주제 : [도전] 넷플릭스 주가 데이터 분석
- 목표 : 파이썬과 Pandas를 사용하여 데이터를 처리한다(데이터 사이언스 기초)

## 1️⃣ 데이터 공유 플랫폼 사용하기

- 캐글을 활용하여 데이터를 다운로드 받아 활용한다.
- 난이도 : 2 / 5 (어려울수록 5에 가깝다)
- 느낀 점 :  
  지난 주 api에서 추출하는 것보다 훨씬 직관적이고, 파일도 엑셀로 제공되어서 쉬웠다.
  데이터 공유 플랫폼의 존재를 알게 되었다.

## 2️⃣ 데이터 전처리 - 데이터 읽어오기

- Pandas 를 사용하여 csv 파일(NLFX.csv)을 DataFrame 으로 읽어온다.
- 일부 데이터만 읽어오도록 구성한다. 칼럼의 범위를 range()로 설정.
- 난이도 : 2 / 5
- 느낀 점 :  
  csv 데이터를 처음 봤는데 깔끔하고 편리했다.

## 3️⃣ 데이터 전처리 – 2021년 이후의 종가 데이터 출력하기

- 읽어온 csv 파일 중 2021년 이후의 데이터만 필터링한다.
- 필터링을 위해 to_datetime()으로 문자열을 날짜형식으로 변경한다.
- 2021년 이후 데이터만 뽑아 저장하여 활용한다.
- matplotlib을 사용하여 x축과 y축 변수를 넣어 그래프를 만든다
- x축의 데이터를 읽기 쉽게 만든다
- 난이도 : 2 / 5

## 4️⃣ 데이터 분석 – 2021년 이후 최고, 최저 종가 출력하기

- 종가(Close) 필드를 활용한다.
- 내장 함수인 min(), max()를 활용한다.
- 난이도 : 2 / 5
- 느낀 점 :  
  활용할 수 있는 함수가 많아서 편리했다.

## 5️⃣ 데이터 분석 - 2021년 이후 월 별 평균 종가 출력하기

- 월 별로 그룹화하여 평균 종가를 계산한 새로운 DataFrame 을 만들어 그래프로 시각화하기
- 과정
  - 그룹화를 하기 위해 연과 월 칼럼을 추가한다
  ```python
  df_after_2021["Year"] = df_after_2021["Date"].dt.year
  df_after_2021["Month"] = df_after_2021["Date"].dt.month
  ```
  - .groupby() 함수를 사용한다. 두 가지 기준을 넣는 것도 가능 ["Year", "Month"]
  - 평균값을 구하는 함수 .mean() ["Close"]칼럼의 평균값을 구한다는 점을 확실히 하는 것을 놓칠뻔했다.
  - 여기에서 명세서 상의 x축 월 표시는 두 달 기준이라 명세서 상의 구현만 한다면 그대로 plot의 x 축에 넣으면 된다.
  - 나는 모든 월을 x 축에 추가했다.
  - 이를 위해 연월을 문자열로 바꾸어 합친 다음 리스트로 만들어 각각 할당했다.
  - 이 과정에서 시간소요가 컸다.
  - 명세서를 정확히 읽어야함을 배웠다..
  - 대신 .DataFrame()을 통해 값을 데이터프레임으로 만드는 법을 배웠다.
- 난이도 : 4 / 5
- 느낀 점:  
  월 뿐만 아니라 연-월 방식으로 나누었다가 다시 합치는 과정이 복잡했다.
  활용할 수 있는 함수가 명확한데 문법을 정확히 써서 원하는 것을 얻는 건 어려웠다.
  코드를 더 간결하게 쓰는 연습이 많이 필요하다.

## 6️⃣ 데이터 시각화 – 2022년 이후 최고, 최저, 종가 시각화하기

- 2022년 이후 데이터만 필터링한다.
- 세가지 요소를 가진 그래프를 시각화한다.
- 난이도: 2 / 5

## ✅ 요약

- 지난 주 과제에 비교했을 때 쉽게 느껴졌다.
- 데이터를 읽어오고 처리하는 새로운 툴을 익히는 과정이 매우 흥미로웠다.
- Numpy, Pandas, Maplotlib 문법을 외우지는 못하더라도 어떻게 이용할지 여러 자료들을 통해 알게 되었다.
- 데이터를 처리할때는 데이터의 타입이 중요하다는 것을 배웠다.

---

# 03 PJT

- 주제: 부트스트랩을 활용하여 포트폴리오 만들기
- 날짜: 2023년 08월 04일

1. 메뉴바

- 부트스트랩의 네비게이션바를 사용하였고 리스트 클릭시 페이지내의 해당 섹션으로 이동합니다

2. 헤더

- 사진에 글을 position absolute 로 띄웠습니다.

3. 자기 소개

- 소개 및 관련 링크를 넣어서 연결되도록 했고, 부트스트랩 그리드를 이용했습니다

4. 프로젝트

- 부트스트랩의 카드 기능을 이용했습니다.

5. 기술 스택

- 로고를 넣었고 flex 디스플레이로 배치했습니다.

6. 교육

- 아직 작업중에 있습니다.

7. 연락처

- 로고에 링크를 걸어서 바로 이동가능하게 했습니다.

부트스트랩과 css를 활용하였습니다.

---

# 04 PJT

- 날짜 : 2023년 10월 06일
- 주제 : [도전] Django에서 데이터 사이언스 활용하기
- 목표 : django환경에서 Pandas, matplotlib을 활용해 데이터를 처리한다

## 1️⃣ 데이터 공유 플랫폼 사용하기

- 캐글을 활용하여 데이터를 다운로드 받아 활용한다.
- 난이도 : 2 / 5
- 느낀 점 :  
  잘 정리된 사이트에서 곧장 받아올 수 있었음.
  파일의 경로는 앱 내 data 폴더를 생성하여 저장.

## 2️⃣ Django 프로젝트와 앱 만들기

- django 프로젝트와 앱을 만들어 서버로 보낼 수 있게 만든다.
- 난이도: 3 / 5
- 느낀 점:
  지난 2주동안 배운 내용을 활용하여 어렵지 않게 url, view, template을 작성하였다.
  뷰함수 내에서 데이터만 잘 처리하고 가공하면 되었다.

## 3️⃣ problem 1

- Pandas 를 사용하여 csv 파일을 DataFrame 으로 읽어온다.
- 난이도 : 3 / 5
- 느낀 점 :  
  데이터의 행과 열이 어떻게 구성되었는지에 대한 감이 잡히지 않아서 파악하는데 시간이 걸렸다.
  참고자료의 도움으로 출력할 수 있었다.

## 4️⃣ problem2

- 일별 최고, 평균, 최저 온도를 선 그래프로 출력.
- 날짜 필드는 날짜 형식으로 변환하여 사용
- matplotlib을 사용하여 x축과 y축 변수를 넣어 그래프를 만든다
- 난이도 : 3 / 5
- 느낀 점:
  그래프 내에 주석, 그리드 등을 넣는 방법을 배웠고,
  다수의 그래프를 하나의 표 안에 넣는 법도 알았다.

## 5️⃣ problem3

- 월 별 최고, 평균, 최저 온도의 평균을 선그래프로 시각화
- 날짜 필드는 날짜 형식으로, 온도필드는 숫자형식으로 변환
- 난이도 : 4 / 5
- 느낀 점 :  
  지난 2회차 관통프로젝트에서도 동일한 부분에서 어려움을 겪었다.
  그때 적어둔 코드를 많이 참고하여서 문제를 해결했다.
- 과정
  - 그룹화를 하기 위해 연과 월 칼럼을 추가한다
  - .groupby() 함수를 사용한다. 두 가지 기준을 넣는 것도 가능 ["Year", "Month"]
  - 평균값을 구하는 함수 .mean()
  - 만들어진 월평균 데이터의 개수와 x축의 날짜 개수가 대응하지 않아 문제가 있었다.
  - 날짜도 월별로 다시 묶어주는 처리를 거쳤다.
  - x축에 출력하는 데이터의 개수 조절하는 방법을 배웠다.

## 6️⃣ problem4

- 기상현상의 발생횟수('Events' 컬럼)를 히스토그램으로 출력한다.
- 난이도 : 3 / 5
- 느낀 점:  
  데이터 전처리를 하는 과정이 까다로웠는데, 파이썬 문법과 자료구조를 활용하여 해결하였다.

## ✅ 요약

- django 활용과 데이터 사이언스가 합쳐지면서 배웠던 것을 결합한다는 점에 흥미를 느끼며 진행하였다.
- jupyter notebook으로 바로 출력할 수 있어 눈으로 확인이 쉬웠던 점에 비해, 에러가 있으면 아무것도 확인할 수 없다는 점이 달랐다.

---

# 05 PJT

- 날짜 : 2023년 10월 13일
- 주제 : [도전] 키워드 검색량 분석을 위한 데이터 수집
- 목표 : 구글 검색엔진을 활용하여 검색 결과에 따른 트렌드 분석 애플리케이션을 구현한다.

## 1️⃣ 모델 클래스 정의

- keyword, trend 모델 정의

## 2️⃣ url 작성

- 앱 내에 url 파일 생성하여 분리함

## 3️⃣ keyword

- 키워드 저장 및 keyword.html 렌더링
- 난이도: 2 / 5
- 느낀 점:
  키워드를 입력받고 저장하여 화면에 출력하면 되는 간단한 태스크였다.

## 4️⃣ keyword_detail

- 키워드 삭제 및 keyword.html 로 리디렉션
- 난이도 : 3 / 5
- 느낀 점 :  
  삭제된 후에도 키워드 번호가 누적 갱신되는 문제를 해결하는 데에 어려움을 겪었다.

## 5️⃣ crawling

- 크롤링 수행 및 crawling.html 렌더링
- 난이도 : 4 / 5
- 느낀 점:
  크롤링하는 과정 자체가 처음이라 어려움이 컸다. 직접 코드를 쓰면서 익힐 수 있었다. 크롤링한 데이터를 가공해서 출력하는 것도 중요하다는 것을 배웠다.
  처음에는 크롤링을 하여 테이블에 저장하는 과정에서 이미 존재하는 name의 keyword 는 갱신만 하는 조건을 잘 맞추지 못하여 같은 name 의 keyword 라도 계속 테이블에 저장되는 문제가 발생하였다. 크롤링을 진행하는 view 메서드에서 테이블에서 데이터를 뽑아올 때 어떤 조건의 필터를 걸고 어떤 변수를 입력하면 뽑히는 자료들을 shell_plus로 하나씩 확인해 보면서 비교하려는 조건과 비교할 자료를 찾는 과정에서 데이터 테이블 중 내가

## 6️⃣ crawling_histogram

- 크롤링 수행 후 수행 결과 막대 그래프 생성 및 crawling_histogram.html 렌더링
- 난이도 : 3 / 5
- 느낀 점 : 이전회차 프로젝트에서 활용했던 것을 그대로 가져와서 어려움이 적었다. 지난번에는 csv 파일을 사용했던 데 비해 이번에는 sql 테이블을 어떻게 가져올 것인가에 대한 고민이 있었다.

## 7️⃣ crawling_advanced

- 지난 1년을 기준으로 크롤링 수행 후 수행 결과 막대 그래프 생성 및 crawling_advanced.html
- 난이도 : 2 / 5
- 느낀 점: 앞의 과정에서 이미 전체기간의 크롤링과 그래프 생성을 진행하였기 때문에 advanced 과정에서는 default로 설정된 전체 기간 crwaling 을 진행했던 경우의 url 에 최근 1년으로 변경한 경우의 url 의 변경사항 중 기간을 설정하는 "&tbs=qdr:y" 를 추가하여 진행하고, 이미 전체기간을 조회한 데이터들이 trends 테이블에 search_period 가 "all" 인 상태로 저장되어있기 때문에 최근 1년의 검색건수 정보를 테이블에 추가할 때 같은 키워드라도 search_period 를 "year" 로 설정하여 crwaling_advanced.html 템플릿에서는 지난 1년의 crawling 결과들만 선택하여 그래프를 작성하였다.
  앞의 전체기간 크롤링과 상당히 유사한 작업이기 때문에 여기서 중요한 것은 검색조건을 바꾸었을때 어떠한 점이 변하는가를 잘 파악하고 이를 구분하여 내가 원하는 데이터를 가져와 저장하고 활용하는 것이라고 느꼈다.

## ✅ 요약

- 크롤링이라는 새로운 개념을 배우고 바로 활용한다는 것이 흥미로웠다.
- 페어와 함께 진행하면서 어렵거나 진행이 막히는 경우 즉각적인 질문과 보완이 가능하여 정말 도움이 많이 되었고 혼자 프로젝트를 진행하는 경우보다 객관적으로 코드를 작성할 수 있었고 각자 자신이 진행한 부분에서 보이지 않던 문제나 개선이 필요한 부분도 바로 파악이 가능하고 보완해줄 수 있어서 좋았다.

---

# 08 PJT

- 날짜 : 2023년 11월 3일
- 주제 : [도전] 알고리즘 구현 및 성능 측정
- 목표 : Django 에서 알고리즘을 구현하고 API를 활용하여 서버에서 성능을 측정한다

## 1️⃣ CSV 데이터를 DataFrame으로 변환 후 반환

- Numpy 또는 Pandas 로 CSV를 읽어온다
- DataFrame으로 변환한다.
- 난이도: 2 / 5
- 느낀 점: csv 파일을 django에서 데이터 프레임으로 변환하는 작업을 진행하였다.
  처음엔 함수를 작성하여 데이터를 로드하였는데, 검색을 통해 조금 더 효율적으로 데이터를 받고 프레임으로 한번에 변환하는 '.read_csv'을 통해 진행하였다.
  변환에도 다양한 방법이 있어서 효율적이고 빠른 방법을 찾는 것이 중요함을 느꼈다

## 2️⃣ 결측치 처리 후 데이터 반환

- Pandas 라이브러리의 특정 값 반환 함수 활용
- 비어있는 값을 'NULL' 문자열로 치환 후 DataFrame 반환
- 난이도: 3/ 5
- 느낀 점: 데이터프레임으로 변환한 데이터들 중에 비어 있는 값을 null로 변환하였다.
  이는 장, 단점이 있는데 장점의 경우에는 빈 값이 있지 않기 때문에 이후에 다른 데이터 형식으로 변환 할 때 에러가 나지 않지만, null값일 경우에는 정수로 되어있는 열의 경우에는 값의 평균 등을 구하는 작업을 할 때 에러가 날 수 있기 때문에 추가적인 조건을 걸어줘야하는 점이 있다 따라서 적절하게 결측치를 관리해야함을 느꼈다

## 3️⃣ 알고리즘 구현하기

- '나이' 필드에서 평균 나이를 구한다
  `df['나이'].mean()`
- 평균 나이와의 차이를 기준으로 데이터를 정렬하여
  `df.sort_values(by=['diff'], inplace=True)` - inplace 속성을 true로 설정해 주어야 데이터 자체가 바뀐다는 점이 중요했다.
- 상위 10개만 반환한다.
  `top_tens = df.head(10)`
- 난이도: 2 / 5
- 느낀 점: pandas 라이브러리 메소드를 활용하여 어렵지 않게 데이터를 뽑아낼 수 있었다.
  필요한 기능을 제공된 자료 또는 구글링을 통해 직접 검색하고 찾아내는 능력이 또한 중요하다는 것을 알았다.
  또한 메소드의 반환이나 속성등을 정확히 파악하고 활용하는 것도 중요하다는 점을 깨달았다.

## 4️⃣ Locust 를 활용한 알고리즘 성능 측정

- Locust 스크립트 파일을 작성한다.
- 구현한 알고리즘 성능을 테스트한다.
- 내 알고리즘과 다른 사람의 알고리즘에 대해 성능을 비교하고 분석한다.
- 난이도 : 2 / 5
- 느낀 점 : Locust라는 새로운 도구를 사용하는 것이 흥미로웠다.
  직접 알고리즘을 서버에 띄워서 성능측정을 해보았고, 또한 locust 가 출력한 결과값을 해석하는 것도 중요했다.
  처음에는 그래프의 수치가 너무 낮게나와서 오류가 난 것으로 생각했는데 자세히 확인했을때 낮은 값이지만 제대로 출력되는 것을 확인했다.

![numberofusers](./readmesource/number_of_users_1698992900.png)

## ✅ 요약

- 새로운 도구를 활용하고 여태 배운것을 복습하고 통합하는 과정이 흥미로웠다.
- 실제로 서버에 사람들이 사용한다는 상황을 가정해 테스트 해보며 앞으로 프로젝트에서 활용할 강력한 도구를 배워 기뻤다.
