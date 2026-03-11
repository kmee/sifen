from __future__ import annotations

from dataclasses import dataclass, field

from pysifen.CommonMixin import CommonMixin
from pysifen.de.bindings.v150.si_consulta_dteasync import RConsultaDte

__NAMESPACE__ = "http://ekuatia.set.gov.py/sifen/xsd"


@dataclass(kw_only=True)
class REnviConsDteAsyncResponse(CommonMixin):
    """
    :ivar dFecProc:
    :ivar dProtConsDTEAsync:
    :ivar dMsgRes: Mensaje del resultado de la consulta
    """

    class Meta:
        name = "rEnviConsDteAsyncResponse"
        namespace = "http://ekuatia.set.gov.py/sifen/xsd"

    dFecProc: str = field(
        metadata={
            "type": "Element",
            "pattern": r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d",
        }
    )
    dProtConsDTEAsync: str = field(
        metadata={
            "type": "Element",
        }
    )
    dMsgRes: str = field(
        metadata={
            "type": "Element",
            "min_length": 1,
            "max_length": 255,
        }
    )


@dataclass(kw_only=True)
class REnviConsDteAsyncRequest(CommonMixin):
    class Meta:
        name = "rEnviConsDteAsyncRequest"
        namespace = "http://ekuatia.set.gov.py/sifen/xsd"

    rConsultaDTE: RConsultaDte = field(
        metadata={
            "type": "Element",
        }
    )
