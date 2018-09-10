
"""
Django settings for lab_core project.

Generated by 'django-admin startproject' using Django 1.9.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""
import datetime
import json
import os

import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

PROD = 'prod'
STAGING = 'staging'
DEV = 'dev'
CI = 'ci'
LOCAL = 'local'


APP_ENVIRONMENT = os.environ.get('APP_ENVIRONMENT', 'local')
DEVELOPER = os.environ.get('DEVELOPER', '').lower()

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '67qgta79^&vxil@_dchypwftn7=d_%k^$^*c3ok94s((p*v_&&@392'

# SECURITY WARNING: don't run with debug turned on in production!
if APP_ENVIRONMENT in (LOCAL, DEV, STAGING, CI):
    DEBUG = True
else:
    DEBUG = False

ALLOWED_HOSTS = ['.saracare.com.br', 'saracare.com.br', '.herokuapp.com', 'localhost', '.localhost', 'aplicativosara.com.br', '.aplicativosara.com.br']

AWS_ACCESS_KEY_ID = 'AKIAI5CNWGWDLQAGJH4Q'
AWS_SECRET_ACCESS_KEY = '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'

# GDAL_LIBRARY_PATH = '/usr/local/lib/libgdal.so'

DATA_UPLOAD_MAX_MEMORY_SIZE = None

if APP_ENVIRONMENT == PROD:
    AWS_S3_CUSTOM_DOMAIN = 'dlvv3jt2897qo.cloudfront.net'
    AWS_STORAGE_BUCKET_NAME = "lab-prod"

    STATICFILES_STORAGE = 'lab_core.s3utils.StaticRootS3BotoStorage'
    DEFAULT_FILE_STORAGE = 'lab_core.s3utils.MediaRootS3BotoStorage'

    # STATIC_URL = '/static/'
    # MEDIA_URL = '/media/'

    BASE_URL = 'https://' + AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com'
    MEDIA_URL = BASE_URL + '/media/'
    STATIC_URL = BASE_URL + '/static/'

    SARA_CLINIC = {
        'endpoint': 'https://clinic-core-prod.herokuapp.com/api/v1/dasa_file_url/{}/',
        'token': 'Token b138bc5f178ea2227160fef01463831f493ef609',
        'crawler_endpoint': 'https://clinic-core-prod.herokuapp.com/api/v1/saraclinic/crawler/results/',
        'crawler_results_endpoint': 'https://clinic-core-prod.herokuapp.com/api/v1/saraclinic/crawler/results/{}/',
        'crawler_sharedoctor_endpoint': 'https://clinic-core-prod.herokuapp.com/api/v1/saraclinic/crawler/sharedoctor/',
        'crawler_social_sharing': 'https://clinic-core-prod.herokuapp.com/api/v1/saraclinic/crawler/socialsharing/'
    }

    ZENDESK = {'email' : 'concierge@saracare.com.br',
               'token': 'CaeHrqZOHoXlt6tuGnqCwnXmxtwFSHSI7ZhbowI0',
               'subdomain': 'aplicativosara'}

elif APP_ENVIRONMENT in (DEV, STAGING):
    AWS_S3_SECURE_URLS = True
    AWS_STORAGE_BUCKET_NAME = "lab-staging-test"
    AWS_S3_CUSTOM_DOMAIN = '%s.s3.amazonaws.com' % AWS_STORAGE_BUCKET_NAME

    STATICFILES_STORAGE = 'lab_core.s3utils.StaticRootS3BotoStorage'
    DEFAULT_FILE_STORAGE = 'lab_core.s3utils.MediaRootS3BotoStorage'

    BASE_URL = 'https://' + AWS_STORAGE_BUCKET_NAME + '.s3.amazonaws.com'
    MEDIA_URL = BASE_URL + '/media/'
    STATIC_URL = BASE_URL + '/static/'

    SARA_CLINIC = {
        'endpoint': 'https://clinic-core.herokuapp.com/api/v1/dasa_file_url/{}/',
        'token': 'Token b138bc5f178ea2227160fef01463831f493ef609',
        'crawler_endpoint': 'https://clinic-core.herokuapp.com/api/v1/saraclinic/crawler/results/',
        'crawler_results_endpoint': 'https://clinic-core.herokuapp.com/api/v1/saraclinic/crawler/results/{}/',
        'crawler_sharedoctor_endpoint': 'https://clinic-core.herokuapp.com/api/v1/saraclinic/crawler/sharedoctor/',
        'crawler_social_sharing': 'https://clinic-core.herokuapp.com/api/v1/saraclinic/crawler/socialsharing/'

    }

    ZENDESK = {'email' : 'concierge@saracare.com.br',
               'token': 'bdmKDN5yUf2QXg9NxUBKMZdc4kKWP6rgKIbS6Haz',
               'subdomain': 'aplicativosara1517798777'}


else:
    STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
    STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
    STATIC_URL = '/static/'
    DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
    MEDIA_ROOT = '{0}/temp/'.format(BASE_DIR)
    MEDIA_URL = '/media/'

    SARA_CLINIC = {
        'endpoint': 'https://clinic-core.herokuapp.com/api/v1/dasa_file_url/{}/',
        'token': 'Token b138bc5f178ea2227160fef01463831f493ef609',
        'crawler_endpoint': 'https://clinic-core.herokuapp.com/api/v1/saraclinic/crawler/results/',
        'crawler_results_endpoint': 'https://clinic-core.herokuapp.com/api/v1/saraclinic/crawler/results/{}/',
        'crawler_sharedoctor_endpoint': 'https://clinic-core.herokuapp.com/api/v1/saraclinic/crawler/sharedoctor/',
        'crawler_social_sharing': 'https://clinic-core.herokuapp.com/api/v1/saraclinic/crawler/socialsharing/'
    }

    ZENDESK = {'email' : 'concierge@saracare.com.br',
               'token': 'bdmKDN5yUf2QXg9NxUBKMZdc4kKWP6rgKIbS6Haz',
               'subdomain': 'aplicativosara1517798777'}



# Application definition

INSTALLED_APPS = [
    'corsheaders',
    'domain.apps.DomainConfig',
    'concierge.apps.ConciergeConfig',
    'patient_api.apps.PatientApiConfig',
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django_extensions',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis',
    'django.contrib.admindocs',
    'rest_framework',
    'rest_framework_gis',
    'rest_framework_swagger',
    'rest_framework_docs',
    'rest_framework.authtoken',
    'reversion',
    'anymail',
    'general_utils',
    'reporting',
    'm2m',
    'debug_toolbar',  # TODO: Only for APP_ENVIRONMENT != prod
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'lab_core.urls'

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

WSGI_APPLICATION = 'lab_core.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

if APP_ENVIRONMENT == CI:
    DATABASES = dict(default=dj_database_url.config(conn_max_age=600, default='postgres://ubuntu@localhost/lab'))
    DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'

else:
    DATABASE_URL = os.environ.get('DATABASE_URL', 'postgres://lab:lab@localhost/lab')
    DATABASES = dict(default=dj_database_url.config(conn_max_age=600, default=DATABASE_URL))
    DATABASES['default']['ENGINE'] = 'django.contrib.gis.db.backends.postgis'


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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

AUTHENTICATION_BACKENDS = [
    'domain.utils.UserModelEmailBackend',  # Login w/ email
    'django.contrib.auth.backends.ModelBackend',  # Login w/ username
]

# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'EXCEPTION_HANDLER': 'domain.utils.custom_exception_handler',
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.IsAuthenticated'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework.authentication.BasicAuthentication',
        'domain.authentication.ExpirableTokenAuthentication',
        'rest_framework_jwt.authentication.JSONWebTokenAuthentication',
    ),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 100,
    'DATETIME_FORMAT': '%d/%m/%Y %H:%M',
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.URLPathVersioning',
    'DEFAULT_VERSION': 'v3'
}


JWT_AUTH = {
    'JWT_EXPIRATION_DELTA': datetime.timedelta(days=15),
    'JWT_ALLOW_REFRESH': True,
    'JWT_REFRESH_EXPIRATION_DELTA': datetime.timedelta(days=25),
}

# Logging
if APP_ENVIRONMENT == PROD:
    ROOT_LEVEL = 'ERROR'
else:
    ROOT_LEVEL = 'DEBUG'
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': '%(asctime)s %(levelname)s [%(name)s] [%(threadName)s] %(message)s'
        },
    },
    'loggers': {
        'root': {
            'level': ROOT_LEVEL,
            'handlers': ['console'],
        },
        'default': {
            'level': 'INFO',
            'handlers': ['console'],
        },
        'django.request': {
            'level': 'ERROR',
            'handlers': ['console'],
        },
        'patient_api.views': {
            'level': 'INFO',
            'handlers': ['console'],
        },
        'domain.signals': {
            'level': 'ERROR',
            'handlers': ['console'],
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'level': 'NOTSET',
            'formatter': 'default',
        },

    },
}

ANYMAIL = {
    # (exact settings here depend on your ESP...)
    "MAILGUN_API_KEY": "<your Mailgun key>",
    "MAILGUN_SENDER_DOMAIN": 'mg.example.com',  # your Mailgun domain, if needed
}

CORS_ORIGIN_WHITELIST = (
    'localhost:8000',
    'localhost:3000',
    'dasa-142114.firebaseapp.com',
    'dasa-staging.firebaseapp.com',
    'concierge.saracare.com.br',
    'staging.concierge.saracare.com.br'
)
DEFAULT_ENCODING = 'utf-8'

if APP_ENVIRONMENT == PROD:
    FB_CONFIG = {
        "apiKey": "AIzaSyAiN_S2-EDMAkpFqExpXF8GOegdl0IxRVg",
        "authDomain": "dasa-142114.firebaseapp.com",
        "databaseURL": "https://dasa-142114.firebaseio.com",
        "storageBucket": "dasa-142114.appspot.com",
        "serviceAccount": os.path.join(BASE_DIR, 'google', 'fb-service-account.json')
    }
elif APP_ENVIRONMENT in (DEV, CI, STAGING):
    FB_CONFIG = {
        "apiKey": "AIzaSyBedN_oHPl6EDOCH826E4KSzYkbOCFeNcU",
        "authDomain": "dasa-staging.firebaseapp.com",
        "databaseURL": "https://dasa-staging.firebaseio.com",
        "storageBucket": "dasa-staging.appspot.com",
        "serviceAccount": os.path.join(BASE_DIR, 'google', 'fb-service-account-staging.json')
    }
else:
    fb_config_file = os.path.join(BASE_DIR, 'google', 'fb-config-{0}.json'.format(DEVELOPER))
    with open(fb_config_file) as data_file:
        FB_CONFIG = json.load(data_file)

FCM_URL = "https://fcm.googleapis.com/fcm/send"
FCM_KEY = "AAAAa_WPxjY:APA91bG5Q6RxeT4WpJwM9CcdYoeMp4rrnXfsrezJxI9TbkJEoVbDSpYZIBoK59wAAZ-aw6VG2ZdNRJH7HeoDNugU6gUPjkllWOagMbeJVE4QV6HVVFBojD7iG2jH1xhtPny9CqNAyt8d7atfxXUFI_onE110uA34pw"
FCM_DEFAULT_NOTIFICATION_ICON_COLOR = "#49A7E1"

# TODO: Remove as we are using pyrebase
if APP_ENVIRONMENT == PROD:
    FB_SERVICE_ACCOUNT_EMAIL = "firebase-adminsdk-plyu6@dasa-142114.iam.gserviceaccount.com"
else:
    FB_SERVICE_ACCOUNT_EMAIL = "dasa-staging-sdk@dasa-staging.iam.gserviceaccount.com"

# TODO: Remove as we are using pyrebase
if APP_ENVIRONMENT == PROD:
    FB_PRIVATE_KEY = "-----BEGIN PRIVATE KEY-----\n" \
                     "MIIEvwIBADANBgkqhkiG9w0BAQEFAASCBKkwggSlAgEAAoIBAQDprrd2inTbxuQs\n" \
                     "6oOEeMY+BY4un/ywxlEPE93GwgePkt3e79wSoFpbNSTzyb8Ra0mKZ4fIqN9RVduo\n" \
                     "B4LtDU3fNjgAwmYRPakBc5K+qZzuCd7O4KNCJ87Vk1A4Q3AImNm4wP9WiShlO209\n" \
                     "RQMZQNvyfLJMGLEEH6VhJXpyU/RsDyuMOKHtGe+f1RV13pBU4w+VUbYKMdwh//m8\n" \
                     "TzbIGHHpB+B6yNe0EOClbWv1DRLoKQfK9MyJiPeRWJqaSCRpUZ1Opy1Jh6iv9UyC\n" \
                     "kKEg65wVe1gn5Q8i/P3BaC4OJ8lp8v1FsfH3HSKWDMQ0fXrzvWqWxffwbZh2wgrR\n" \
                     "jw55y02fAgMBAAECggEBANP2zSdTU8h+0j4DwqQIwRlFBME6EYVvfdtFU+eT3DPZ\n" \
                     "LjOoMmEa3prYy9nuZ8evH5fRbRMQSvCGBqaVmabYaIhNr+LQcrC003YjlToos9Yf\n" \
                     "UeEpVi0N2slTxHIkiZziuKqjNXkTFHcuvlnTHYpskJWVkk0AIKDy65oA2t6VVKIm\n" \
                     "LFzCRDG8XH3kdNKTocEQxS9eJ9ig/kOA1zgtAyOxCg+xJ/EOhTae3r1xl5aENzoK\n" \
                     "gYoqHg5ndnxNL87FY3zgd7lpdsR80/3O4amvZvHf3w91Uh6DAchVfRJf+5eo0yT1\n" \
                     "MwgK6H//KEkni8s0xeZU6pNN6DL5Vfh0UwCFN9Ts6IECgYEA/69JP3Mq5Ed+hSly\n" \
                     "fP8NdDnuT+JO75nWq2HkaodYDkJC38w8OEfjQ3xTxY2rh+sNWso36f8/5ibrE1rL\n" \
                     "MhT9tSzi0+Uj+TTWgm8aFKYjAzPQluCqHVgPtuwCJa8Nfo/z44rbJgARLMg3TEfk\n" \
                     "edeLh70kicQi/Dit9ib/W2WW86ECgYEA6fh8I/kIBUfQiTA/X5T5FzwyAfe4Pk8P\n" \
                     "3E5S39F9ZkZ0j2VfWjadTLKnnH+ivBkeR1epCAVmUnPTbTPxEpnDyzgT6fwqvDU/\n" \
                     "vpNOygEfmasNHZva+FvH83zPjr4DvY78UY/Im+j1Iod+TV+aTNRizaK9H3Kb3Cab\n" \
                     "bO+RDNvWuT8CgYBMjoiJFgvGtF1+s61THe9CWMIxaxqlhVOQl0wUVZgZFN//MKDr\n" \
                     "XSMAJu7SXRv6I3gpMhlR2Bqi6A5FCk+DHGPm5py4Q4jk6lw8S9XsTt527AHN21E0\n" \
                     "XhS+eaYe8G5C8gldnUsG8sgxt3VPQst3bAGcUBbrpS2whawY4w5cqGttYQKBgQDj\n" \
                     "QkoKgvSodGX5K1UTGVeNmxmT0bMzSoZEXguffRNJyXukYTnqHYxSmGG34D4IaHmB\n" \
                     "oIL92IjX48tkkgRCJfsJJHIrX5V+9FXzXZA1JDw2ffAiZ2WcwUGJnxzYMHbfo8gv\n" \
                     "zPJ1hiS9IlCrBQaSQ+Woib8bka4Ue6eSe2wvykVZ7wKBgQCwtxPyX/DWAK2WAILx\n" \
                     "NtHgiGAu55ODbT6GZCPt7mCCyUw+RRrH/xjFWckgCfFZAFHMA2UJyOmpvc9HeodS\n" \
                     "bYttcZP9ZwH5zuWnuRGnuwgEPo7dA1w08ewAW4opHJEpOL5Aawqc7JPBEXEClOnj\n" \
                     "0UMUOzY8z6Rb6jZ9N44fEVAbCQ==\n-----END PRIVATE KEY-----\n"
else:
    FB_PRIVATE_KEY = "-----BEGIN PRIVATE KEY-----\n" \
                     "MIIEvQIBADANBgkqhkiG9w0BAQEFAASCBKcwggSjAgEAAoIBAQC9BhtT8rfex6Th\n" \
                     "Ho/FUww909UZo4Iop7DEnTGhCMt1jGwCm4lULbAbqYCu370WytQ03mlY+v30roC/\n" \
                     "rtTTUFqkNL2HagJZ9kEeAMo/2Kzux73VXrZPuAf6rkfch7s6w0Y40jenyOtJrDi7\n" \
                     "swhJkCEiKRI0mig3q74MzlbQIGhlajsbtnJmFoUmZZAvIf2POvrtKzSVfiwWLy3N\n" \
                     "rNOXx2bZYAGLy46o3QeVNRg3rfu7N3X/9sTg6ybYszX5O1zkZZ5v5DnkU+YHqkB/\n" \
                     "fjb019c3PXOeHqH9nf9vf7YIu+YwfER1PdosBmwSncCRJ3D3Oj4QbzxnT47xGJHz\n" \
                     "mpVpWQE5AgMBAAECggEAQlfUW6CC/IQh0ImDeIRvdXvV/Yuv8Uj59+gcNSL7FiTU\n" \
                     "/A1PI+ZtOyhA7B/HJCrIVE4Dt6FQZQKiWaSpOgmn5p5ELzT74ktWC4vHcKVB/QTK\n" \
                     "EguN/WjgFBH7UuGoyzUifmr58b/JJTB3MRnjPL6DgpPbue6pUvDKYYBCZAYb3gvS\n" \
                     "SUvWYLKiz1kKisDwv/CD2I8/3cyllc54b73HrPX4XL5X82BRwAagZCUhIJdvbXr7\n" \
                     "8WtGhAeJ+GYLTzD0lwkttcLZ2910tqb4HCGz7JmQsV+SwRjyp/Xn7iQQwe3nioVh\n" \
                     "HY3hKE5PmmkvGeZSwS9nNxc5bUR4VkH42+TD/a1CyQKBgQDpLxcy+2jVeyATiseW\n" \
                     "4Iw0z+Kc2c0jQ5bHojRQeg3PQDKQ62Ma+vCBNOO1I/8qjmbFMcK3jEznzHGHn+7a\n" \
                     "ORS/YwosArwilx3eyXPOpV5R0wLCMEfUIF9ubwFrX0aKjpfEyEKxtJxPdXNPTdKG\n" \
                     "9Fi6RMK6OBiihoVsEumbJ//4fwKBgQDPhN8t04G69FljOX5mOjW7cL4MYW0EnFPR\n" \
                     "DgrChgjGVYwIXm31pT0er3+PZcR/QIKAXZTyKP1yn12eh/7DLPoNmv23nrCqLK81\n" \
                     "W+qTmcfbrdB41uHenXdfV3s1vRVcbdGVKt3Vy3KpA+d+NKWvOxrwPFJJjV74wwz1\n" \
                     "a+cihEnqRwKBgQDBDJRnR87N1qaCp0V/+pz46BaThpmXlVBSLE6lRbcDGwICCm49\n" \
                     "Gv1b6t6Ny6RnpgcdQIoVDVlqGk7vWpATKGit3h/Aue7psDQxipSOw0en9Er3W6NL\n" \
                     "0hVPxyTksLck5NJvPuBAYOd7vR/eyu39fnOqmlygcOqsOzRgefPe2SnInwKBgBWa\n" \
                     "yL11orD7FX9OEgnEj6mHEFIrpnTvbY57PsWHvMwhReXtJteHL3jNXqNoPe/doHiK\n" \
                     "xaH8gH55dv61O+HIAfR+qWF/hPcCle8hNafOP89wJh8eh/9sN2xWqD4tBFdOG57D\n" \
                     "CrtiZfqQrH4oLwOyTJisPwjnTfbqH6RBapveV++rAoGAZ2JxqyV3eO5efOz9fWvY\n" \
                     "OQJMFKtAbahs2SPEo6L849P8DPaAUiOZZPvZQsi788dKXH0S/Snq2V5rm832Gyuf\n" \
                     "zDOdLe846R9qLR+nsuXVdqp8aeUUbj4TbWpclq8X5QuxXuj7o0b3WLsrX+Y7WWyn\n9" \
                     "IAupMTYemJPYw/2N/CyWBE=\n-----END PRIVATE KEY-----\n"

NOTIFICATION_BEFORE_EXAM_IN_MINUTES = 60
NOTIFICATION_BEFORE_EXAM_PREPARATION_IN_MINUTES = 15
NOTIFICATION_BEFORE_EXAM_PREPARATION_IN_DAYS = 1
NOTIFICATION_BEFORE_EXAM_PREPARATION_EXACT_HOURS = 10
NOTIFICATION_BEFORE_CALL_IN_MINUTES = 60
NOTIFICATION_EXACT_TIME_HOURS = 10
NOTIFICATION_AFTER_PRESCRIPTION_EXPIRES_IN_HOURS = 10
NOTIFICATION_BEFORE_PRESCRIPTION_EXPIRES_IN_DAYS = 3

CELERY_BROKER_URL = os.environ.get('CLOUDAMQP_URL', 'amqp://guest:guest@localhost:5672/')

CELERY_TASK_SERIALIZER = "json"

CELERY_SEND_EVENTS = False

# Tell nose to measure coverage on the given apps
NOSE_ARGS = [
    '--with-coverage',
    '--cover-package=.',
]


TOKEN_EXPIRATION_IN_MINUTES = 259200  # 6 months during V1
TOKEN_EXPIRATION_DELTA_IN_DAYS = 365

TOKEN_EXPIRATION_IN_SECONDS = 5
TOKEN_EXPIRATION_DELTA_IN_SECONDS = 15

LABORATORY_LIST_LIMIT = 50

if APP_ENVIRONMENT != LOCAL:
    google_maps_key_file = os.path.join(BASE_DIR, 'google', 'maps-key-{0}'.format(APP_ENVIRONMENT))
else:
    google_maps_key_file = os.path.join(BASE_DIR, 'google', 'maps-key-{0}'.format(DEVELOPER))

with open(google_maps_key_file) as google_maps_key:
    GOOGLE_MAPS_KEY = google_maps_key.read()


EMAIL_BACKEND = "anymail.backends.mailgun.MailgunBackend"  # or sendgrid.SendGridBackend, or...
DEFAULT_FROM_EMAIL = "sara@saracare.com.br"  #
MAILGUN_URL = "https://api.mailgun.net/v3/saracare.com.br/messages"
MAILGUN_SECRET_API_KEY = "key-1dff904c1771f6c13d205bce25a007fa"
MAILGUN_EMAIL_SENDER = "sara@saracare.com.br"

RESET_PASSWORD_EXPIRATION_IN_HOURS = 24
RESET_PASSWORD_EXPIRATION_IN_SECONDS = 3

if APP_ENVIRONMENT == LOCAL:
    DOMAIN_NAME = "http://localhost:5000"
elif APP_ENVIRONMENT == PROD:
    DOMAIN_NAME = "https://www.saracare.com.br"
else:
    DOMAIN_NAME = "http://staging.saracare.com.br"

CUSTOM_SCHEMA = "sararoundpegs://"

IOS = "ios"
ANDROID = "android"

DEVICE_TYPE_HEADERS = "HTTP_DEVICE_TYPE"

UNKNOWN_DATE = "Unknown"
NOT_FOUND = "Não encontrado"

USERS_REPORT_LIST = ["sandro.lourenco@roundpe.gs", "henriqueperticarati@roundpe.gs", "andersonreis@roundpe.gs", "pedro@roundpe.gs", "emersonniide@roundpe.gs", "alvaro@roundpe.gs", ]
DATA_REPORT_LIST = ["eduardo.lemos@dasa.com.br", "ricardo.orlando@dasa.com.br", "evandro.alves@dasa.com.br",
                    "flavia.suzuki@dasa.com.br","liderescanal@dasa.com.br","plopes@dasa.com.br", "diego.alvarez@dasa.com.br"]

# m2m integration Sara Clinic


#ADMIN INTERFACE
GRAPPELLI_ADMIN_TITLE = "Sara Care Admin"
GRAPPELLI_SWITCH_USER = True
GRAPPELLI_AUTOCOMPLETE_LIMIT = 30
GRAPPELLI_CLEAN_INPUT_TYPES = True

OP_CLOSING_TIME_SAT = 18
OP_CLOSING_TIME_SUN = 14
OP_CLOSING_TIME_OTHER = 21
NEXT_DAY_CALL_TIME = 10





