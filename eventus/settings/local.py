from .base import *
# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

#POSTGRES
DATABASES = {
	'default' : {
		'ENGINE': 'django.db.backends.postgresql_psycopg2',
		'NAME': 'eventus',
		'USER': 'postgres',
		'PASSWORD': 'Mm0925163347',
		'HOST': 'localhost',
		'PORT': '5432',
	}
}


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/
STATIC_URL = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR.child('media')