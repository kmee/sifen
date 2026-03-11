from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal

from sifenlib.CommonMixin import CommonMixin
from sifenlib.de.bindings.v150.evento_types_v150 import (
    TcMotDet,
    TcMotImp,
    TcMotOa,
    TcMotPc,
    TdMotDesDet,
    TdMotDesImp,
    TdMotDesOa,
    TdMotDesPc,
    TdMotEv,
    TdTipEnd,
    TdTipIdenVeh,
    TiTiDeev,
    TiTipEve,
    TiTipFac,
)
from sifenlib.de.bindings.v150.fe_types_v141 import (
    TdDesModTrans,
    TdDtipDoc,
    TdDtipDocRec,
)
from sifenlib.de.bindings.v150.paises_v100 import PaisType
from sifenlib.de.bindings.v150.xmldsig_core_schema import Signature

__NAMESPACE__ = "http://ekuatia.set.gov.py/sifen/xsd"


@dataclass(kw_only=True)
class RGeEvenAntRem(CommonMixin):
    """
    Grupo de Datos que identifican al Evento anticipo ó remision.
    """

    class Meta:
        name = "rGeEvenAntRem"

    Id: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "length": 44,
            "pattern": r"[0-9]{2}([0-9]{7}[0-9A-D]?)[0-9]{34}",
        }
    )


@dataclass(kw_only=True)
class TrGeDeVtr(CommonMixin):
    """
    Grupo de Datos que identifican al Evento por actualización de datos del
    transporte.
    """

    class Meta:
        name = "trGeDeVTr"

    Id: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "length": 44,
            "pattern": r"[0-9]{2}([0-9]{7}[0-9A-D]?)[0-9]{34}",
        },
    )
    dMotEv: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "max_length": 10,
        },
    )
    cDepEnt: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "max_length": 10,
        },
    )
    dDesDepEnt: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d",
        },
    )
    cDisEnt: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d",
        },
    )
    dDesDisEnt: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d",
        },
    )
    cCiuEnt: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "length": 44,
            "pattern": r"[0-9]{2}([0-9]{7}[0-9A-D]?)[0-9]{34}",
        },
    )
    dDesCiuEnt: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "max_length": 10,
        },
    )
    dDirEnt: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "max_length": 10,
        },
    )
    dNumCas: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d",
        },
    )
    dCompDir1: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d",
        },
    )
    dNomChof: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d",
        },
    )
    dNumIDChof: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "length": 44,
            "pattern": r"[0-9]{2}([0-9]{7}[0-9A-D]?)[0-9]{34}",
        },
    )
    iNatTrans: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "max_length": 10,
        },
    )
    dRucTrans: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "max_length": 10,
        },
    )
    dDVTrans: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d",
        },
    )
    dNomTrans: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d",
        },
    )
    iTipIDTrans: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d",
        },
    )
    dDTipIDTrans: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "length": 44,
            "pattern": r"[0-9]{2}([0-9]{7}[0-9A-D]?)[0-9]{34}",
        },
    )
    dNumIDTrans: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "max_length": 10,
        },
    )
    iTipTrans: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "max_length": 10,
        },
    )
    dDesTipTrans: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d",
        },
    )
    iModTrans: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d",
        },
    )
    dDesModTrans: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d",
        },
    )
    dTiVehTras: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "length": 44,
            "pattern": r"[0-9]{2}([0-9]{7}[0-9A-D]?)[0-9]{34}",
        },
    )
    dMarVeh: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "max_length": 10,
        },
    )
    dTipIdenVeh: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "max_length": 10,
        },
    )
    dNroIDVeh: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d",
        },
    )
    dNroMatVeh: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d",
        },
    )


@dataclass(kw_only=True)
class TrGeDevCcff(CommonMixin):
    """
    Grupo de Datos que identifican al Evento de devolución de créditos
    fiscales - Cuestionado ó Devuelto.
    """

    class Meta:
        name = "trGeDevCCFF"

    Id: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "length": 44,
            "pattern": r"[0-9]{2}([0-9]{7}[0-9A-D]?)[0-9]{34}",
        }
    )
    dNumDevSol: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "max_length": 10,
        }
    )
    dNumDevInf: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "max_length": 10,
        }
    )
    dNumDevRes: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "max_length": 10,
        }
    )
    dFeEmiSol: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d",
        }
    )
    dFeEmiInf: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d",
        }
    )
    dFeEmiRes: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d",
        }
    )


