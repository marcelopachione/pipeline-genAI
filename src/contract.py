from datetime import datetime
from typing import Tuple
from pydantic import BaseModel, EmailStr, validator, PositiveFloat, PositiveInt
from enum import Enum

class ProdutoEnum(str, Enum):
    produto1 = "Zap com Gemini"
    produto2 = "Zap com GPT"
    produto3 = "Zap com Llama3"


class Vendas(BaseModel):
    email: EmailStr
    data: datetime
    valor: PositiveFloat
    quantidade: PositiveInt
    produto: ProdutoEnum
