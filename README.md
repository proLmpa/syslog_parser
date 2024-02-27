# syslog_parser

1. 가상환경 만들기

2. 정규식 적용
 i. 로그 파일 읽기
 ii. JSON화 (보류)

3. Flask로 띄우기
 출처 : https://m.blog.naver.com/21ahn/221830372908

4. render_template으로 HTML 게시
 출처 : https://m.blog.naver.com/xowww/220858579104

5. 파이썬 HTML <table> 작성
 i. 문자열 포매팅
 출처 : https://smart-worker.tistory.com/55

 ii. <table> 작성 
 출처 : https://stackoverflow.com/questions/24620442/creating-a-html-table-with-python

=======================================
개선 사항
 1. Windows에서 배포 - 웹 서버에 띄우는 방법 IIS 등 공부하기 (성공)
 2. 실시간 변화 감지 -> 1 / 5/ 10 초 단위로 refresh
 3. 달력에서 날짜 선택 기능
=======================================

과제. Windows IIS에 웹 서버 띄우기

접근1) https://blog.gapmoe.net/entry/IIS%EC%97%90-Flask-%EC%97%B0%EA%B2%B0%ED%95%98%EA%B8%B0
1. CGI 허용하기
 => 제어판 > 프로그램 > Windows 기능 켜기/끄기 > 인터넷 정보 서비스 > World Wide Web 서비스 > 응용 프로그램 개발 기능 > "CGI 허용"
 - 출처 : https://blog.naver.com/PostView.nhn?blogId=choda100&logNo=220553445812

2. 'Bad Request - Invalid Hostname, HTTP Error 400. The request hostname is invalid.' 에러 발생
 400 : "서버가 크라이언트의 요청을 이해하지 못했다."
 -> 모든 IP 주소에 대한 접근 허용
 - 출처 : https://stackoverflow.com/questions/4831097/bad-request-invalid-hostname-iis7

3. '500 - <handler> scriptProcessor를 <fastCGI> 애플리케이션 구성에서 찾을 수 없습니다.' 에러 발생
 web.config의 요청 경로를 '*' 에서 '*.php'로 수정
 - 출처 : https://holjjack.tistory.com/280

4. '403.14 Frobidden - 웹 서버가 이 디렉터리의 내용을 표시하지 못하도록 구성되었습니다' 에러 발생
 디렉토리 내용 표시 허용
 - 출처 : 

5. localhost:8000 입력 시 프로젝트 파일들이 들어간 파일 시스템이 출력된다.
=> 실패

접근2) https://urame.tistory.com/entry/IIS%EC%99%80-Flask-Python-%EC%97%B0%EB%8F%99#:~:text=IIS%EC%99%80%20Flask%20%28Python%29%20%EC%97%B0%EB%8F%99%201%201.%20IIS%EB%A5%BC%20%EC%82%AC%EC%9A%A9%ED%95%98%EA%B8%B0,%ED%95%9C%EB%8B%A4.%20Python%20%ED%8F%B4%EB%8D%94%EC%97%90%20IIS%20%EA%B6%8C%ED%95%9C%20%EB%B6%80%EC%97%AC%20%EA%B8%B0%ED%83%80%20%ED%95%AD%EB%AA%A9
=> 바로 성공!!!
