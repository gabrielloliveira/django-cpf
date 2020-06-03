SECRET_KEY = 'fake-key'

INSTALLED_APPS = [
    'cpf_field',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase',
    }
}
