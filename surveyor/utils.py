"""
Basic utilities for the Surveyor application.
"""

import redis

from django.conf import settings

def get_redis_connection():
    return redis.Redis(settings.REDIS_HOST,
                       settings.REDIS_PORT,
                       db=settings.REDIS_DB)

# The thought here is that we store all data in a volatile manner
# in Redis in memory. This allows for a certain degree of anonyminity,
# 
# Question ID's are pushed and popped from a set keyed on a user email
# (which will go away after we deliver the report, possibly using expiring keys)
#
# Answers will be pushed under question ID's somehow, and popped on report
# Creation time.

class RedisClient

    conn = get_redis_connection()

    @classmethod
    def question_to_redis(cls, email, question_id):
        return cls.conn.set(question_id, email)

    @classmethod
    def get_question_email(cls, question_id):
        return cls.conn.get(question_id)

    @classmethod
    def question_answer_to_redis(cls, email, question_id, answer):
        """Push to a list under a certain email on Redis"""
        return cls.conn.sadd(f"{email}:{question_id}", answer)
