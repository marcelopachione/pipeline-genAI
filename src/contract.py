from datetime import datetime
from typing import Tuple
from pydantic import BaseModel, EmailStr, validator, PositiveFloat, PositiveInt
from enum import Enum

class ProdutoEnum(str, Enum):
    produto1 = "Zap com Gemini"
    produto2 = "Zap com GPT"
    produto3 = "Zap com Llama3"


class Vendas(BaseModel):
    """
    Essa é a clasee de vendas do meu banco de dados

    Args:
        email (EmailStr): email do comprador
        data (datetie): data da compra
        valor (PositiveFloat): valor da compra - deve ser um valor positivo
        quantidade (PositiveInt): quantidade de produtos
        produto (ProdutoEnum): categoria do produto
    """
    email: EmailStr
    data: datetime
    valor: PositiveFloat
    quantidade: PositiveInt
    produto: ProdutoEnum
