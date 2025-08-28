"""from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import List, Optional

# Esquemas base
class UserBase(BaseModel):
    email: EmailStr
    username: str

class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    username: Optional[str] = None
    is_active: Optional[bool] = None

class User(UserBase):
    id: int
    is_active: bool
    created_at: datetime
    updated_at: Optional[datetime] = None

    class Config:
        from_attributes = True

# Esquemas para Post
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = False

class PostCreate(PostBase):
    pass

class PostUpdate(BaseModel):
    title: Optional[str] = None
    content: Optional[str] = None
    published: Optional[bool] = None

class Post(PostBase):
    id: int
    owner_id: int
    created_at: datetime
    updated_at: Optional[datetime] = None
    owner: User

    class Config:
        from_attributes = True

# Esquemas con relaciones
class UserWithPosts(User):
    posts: List[Post] = []
"""    
    
    
from pydantic import BaseModel
from typing import List, Optional

# Schemas para Categoría
class CategoriaBase(BaseModel):
    nombre: str
    descripcion: str

class CategoriaCreate(CategoriaBase):
    pass

class Categoria(CategoriaBase):
    id: int

    class Config:
        from_attributes = True

# Schemas actualizados para Producto
class ProductoBase(BaseModel):
    nombre: str
    precio: float
    descripcion: str
    categoria_id: Optional[int] = None

class ProductoCreate(ProductoBase):
    pass

class ProductoUpdate(BaseModel):
    nombre: str = None
    precio: float = None
    descripcion: str = None
    categoria_id: int = None

# Producto con información de categoría incluida
class ProductoConCategoria(ProductoBase):
    id: int
    categoria: Optional[Categoria] = None

    class Config:
        from_attributes = True

# Categoría con lista de productos
class CategoriaConProductos(Categoria):
    productos: List[ProductoBase] = []

    class Config:
        from_attributes = True