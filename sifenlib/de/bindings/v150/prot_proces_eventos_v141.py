from __future__ import annotations

from dataclasses import dataclass, field

from sifenlib.CommonMixin import CommonMixin

__NAMESPACE__ = "http://ekuatia.set.gov.py/sifen/xsd"


@dataclass(kw_only=True)
class TgResProc(CommonMixin):
    """
    Grupo Resultado de Procesamiento.
    """

    class Meta:
        name = "tgResProc"

    dCodRes: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"[0-9]{4}",
        }
    )
    dMsgRes: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "max_length": 255,
        }
    )


@dataclass(kw_only=True)
class TgResProcEve(CommonMixin):
    """
    Grupo de resultado de procesamiento.
    """

    class Meta:
        name = "tgResProcEVe"

    dEstRes: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 8,
            "max_length": 30,
        }
    )
    dProtAut: None | int = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )
    id: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_inclusive": "0",
            "max_inclusive": "9999999999",
            "pattern": r"[0-9]{1,10}",
        }
    )
    gResProc: list[TgResProc] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_occurs": 1,
            "max_occurs": 100,
        },
    )
