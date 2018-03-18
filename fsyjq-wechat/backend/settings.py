"""
Django settings for backend project.

Generated by 'django-admin startproject' using Django 1.11.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os
import datetime

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'gri)@qh)93@qlme_1oi*pr$i14fn*c9!3^^6p13+p*=kg)pocg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1', 'fsyjq.roswellcsy.com', 'fsyjq-admin.roswellcsy.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'gunicorn',
    'rest_framework',
    'api',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CORS_ORIGIN_WHITELIST = (
    # '*'
    '127.0.0.1:8080',  # 请求的域名
    'localhost:8080',
    'localhost',
    'localhost:9528',
    'fsyjq.roswellcsy.com'
)

ROOT_URLCONF = 'backend.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'backend.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        # 开发环境
        'NAME': 'fsyjq-dev',
        # 生产环境
        # 'NAME': 'fsyjq',
        'OPTIONS': {
            'charset': 'utf8mb4',
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",
        },

        # 开发环境
        'USER': 'fsyjq',
        'PASSWORD': 'Gdkyit2018%',
        'HOST': 'rm-wz9ec4kz5ildi1t96o.mysql.rds.aliyuncs.com',
        'PORT': '3306',
        # 正式环境
        # 'USER': 'fsyjq',
        # 'PASSWORD': 'Gdkyit2018%',
        # 'HOST': 'rm-wz9ec4kz5ildi1t96o.mysql.rds.aliyuncs.com',
        # 'PORT': '3306',
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')


# Media files(jpg)
# MEDIA_URL = '/media/'

# MEDIA_ROOT = os.path.join(STATIC_ROOT, 'media')


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    # 'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    # 'PAGE_SIZE': 10,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
    ),
}

AUTH_USER_MODEL = 'api.User'

JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=30),
}

# 七牛云对象存储配置

QINIU_ACCESS_KEY = 'wzvjBgDiFHcFCC51s-mRSJDgZNZH-d1bj-2g6E-M'
QINIU_SECRET_KEY = 'cVYKZjPrSeuLnU1HQOQ7br3JGzMa54VKMmAHVjYm'
QINIU_BUCKET_NAME = 'fsyjq'
QINIU_BUCKET_DOMAIN = 'fsyjq-static.roswellcsy.com'
QINIU_SECURE_URL = False      #使用http 


# PREFIX_URL = 'http://'
# QINIU_BUCKET_DOMAIN + 

MEDIA_URL = '/'
MEDIA_ROOT = os.path.join(MEDIA_URL, '')

DEFAULT_FILE_STORAGE = 'qiniustorage.backends.QiniuMediaStorage'

# STATIC_URL = '/static/'

# STATIC_ROOT = os.path.join(STATIC_URL, '')

# # STATICFILES_DIRS = [
# #     os.path.join(STATIC_URL, ''),
# # ]


# STATICFILES_STORAGE = 'qiniustorage.backends.QiniuStaticStorage'