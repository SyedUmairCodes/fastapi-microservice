from typing import List
from fastapi import APIRouter, HTTPException
from redis_om import NotFoundError
from models import Product

prod_router = APIRouter(prefix="/products", tags=["products"])

@prod_router.post("", response_model=Product)
async def create_product(product: Product):
    return product.save()

@prod_router.get("", response_model=List[Product])
async def list_products():
    # Fetch all records
    pks = Product.all_pks()
    return [Product.get(pk) for pk in pks]

@prod_router.get("/{pk}", response_model=Product)
async def get_product(pk: str):
    try:
        return Product.get(pk)
    except NotFoundError:
        raise HTTPException(status_code=404, detail="Product not found")

@prod_router.put("/{pk}", response_model=Product)
async def update_product(pk: str, name: str = None, price: float = None, quantity: int = None):
    try:
        product = Product.get(pk)
        if name is not None: product.name = name
        if price is not None: product.price = price
        if quantity is not None: product.quantity = quantity
        return product.save()
    except NotFoundError:
        raise HTTPException(status_code=404, detail="Product not found")

@prod_router.delete("/{pk}")
async def delete_product(pk: str):
    if Product.delete(pk):
        return {"message": "Successfully deleted"}
    raise HTTPException(status_code=404, detail="Product not found")
