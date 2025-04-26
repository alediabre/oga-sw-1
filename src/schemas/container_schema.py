from pydantic import BaseModel, model_validator
from typing import List

class ContenedoresRequest(BaseModel):
    contenedores: List[List[int]]

    @model_validator(mode='before')  # mode='before' es equivalente al antiguo pre=True
    def validate_contenedores(cls, values):
        contenedores = values.get('contenedores')
        if len(contenedores) != 3:
            raise ValueError("Debe haber exactamente 3 contenedores")
        if contenedores:
            # Tomamos el tamaño de la primera sublista como referencia
            expected_length = len(contenedores[0])
            for index, fila in enumerate(contenedores):
                if len(fila) != expected_length:
                    raise ValueError("Todos los contenedores deben tener el mismo número de residuos.")
        return values