@dataclass(kw_only=True)
class TrGeVeCcff(CommonMixin):
    """
    Grupo de Datos que identifican al Evento de créditos fiscales.
    """

    class Meta:
        name = "trGeVeCCFF"

    Id: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "length": 44,
            "pattern": r"[0-9]{2}([0-9]{7}[0-9A-D]?)[0-9]{34}",
        }
    )
    dNumTraCCFF: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "max_length": 10,
        }
    )
    dFeAceTraCCFF: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d",
        }
    )


@dataclass(kw_only=True)
class TrGeVeCan(CommonMixin):
    """
    Grupo de Datos que identifican al evento de Cancelación del DTE.
    """

    class Meta:
        name = "trGeVeCan"

    Id: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "length": 44,
            "pattern": r"[0-9]{2}([0-9]{7}[0-9A-D]?)[0-9]{34}",
        }
    )
    mOtEve: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 5,
            "max_length": 500,
        }
    )


@dataclass(kw_only=True)
class TrGeVeDisconf(CommonMixin):
    """
    Grupo de Datos que identifican al evento receptor Disconformidad.
    """

    class Meta:
        name = "trGeVeDisconf"

    Id: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "length": 44,
            "pattern": r"[0-9]{2}([0-9]{7}[0-9A-D]?)[0-9]{34}",
        }
    )
    mOtEve: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 5,
            "max_length": 500,
        }
    )


@dataclass(kw_only=True)
class TrGeVeRetAce(CommonMixin):
    """
    Grupo de Datos que identifican al Evento de retención.
    """

    class Meta:
        name = "trGeVeRetAce"

    Id: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "length": 44,
            "pattern": r"[0-9]{2}([0-9]{7}[0-9A-D]?)[0-9]{34}",
        }
    )
    dRuc: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 5,
            "max_length": 8,
            "pattern": r"[1-9][0-9]*[0-9A-D]?",
        }
    )
    dNumTimRet: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 8,
            "max_length": 8,
            "pattern": r"0+[1-9][0-9]*|[1-9]+[0-9]+",
        }
    )
    dEstRet: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 3,
            "pattern": r"[0-9]{3}",
        }
    )
    dPunExpRet: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 3,
            "pattern": r"[0-9]{3}",
        }
    )
    dNumDocRet: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 7,
            "max_length": 7,
            "pattern": r"0+[1-9][0-9]*|[1-9]+[0-9]+",
        }
    )
    dCodConRet: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "max_length": 40,
        }
    )
    dFeEmiRet: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d",
        }
    )
    dMonRet: Decimal = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("999999999999999.99999999"),
            "total_digits": 23,
            "fraction_digits": 8,
        }
    )


@dataclass(kw_only=True)
class TrGeVeRetAnu(CommonMixin):
    """
    Grupo de Datos que identifican al Evento de retención anulación.
    """

    class Meta:
        name = "trGeVeRetAnu"

    Id: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "length": 44,
            "pattern": r"[0-9]{2}([0-9]{7}[0-9A-D]?)[0-9]{34}",
        }
    )
    dRuc: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 5,
            "max_length": 8,
            "pattern": r"[1-9][0-9]*[0-9A-D]?",
        }
    )
    dNumTimRet: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 8,
            "max_length": 8,
            "pattern": r"0+[1-9][0-9]*|[1-9]+[0-9]+",
        }
    )
    dEstRet: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 3,
            "pattern": r"[0-9]{3}",
        }
    )
    dPunExpRet: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 3,
            "pattern": r"[0-9]{3}",
        }
    )
    dNumDocRet: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 7,
            "max_length": 7,
            "pattern": r"0+[1-9][0-9]*|[1-9]+[0-9]+",
        }
    )
    dCodConRet: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "max_length": 40,
        }
    )
    dFeEmiRet: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d",
        }
    )
    dFecAnRet: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d",
        }
    )
    dMonRet: Decimal = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("999999999999999.99999999"),
            "total_digits": 23,
            "fraction_digits": 8,
        }
    )


