"""
Basic utilities for the Surveyor application.
"""

import redis

from django.conf import settings

def get_redis_connection():
    return redis.Redis(settings.REDIS_HOST,
                       settings.REDIS_PORT,
                       db=settings.REDIS_DB)