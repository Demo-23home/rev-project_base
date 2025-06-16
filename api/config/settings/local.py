from os import path, getenv
from dotenv import load_dotenv

from .base import * #noqa

from .base import BASE_DIR

local_env_file = path.join(BASE_DIR, ".envs", ".envs.local")

if path.isfile(load_dotenv): 
    load_dotenv(local_env_file)

DEBUG = True

SECRET_KEY = getenv("SECRET_KEY", "zymJqYSgQrxHLGS1MbVPB043BbXZPlBDHAkcIVPuskhiFMj4TY8")

SITE_NAME = getenv("SITE_NAME")

ADMIN_URL = getenv("DJANGO_ADMIN_URL")

EMAIL_BACKEND = "djcelery.email.backends.CeleryEmailBackend"

EMAIL_HOST = getenv("EMAIL_HOST")

EMAIL_PORT = getenv("EMAIL_PORT") 

DEFAULT_FROM_EMAIL = getenv("DEFAULT_FROM_EMAIL")

DOMAIN = getenv("DOMAIN")

ALLOWED_HOSTS = ["0.0.0.0", "local_host", "127.0.0.1"]