@dataclass(kw_only=True)
class TrGeveNom(CommonMixin):
    """
    Grupo de Datos que identifican al Evento de Nominación.

    :ivar Id:
    :ivar mOtEve:
    :ivar iNatRec:
    :ivar iTiOpe:
    :ivar cPaisRec:
    :ivar dDesPaisRe:
    :ivar iTiContRec:
    :ivar dRucRec:
    :ivar dDVRec:
    :ivar iTipIDRec:
    :ivar dDTipIDRec:
    :ivar dNumIDRec:
    :ivar dNomRec:
    :ivar dNomFanRec:
    :ivar dDirRec:
    :ivar dNumCasRec:
    :ivar cDepRec:
    :ivar dDesDepRec:
    :ivar cDisRec:
    :ivar dDesDisRec:
    :ivar cCiuRec:
    :ivar dDesCiuRec:
    :ivar dTelRec:
    :ivar dCelRec:
    :ivar dEmailRec:
    :ivar dCodCliente: Codigo del Cliente
    """

    class Meta:
        name = "trGEveNom"

    Id: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "length": 44,
            "pattern": r"[0-9]{2}([0-9]{7}[0-9A-D]?)[0-9]{34}",
        }
    )
    mOtEve: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 5,
            "max_length": 500,
        }
    )
    iNatRec: TiTipEve = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )
    iTiOpe: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "white_space": "preserve",
            "pattern": r"[1-2]|[4]",
        }
    )
    cPaisRec: PaisType = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )
    dDesPaisRe: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 4,
            "max_length": 30,
            "white_space": "preserve",
            "pattern": r".*[^\s].*",
        }
    )
    iTiContRec: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "white_space": "collapse",
            "pattern": r"[1-2]",
        },
    )
    dRucRec: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 5,
            "max_length": 8,
            "pattern": r"[1-9][0-9]*[0-9A-D]?",
        },
    )
    dDVRec: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "white_space": "collapse",
            "pattern": r"[0-9]",
        },
    )
    iTipIDRec: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "white_space": "collapse",
            "pattern": r"[1-5]",
        },
    )
    dDTipIDRec: None | TdDtipDocRec = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )
    dNumIDRec: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"[0-9A-Za-z\-]{1,20}",
        },
    )
    dNomRec: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 4,
            "max_length": 255,
        }
    )
    dNomFanRec: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 4,
            "max_length": 255,
        },
    )
    dDirRec: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "max_length": 255,
        },
    )
    dNumCasRec: None | int = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_inclusive": 0,
            "total_digits": 6,
        },
    )
    cDepRec: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_inclusive": "1",
            "max_inclusive": "99",
            "pattern": r"[0-9]{1,2}",
        },
    )
    dDesDepRec: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 6,
            "max_length": 16,
        },
    )
    cDisRec: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_inclusive": "1",
            "max_inclusive": "9999",
            "pattern": r"[0-9]{1,4}",
        },
    )
    dDesDisRec: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "max_length": 30,
        },
    )
    cCiuRec: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_inclusive": "1",
            "max_inclusive": "99999",
            "pattern": r"[0-9]{1,5}",
        },
    )
    dDesCiuRec: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "max_length": 30,
        },
    )
    dTelRec: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"\d{8,15}",
        },
    )
    dCelRec: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"\d{10,20}",
        },
    )
    dEmailRec: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"([0-9a-zA-Z#$%]([-.\w]*[0-9a-zA-Z#$%'\.\-_])*@([0-9a-zA-Z][-\w]*[0-9a-zA-Z]\.)+[a-zA-Z]{2,9})",
        },
    )
    dCodCliente: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 3,
            "max_length": 15,
            "white_space": "collapse",
        },
    )


