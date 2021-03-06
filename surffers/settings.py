"""
Django settings for surffers project.

Generated by 'django-admin startproject' using Django 3.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ocf-(@ymg*43crd=_0$)ji_hc!81in)k#^jyp1h&w)gk(*3s83'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']

# DEBUG = False
# ALLOWED_HOSTS = ["127.0.0.1"]

LOGIN_URL = '/accounts/login/?next=/'
LOGIN_REDIRECT_URL = '/'
#LOGOUT_REDIRECT_URL = '/blog'

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = BASE_DIR / 'emails'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.humanize',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'debug_toolbar',
    'apps.core',
    'apps.feed',
    'apps.profiles',
    'rest_framework',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    # 'allauth.socialaccount.providers.facebook',
    # 'allauth.socialaccount.providers.twitter',
    # 'allauth.socialaccount.providers.vk',
    "djpaddle",

]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',  #debag_toolbar
    
]



ROOT_URLCONF = 'surffers.urls'

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
                'djpaddle.context_processors.vendor_id',
                # 'djpaddle.context_processors.sandbox',
            ],
        },
    },
]

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

WSGI_APPLICATION = 'surffers.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
# DATABASES={
#    'default':{
#       'ENGINE':'django.db.backends.postgresql_psycopg2',
#       'NAME':'surffers',
#       'USER':'surff',
#       'PASSWORD':'123456god',
#       'HOST':'localhost',
#       'PORT':'5432',
#    }
# }

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / "static",
]


MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


#debag_toolbar
INTERNAL_IPS = [
    '127.0.0.1',
]

# Allauth
SITE_ID = 2

ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_EMAIL_UNIQUE = True
# ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

if DEBUG:
    EMAIL_BACKEND = 'django.core.mail.backends.dummy.EmailBackend'

# Provider specific settings
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}



# can be found at https://vendors.paddle.com/authentication
DJPADDLE_VENDOR_ID = '137716'

# create one at https://vendors.paddle.com/authentication
DJPADDLE_API_KEY = 'b85c4ed3e660cc4a5e1b778d31d1f256e6b2ffeabbade2f632'

# can be found at https://vendors.paddle.com/public-key
DJPADDLE_PUBLIC_KEY = """-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEA7mBSiQRLhX2JtfEe1+lp
RtK1kJDCTgxEuhD2Vq9hrf0ZkaV7avPWQDsW3V+xJtl7yu2q2Jsgg8K6xCuTQCYe
JTkMhp8Dr5vg61Z1L/NM6v76dxB0GbxsaDLOXIRIfkAoNVaXDi5htxnCAeuEQ/s4
LNPmmgkHnfglNhvBexSn3DYju/jdsWbjCc36G0XJrIloojWSMGdghdM6TltLnroc
p8N9f6L2V/+6q0bpCtpYUYd8iQveHxGJxXmsvYGSoNnoAm+rIQLOChdQI5Oz4kPJ
xxgUPhmF/qIrmcYM5x7sGE0v3EqPwwE6TXuwcMBuwOpvqA9PYIm7/wXpAE+Xnd0T
1428NbrPurWoKzL4OmH2Cq+16USJYUtvWXhP0wKq1zuJvtlr3KErjBBvSVElqqrU
HaVPNxiFaJV4CEf9uHV8I2bP6isvCuK93m0gi422/k4Leh85y4vG0p59HU7vmo2k
fak8GN+WiHjSpQOsi4r18rZFRc4hMMXhkNT1gTbC3OLu5D2bcczvPTdiFf8P5xal
ogdyB80pPDchPQ3ESCATAmV7heiMhDby4n3zzIjzFTUXYIw1fJ35b217AP42MOlB
7k/kbdlzxm8AncDABkl3LYDVmjVIuwbr2qWphrswimGzAHUhAC0smqEGmQouZMuv
uVe8MSlfjknQ013guRdp2eECAwEAAQ==
-----END PUBLIC KEY-----"""




