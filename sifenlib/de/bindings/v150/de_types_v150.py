from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://ekuatia.set.gov.py/sifen/xsd"


class TdDtipIdrespDeValue(Enum):
    C_DULA_PARAGUAYA = "Cédula paraguaya"
    PASAPORTE = "Pasaporte"
    C_DULA_EXTRANJERA = "Cédula extranjera"
    CARNET_DE_RESIDENCIA = "Carnet de residencia"


class TdDesForPagValue(Enum):
    EFECTIVO = "Efectivo"
    TRANSFERENCIA_BANCARIA = "Transferencia bancaria"


class TiForPag(Enum):
    """
    Código de Forma de Pago.
    """

    VALUE_1 = 1
    VALUE_2 = 2
