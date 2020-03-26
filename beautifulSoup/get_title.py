import requests
from urllib.request import urlopen
from bs4 import BeautifulSoup # 정규표현식을 사용해서 크롤링한 데이터(html, xml 등)내에서 원하는 부분을 추출할 수 있도록 어시스트

'''
1. 데이터를 보낼때 requests는 딕셔너리 형태, urllib는 인코딩하여 바이너리 형태로 전송합니다.

2. requests는 요청 메소드(get, post)를 명시하지만 urllib는 데이터의 여부에 따라 get과 post 요청을 구분합니다.

3. 없는 페이지 요청시 requests는 에러를 띄우지 않지만 urllib는 에러를 띄웁니다.

r.textHTML 또는 XML 문서와 같은 텍스트 응답에는 r.content선호 될 것이며 이미지 또는 PDF 파일과 같은 "이진"파일 형식에는 선호 될 것입니다

r.text응답의 내용은 유니 코드 r.content로 표시되며 응답의 내용 (바이트)
'''

class SearchNews():

    pass

rq = requests.get('https://search.naver.com/search.naver?where=news&query=%EC%82%BC%EC%84%B1&sm=tab_srt&sort=1&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so%3Add%2Cp%3Aall%2Ca%3Aall&mynews=0&refresh_start=0&related=0')
#rq2 = urlopen('https://search.naver.com/search.naver?where=news&query=%EC%82%BC%EC%84%B1&sm=tab_srt&sort=1&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so%3Add%2Cp%3Aall%2Ca%3Aall&mynews=0&refresh_start=0&related=0')

bsObject = BeautifulSoup(rq.content, "html.parser")
#bsObject2 = BeautifulSoup(rq2, "html.parser")

''' find : 최초 하나만 추출
태그에 있는 id 검색 : id=, 
HTML 태그와 CSS class를 활용하여 추출 class_=
HTML 태그와 태그에 있는 속성 attrs={'':''}
텍스트 추출 .get_text()
'''
''' find_all : 모든 데이터를 리스트 형태로 추출
문자열 검색의 경우 'html.parser' -> 'html5lib' 형식
string = ''
'''

print(len(bsObject.find_all(class_='_sp_each_title')))
print(len(bsObject.find_all(class_='_sp_each_url')))

for val in bsObject.find_all(class_='_sp_each_title'):
    print(val['title'])