import httpx
from fastapi import APIRouter,HTTPException
from redis_om import NotFoundError
from models import Order, OrderStatusUpdate

checkout_router = APIRouter(prefix="/orders", tags=["Order"])

@checkout_router.post("")
async def checkout(product_id: str, quantity: int):
    order = Order(product_id=product_id, quantity=quantity, status="pending")
    order.save()

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(
                f"http://inventory-api:8000/products/{product_id}/decrement?quantity={quantity}"
            )

            if response.status_code == 200:
                order.status = "completed"
                return order.save()
            else:
                order.status = "failed"
                order.save()
                raise HTTPException(status_code=response.status_code, detail=response.json())

        except httpx.RequestError:
            order.status = "error"
            order.save()
            raise HTTPException(status_code=500, detail="Inventory service unavailable")

@checkout_router.patch("/{pk}/status", response_model=Order)
async def update_order_status(pk: str, update: OrderStatusUpdate):
    try:
        # 2. Fetch the existing order from Redis
        order = Order.get(pk)

        # 3. Update only the status field
        order.status = update.status

        # 4. Save and return the updated order
        return order.save()

    except NotFoundError:
        raise HTTPException(status_code=404, detail="Order not found")
