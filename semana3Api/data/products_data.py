from datetime import datetime
from typing import Dict, List, Optional
from models.product_models import ProductResponse, CategoryEnum

# Simulamos una base de datos en memoria
products_db: Dict[int, dict] = {
    1: {
        "id": 1,
        "name": "Laptop Gaming",
        "price": 1299.99,
        "description": "Laptop para gaming de alta performance",
        "category": CategoryEnum.electronics,
        "in_stock": True,
        "stock_quantity": 15,
        "created_at": datetime(2025, 7, 20, 10, 0, 0),
        "updated_at": None
    },
    2: {
        "id": 2,
        "name": "Camiseta Algodón",
        "price": 29.99,
        "description": "Camiseta 100% algodón, muy cómoda",
        "category": CategoryEnum.clothing,
        "in_stock": True,
        "stock_quantity": 50,
        "created_at": datetime(2025, 7, 21, 14, 30, 0),
        "updated_at": None
    },
    3: {
        "id": 3,
        "name": "Python para Principiantes",
        "price": 45.00,
        "description": "Libro completo de programación en Python",
        "category": CategoryEnum.books,
        "in_stock": False,
        "stock_quantity": 0,
        "created_at": datetime(2025, 7, 22, 9, 15, 0),
        "updated_at": None
    }
}

# Counter para IDs autoincrementales
next_id = 4

def get_next_id() -> int:
    global next_id
    current_id = next_id
    next_id += 1
    return current_id

def get_all_products() -> List[dict]:
    return list(products_db.values())

def get_product_by_id(product_id: int) -> Optional[dict]:
    return products_db.get(product_id)

def create_product(product_data: dict) -> dict:
    product_id = get_next_id()
    new_product = {
        "id": product_id,
        **product_data,
        "created_at": datetime.now(),
        "updated_at": None
    }
    products_db[product_id] = new_product
    return new_product

def update_product(product_id: int, product_data: dict) -> Optional[dict]:
    if product_id in products_db:
        updated_product = {
            **products_db[product_id],
            **product_data,
            "updated_at": datetime.now()
        }
        products_db[product_id] = updated_product
        return updated_product
    return None

def delete_product(product_id: int) -> bool:
    if product_id in products_db:
        del products_db[product_id]
        return True
    return False

def filter_products(
    category: Optional[str] = None,
    in_stock: Optional[bool] = None,
    min_price: Optional[float] = None,
    max_price: Optional[float] = None
) -> List[dict]:
    products = get_all_products()

    if category:
        products = [p for p in products if p["category"] == category]

    if in_stock is not None:
        products = [p for p in products if p["in_stock"] == in_stock]

    if min_price is not None:
        products = [p for p in products if p["price"] >= min_price]

    if max_price is not None:
        products = [p for p in products if p["price"] <= max_price]

    return products