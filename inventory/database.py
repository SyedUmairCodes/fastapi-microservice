import os
from redis_om import get_redis_connection

redis_conn = get_redis_connection(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=os.getenv("REDIS_PORT", 6379),
    decode_responses=True
)
