from redis_om import HashModel, Field, Migrator
from database import redis_conn
class Product(HashModel):
    name: str = Field(index=True)
    price: float = Field(index=True)
    quantity: int = Field(index=True)

    class Meta:
        database = redis_conn

Migrator().run()
