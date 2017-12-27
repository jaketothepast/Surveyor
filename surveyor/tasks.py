from rq import Queue
from redis_lib.utils import get_client_connection

# RQ queue, used like this queue.enqueue(function_object, *args, **kwargs)
queue = Queue(connection=get_client_connection())

def question_up(email, question_id):
    """Place an email and question id into redis for later retrieval"""
    get_client_connection().set(question_id, email)

def question_down(question_id):
    """Take the question off of Redis and return the email"""
    get_client_connection.del(question_id)

def poll_for_question_expiration():
    """Poll Redis for the question expiring"""
    pass