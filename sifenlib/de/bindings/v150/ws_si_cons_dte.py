from __future__ import annotations

from dataclasses import dataclass, field

from sifenlib.CommonMixin import CommonMixin
from sifenlib.de.bindings.v150.si_consulta_dteasync import RConsultaDte

__NAMESPACE__ = "http://ekuatia.set.gov.py/sifen/xsd"


@dataclass(kw_only=True)
class RConsDteResponse(CommonMixin):
    """
    :ivar dFecProc:
    :ivar dMsgRes: Mensaje del resultado de la consulta
    :ivar rConsDte: Archivo zip generado en la consulta de mis DTEs
    """

    class Meta:
        name = "rConsDteResponse"
        namespace = "http://ekuatia.set.gov.py/sifen/xsd"

    dFecProc: str = field(
        metadata={
            "type": "Element",
            "pattern": r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d",
        }
    )
    dMsgRes: str = field(
        metadata={
            "type": "Element",
            "min_length": 1,
            "max_length": 255,
        }
    )
    rConsDte: None | bytes = field(
        default=None,
        metadata={
            "type": "Element",
            "format": "base64",
        },
    )


@dataclass(kw_only=True)
class RConsDteRequest(CommonMixin):
    class Meta:
        name = "rConsDteRequest"
        namespace = "http://ekuatia.set.gov.py/sifen/xsd"

    rConsultaDTE: RConsultaDte = field(
        metadata={
            "type": "Element",
        }
    )