@dataclass(kw_only=True)
class TrGeVeConf(CommonMixin):
    """
    Grupo de Datos que identifican al evento receptor Conformidad.
    """

    class Meta:
        name = "trGeVeConf"

    Id: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "length": 44,
            "pattern": r"[0-9]{2}([0-9]{7}[0-9A-D]?)[0-9]{34}",
        }
    )
    iTipConf: TiTipEve = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )
    dFecRecep: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d",
        },
    )


@dataclass(kw_only=True)
class TrGeVeDescon(CommonMixin):
    """
    Grupo de Datos que identifican al evento receptor Desconocimiento.
    """

    class Meta:
        name = "trGeVeDescon"

    Id: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "length": 44,
            "pattern": r"[0-9]{2}([0-9]{7}[0-9A-D]?)[0-9]{34}",
        }
    )
    dFecEmi: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d",
        }
    )
    dFecRecep: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d",
        }
    )
    iTipRec: TiTipEve = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )
    dNomRec: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 4,
            "max_length": 255,
        }
    )
    dRucRec: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 5,
            "max_length": 8,
            "pattern": r"[1-9][0-9]*[0-9A-D]?",
        },
    )
    dDVRec: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "white_space": "collapse",
            "pattern": r"[0-9]",
        },
    )
    dTipIDRec: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "white_space": "collapse",
            "pattern": r"[1-4]",
        },
    )
    dNumID: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"[0-9A-Za-z\-]{1,20}",
        },
    )
    mOtEve: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 5,
            "max_length": 500,
        }
    )


@dataclass(kw_only=True)
class TrGeVeDet(CommonMixin):
    """
    Grupo de Datos que identifican al Evento Origen Set Determinacion del
    DTE.
    """

    class Meta:
        name = "trGeVeDet"

    Id: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "length": 44,
            "pattern": r"[0-9]{2}([0-9]{7}[0-9A-D]?)[0-9]{34}",
        }
    )
    dFechaDet: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"\d{4}-\d\d-\d\d",
        }
    )
    cMotDet: TcMotDet = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )
    dMotDesDet: TdMotDesDet = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )
    dObsEveDet: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "max_length": 500,
        },
    )


@dataclass(kw_only=True)
class TrGeVeEnd(CommonMixin):
    """
    Grupo de Datos que identifican al Evento de Endoso.
    """

    class Meta:
        name = "trGeVeEnd"

    Id: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "length": 44,
            "pattern": r"[0-9]{2}([0-9]{7}[0-9A-D]?)[0-9]{34}",
        }
    )
    iTipRec: TiTipEve = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )
    dNomRec: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 4,
            "max_length": 255,
        }
    )
    dRucRec: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 5,
            "max_length": 8,
            "pattern": r"[1-9][0-9]*[0-9A-D]?",
        },
    )
    dDVRec: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "white_space": "collapse",
            "pattern": r"[0-9]",
        },
    )
    dTipIDRec: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "white_space": "collapse",
            "pattern": r"[1-4]",
        },
    )
    dNumIDRec: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"[0-9A-Za-z\-]{1,20}",
        },
    )
    dRucEmi: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 5,
            "max_length": 8,
            "pattern": r"[1-9][0-9]*[0-9A-D]?",
        }
    )
    dDVEmi: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "white_space": "collapse",
            "pattern": r"[0-9]",
        }
    )
    dNomEmi: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 4,
            "max_length": 255,
        }
    )
    dTipEnd: TdTipEnd = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )
    iTipFac: TiTipFac = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )
    dNomFac: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 4,
            "max_length": 255,
        }
    )
    dRucFac: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 5,
            "max_length": 8,
            "pattern": r"[1-9][0-9]*[0-9A-D]?",
        }
    )
    dDVFac: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "white_space": "collapse",
            "pattern": r"[0-9]",
        }
    )
    dNumCon: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "max_length": 50,
        },
    )
    dNumRegPubCon: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "max_length": 50,
        },
    )
    dTotalGs: Decimal = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("999999999999999.99999999"),
            "total_digits": 23,
            "fraction_digits": 8,
        }
    )
    dPorDes: Decimal = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("999.99999999"),
            "total_digits": 11,
            "fraction_digits": 8,
        }
    )
    dMonDesMonExt: None | Decimal = field(
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
    dTipCamDesMonExt: None | Decimal = field(
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
    dMonDesGs: Decimal = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("999999999999999.99999999"),
            "total_digits": 23,
            "fraction_digits": 8,
        }
    )
    dTotOpeEndGs: Decimal = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("999999999999999.99999999"),
            "total_digits": 23,
            "fraction_digits": 8,
        }
    )


