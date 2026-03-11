from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum

from sifenlib.CommonMixin import CommonMixin
from sifenlib.de.bindings.v150.de_types_v150 import (
    TdDesForPagValue,
    TdDtipIdrespDeValue,
    TiForPag,
)
from sifenlib.de.bindings.v150.unidades_medida_v141 import (
    TcUniMed,
    TdDesUniMed,
)

__NAMESPACE__ = "http://ekuatia.set.gov.py/sifen/xsd"


class TgCamCargICarCarga(Enum):
    VALUE_1 = 1
    VALUE_2 = 2
    VALUE_3 = 3


class TgCamCargValue(Enum):
    MERCADER_AS_CON_CADENA_DE_FR_O = "Mercaderías con cadena de frío"
    CARGA_PELIGROSA = "Carga peligrosa"


@dataclass(kw_only=True)
class TgGrupPolSeg(CommonMixin):
    """
    Póliza de seguros.

    :ivar dPoliza:
    :ivar dUnidVig: Descripción de la unidad de tiempo de vigencia
    :ivar dVigencia:
    :ivar dNumPoliza: Número de la póliza
    :ivar dFecIniVig:
    :ivar dFecFinVig:
    :ivar dCodInt: Código interno del ítem
    """

    class Meta:
        name = "tgGrupPolSeg"

    dPoliza: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "max_length": 20,
            "white_space": "collapse",
        }
    )
    dUnidVig: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 3,
            "max_length": 15,
            "white_space": "collapse",
            "pattern": r".*[^\s].*",
        }
    )
    dVigencia: Decimal = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("99.9"),
            "total_digits": 3,
            "fraction_digits": 1,
        }
    )
    dNumPoliza: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "max_length": 25,
            "white_space": "collapse",
            "pattern": r".*[^\s].*",
        }
    )
    dFecIniVig: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d",
        },
    )
    dFecFinVig: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d",
        },
    )
    dCodInt: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "max_length": 50,
            "white_space": "collapse",
            "pattern": r".*[^\s].*",
        },
    )


@dataclass(kw_only=True)
class TgOblAfe(CommonMixin):
    """
    Grupo de campos que identifican las obligaciones afectadas.
    """

    class Meta:
        name = "tgOblAfe"

    cOblAfe: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "total_digits": 3,
            "white_space": "collapse",
            "pattern": r"[1-9][0-9][0-9]",
        }
    )
    dDesOblAfe: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 21,
            "max_length": 65,
            "white_space": "preserve",
            "pattern": r".*[^\s].*",
        }
    )


@dataclass(kw_only=True)
class TgValorRestaItem(CommonMixin):
    """
    Campos que describen los descuentos, anticipos y valor total por item.
    """

    class Meta:
        name = "tgValorRestaItem"

    dDescItem: None | Decimal = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("999999999999999.99999999"),
            "total_digits": 23,
            "fraction_digits": 8,
        },
    )
    dPorcDesIt: None | Decimal = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("100"),
            "total_digits": 11,
            "fraction_digits": 8,
        },
    )
    dDescGloItem: None | Decimal = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("999999999999999.99999999"),
            "total_digits": 23,
            "fraction_digits": 8,
        },
    )
    dAntPreUniIt: None | Decimal = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("999999999999999.99999999"),
            "total_digits": 23,
            "fraction_digits": 8,
        },
    )
    dAntGloPreUniIt: None | Decimal = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("999999999999999.99999999"),
            "total_digits": 23,
            "fraction_digits": 8,
        },
    )
    dTotOpeItem: Decimal = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("999999999999999.99999999"),
            "total_digits": 23,
            "fraction_digits": 8,
        }
    )
    dTotOpeGs: None | Decimal = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("999999999999999.99999999"),
            "total_digits": 23,
            "fraction_digits": 8,
        },
    )


@dataclass(kw_only=True)
class TgCamCarg(CommonMixin):
    """
    Campos generales de la carga.

    :ivar cUniMedTotVol:
    :ivar dDesUniMedTotVol:
    :ivar dTotVolMerc: Total volumen de la mercaderia
    :ivar cUniMedTotPes:
    :ivar dDesUniMedTotPes:
    :ivar dTotPesMerc: Total peso de la mercadería
    :ivar iCarCarga:
    :ivar dDesCarCarga:
    """

    class Meta:
        name = "tgCamCarg"

    cUniMedTotVol: None | TcUniMed = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )
    dDesUniMedTotVol: None | TdDesUniMed = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )
    dTotVolMerc: None | int = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "total_digits": 20,
        },
    )
    cUniMedTotPes: None | TcUniMed = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )
    dDesUniMedTotPes: None | TdDesUniMed = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )
    dTotPesMerc: None | int = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "total_digits": 20,
        },
    )
    iCarCarga: None | TgCamCargICarCarga = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )
    dDesCarCarga: None | TgCamCargValue = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )


@dataclass(kw_only=True)
class TgCamRde(CommonMixin):
    """
    Campos que componen el Recibo de Dinero Electrónico.

    :ivar iForPag:
    :ivar dDesForPag:
    :ivar dNumTrans: Número de Transacción
    :ivar dConc: Concepto/Observación
    :ivar dRucEntFin:
    :ivar dDvEntFin:
    :ivar dNomEntFin: Nombre o Razón Social de la Entidad Financiera
    :ivar dImpPag:
    """

    class Meta:
        name = "tgCamRDE"

    iForPag: TiForPag = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )
    dDesForPag: str | TdDesForPagValue = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "white_space": "preserve",
            "pattern": r".+",
        }
    )
    dNumTrans: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 3,
            "max_length": 10,
            "white_space": "collapse",
            "pattern": r".*[^\s].*",
        },
    )
    dConc: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "max_length": 255,
            "white_space": "collapse",
            "pattern": r".*[^\s].*",
        }
    )
    dRucEntFin: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 5,
            "max_length": 8,
            "pattern": r"[1-9][0-9]*[0-9A-D]?",
        },
    )
    dDvEntFin: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "white_space": "collapse",
            "pattern": r"[0-9]",
        },
    )
    dNomEntFin: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 4,
            "max_length": 255,
            "white_space": "collapse",
            "pattern": r".*[^\s].*",
        },
    )
    dImpPag: Decimal = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("999999999999999.9999"),
            "total_digits": 19,
            "fraction_digits": 4,
        }
    )


@dataclass(kw_only=True)
class TgRespDe(CommonMixin):
    """
    Grupo de Campos que identifican al responsable de la generación del DE.
    """

    class Meta:
        name = "tgRespDE"

    iTipIDRespDE: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "white_space": "collapse",
            "pattern": r"[1-4]|9",
        }
    )
    dDTipIDRespDE: str | TdDtipIdrespDeValue = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "white_space": "preserve",
            "pattern": r".+",
        }
    )
    dNumIDRespDE: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"[0-9A-Za-z\-]{1,20}",
        }
    )
    dNomRespDE: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r".*[^\s].*",
        }
    )
    dCarRespDE: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 4,
            "max_length": 100,
            "white_space": "preserve",
            "pattern": r".*[^\s].*",
        }
    )
