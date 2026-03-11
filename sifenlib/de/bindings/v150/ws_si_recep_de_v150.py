from __future__ import annotations

from dataclasses import dataclass, field

from sifenlib.CommonMixin import CommonMixin
from sifenlib.de.bindings.v150.prot_proces_de_v150 import RProtDe

__NAMESPACE__ = "http://ekuatia.set.gov.py/sifen/xsd"


@dataclass(kw_only=True)
class REnviDe(CommonMixin):
    """
    Recepcion de Documentos Electronicos.

    :ivar dId: Identificador de control de envio
    :ivar xDE: XML del Documento Electronico Transferido
    """

    class Meta:
        name = "rEnviDe"
        namespace = "http://ekuatia.set.gov.py/sifen/xsd"

    dId: int = field(
        metadata={
            "type": "Element",
            "total_digits": 15,
        }
    )
    xDE: REnviDe.XDe = field(
        metadata={
            "type": "Element",
        }
    )

    @dataclass(kw_only=True)
    class XDe(CommonMixin):
        ekuatia_set_gov_pysifenxsd_element: None | object = field(
            default=None,
            metadata={
                "type": "Wildcard",
                "process_contents": "skip",
            },
        )


@dataclass(kw_only=True)
class RRetEnviDe(CommonMixin):
    """
    Respuesta de la recepcion de Documentos Electronicos.

    :ivar rProtDe: Protocolo de procesamiento de DE
    """

    class Meta:
        name = "rRetEnviDe"
        namespace = "http://ekuatia.set.gov.py/sifen/xsd"

    rProtDe: RProtDe = field(
        metadata={
            "type": "Element",
        }
    )