@dataclass(kw_only=True)
class TrGeVeImp(CommonMixin):
    """
    Grupo de Datos que identifican al Evento Origen Set Impugnacion del
    DTE.
    """

    class Meta:
        name = "trGeVeImp"

    Id: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "length": 44,
            "pattern": r"[0-9]{2}([0-9]{7}[0-9A-D]?)[0-9]{34}",
        }
    )
    dFechaImp: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"\d{4}-\d\d-\d\d",
        }
    )
    cMotImp: TcMotImp = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )
    dMotDesImp: TdMotDesImp = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )
    dObsEveImp: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "max_length": 500,
        },
    )


@dataclass(kw_only=True)
class TrGeVeInu(CommonMixin):
    """
    Grupo de Datos que identifican al evento de Inutilización de numero de
    un DE.
    """

    class Meta:
        name = "trGeVeInu"

    dNumTim: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 8,
            "max_length": 8,
            "pattern": r"0+[1-9][0-9]*|[1-9]+[0-9]+",
        }
    )
    dEst: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 3,
            "pattern": r"[0-9]{3}",
        }
    )
    dPunExp: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 3,
            "pattern": r"[0-9]{3}",
        }
    )
    dNumIn: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 7,
            "pattern": r"0+[1-9][0-9]*|[1-9]+[0-9]+",
        }
    )
    dNumFin: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 7,
            "pattern": r"0+[1-9][0-9]*|[1-9]+[0-9]+",
        }
    )
    iTiDE: TiTiDeev = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )
    mOtEve: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 5,
            "max_length": 500,
        }
    )
    dSerieNum: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 2,
            "max_length": 2,
            "pattern": r"[A-Z][A-Z]",
        },
    )


@dataclass(kw_only=True)
class TrGeVeNotRec(CommonMixin):
    """
    Grupo de Datos que identifican al evento receptor Notificación -
    Recepción de un DE/DTE.
    """

    class Meta:
        name = "trGeVeNotRec"

    Id: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "length": 44,
            "pattern": r"[0-9]{2}([0-9]{7}[0-9A-D]?)[0-9]{34}",
        }
    )
    dFecEmi: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d",
        }
    )
    dFecRecep: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d",
        }
    )
    iTipRec: TiTipEve = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )
    dNomRec: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 4,
            "max_length": 255,
        }
    )
    dRucRec: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 5,
            "max_length": 8,
            "pattern": r"[1-9][0-9]*[0-9A-D]?",
        },
    )
    dDVRec: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "white_space": "collapse",
            "pattern": r"[0-9]",
        },
    )
    dTipIDRec: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "white_space": "collapse",
            "pattern": r"[1-5]",
        },
    )
    dNumID: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"[0-9A-Za-z\-]{1,20}",
        },
    )
    dTotalGs: Decimal = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("999999999999999.99999999"),
            "total_digits": 23,
            "fraction_digits": 8,
        }
    )


@dataclass(kw_only=True)
class TrGeVeOa(CommonMixin):
    """
    Grupo de Datos que identifican al Evento Origen Set Objeto de Analisis.
    """

    class Meta:
        name = "trGeVeOA"

    Id: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "length": 44,
            "pattern": r"[0-9]{2}([0-9]{7}[0-9A-D]?)[0-9]{34}",
        }
    )
    dFechaOA: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"\d{4}-\d\d-\d\d",
        }
    )
    cMotOA: TcMotOa = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )
    dMotDesOA: TdMotDesOa = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )
    dObsOA: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "max_length": 500,
        },
    )


