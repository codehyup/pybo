"""
1. 사이트에 들어가고 싶음(페이지 요청)
-> url 매핑을 해야함
-> config/urls.py에다가 url 매핑시키기
-> 매핑 시킬 때 사용한 함수를 만들기 위해 views.py 에다가 함수 추가
-> views.py에 있는 함수를 실행에 사이트 화면에 출력

2. config/urls.py 보단 pybo/urls.py에다가 작성하는게 좀 더 짜임새가 있음
-> config/urls.py에 include를 import해서 pybo/urls.py로 include시킴 {include('pybo.urls')}
-> pybo/로 시작되는 페이지 요청은 pybo/urls.py에 있는 url 매핑을 참고하라는 뜻
-> pybo/urls.py 파일 제작 후 url 매핑 시키기

3. 모델로 데이터를 관리하기
-> django는 ORM을 제공하기 때문에 쿼리문을 익히지 않아도 데이터 작업(테이블 생성) 가능.
    (ㄹㅇ 대박기술. sqlite3 테이블 제작 개 귀찮은데 ORM 때문에 완전 편함 ^^)
-> pybo/models.py에 모델 제작하기 (class를 만들면 그게 model역할을 함)
-> 클래스 제작 후 모델 속성 추가 {ex) subject, content, create_date}
-> model을 통해서 테이블을 제작하려면 앱을 추가해야함!
-> 앱을 추가하려면 config/settings.py에 pybo app등록 시켜줘야함
-> makemigrations 명령어를 통해 테이블 작업을 수행하기 위한 파일 생성
-> migrate 명령어를 통해서 테이블 생성

4. Admin 사용하기
-> createsuperuser 명령어를 통해서 admin 계정 생성
-> 장고 admin 계정에 로그인하기
-> 장고 admin 계정에서는 모델 관리가 가능함
-> 모델 관리하기 위해서는 pybo/admin.py에서 모델 임포트해서 사용해야함
-> Admin에서 데이터 검색 기능 추가하려면 QuestionAdmin 클래스 추가하고
    search_fieldxs = ['subject']를 추가
    
5. 질문 목록 조회 구현하기
-> pybo/views.py에서 Question 모델을 import해서 작성한 날짜의 역순으로 조회하기 위해
    order_by('-create_date')추가
-> Question 모델 데이터를 context 변수에 저장하기
-> render를 import해서 template 파일을 사용하여 화면에 출력하기
-> render 함수는 context에 있는 question_list를 pybo/question_list.html(템플릿)에 적용해
    HTML코드로 변환
-> config/settings.py에서 TEMPLATES 항목에 DIRS 추가하고 templates 파일 만들기
-> pybo/question_list.html 템플릿 파일 생성 후 템플릿 파일에 코드 작성
-> 템플릿 파일에 추가된 사이트를 url 매핑시키기
-> detail 함수를 views.py에 추가
-> detail 함수에 question_id를 매개변수로 추가
-> detail 함수에서 render 변수에 넣은 html 파일을 생성
-> 잘못된 주소에 접속할 수도 있으니 get_object_or_404를 추가

6. url 하드 코딩보다 별칭으로 사용하는게 편함
-> pybo/urls.py에 name 속성 부여
-> pybo/question_list.htlm에서 URL 별칭 사용
-> URL 별칭 중복 사용을 피하기 위해 pybo/urls.py에 URL 네임스페이스를 추가
-> 템플릿에서 namespace부분 추가하기
"""