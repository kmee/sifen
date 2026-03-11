from __future__ import annotations

from dataclasses import dataclass, field

from sifenlib.CommonMixin import CommonMixin

__NAMESPACE__ = "http://ekuatia.set.gov.py/sifen/xsd"


@dataclass(kw_only=True)
class REnviConsRuc(CommonMixin):
    class Meta:
        name = "rEnviConsRUC"
        namespace = "http://ekuatia.set.gov.py/sifen/xsd"

    dId: int = field(
        metadata={
            "type": "Element",
            "total_digits": 15,
        }
    )
    dRUCCons: str = field(
        metadata={
            "type": "Element",
            "min_length": 5,
            "max_length": 8,
            "pattern": r"[1-9][0-9]*[0-9A-D]?",
        }
    )


@dataclass(kw_only=True)
class TContenedorRuc(CommonMixin):
    """
    Respuesta del protocolo de procesamiento del DE.
    """

    class Meta:
        name = "tContenedorRuc"

    dRUCCons: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 5,
            "max_length": 8,
            "pattern": r"[1-9][0-9]*[0-9A-D]?",
        }
    )
    dRazCons: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "max_length": 250,
            "white_space": "preserve",
        }
    )
    dCodEstCons: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "length": 3,
        }
    )
    dDesEstCons: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "max_length": 25,
        }
    )
    dRUCFactElec: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "length": 1,
        }
    )


@dataclass(kw_only=True)
class RResEnviConsRuc(CommonMixin):
    """
    :ivar dCodRes:
    :ivar dMsgRes: Mensaje del resultado de procesamiento
    :ivar xContRUC: Contenedor del RUC
    """

    class Meta:
        name = "rResEnviConsRUC"
        namespace = "http://ekuatia.set.gov.py/sifen/xsd"

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
    xContRUC: None | TContenedorRuc = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
