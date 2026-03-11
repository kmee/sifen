from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from pysifen.CommonMixin import CommonMixin
from pysifen.de.bindings.v150.prot_proces_eventos_v141 import TgResProc

__NAMESPACE__ = "http://ekuatia.set.gov.py/sifen/xsd"


@dataclass(kw_only=True)
class REnviConsLoteDe(CommonMixin):
    """
    Recepcion de Documentos Para Consulta de Lote.

    :ivar dId:
    :ivar dProtConsLote: Número de Lote
    :ivar dCDC:
    """

    class Meta:
        name = "rEnviConsLoteDe"
        namespace = "http://ekuatia.set.gov.py/sifen/xsd"

    dId: int = field(
        metadata={
            "type": "Element",
            "total_digits": 15,
        }
    )
    dProtConsLote: None | Decimal = field(
        default=None,
        metadata={
            "type": "Element",
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("9999999999999999999999999999"),
            "total_digits": 28,
            "fraction_digits": 0,
        },
    )
    dCDC: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "max_length": 50,
        },
    )


@dataclass(kw_only=True)
class TgResProcLote(CommonMixin):
    """
    Grupo de resultado de procesamiento.

    :ivar id: CDC del DE procesado
    :ivar dEstRes: Estado del resultado
    :ivar dProtAut: Número de transacción
    :ivar gResProc:
    """

    class Meta:
        name = "tgResProcLote"

    id: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "max_length": 47,
        }
    )
    dEstRes: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 8,
            "max_length": 30,
        }
    )
    dProtAut: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"[0-9]{1,10}",
        },
    )
    gResProc: list[TgResProc] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_occurs": 1,
            "max_occurs": 5,
        },
    )


@dataclass(kw_only=True)
class RResEnviConsLoteDe(CommonMixin):
    """
    Respuesta de la Consulta de Documentos Electronicos por Lote.

    :ivar dFecProc:
    :ivar dCodResLot: Código de resultado de procesamiento del lote
    :ivar dMsgResLot: Mensaje del resultado de recepción
    :ivar gResProcLote:
    """

    class Meta:
        name = "rResEnviConsLoteDe"
        namespace = "http://ekuatia.set.gov.py/sifen/xsd"

    dFecProc: str = field(
        metadata={
            "type": "Element",
            "pattern": r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d[+|-]\d\d:\d\d",
        }
    )
    dCodResLot: str = field(
        metadata={
            "type": "Element",
            "min_length": 1,
            "max_length": 4,
        }
    )
    dMsgResLot: str = field(
        metadata={
            "type": "Element",
            "min_length": 1,
            "max_length": 255,
        }
    )
    gResProcLote: list[TgResProcLote] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "max_occurs": 50,
        },
    )
