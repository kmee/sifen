from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum

from sifenlib.CommonMixin import CommonMixin

__NAMESPACE__ = "http://ekuatia.set.gov.py/sifen/xsd"


@dataclass(kw_only=True)
class Prodid(CommonMixin):
    class Meta:
        name = "prodid"
        namespace = "http://ekuatia.set.gov.py/sifen/xsd"

    value: str = field(
        default="",
        metadata={
            "pattern": r"[0-9][0-9][0-9][0-9][0-9]",
        },
    )


class TcMotDet(Enum):
    """
    Código del motivo del evento Determinacion del DTE.
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5
    VALUE_6 = 6


class TcMotImp(Enum):
    """
    Código del motivo del evento Impugnacion del DTE.
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5


class TcMotOa(Enum):
    """
    Código del motivo del evento Objeto de Análisis.
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4
    VALUE_5 = 5


class TcMotPc(Enum):
    """
    Código del motivo del evento Proceso de Control.
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4


class TdMotDesDet(Enum):
    """
    Descripción del motivo del evento Determinacion del DTE.
    """

    APLICACI_N_DE_MULTA_AL_EMISOR = "Aplicación de multa al Emisor"
    APLICACI_N_DE_MULTA_AL_RECEPTOR = "Aplicación de multa al Receptor"
    CORRECCI_N_CR_DITO_FISCAL = "Corrección Crédito fiscal"
    CORRECCI_N_D_BITO_FISCAL = "Corrección Débito fiscal"
    ANULACI_N_DE_IMPUGNACI_N_POR_FALLO_JUDICIAL = (
        "Anulación de Impugnación por fallo judicial"
    )
    OTRO = "Otro"


class TdMotDesImp(Enum):
    """
    Descripción del motivo del evento Impugnacion del DTE.
    """

    OPERACIONES_NO_RECONOCIDAS_POR_EL_CONTRIBUYENTE_PROVEEDOR_O_CLIENTE = (
        "Operaciones no reconocidas por el contribuyente (proveedor o cliente)"
    )
    SIMULACI_N_DE_OPERACIONES = "Simulación de operaciones"
    INCONSISTENCIAS_DETECTADAS = "Inconsistencias detectadas"
    CONTENIDO_FALSO = "Contenido falso"
    OTROS = "Otros"


class TdMotDesOa(Enum):
    """
    Descripción del motivo del evento Objeto de Análisis.
    """

    OPERACIONES_NO_RECONOCIDAS_POR_EL_CONTRIBUYENTE = (
        "Operaciones no reconocidas por el contribuyente"
    )
    SIMULACI_N_DE_OPERACIONES = "Simulación de operaciones"
    OMISI_N_DE_INGRESOS = "Omisión de ingresos"
    PROVEEDORES_INCONSISTENTES = "Proveedores inconsistentes"
    OTROS = "Otros"


class TdMotDesPc(Enum):
    """
    Descripción del motivo del evento Proceso de Control.
    """

    PROCESO_DE_CONTROL_INTERNO = "Proceso de control Interno"
    PROCESO_DE_FISCALIZACI_N = "Proceso de Fiscalización"
    PROCESO_DE_COBRANZAS = "Proceso de Cobranzas"
    PROCESO_DE_DEVOLUCI_N_DE_CR_DITOS_FISCALES = (
        "Proceso de Devolución de Créditos Fiscales"
    )


class TdMotEv(Enum):
    """
    Motivo del Evento.
    """

    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3
    VALUE_4 = 4


class TdTipEnd(Enum):
    """
    Tipo de Endoso.
    """

    VALUE_1 = 1
    VALUE_2 = 2


class TdTipIdenVeh(Enum):
    """
    Tipo de identificación del vehículo.
    """

    VALUE_1 = 1
    VALUE_2 = 2


class TiTiDeev(Enum):
    """
    Tipo de documento electronico.
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


class TiTipEve(Enum):
    """
    Tipo de Receptor.
    """

    VALUE_1 = 1
    VALUE_2 = 2


class TiTipFac(Enum):
    """
    Tipo de Factor.
    """

    VALUE_1 = 1
