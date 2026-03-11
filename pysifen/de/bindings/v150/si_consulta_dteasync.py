from __future__ import annotations

from dataclasses import dataclass, field

from pysifen.CommonMixin import CommonMixin
from pysifen.de.bindings.v150.xmldsig_core_schema import Signature

__NAMESPACE__ = "http://ekuatia.set.gov.py/sifen/xsd"


@dataclass(kw_only=True)
class RConsultaDte(CommonMixin):
    """
    :ivar ConsultaDTE:
    :ivar Signature: Firma Digital de la ConsultaDTE
    """

    class Meta:
        name = "rConsultaDTE"
        namespace = "http://ekuatia.set.gov.py/sifen/xsd"

    ConsultaDTE: RConsultaDte.ConsultaDte = field(
        metadata={
            "type": "Element",
        }
    )
    Signature: Signature = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        }
    )

    @dataclass(kw_only=True)
    class ConsultaDte(CommonMixin):
        dRuc: str = field(
            metadata={
                "type": "Element",
                "min_length": 5,
                "max_length": 8,
                "pattern": r"[1-9][0-9]*[0-9A-D]?",
            }
        )
        dTiDE: str = field(
            metadata={
                "type": "Element",
                "pattern": r"1|[5-6]",
            }
        )
        dFecIni: str = field(
            metadata={
                "type": "Element",
                "pattern": r"([0][0-9]|[1-2][0-9]|[3][0-1])-([0][1-9]|[1][0-2])-[1-9][0-9]{3}",
            }
        )
        dFecFin: str = field(
            metadata={
                "type": "Element",
                "pattern": r"([0][0-9]|[1-2][0-9]|[3][0-1])-([0][1-9]|[1][0-2])-[1-9][0-9]{3}",
            }
        )
        Id: str = field(
            metadata={
                "type": "Attribute",
            }
        )
