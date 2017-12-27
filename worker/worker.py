import sys
from rq import Connection, Worker

# similar to rq worker
# Taken from python-rq.or
# Setup for redis container
with Connection('redis', 6789):
    qs = sys.argv[1:] or ['default']

    w = Worker(qs)
    w.work()
