"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.0.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure--f2vjx$jc!ne=^=#owb&)o@&$fhby#&)_)wo2-e=q1h&um81pr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

### 추가 부분: 아이피 또는 도메인 추가
ALLOWED_HOSTS = ['127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'firstapp',
    'secondapp',
    'mainapp',
    'frontapp',
    'oracleapp',
    'nonmodelapp',
    'thirdapp',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'config.urls'

### HTML 파일이 위치할 곳 지정하기(front-end)
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    },
    ### 오라클 데이터베이스 추가
    'oracle': {
        'ENGINE': 'django.db.backends.oracle',
        'NAME': 'xe',
        'USER': 'gwangju_a',
        'PASSWORD': 'dbdb',
        'HOST':'localhost',
        'PORT':'1521',
    },
}

### 오라클 또는 Mysql 데이터베이스 등 외부 데이터베이스가 추가되는 경우
### - 추가된 DB를 사용할 app 지정
DATABASE_ROUTERS = [
    'oracleapp.router.DBRouter',
    'secondapp.router.DBRouter',
]

### Logging 처리
# - DB 실행 내용을 console 창에서 확인할 수 있도록 처리
LOGGING = {
    'version':1,
    'disable_existing_loggers':False,
    'handlers':{
        'console':{
            'level':'DEBUG',
            'class': 'logging.StreamHandler',
        }
    },
    'loggers':{
        'django.db.backends':{
        'handlers':['console'],
        'level':'DEBUG',
        }
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.0/topics/i18n/

### 한글 처리
# LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'ko-kr'

### 서울로 시간대 변경
# TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

### 정적 파일 관리(css, javascript, 이미지 등)
STATIC_URL = 'static/'
### 추가 []:웹에서 사용되는 경로 설정
STATICFILES_DIRS = [BASE_DIR / 'static']

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

### 로그인 상태에서 브라우저가 닫혔을 때, 세션 정보 삭제하기
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

###### Google Email SMTP 설정하기 ######
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = '107131n@gmail.com'
EMAIL_HOST_PASSWORD = 'tokrbtgxdnaehpby'
EMAIL_USE_TLS = True
DEFAULT_FROM_EMAIL = EMAIL_HOST_USER