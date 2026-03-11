from __future__ import annotations

from dataclasses import dataclass, field

from sifenlib.CommonMixin import CommonMixin
from sifenlib.de.bindings.v150.prot_proces_eventos_v141 import TgResProc

__NAMESPACE__ = "http://ekuatia.set.gov.py/sifen/xsd"


@dataclass(kw_only=True)
class RProtDe(CommonMixin):
    """
    Respuesta del protocolo de procesamiento del DE.

    :ivar Id: cdc resultado
    :ivar dFecProc:
    :ivar dDigVal: Valor hash del DE procesado
    :ivar dEstRes: Estado del resultado
    :ivar dProtAut:
    :ivar gResProc:
    """

    class Meta:
        name = "rProtDe"

    Id: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )
    dFecProc: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d[+|-]\d\d:\d\d",
        }
    )
    dDigVal: None | bytes = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "format": "base64",
        },
    )
    dEstRes: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )
    dProtAut: None | int = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )
    gResProc: list[TgResProc] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "max_occurs": 100,
        },
    )
