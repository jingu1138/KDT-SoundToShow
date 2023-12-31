# my_settings.py

DATABASES = {
    'default':{
        # 1. 사용할 엔진 설정
        'ENGINE': 'django.db.backends.mysql',
        # 2. 연동할 MySQL의 데이터베이스 이름
        'NAME': 's2s',
        # 3. DB 접속 계정명  / 연결할 db에 따라 다를 수 있음
        'USER': '',
        # 4. DB 패스워드
        'PASSWORD': '',
        # 5. DB 주소 / 연결할 db에 따라 다를 수 있음
        'HOST': '127.0.0.1',
        # 6. 포트번호
        'PORT': '',
    }
}
SECRET_KEY = ""
