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

def question_answer_to_redis(email, question_id, answer):
    """Push to a list under a certain email on Redis"""
    
    conn = get_redis_connection()

    conn.sadd(f"{email}:{question_id}", answer)

# def question_from_redis(email, question_id):
#     """Remove a question id from the set in Redis"""

#     conn = get_redis_connection()

#     result = conn.spop(email, question_id)

#     # spop returns a nil if nothing was popped
#     if not result:
#         return False

#     return True