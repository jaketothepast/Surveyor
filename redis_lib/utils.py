from redis import StrictRedis
from django.conf import settings

def get_client_connection():
    return StrictRedis(host=settings.REDIS_HOST,
                       port=settings.REDIS_PORT,
                       db=settings.REDIS_DB)