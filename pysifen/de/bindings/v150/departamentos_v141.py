from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://ekuatia.set.gov.py/sifen/xsd"


class TDepartamentos(Enum):
    """
    Código del departamento donde se realiza la transacción.

    :cvar VALUE_1: CAPITAL
    :cvar VALUE_2: CONCEPCION
    :cvar VALUE_3: SAN PEDRO
    :cvar VALUE_4: CORDILLERA
    :cvar VALUE_5: GUAIRA
    :cvar VALUE_6: CAAGUAZU
    :cvar VALUE_7: CAAZAPA
    :cvar VALUE_8: ITAPUA
    :cvar VALUE_9: MISIONES
    :cvar VALUE_10: PARAGUARI
    :cvar VALUE_11: ALTO PARANA
    :cvar VALUE_12: CENTRAL
    :cvar VALUE_13: NEEMBUCU
    :cvar VALUE_14: AMAMBAY
    :cvar VALUE_15: PTE. HAYES
    :cvar VALUE_16: BOQUERON
    :cvar VALUE_17: ALTO PARAGUAY
    :cvar VALUE_18: CANINDEYU
    :cvar VALUE_19: CHACO
    :cvar VALUE_20: NUEVA ASUNCION
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6
    VALUE_7 = 7
    VALUE_8 = 8
    VALUE_9 = 9
    VALUE_10 = 10
    VALUE_11 = 11
    VALUE_12 = 12
    VALUE_13 = 13
    VALUE_14 = 14
    VALUE_15 = 15
    VALUE_16 = 16
    VALUE_17 = 17
    VALUE_18 = 18
    VALUE_19 = 19
    VALUE_20 = 20


class TDesDepartamento(Enum):
    """
    Descripción del departamento donde se realiza la transacción.
    """

    CAPITAL = "CAPITAL"
    CONCEPCION = "CONCEPCION"
    SAN_PEDRO = "SAN PEDRO"
    CORDILLERA = "CORDILLERA"
    GUAIRA = "GUAIRA"
    CAAGUAZU = "CAAGUAZU"
    CAAZAPA = "CAAZAPA"
    ITAPUA = "ITAPUA"
    MISIONES = "MISIONES"
    PARAGUARI = "PARAGUARI"
    ALTO_PARANA = "ALTO PARANA"
    CENTRAL = "CENTRAL"
    NEEMBUCU = "NEEMBUCU"
    AMAMBAY = "AMAMBAY"
    PTE_HAYES = "PTE. HAYES"
    BOQUERON = "BOQUERON"
    ALTO_PARAGUAY = "ALTO PARAGUAY"
    CANINDEYU = "CANINDEYU"
    CHACO = "CHACO"
    NUEVA_ASUNCION = "NUEVA ASUNCION"