@dataclass(kw_only=True)
class TrGeVePc(CommonMixin):
    """
    Grupo de Datos que identifican al Evento Origen Set Proceso de Control.
    """

    class Meta:
        name = "trGeVePC"

    Id: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "length": 44,
            "pattern": r"[0-9]{2}([0-9]{7}[0-9A-D]?)[0-9]{34}",
        }
    )
    dFechaPC: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"\d{4}-\d\d-\d\d",
        }
    )
    cMotPC: TcMotPc = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )
    dMotDesPC: TdMotDesPc = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )
    dObsEvePC: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "max_length": 500,
        },
    )


@dataclass(kw_only=True)
class TrGeVeTr(CommonMixin):
    """
    Grupo de Datos que identifican al Evento de Transporte.
    """

    class Meta:
        name = "trGeVeTr"

    Id: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "length": 44,
            "pattern": r"[0-9]{2}([0-9]{7}[0-9A-D]?)[0-9]{34}",
        }
    )
    dMotEv: TdMotEv = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )
    cDepEnt: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_inclusive": "1",
            "max_inclusive": "99",
            "pattern": r"[0-9]{1,2}",
        },
    )
    dDesDepEnt: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 6,
            "max_length": 16,
        },
    )
    cDisEnt: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_inclusive": "1",
            "max_inclusive": "9999",
            "pattern": r"[0-9]{1,4}",
        },
    )
    dDesDisEnt: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "max_length": 30,
        },
    )
    cCiuEnt: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_inclusive": "1",
            "max_inclusive": "99999",
            "pattern": r"[0-9]{1,5}",
        },
    )
    dDesCiuEnt: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "max_length": 30,
        },
    )
    dDirEnt: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "max_length": 255,
        },
    )
    dNumCas: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_inclusive": "0",
            "max_inclusive": "999999",
            "pattern": r"[0-9]{1,6}",
        },
    )
    dCompDir1: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "max_length": 255,
        },
    )
    dNomChof: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 4,
            "max_length": 255,
        },
    )
    dNumIDChof: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"[0-9A-Za-z\-]{1,20}",
        },
    )
    iNatTrans: None | TiTipEve = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )
    dRucTrans: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 5,
            "max_length": 8,
            "pattern": r"[1-9][0-9]*[0-9A-D]?",
        },
    )
    dDVTrans: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "white_space": "collapse",
            "pattern": r"[0-9]",
        },
    )
    dNomTrans: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 4,
            "max_length": 255,
        },
    )
    iTipIDTrans: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "white_space": "collapse",
            "pattern": r"[1-4]",
        },
    )
    dDTipIDTrans: None | TdDtipDoc = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )
    dNumIDTrans: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"[0-9A-Za-z\-]{1,20}",
        },
    )
    iTipTrans: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "white_space": "collapse",
            "pattern": r"[1-2]",
        },
    )
    dDesTipTrans: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 6,
            "max_length": 7,
        },
    )
    iModTrans: None | TdMotEv = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )
    dDesModTrans: None | TdDesModTrans = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )
    dTiVehTras: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 4,
            "max_length": 10,
        },
    )
    dMarVeh: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "max_length": 10,
        },
    )
    dTipIdenVeh: None | TdTipIdenVeh = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )
    dNroIDVeh: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "max_length": 20,
        },
    )
    dNroMatVeh: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "length": 6,
        },
    )


@dataclass(kw_only=True)
class TgGroupEvt(CommonMixin):
    """
    Grupo del evento.
    """

    class Meta:
        name = "tgGroupEvt"

    rGeVeCan: None | TrGeVeCan = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )
    rGeVeInu: None | TrGeVeInu = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )
    rGeVeNotRec: None | TrGeVeNotRec = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )
    rGeVeConf: None | TrGeVeConf = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )
    rGeVeDisconf: None | TrGeVeDisconf = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )
    rGeVeDescon: None | TrGeVeDescon = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )
    rGeVeEnd: None | TrGeVeEnd = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )
    rGeVeTr: None | TrGeVeTr = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )
    rGEveNom: None | TrGeveNom = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )


