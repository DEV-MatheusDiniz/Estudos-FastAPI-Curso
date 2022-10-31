from typing import Optional

from pydantic import BaseModel as SCBaseModel
from pydantic import HttpUrl


class ArtigoSchema(SCBaseModel):
    id: Optional[int] = None
    titulo: str
    descricao: str
    url_fonte: HttpUrl
    usuario_id: Optional[int]

    class Config:
        orm_mode = True
