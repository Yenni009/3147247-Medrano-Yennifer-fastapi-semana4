from pydantic import BaseModel, Field, validator
from typing import Optional, List
from datetime import datetime
from enum import Enum

class CategoryEnum(str, Enum):
    electronics = "electronics"
    clothing = "clothing"
    books = "books"
    home = "home"
    sports = "sports"

class ProductBase(BaseModel):
    name: str = Field(..., min_length=1, max_length=100, description="Nombre del producto")
    price: float = Field(..., gt=0, le=999999.99, description="Precio del producto")
    description: Optional[str] = Field(None, max_length=500, description="Descripción del producto")
    category: CategoryEnum = Field(..., description="Categoría del producto")

    @validator('name')
    def name_must_not_be_empty(cls, v):
        if not v.strip():
            raise ValueError('El nombre no puede estar vacío')
        return v.strip().title()

class ProductCreate(ProductBase):
    in_stock: bool = Field(True, description="Producto en stock")
    stock_quantity: int = Field(0, ge=0, le=9999, description="Cantidad en stock")

class ProductUpdate(ProductBase):
    in_stock: bool = Field(..., description="Producto en stock")
    stock_quantity: int = Field(..., ge=0, le=9999, description="Cantidad en stock")

class ProductResponse(ProductBase):
    id: int = Field(..., description="ID único del producto")
    in_stock: bool
    stock_quantity: int
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "name": "Laptop Gaming",
                "price": 1299.99,
                "description": "Laptop para gaming de alta performance",
                "category": "electronics",
                "in_stock": True,
                "stock_quantity": 15,
                "created_at": "2025-07-24T10:00:00",
                "updated_at": None
            }
        }

class ProductList(BaseModel):
    products: List[ProductResponse]
    total: int
    page: int
    page_size: int

class ErrorResponse(BaseModel):
    success: bool = False
    error: str
    detail: Optional[str] = None