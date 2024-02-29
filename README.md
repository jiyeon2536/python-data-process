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

# 06 PJT

## 1️⃣ A. 유저 기능

1. 회원가입

- Django에서 제공하는 유저모델을 활용해서 CustomUserCreationForm을 만들었습니다.

2. 로그인 & 로그아웃

- Django에서 제공하는 로그인 폼과 메서드를 이용해서 로그인 및 로그아웃을 기능을 구현했습니다.

## 2️⃣ B. Boards 앱기능

1. 게시글 CRUD 기능

- 생성, 조회

  - 메인 화면에 게시글을 조회할 수 있는 기능을 구현했습니다.
  - 생성을 할 때에는 인증된 사용자만 할 수 있도록 구현하였습니다.

- 수정, 삭제
  - 인증된 사용자와 게시글을 쓴 작성자가 일치하는지 확인 후 수정 및 삭제가 가능하도록 구현하였습니다.

2. 댓글 생성, 삭제

- 인증된 사용자만 쓸 수 있도록 구현하였습니다. 삭제를 할 때는 본인이 작성한 것만 지울 수 있도록 하였습니다.

## 3️⃣ C. 프로필 페이지

- 회원 정보 출력

  - 프로필 페이지를 만들어서 유저의 정보가 나타나도록 하였습니다. 또한 해당 유저가 쓴 글과 댓글을 보여줄 수 있도록 하였습니다.
  - 프로필 페이지는 로그인하지 않아도 조회할 수 있도록 해주었습니다.

- 해당 회원이 작성한 게시글 목록

  - 게시글을 클릭하면 해당 게시글로 이동할 수 있도록 하였습니다.

- 해당 회원이 작성한 댓글 목록
  - 회원이 쓴 댓글들을 나타내 주었습니다.

## 4️⃣ D. 유저 팔로우 기능

- 프로필 페이지에 팔로워, 팔로잉 수를 표시

  - 프로필 페이지에 팔로워를 나타낼 수 있게 유저 모델에 팔로우를 추가해주었습니다.
  - html에 팔로우 및 팔로워 수를 나타내주었습니다.

- 로그인된 상태에서만 팔로우가 가능하도록, 자기 자신은 팔로우 할 수 없도록 기능 구헌

## 5️⃣ 트러블 슈팅 및 전체 소감

- 저희 조는 배운 내용들을 세명 모두가 구현해보기로 하였습니다. 진행하면서 까다로운 부분을 만나면 서로 의견을 공유하면서 작업을 진행하였습니다.

- 배운지 오래된 부트스트랩을 다시 이용하려다보니 ui를 만들기가 까다로웠습니다. 부트스트랩 docs를 다시 찾아보며 기능을 구현할 수 있도록 노력하였습니다.

## 6️⃣ 개인 소감

- 핵심 기능인 crud를 직접 구현하면서 배운 내용을 복습하고 익숙해 지는 과정이었습니다.
- 비교적 최근에 학습한 django보다도 프론트엔드 단의 css와 bootstrap을 다루는 데에 조금 더 어려움을 겪어서 꾸준한 복습이 필요하다는 점을 느꼈습니다.
- django를 이용한 백엔드단 뿐 아니라 프론트엔드를 구현하는 것도 다른 방식으로 흥미롭고 중요하다 느껴 다른 프레임워크도 학습하고자 하는 생각이 생겼습니다.

---

# 07 PJT

- 날짜 : 2023년 10월 27일
- 주제 : [도전] 금융 상품 데이터를 활용한 REST API Server 구축
- 목표 : 금융상품통합비교공시 API를 통해 조건에 맞는 데이터를 가져와 REST API 서버를 구축한다
- 역할분담 : 정은진(정기예금 상품 목록 DB 저장) / 김지연(전체 정기 예금 상품 목록 출력, 정기 예금 상품 추가하기, 금리가 가장 높은 상품의 정보 출력) / 임승환(특정 상품의 옵션 리스트 출력)

## 1️⃣ 모델 정의

- DepositProducts
- DepositOptions
- 저장할 정보를 필드로 설정하여 해당하는 데이터를 저장한다.

## 2️⃣ Url, View, Serializer 작성

- 기능

1. 정기 예금 상품 목록 DB 저장
2. 정기 예금 상품 목록 출력 & 데이터 삽입
3. 특정 상품의 옵션 리스트 출력
4. 최고 금리가 가장 높은 금융 상품과 당 상품의 옵션 리스트 출력

## 3️⃣ 정기예금 상품 목록 DB 저장

- 정기 예금 API로부터 전달받은 데이터 중 상품 목록 정보와 옵션 목록 정보를 DB에 저장하기
- 데이터 전처리
- 난이도: 4 / 5
- 느낀 점:
  API를 통해 데이터를 전달받고 저장하는 작업을 하는 것이 어려웠다.
  필드를 설정하고 외래키를 참조해서 데이터를 가져와야하는 부분에서 막혀서 오랜 시간을 소모했다. pk를 설정하고 객체를 그대로 가져오는 방법을 통해 해결했지만, 페어들의 도움을 많이 받아 협업의 중요성을 깨달았다.