@dataclass(kw_only=True)
class TgGroupEvtEmi(CommonMixin):
    """
    Grupo del evento Emisores.
    """

    class Meta:
        name = "tgGroupEvtEmi"

    rGeVeRetAce: None | TrGeVeRetAce = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )
    rGeVeRetAnu: None | TrGeVeRetAnu = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )
    rGeVeCCFF: None | TrGeVeCcff = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )
    rGeDevCCFFCue: None | TrGeDevCcff = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )
    rGeDevCCFFDev: None | TrGeDevCcff = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )
    rGeVeAnt: None | RGeEvenAntRem = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )
    rGeVeRem: None | RGeEvenAntRem = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )
    rGEveNom: None | TrGeveNom = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )


@dataclass(kw_only=True)
class TgGroupEvtRecep(CommonMixin):
    """
    Grupo del evento Receptores.
    """

    class Meta:
        name = "tgGroupEvtRecep"

    rGeVeNotRec: None | TrGeVeNotRec = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )
    rGeVeConf: None | TrGeVeConf = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )
    rGeVeDisconf: None | TrGeVeDisconf = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )
    rGeVeDescon: None | TrGeVeDescon = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )


@dataclass(kw_only=True)
class TgGroupEvtSet(CommonMixin):
    """
    Grupo del evento Origen SET.
    """

    class Meta:
        name = "tgGroupEvtSet"

    rGeVeOA: None | TrGeVeOa = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )
    rGeVePC: None | TrGeVePc = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )
    rGeVeImp: None | TrGeVeImp = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )
    rGeVeDet: None | TrGeVeDet = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )


@dataclass(kw_only=True)
class TrEve(CommonMixin):
    class Meta:
        name = "trEve"

    dFecFirma: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d",
        }
    )
    dVerFor: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "total_digits": 3,
            "pattern": r"[1][4][1]|[1][5][0]",
        }
    )
    gGroupTiEvt: TgGroupEvt = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )
    Id: str = field(
        metadata={
            "type": "Attribute",
            "min_inclusive": "1",
            "max_inclusive": "9999999999",
            "pattern": r"[0-9]+",
        }
    )


@dataclass(kw_only=True)
class TrEveEmi(CommonMixin):
    class Meta:
        name = "trEveEmi"

    dFecFirma: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d",
        }
    )
    dVerFor: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "total_digits": 3,
            "pattern": r"[1][4][1]|[1][5][0]",
        }
    )
    gGroupTiEvt: TgGroupEvtEmi = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )


@dataclass(kw_only=True)
class TrEveRecep(CommonMixin):
    class Meta:
        name = "trEveRecep"

    dFecFirma: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d",
        }
    )
    dVerFor: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "total_digits": 3,
            "pattern": r"[1][4][1]|[1][5][0]",
        }
    )
    gGroupTiEvt: TgGroupEvtRecep = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )


@dataclass(kw_only=True)
class TrEveSet(CommonMixin):
    class Meta:
        name = "trEveSet"

    dFecFirma: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d",
        }
    )
    dVerFor: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "total_digits": 3,
            "pattern": r"[1][4][1]|[1][5][0]",
        }
    )
    gGroupTiEvt: TgGroupEvtSet = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )


@dataclass(kw_only=True)
class TrGesEve(CommonMixin):
    """
    :ivar rEve:
    :ivar Signature: Firma Digital del DE
    """

    class Meta:
        name = "trGesEve"

    rEve: TrEve = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )
    Signature: Signature = field(
        metadata={
            "type": "Element",
            "namespace": "http://www.w3.org/2000/09/xmldsig#",
        }
    )


@dataclass(kw_only=True)
class TrGesEveEmi(CommonMixin):
    class Meta:
        name = "trGesEveEmi"

    rEve: TrEveEmi = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )


@dataclass(kw_only=True)
class TrGesEveRecep(CommonMixin):
    class Meta:
        name = "trGesEveRecep"

    rEve: TrEveRecep = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )


@dataclass(kw_only=True)
class TrGesEveSet(CommonMixin):
    class Meta:
        name = "trGesEveSet"

    rEve: TrEveSet = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )


@dataclass(kw_only=True)
class TgGroupGesEve(CommonMixin):
    class Meta:
        name = "tgGroupGesEve"

    rGesEve: list[TrGesEve] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_occurs": 1,
            "max_occurs": 15,
        },
    )
