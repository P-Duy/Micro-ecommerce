# To use Neon with Django, you have to create a Project on Neon and specify 
# the project connection settings in your settings.py in the same way as for standalone Postgres.

DATABASES = {
  'default': {
    'ENGINE': 'django.db.backends.postgresql',
    'NAME': 'neondb',
    'USER': 'P-Duy',
    'PASSWORD': '65xVdBemlqAf',
    'HOST': 'ep-rapid-wildflower-560331-pooler.us-east-2.aws.neon.tech',
    'PORT': '5432',
  }
}