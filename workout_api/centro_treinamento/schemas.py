from typing import Annotated
from pydantic import UUID4, Field

from workout_api.contrib.schemas import BaseSchema

class CentroTreinamentoIn(BaseSchema):
    nome: Annotated[str, Field(description='Nome do centro de treinamento', example='CT King', max_length=20)]
    endereco: Annotated[str, Field(description='Endereco do centro de treinamento', example='Rua X, quadra Y', max_length=60)]
    proprietario: Annotated[str, Field(description='Proprietario do centro de treinamento', example='Kaio', max_length=30)]

class CentroTreinamento(BaseSchema):
    nome: Annotated[str, Field(description='Nome do centro de treinamento', example='CT King', max_length=20)]

class CentroTreinamentoOut(CentroTreinamentoIn):
    id: Annotated[UUID4, Field(description='Identificador da categoria')]