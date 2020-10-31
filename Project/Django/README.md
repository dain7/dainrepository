# Django Project

20.10.22
- 웹 프로그래밍 공부 (https://cowimming.tistory.com/59)
- Django 설치 --> 그러나 DB를 연결하는 과정에서 Django와 원래 쓰던 Oracle의 버전이 맞지 않아 삭제

20.10.23
- 파이썬은 3.7, Django는 3.12, Oracle은 18c로 진행한 결과 migrate에서 에러 X
- 장고 디렉토리 생성
- 데이터베이스 지정(oracle 연결)
- models.py 정의 (테이블 2개 생성) --> admin.py 수정

django 2버전 이상부터는 foreign key 조건에 on_delete문을 추가해줘야함.
models.ForeignKey('Question', on_delete=models.CASCADE,)

- URLconf 코딩

path(경로, 함수) --> 해당 경로에 들어가면 정해놓은 함수 실행

- Templates(.html)과 Views(함수) 코딩

보통 템플릿을 먼저 작성하고 함수를 작성한다.

20.10.30
- 회원가입 구현

20.10.31
- 로그인/로그아웃 구현
