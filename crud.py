from sqlalchemy.orm import Session
from sqlalchemy.orm import Session, joinedload
from sqlalchemy import or_
import models, schemas

def crear_producto(db: Session, producto: schemas.ProductoCreate):
    """Crear un nuevo producto"""
    db_producto = models.Producto(**producto.dict())
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto

def obtener_producto(db: Session, producto_id: int):
    """Obtener producto por ID"""
    return db.query(models.Producto).filter(models.Producto.id == producto_id).first()

def obtener_productos(db: Session, skip: int = 0, limit: int = 10):
    """Obtener lista de productos con paginación"""
    return db.query(models.Producto).offset(skip).limit(limit).all()

def buscar_productos(db: Session, busqueda: str):
    """Buscar productos por nombre o descripción"""
    return db.query(models.Producto).filter(
        or_(
            models.Producto.nombre.contains(busqueda),
            models.Producto.descripcion.contains(busqueda)
        )
    ).all()

def actualizar_producto(db: Session, producto_id: int, producto: schemas.ProductoUpdate):
    """Actualizar producto existente"""
    db_producto = db.query(models.Producto).filter(models.Producto.id == producto_id).first()
    if db_producto:
        # Solo actualizar campos que no sean None
        update_data = producto.dict(exclude_unset=True)
        for field, value in update_data.items():
            setattr(db_producto, field, value)
        db.commit()
        db.refresh(db_producto)
    return db_producto

def eliminar_producto(db: Session, producto_id: int):
    """Eliminar producto"""
    db_producto = db.query(models.Producto).filter(models.Producto.id == producto_id).first()
    if db_producto:
        db.delete(db_producto)
        db.commit()
    return db_producto

def contar_productos(db: Session):
    """Contar total de productos"""
    return db.query(models.Producto).count()

# Funciones CRUD para Categorías
def crear_categoria(db: Session, categoria: schemas.CategoriaCreate):
    """Crear una nueva categoría"""
    db_categoria = models.Categoria(**categoria.dict())
    db.add(db_categoria)
    db.commit()
    db.refresh(db_categoria)
    return db_categoria

def obtener_categorias(db: Session):
    """Obtener todas las categorías"""
    return db.query(models.Categoria).all()

def obtener_categoria(db: Session, categoria_id: int):
    """Obtener categoría por ID"""
    return db.query(models.Categoria).filter(models.Categoria.id == categoria_id).first()

def obtener_categoria_con_productos(db: Session, categoria_id: int):
    """Obtener categoría con sus productos"""
    return db.query(models.Categoria).options(
        joinedload(models.Categoria.productos)
    ).filter(models.Categoria.id == categoria_id).first()

# Funciones actualizadas para Productos
def obtener_productos_con_categoria(db: Session, skip: int = 0, limit: int = 10):
    """Obtener productos con información de categoría"""
    return db.query(models.Producto).options(
        joinedload(models.Producto.categoria)
    ).offset(skip).limit(limit).all()

def obtener_productos_por_categoria(db: Session, categoria_id: int):
    """Obtener productos de una categoría específica"""
    return db.query(models.Producto).filter(
        models.Producto.categoria_id == categoria_id
    ).all()