## 4️⃣ 전체 정기 예금 상품 목록 출력

- DB에 저장된 정기예금 상품 목록 반환
- 난이도: 2 / 5
- 느낀 점:
  request method가 get일때를 조건으로 처리해서 알맞은 정보를 serializer로 넘겨서 출력하면 되어 간단했다.

## 5️⃣ 정기 예금 상품 추가하기

- 요청과 함께 전송한 데이터를 DB에 저장하기
- 난이도 : 2 / 5
- 느낀 점 :  
  위와 같은 함수 내에서 request method가 post일때를 조건으로 처리했고, 데이터 유효성 판단하여 올바를 때만 저장하도록 구현했다.
  명세서에 적힌 status 코드를 동일하게 구현하기 위해 raise exception은 따로 처리하지 않았다.

## 6️⃣ 특정 상품의 옵션 리스트 출력

- 상품 코드에 따라 해당 상품의 옵션 리스트를 출력한다.
- 난이도 : 3 / 5
- 느낀 점:
  특정 상품의 옵션 리스트를 반환하는 문제로, 여러개를 받을때 model.objects.filter(pk=pk)로 get대신 filter를 쓰는 것과 1:N 관계에서 many=True를 지정해 Serializer를 사용했습니다. 이전 프로젝트에 비해 상대적으로 어렵지 않았습니다.

## 7️⃣ 금리가 가장 높은 상품의 정보 출력

- 금리가 가장 높은 상품의 상세정보와 옵션을 반환한다
- 난이도 : 3 / 5
- 느낀 점 : 쿼리셋을 정리하고 그 정보에서 출력하여 다시한번 같은 값의 정보를 출력하여 옵션 리스트를 받는 과정을 신경써야 했다. 출력 데이터를 처리할 때 딕셔너리 형태로 바꾸는 과정을 거치는 것이 까다로웠다.

## ✅ 요약

- API 를 받아오는 과정은 이전에 해보았는데 다시 학습할 수 있었고, 과정에 대한 이해도가 높아졌다.
- 이론으로 배운 내용을 실제 데이터에 적용해보는 경험이 흥미로웠다.
- 트러블슈팅에 있어서 페어와의 협력 및 학급 동기들의 도움이 중요하다는 점을 다시한번 깨달았다.
- 또한 디버깅 과정에서 문제를 작은 단위로 쪼개어 출력하여 확인하는 과정을 거치는 것도 중요하다는 것을 알았다.

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

---

# 09 PJT

- 주제: [도전] 동영상 검색 관리 서비스 구현
- 담당 부분: B - 동영상 상세 정보 출력, CSS
- 내용:

1. 검색 결과에서 특정 비디오를 클릭하면 동영상 상세 정보를 출력
2. iframe 태그를 활용하여 동영상 재생

## 1️⃣ 어려웠던 점

1. 동영상 하나의 정보를 가져오는 URL을 찾는 데에 어려움이 있었습니다. 처음 접근시에는 기존에 요청했던 검색어 중에서 하나의 영상을 뽑아내는 방법을 구했습니다. 그랬더니 연관이 없는 영상들과, 단일 영상이 아닌 여러개의 영상 리스트가 정보로 들어왔습니다. YouTube API 공식문서를 다시 제대로 살펴읽으며 단일한 영상을 가져올 수 있는 URL은 쿼리가 다르다는 걸 알게되었습니다.
   최종적으로

```
const storeURL = `https://www.googleapis.com/youtube/v3/videos?key=${apikey}&part=snippet&id=${videoId}`;
```

이러한 url로 변경했을 때 단일 비디오에 접근이 가능했습니다.

2. CSS 를 구성하면서, 검색 결과가 나오는 페이지의 영상 썸네일에 위아래가 검은 여백을 포함한 이미지로 나오는 것을, 여백없이 콘텐츠만 있도록 수정하고자 했습니다. 처음 접근은 object-fit 속성을 이용했는데, 불가능했습니다. 도저히 찾기 어려워 교수님 도움을 요청했습니다. 그래서 YouTube 썸네일을 자르는 방법이 따로 있다는 것을 알게되었습니다.
   최종 코드는

```
<img :src="video.snippet.thumbnails.default.url.replace('default', 'mqdefault')" class="ratio ratio-4-3" />
```

이렇게 `default` 문자열을 `mqdefault`로 변경하여 구현했습니다.

## 2️⃣ 느낀점

가장 중요한 것은 API 사용 공식문서를 잘 살펴보는 것이라는 걸 깨달았습니다. 또, 썸네일관련하여 이전에도 같은 트러블을 겪은 적이 있었는데, 당시에는 로컬에 저장한 이미지 파일을 비율로 크롭하는 방법을 썼습니다. 이번에는 같은 트러블이지만 API를 통해 정보를 받아오는 방식이라 다른 접근법이 필요하다는 것을 깨달았습니다. 또, 한번 겪었던 문제들에 대해서는 반드시 기록으로 남겨서 다음번에 비슷한 문제들을 겪지 않도록, 또는 해결을 더 수월하게 하도록 해야겠다고 생각했습니다.
