from __future__ import annotations

from dataclasses import dataclass, field

from sifenlib.CommonMixin import CommonMixin

__NAMESPACE__ = "http://ekuatia.set.gov.py/sifen/xsd"


@dataclass(kw_only=True)
class REnviConsDeRequest(CommonMixin):
    class Meta:
        name = "rEnviConsDeRequest"
        namespace = "http://ekuatia.set.gov.py/sifen/xsd"

    dId: int = field(
        metadata={
            "type": "Element",
            "total_digits": 15,
        }
    )
    dCDC: str = field(
        metadata={
            "type": "Element",
            "length": 44,
            "pattern": r"[0-9]{2}([0-9]{7}[0-9A-D])[0-9]{34}",
        }
    )


@dataclass(kw_only=True)
class REnviConsDeResponse(CommonMixin):
    """
    :ivar dFecProc:
    :ivar dCodRes:
    :ivar dMsgRes: Mensaje del resultado de procesamiento
    :ivar xContenDE: Contenedor del DE
    """

    class Meta:
        name = "rEnviConsDeResponse"
        namespace = "http://ekuatia.set.gov.py/sifen/xsd"

    dFecProc: str = field(
        metadata={
            "type": "Element",
            "pattern": r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d[+|-]\d\d:\d\d",
        }
    )
    dCodRes: str = field(
        metadata={
            "type": "Element",
            "length": 4,
        }
    )
    dMsgRes: str = field(
        metadata={
            "type": "Element",
            "min_length": 1,
            "max_length": 255,
        }
    )
    xContenDE: None | str = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
