from redis_om import HashModel, Migrator
from database import redis_conn
from pydantic import BaseModel
from typing import Literal
class Order(HashModel):
    product_id: str
    quantity: int
    status: str  # e.g., "pending", "completed", "failed"

    class Meta:
        database = redis_conn

Migrator().run()

class OrderStatusUpdate(BaseModel):
    status: Literal["pending", "completed", "canceled", "refunded", "shipped"]
