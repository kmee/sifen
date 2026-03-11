from __future__ import annotations

from dataclasses import dataclass, field
from decimal import Decimal
from enum import Enum

from xsdata.models.datatype import XmlDate

from sifenlib.CommonMixin import CommonMixin
from sifenlib.de.bindings.v150.departamentos_v141 import (
    TDepartamentos,
    TDesDepartamento,
)
from sifenlib.de.bindings.v150.fe_types_v141 import (
    TcCatIsc,
    TcCondNeg,
    TcTasaIsc,
    TdCondTiCam,
    TdDcondCred,
    TdDcondOpe,
    TdDesAfecIva,
    TdDesCatIsc,
    TdDesDenTarjValue,
    TdDesIndPresValue,
    TdDesModTrans,
    TdDesMotEmi,
    TdDesTiDe,
    TdDesTimp,
    TdDesTiPag,
    TdDesTipComValue,
    TdDesTipDocAso,
    TdDesTipEmi,
    TdDesTipoDoc,
    TdDesTipOpVnValue,
    TdDesTiTran,
    TdDesTtrans,
    TdDmotivTrasValue,
    TdDtipDoc,
    TdDtipDocRec,
    TdTipCons,
    TiAfecIva,
    TiCondOpe,
    TiDenTarj,
    TiForProPa,
    TiIndPres,
    TiModTrans,
    TiMotEmi,
    TiMotivTras,
    TiRespEmiNr,
    TiRespFlete,
    TiTimp,
    TiTiPago,
    TiTipCom,
    TiTipDocAso,
    TiTipoDoc,
    TiTipOpVn,
    TiTipTra,
    TiTtrans,
)
from sifenlib.de.bindings.v150.monedas_v100 import CMondT
from sifenlib.de.bindings.v150.paises_v100 import PaisType
from sifenlib.de.bindings.v150.unidades_medida_v141 import (
    TcUniMed,
    TdDesUniMed,
)
from sifenlib.de.bindings.v150.xmldsig_core_schema import Signature

__NAMESPACE__ = "http://ekuatia.set.gov.py/sifen/xsd"


@dataclass(kw_only=True)
class TgActEco(CommonMixin):
    """
    Grupo de Campos de la Actividad Economica.
    """

    class Meta:
        name = "tgActEco"

    cActEco: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "max_length": 8,
            "pattern": r"[0-9A-Z]{1,8}",
        }
    )
    dDesActEco: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "max_length": 300,
            "white_space": "preserve",
            "pattern": r".*[^\s].*",
        }
    )


@dataclass(kw_only=True)
class TgCamFuFd(CommonMixin):
    """
    Campos fuera de la firma digital.

    :ivar dCarQR: Caracteres correspondiente al codigo QR
    :ivar dInfAdic: Información adicional de interés para el emisor
    """

    class Meta:
        name = "tgCamFuFD"

    dCarQR: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 100,
            "max_length": 600,
            "white_space": "preserve",
            "pattern": r".*[^\s].*",
        }
    )
    dInfAdic: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "max_length": 5000,
            "white_space": "preserve",
            "pattern": r".*[^\s].*",
        },
    )


@dataclass(kw_only=True)
class TgCamGen(CommonMixin):
    """
    Campos complementarios comerciales de uso general.

    :ivar dOrdCompra: Numero de orden de compra
    :ivar dOrdVta: Numero de orden de venta
    :ivar dAsiento: Número de asiento contable
    """

    class Meta:
        name = "tgCamGen"

    dOrdCompra: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "max_length": 15,
            "white_space": "collapse",
        },
    )
    dOrdVta: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "max_length": 15,
            "white_space": "collapse",
        },
    )
    dAsiento: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "max_length": 10,
            "white_space": "collapse",
        },
    )


@dataclass(kw_only=True)
class TgCompPub(CommonMixin):
    """
    Campos que describen informaciones de compras publicas.
    """

    class Meta:
        name = "tgCompPub"

    dModCont: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "length": 2,
            "white_space": "preserve",
            "pattern": r".*[^\s].*",
        }
    )
    dEntCont: str = field(
        metadata={
            "name": "dEntCont ",
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_inclusive": "1",
            "pattern": r"[0-9]{5}",
        }
    )
    dAnoCont: int = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "total_digits": 2,
        }
    )
    dSecCont: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_inclusive": "1",
            "pattern": r"[0-9]{7}",
        }
    )
    dFeCodCont: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"[2-9][0-9]{3}-([0][1-9]|[1][0-2])-([0][0-9]|[1-2][0-9]|[3][0-1])",
        }
    )


@dataclass(kw_only=True)
class TgCuotas(CommonMixin):
    """
    Campos que describen las cuotas.
    """

    class Meta:
        name = "tgCuotas"

    dMonCuota: Decimal = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("999999999999999.9999"),
            "total_digits": 19,
            "fraction_digits": 4,
        }
    )
    dVencCuo: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"[2-9][0-9]{3}-([0][1-9]|[1][0-2])-([0][0-9]|[1-2][0-9]|[3][0-1])",
        },
    )


@dataclass(kw_only=True)
class TgGrupAdi(CommonMixin):
    """
    Grupo de datos adicionales de uso comercial.

    :ivar dCiclo:
    :ivar dFecIniC:
    :ivar dFecFinC:
    :ivar dVencPag:
    :ivar dContrato: Numero de contrato
    :ivar dSalAnt:
    """

    class Meta:
        name = "tgGrupAdi"

    dCiclo: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "max_length": 15,
            "white_space": "preserve",
            "pattern": r".*[^\s].*",
        },
    )
    dFecIniC: None | XmlDate = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_inclusive": XmlDate(2018, 5, 1),
        },
    )
    dFecFinC: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"[2-9][0-9]{3}-([0][1-9]|[1][0-2])-([0][0-9]|[1-2][0-9]|[3][0-1])",
        },
    )
    dVencPag: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "max_occurs": 3,
            "pattern": r"[2-9][0-9]{3}-([0][1-9]|[1][0-2])-([0][0-9]|[1-2][0-9]|[3][0-1])",
        },
    )
    dContrato: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "max_length": 30,
        },
    )
    dSalAnt: None | Decimal = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("999999999999999.9999"),
            "total_digits": 19,
            "fraction_digits": 4,
        },
    )


@dataclass(kw_only=True)
class TgGrupEner(CommonMixin):
    """
    Grupo del sector de energia electrica.

    :ivar dNroMed: Numero de medidor
    :ivar dActiv: Codigo de actividad
    :ivar dCateg: Codigo de categoría
    :ivar dLecAnt:
    :ivar dLecAct:
    :ivar dConKwh:
    """

    class Meta:
        name = "tgGrupEner"

    dNroMed: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "max_length": 50,
        },
    )
    dActiv: None | int = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "total_digits": 2,
        },
    )
    dCateg: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "max_length": 3,
        },
    )
    dLecAnt: None | Decimal = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("99999999999.99"),
            "total_digits": 13,
            "fraction_digits": 2,
        },
    )
    dLecAct: None | Decimal = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("99999999999.99"),
            "total_digits": 13,
            "fraction_digits": 2,
        },
    )
    dConKwh: None | Decimal = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("99999999999.99"),
            "total_digits": 13,
            "fraction_digits": 2,
        },
    )


@dataclass(kw_only=True)
class TgGrupSeg(CommonMixin):
    """
    Datos del sector de seguros.

    :ivar dCodEmpSeg: Codigo de la empresa de seguros en la
        Superintedencia Nacional de Seguros
    :ivar dPoliza:
    :ivar dUnidVig: Descripción de la unidad de tiempo de vigencia
    :ivar dVigencia:
    :ivar dNumPoliza: Número de la póliza
    """

    class Meta:
        name = "tgGrupSeg"

    dCodEmpSeg: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "max_length": 20,
            "white_space": "collapse",
        },
    )
    dPoliza: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "max_length": 20,
            "white_space": "collapse",
        },
    )
    dUnidVig: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 3,
            "max_length": 15,
            "white_space": "collapse",
        },
    )
    dVigencia: None | Decimal = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("99.9"),
            "total_digits": 3,
            "fraction_digits": 1,
        },
    )
    dNumPoliza: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "max_length": 17,
            "white_space": "collapse",
        },
    )


@dataclass(kw_only=True)
class TgGrupSup(CommonMixin):
    """
    Grupo del sector de supermercados.

    :ivar dNomCaj: Nombre del cajero
    :ivar dEfectivo:
    :ivar dVuelto: Vuelto
    :ivar dDonac: Monto de la donacion
    :ivar dDesDonac: Descripcion de la donacion
    """

    class Meta:
        name = "tgGrupSup"

    dNomCaj: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "max_length": 20,
        },
    )
    dEfectivo: None | Decimal = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("999999999999999.9999"),
            "total_digits": 19,
            "fraction_digits": 4,
        },
    )
    dVuelto: None | Decimal = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("999999.9999"),
            "total_digits": 10,
            "fraction_digits": 4,
        },
    )
    dDonac: None | Decimal = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("999999.9999"),
            "total_digits": 10,
            "fraction_digits": 4,
        },
    )
    dDesDonac: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "max_length": 20,
            "white_space": "collapse",
        },
    )


@dataclass(kw_only=True)
class TgPagCheq(CommonMixin):
    """
    Campos que describen el pago o entrega inicial de la operación con
    cheque.
    """

    class Meta:
        name = "tgPagCheq"

    dNumCheq: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 8,
            "max_length": 8,
            "pattern": r"[0-9]{8}",
        }
    )
    dBcoEmi: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 4,
            "max_length": 20,
            "white_space": "collapse",
        }
    )


class TgPagCredICondCred(Enum):
    VALUE_1 = 1
    VALUE_2 = 2


@dataclass(kw_only=True)
class TgRasMerc(CommonMixin):
    """
    Grupo de rastreo de la mercaderia.

    :ivar dNumLote:
    :ivar dVencMerc:
    :ivar dNSerie: Numero de serie
    """

    class Meta:
        name = "tgRasMerc"

    dNumLote: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "max_length": 80,
            "white_space": "preserve",
            "pattern": r".+",
        },
    )
    dVencMerc: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"[2-9][0-9]{3}-([0][1-9]|[1][0-2])-([0][0-9]|[1-2][0-9]|[3][0-1])",
        },
    )
    dNSerie: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "max_length": 10,
        },
    )


@dataclass(kw_only=True)
class TgTotSub(CommonMixin):
    """
    F.

    Campos que describen los subtotales y totales de la transacción
    documentada.

    :ivar dSubExe:
    :ivar dSubExo:
    :ivar dSub5:
    :ivar dSub10:
    :ivar dSubISC:
    :ivar dTotOpe:
    :ivar dTotDesc:
    :ivar dPorcDescTotal: Porcentaje de descuento sobre total de la
        operacion
    :ivar dDescTotal:
    :ivar dAnticipo:
    :ivar dRedon:
    :ivar dTotGralOpe:
    :ivar dIVA5:
    :ivar dIVA10:
    :ivar dTotIVA:
    :ivar dBaseGrav5:
    :ivar dBaseGrav10:
    :ivar dTBasGraIVA:
    :ivar dLTotISC:
    :ivar dTBasGravISC:
    :ivar dTotalGs:
    :ivar dTotCom:
    :ivar dComi:
    :ivar dIVAComi:
    """

    class Meta:
        name = "tgTotSub"

    dSubExe: None | Decimal = field(
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
    dSubExo: None | Decimal = field(
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
    dSub5: None | Decimal = field(
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
    dSub10: None | Decimal = field(
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
    dSubISC: None | Decimal = field(
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
    dTotOpe: Decimal = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("999999999999999.99999999"),
            "total_digits": 23,
            "fraction_digits": 8,
        }
    )
    dTotDesc: Decimal = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("999999999999999.99999999"),
            "total_digits": 23,
            "fraction_digits": 8,
        }
    )
    dPorcDescTotal: Decimal = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("999.99999999"),
            "total_digits": 11,
            "fraction_digits": 8,
        }
    )
    dDescTotal: Decimal = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("999999999999999.99999999"),
            "total_digits": 23,
            "fraction_digits": 8,
        }
    )
    dAnticipo: Decimal = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("999999999999999.99999999"),
            "total_digits": 23,
            "fraction_digits": 8,
        }
    )
    dRedon: Decimal = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("9999.9999"),
            "total_digits": 8,
            "fraction_digits": 4,
        }
    )
    dTotGralOpe: Decimal = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("999999999999999.99999999"),
            "total_digits": 23,
            "fraction_digits": 8,
        }
    )
    dIVA5: None | Decimal = field(
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
    dIVA10: None | Decimal = field(
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
    dTotIVA: None | Decimal = field(
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
    dBaseGrav5: None | Decimal = field(
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
    dBaseGrav10: None | Decimal = field(
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
    dTBasGraIVA: None | Decimal = field(
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
    dLTotISC: None | Decimal = field(
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
    dTBasGravISC: None | Decimal = field(
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
    dTotalGs: None | Decimal = field(
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
    dTotCom: None | Decimal = field(
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
    dComi: None | Decimal = field(
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
    dIVAComi: None | Decimal = field(
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
class TgValorItem(CommonMixin):
    """
    Campos que describen los precios, descuentos y valor total por item.

    :ivar dPUniProSer:
    :ivar dDescItem:
    :ivar dPorcDesIt: Porcentaje de descuento por item
    :ivar dTotOpeItem:
    :ivar dTiCamIt: Tipo de cambio por ítem
    :ivar dTotOpeGs:
    """

    class Meta:
        name = "tgValorItem"

    dPUniProSer: Decimal = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("999999999999999.99999999"),
            "total_digits": 23,
            "fraction_digits": 8,
        }
    )
    dDescItem: Decimal = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("999999999999999.99999999"),
            "total_digits": 23,
            "fraction_digits": 8,
        }
    )
    dPorcDesIt: None | Decimal = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("999.99999999"),
            "total_digits": 11,
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
    dTiCamIt: None | Decimal = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_inclusive": Decimal("1"),
            "max_inclusive": Decimal("99999.9999"),
            "total_digits": 9,
            "fraction_digits": 4,
        },
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
class TgCopeDe(CommonMixin):
    """
    Campos de la operacion del Documento Electronico.
    """

    class Meta:
        name = "tgCOpeDE"

    iTipEmi: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"[1-2]",
        }
    )
    dDesTipEmi: TdDesTipEmi = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )
    dCodSeg: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_inclusive": "1",
            "pattern": r"[0-9]{9}",
        }
    )
    dInfoEmi: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "max_length": 3000,
            "pattern": r".+",
        },
    )
    dInfoFisc: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "max_length": 3000,
            "pattern": r".+",
        },
    )


@dataclass(kw_only=True)
class TgCamAe(CommonMixin):
    """
    Campos que componen la Autofatura electrónica.

    :ivar iTipCons:
    :ivar dDesTipCons:
    :ivar dNumCons: Numero de constancia
    :ivar dNumControl: Numero de control
    :ivar iTipIDVen:
    :ivar dDTipIDVen:
    :ivar dNumIDVen:
    :ivar dNomVen:
    :ivar dDirVen:
    :ivar dNumCasVen:
    :ivar cDepVen:
    :ivar dDesDepVen:
    :ivar cDisVen:
    :ivar dDesDisVen:
    :ivar cCiuVen:
    :ivar dDesCiuVen:
    :ivar dDirProv:
    :ivar cDepProv:
    :ivar dDesDepProv:
    :ivar cDisProv:
    :ivar dDesDisProv:
    :ivar cCiuProv:
    :ivar dDesCiuProv:
    """

    class Meta:
        name = "tgCamAE"

    iTipCons: TdTipCons = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )
    dDesTipCons: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 30,
            "max_length": 34,
            "white_space": "preserve",
            "pattern": r".*[^\s].*",
        }
    )
    dNumCons: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"[0-9]{11}",
        }
    )
    dNumControl: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"[0-9]{8}",
        }
    )
    iTipIDVen: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "white_space": "collapse",
            "pattern": r"[1-4]",
        }
    )
    dDTipIDVen: TdDtipDoc = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )
    dNumIDVen: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"[0-9A-Za-z\-]{1,20}",
        }
    )
    dNomVen: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 4,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r".*[^\s].*",
        }
    )
    dDirVen: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "max_length": 150,
            "white_space": "preserve",
            "pattern": r".*[^\s].*",
        }
    )
    dNumCasVen: int = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "total_digits": 6,
        }
    )
    cDepVen: TDepartamentos = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )
    dDesDepVen: TDesDepartamento = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )
    cDisVen: None | int = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "total_digits": 4,
        },
    )
    dDesDisVen: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "max_length": 30,
            "white_space": "preserve",
            "pattern": r".*[^\s].*",
        },
    )
    cCiuVen: int = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "total_digits": 5,
        }
    )
    dDesCiuVen: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "max_length": 30,
            "white_space": "preserve",
            "pattern": r".*[^\s].*",
        }
    )
    dDirProv: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "max_length": 150,
            "white_space": "preserve",
            "pattern": r".*[^\s].*",
        }
    )
    cDepProv: TDepartamentos = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )
    dDesDepProv: TDesDepartamento = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )
    cDisProv: int = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "total_digits": 4,
        }
    )
    dDesDisProv: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "max_length": 30,
            "white_space": "preserve",
            "pattern": r".*[^\s].*",
        }
    )
    cCiuProv: int = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "total_digits": 5,
        }
    )
    dDesCiuProv: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "max_length": 30,
            "white_space": "preserve",
            "pattern": r".*[^\s].*",
        }
    )


@dataclass(kw_only=True)
class TgCamDeasoc(CommonMixin):
    """
    Campos que identifican al documento asociado.

    :ivar iTipDocAso:
    :ivar dDesTipDocAso:
    :ivar dCdCDERef:
    :ivar dNTimDI:
    :ivar dEstDocAso:
    :ivar dPExpDocAso: Punto de expedicion
    :ivar dNumDocAso: Numero del documento
    :ivar iTipoDocAso:
    :ivar dDTipoDocAso:
    :ivar dFecEmiDI:
    :ivar dNumComRet: Numero de comprobante de retencion
    :ivar dNumResCF: Numero de resolucion de Credito Fiscal
    """

    class Meta:
        name = "tgCamDEAsoc"

    iTipDocAso: TiTipDocAso = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )
    dDesTipDocAso: TdDesTipDocAso = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )
    dCdCDERef: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "length": 44,
            "pattern": r"[0-9]{2}([0-9]{7}[0-9A-D])[0-9]{34}",
        },
    )
    dNTimDI: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 8,
            "max_length": 8,
            "pattern": r"0+[1-9][0-9]*|[1-9]+[0-9]+",
        },
    )
    dEstDocAso: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 3,
            "pattern": r"[0-9]{3}",
        },
    )
    dPExpDocAso: None | int = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "total_digits": 3,
        },
    )
    dNumDocAso: None | int = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "total_digits": 7,
        },
    )
    iTipoDocAso: None | TiTipoDoc = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )
    dDTipoDocAso: None | TdDesTipoDoc = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )
    dFecEmiDI: None | XmlDate = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_inclusive": XmlDate(2018, 5, 1),
        },
    )
    dNumComRet: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 15,
            "max_length": 15,
            "white_space": "collapse",
        },
    )
    dNumResCF: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 15,
            "max_length": 15,
            "white_space": "collapse",
        },
    )


@dataclass(kw_only=True)
class TgCamEnt(CommonMixin):
    """
    Campos que identifican el local de entrega de las mercaderías.

    :ivar dDirLocEnt:
    :ivar dNumCasEnt: Numero de casa
    :ivar dComp1Ent:
    :ivar dComp2Ent:
    :ivar cDepEnt:
    :ivar dDesDepEnt:
    :ivar cDisEnt:
    :ivar dDesDisEnt:
    :ivar cCiuEnt:
    :ivar dDesCiuEnt:
    :ivar dTelEnt:
    """

    class Meta:
        name = "tgCamEnt"

    dDirLocEnt: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "max_length": 150,
            "white_space": "preserve",
            "pattern": r".*[^\s].*",
        }
    )
    dNumCasEnt: int = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "total_digits": 6,
        }
    )
    dComp1Ent: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "max_length": 150,
            "white_space": "preserve",
            "pattern": r".*[^\s].*",
        },
    )
    dComp2Ent: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "max_length": 15,
            "white_space": "preserve",
            "pattern": r".*[^\s].*",
        },
    )
    cDepEnt: TDepartamentos = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )
    dDesDepEnt: TDesDepartamento = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )
    cDisEnt: None | int = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "total_digits": 4,
        },
    )
    dDesDisEnt: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "max_length": 30,
            "white_space": "preserve",
            "pattern": r".*[^\s].*",
        },
    )
    cCiuEnt: int = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "total_digits": 5,
        }
    )
    dDesCiuEnt: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "max_length": 30,
            "white_space": "preserve",
            "pattern": r".*[^\s].*",
        }
    )
    dTelEnt: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"\d{8,15}",
        },
    )


@dataclass(kw_only=True)
class TgCamFe(CommonMixin):
    """
    Campos que componen la factura electronica.
    """

    class Meta:
        name = "tgCamFE"

    iIndPres: TiIndPres = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )
    dDesIndPres: str | TdDesIndPresValue = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r".+",
        }
    )
    gCompPub: None | TgCompPub = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )


@dataclass(kw_only=True)
class TgCamFee(CommonMixin):
    """
    Campos que componen la factura electronica de exportacion.

    :ivar cFleExp:
    :ivar dDesFleExp:
    :ivar dPuEmb: Puerto de embarque
    """

    class Meta:
        name = "tgCamFEE"

    cFleExp: PaisType = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )
    dDesFleExp: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 4,
            "max_length": 30,
            "white_space": "preserve",
            "pattern": r".*[^\s].*",
        }
    )
    dPuEmb: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 5,
            "max_length": 30,
            "white_space": "preserve",
            "pattern": r".*[^\s].*",
        }
    )


@dataclass(kw_only=True)
class TgCamFei(CommonMixin):
    """
    Campos que componen la factura electronica de importacion FEI.
    """

    class Meta:
        name = "tgCamFEI"

    cTipRegImp: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"[0-9]{4}",
        }
    )
    dPuLleg: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 5,
            "max_length": 50,
            "white_space": "preserve",
            "pattern": r".*[^\s].*",
        }
    )
    dNuDesp: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "max_length": 16,
            "white_space": "preserve",
            "pattern": r".*[^\s].*",
        }
    )
    dFecDesp: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"[2-9][0-9]{3}-([0][1-9]|[1][0-2])-([0][0-9]|[1-2][0-9]|[3][0-1])",
        }
    )
    dNomDesp: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 4,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r".*[^\s].*",
        }
    )
    dRucDesp: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 5,
            "max_length": 8,
            "pattern": r"[1-9][0-9]*[0-9A-D]?",
        }
    )
    dDVDesp: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "white_space": "collapse",
            "pattern": r"[0-9]",
        }
    )
    cPaisProd: PaisType = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )
    dDesPaisProd: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 4,
            "max_length": 30,
            "white_space": "preserve",
            "pattern": r".*[^\s].*",
        }
    )
    dVend: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 4,
            "max_length": 30,
            "white_space": "preserve",
            "pattern": r".*[^\s].*",
        }
    )
    dValorInv: Decimal = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "total_digits": 12,
            "fraction_digits": 4,
        }
    )
    dValorFle: Decimal = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "total_digits": 10,
            "fraction_digits": 4,
        }
    )
    dValorSeg: Decimal = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_exclusive": Decimal("0"),
            "max_inclusive": Decimal("9999999999"),
            "total_digits": 10,
            "fraction_digits": 4,
        }
    )
    dValorImpGs: int = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_exclusive": 0,
            "max_inclusive": 9999999999,
        }
    )
    dDerAdu: Decimal = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_exclusive": Decimal("0"),
            "max_inclusive": Decimal("99999999.9999"),
            "total_digits": 12,
            "fraction_digits": 4,
        }
    )
    dIndi: Decimal = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_exclusive": Decimal("0"),
            "max_inclusive": Decimal("99999999.9999"),
            "total_digits": 12,
            "fraction_digits": 4,
        }
    )
    dSerValor: Decimal = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_exclusive": Decimal("0"),
            "max_inclusive": Decimal("99999999.9999"),
            "total_digits": 12,
            "fraction_digits": 4,
        }
    )
    dIVAImp: Decimal = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_exclusive": Decimal("0"),
            "max_inclusive": Decimal("99999999.9999"),
            "total_digits": 12,
            "fraction_digits": 4,
        }
    )
    dTasaIntAd: int = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_inclusive": 1,
            "max_inclusive": 99,
        }
    )


@dataclass(kw_only=True)
class TgCamIsc(CommonMixin):
    """
    Campos que describen el ISC de la operacion por ítem.
    """

    class Meta:
        name = "tgCamISC"

    cCatISC: TcCatIsc = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )
    dDesCatISC: TdDesCatIsc = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )
    cTasaISC: TcTasaIsc = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )
    dBaseGravISC: Decimal = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("999999999999999.99999999"),
            "total_digits": 23,
            "fraction_digits": 8,
        }
    )
    dLiqISCItem: Decimal = field(
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
class TgCamIva(CommonMixin):
    """
    Campos que describen el IVA de la operación por ítem.
    """

    class Meta:
        name = "tgCamIVA"

    iAfecIVA: TiAfecIva = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )
    dDesAfecIVA: TdDesAfecIva = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )
    dPropIVA: int = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_inclusive": 0,
            "max_inclusive": 100,
            "total_digits": 3,
        }
    )
    dTasaIVA: int = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_inclusive": 0,
            "total_digits": 2,
        }
    )
    dBasGravIVA: Decimal = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("999999999999999.99999999"),
            "total_digits": 23,
            "fraction_digits": 8,
        }
    )
    dLiqIVAItem: Decimal = field(
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
class TgCamNcde(CommonMixin):
    """
    Campos que componen la Nota de credito/Debito Electronica.
    """

    class Meta:
        name = "tgCamNCDE"

    iMotEmi: TiMotEmi = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )
    dDesMotEmi: TdDesMotEmi = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )


@dataclass(kw_only=True)
class TgCamNre(CommonMixin):
    """
    Campos que componen la nora de remision electronica.

    :ivar iMotEmiNR:
    :ivar dDesMotEmiNR:
    :ivar iRespEmiNR:
    :ivar dKmR: Kilometros estimados de recorrido
    """

    class Meta:
        name = "tgCamNRE"

    iMotEmiNR: list[TiMotivTras] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_occurs": 1,
            "max_occurs": 15,
        },
    )
    dDesMotEmiNR: list[str | TdDmotivTrasValue] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_occurs": 1,
            "max_occurs": 15,
        },
    )
    iRespEmiNR: TiRespEmiNr = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )
    dKmR: None | int = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_inclusive": 1,
            "max_inclusive": 5,
        },
    )


@dataclass(kw_only=True)
class TgCamSal(CommonMixin):
    """
    Campos que identifican el local de salida de las mercaderías.

    :ivar dDirLocSal:
    :ivar dNumCasSal: Numero de casa
    :ivar dComp1Sal:
    :ivar dComp2Sal:
    :ivar cDepSal:
    :ivar dDesDepSal:
    :ivar cDisSal:
    :ivar dDesDisSal:
    :ivar cCiuSal:
    :ivar dDesCiuSal:
    :ivar dTelSal:
    """

    class Meta:
        name = "tgCamSal"

    dDirLocSal: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "max_length": 150,
            "white_space": "preserve",
            "pattern": r".*[^\s].*",
        }
    )
    dNumCasSal: int = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "total_digits": 6,
        }
    )
    dComp1Sal: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "max_length": 150,
            "white_space": "preserve",
            "pattern": r".*[^\s].*",
        },
    )
    dComp2Sal: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "max_length": 15,
            "white_space": "preserve",
            "pattern": r".*[^\s].*",
        },
    )
    cDepSal: TDepartamentos = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )
    dDesDepSal: TDesDepartamento = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )
    cDisSal: None | int = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "total_digits": 4,
        },
    )
    dDesDisSal: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "max_length": 30,
            "white_space": "preserve",
            "pattern": r".*[^\s].*",
        },
    )
    cCiuSal: int = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "total_digits": 5,
        }
    )
    dDesCiuSal: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "max_length": 30,
            "white_space": "preserve",
            "pattern": r".*[^\s].*",
        }
    )
    dTelSal: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"\d{8,15}",
        },
    )


@dataclass(kw_only=True)
class TgCamTrans(CommonMixin):
    """
    Campos que identifican al transportista (persona física o jurídica).

    :ivar iNatTrans:
    :ivar dNomTrans: Nombre o razon social del transportista
    :ivar dRucTrans:
    :ivar dDVTrans:
    :ivar iTipIDTrans:
    :ivar dDTipIDTrans:
    :ivar dNumIDTrans:
    :ivar cNacTrans:
    :ivar dDesNacTrans:
    :ivar dNumIDChof:
    :ivar dNomChof:
    """

    class Meta:
        name = "tgCamTrans"

    iNatTrans: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "white_space": "collapse",
            "pattern": r"[1-2]",
        }
    )
    dNomTrans: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 4,
            "max_length": 60,
        }
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
    cNacTrans: None | PaisType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )
    dDesNacTrans: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 4,
            "max_length": 30,
            "white_space": "preserve",
            "pattern": r".*[^\s].*",
        },
    )
    dNumIDChof: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"[0-9A-Za-z\-]{1,20}",
        }
    )
    dNomChof: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 4,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r".*[^\s].*",
        }
    )


@dataclass(kw_only=True)
class TgDtim(CommonMixin):
    """
    Campos de datos del timbrado.
    """

    class Meta:
        name = "tgDTim"

    iTiDE: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"1|[5-6]",
        }
    )
    dDesTiDE: TdDesTiDe = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )
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
    dNumDoc: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 7,
            "max_length": 7,
            "pattern": r"0+[1-9][0-9]*|[1-9]+[0-9]+",
        }
    )
    dFeIniT: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_inclusive": "2018-05-01",
            "pattern": r"[2-9][0-9]{3}-([0][1-9]|[1][0-2])-([0][0-9]|[1-2][0-9]|[3][0-1])",
        }
    )
    dFeFinT: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"[2-9][0-9]{3}-([0][1-9]|[1][0-2])-([0][0-9]|[1-2][0-9]|[3][0-1])",
        }
    )


@dataclass(kw_only=True)
class TgDatRec(CommonMixin):
    """
    Campos que identifican al receptor del Documento Electrónico DE.

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
    :ivar dTelRec:
    :ivar dCelRec:
    :ivar dEmailRec:
    :ivar dCodCliente: Codigo del Cliente
    """

    class Meta:
        name = "tgDatRec"

    iNatRec: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "white_space": "collapse",
            "pattern": r"[1-2]",
        }
    )
    iTiOpe: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "white_space": "collapse",
            "pattern": r"[1-3]",
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
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r".*[^\s].*",
        }
    )
    dNomFanRec: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r".*[^\s].*",
        },
    )
    dDirRec: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "max_length": 150,
            "white_space": "preserve",
            "pattern": r".*[^\s].*",
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
class TgEmis(CommonMixin):
    """
    Campos que identifican al emisor del Documento Electrónico DE.

    :ivar dRucEm:
    :ivar dDVEmi:
    :ivar iTipCont:
    :ivar cTipReg:
    :ivar dNomEmi: Nombre o razon social del emisor del DE
    :ivar dNomFanEmi: Nombre de fantasía
    :ivar dDirEmi:
    :ivar dNumCas: Numero de casa
    :ivar dCompDir1:
    :ivar dCompDir2:
    :ivar cDepEmi:
    :ivar dDesDepEmi:
    :ivar cDisEmi:
    :ivar dDesDisEmi:
    :ivar cCiuEmi:
    :ivar dDesCiuEmi:
    :ivar dTelEmi:
    :ivar dEmailE:
    :ivar dDenSuc: Denominación comercial de la sucursal
    :ivar gActEco:
    """

    class Meta:
        name = "tgEmis"

    dRucEm: str = field(
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
    iTipCont: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "white_space": "collapse",
            "pattern": r"[1-2]",
        }
    )
    cTipReg: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"[1-8]",
        },
    )
    dNomEmi: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 4,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r".*[^\s].*",
        }
    )
    dNomFanEmi: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 4,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r".*[^\s].*",
        },
    )
    dDirEmi: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "max_length": 150,
            "white_space": "preserve",
            "pattern": r".*[^\s].*",
        }
    )
    dNumCas: int = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "total_digits": 6,
        }
    )
    dCompDir1: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "max_length": 150,
            "white_space": "preserve",
            "pattern": r".*[^\s].*",
        },
    )
    dCompDir2: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "max_length": 15,
            "white_space": "preserve",
            "pattern": r".*[^\s].*",
        },
    )
    cDepEmi: TDepartamentos = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )
    dDesDepEmi: TDesDepartamento = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )
    cDisEmi: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_inclusive": "1",
            "pattern": r"[0-9]{1,4}",
        },
    )
    dDesDisEmi: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "max_length": 30,
            "white_space": "preserve",
            "pattern": r".*[^\s].*",
        },
    )
    cCiuEmi: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_inclusive": "1",
            "max_inclusive": "99999",
            "pattern": r"[0-9]{1,5}",
        }
    )
    dDesCiuEmi: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "max_length": 30,
            "white_space": "preserve",
            "pattern": r".*[^\s].*",
        }
    )
    dTelEmi: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"\d{8,15}",
        }
    )
    dEmailE: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"([0-9a-zA-Z#$%]([-.\w]*[0-9a-zA-Z#$%'\.\-_])*@([0-9a-zA-Z][-\w]*[0-9a-zA-Z]\.)+[a-zA-Z]{2,9})",
        }
    )
    dDenSuc: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "max_length": 30,
            "white_space": "preserve",
            "pattern": r".*[^\s].*",
        },
    )
    gActEco: list[TgActEco] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_occurs": 1,
            "max_occurs": 9,
        },
    )


@dataclass(kw_only=True)
class TgOpeCom(CommonMixin):
    """
    Campos inherentes a la operacion comercial.

    :ivar iTipTra:
    :ivar dDesTipTra:
    :ivar iTImp:
    :ivar dDesTImp:
    :ivar cMoneOpe:
    :ivar dDesMoneOpe: Descripcion de la moneda de la operacion
    :ivar dCondTiCam:
    :ivar dTiCam: Tipo de cambio
    """

    class Meta:
        name = "tgOpeCom"

    iTipTra: None | TiTipTra = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )
    dDesTipTra: None | TdDesTiTran = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )
    iTImp: TiTimp = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )
    dDesTImp: TdDesTimp = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )
    cMoneOpe: CMondT = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )
    dDesMoneOpe: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 3,
            "max_length": 20,
            "white_space": "preserve",
            "pattern": r".*[^\s].*",
        }
    )
    dCondTiCam: None | TdCondTiCam = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )
    dTiCam: None | Decimal = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_inclusive": Decimal("1"),
            "max_exclusive": Decimal("99999.9999"),
            "total_digits": 9,
            "fraction_digits": 4,
        },
    )


@dataclass(kw_only=True)
class TgPagCred(CommonMixin):
    """
    Campos que describen la operación a crédito.

    :ivar iCondCred: Condicion de la operacion de credito
    :ivar dDCondCred:
    :ivar dPlazoCre: Plazo del crédito
    :ivar dCuotas: Cantidad de cuotas
    :ivar dMonEnt:
    :ivar gCuotas:
    """

    class Meta:
        name = "tgPagCred"

    iCondCred: TgPagCredICondCred = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "total_digits": 1,
        }
    )
    dDCondCred: TdDcondCred = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )
    dPlazoCre: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 2,
            "max_length": 15,
            "white_space": "collapse",
        },
    )
    dCuotas: None | int = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "total_digits": 3,
        },
    )
    dMonEnt: None | Decimal = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("999999999999999.9999"),
            "total_digits": 19,
            "fraction_digits": 4,
        },
    )
    gCuotas: list[TgCuotas] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "max_occurs": 999,
        },
    )


@dataclass(kw_only=True)
class TgPagTarCd(CommonMixin):
    """
    Campos que describen el pago o entrega inicial de la operación con
    tarjeta de crédito/débito.

    :ivar iDenTarj:
    :ivar dDesDenTarj:
    :ivar dRSProTar: Razón social de la procesadora de tarjeta
    :ivar dRUCProTar:
    :ivar dDVProTar:
    :ivar iForProPa:
    :ivar dCodAuOpe:
    :ivar dNomTit: Nombre del titular de la tarjeta
    :ivar dNumTarj: Numero de la tarjeta
    """

    class Meta:
        name = "tgPagTarCD"

    iDenTarj: TiDenTarj = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )
    dDesDenTarj: str | TdDesDenTarjValue = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r".+",
        }
    )
    dRSProTar: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 4,
            "max_length": 60,
            "white_space": "preserve",
            "pattern": r".*[^\s].*",
        },
    )
    dRUCProTar: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 5,
            "max_length": 8,
            "pattern": r"[1-9][0-9]*[0-9A-D]?",
        },
    )
    dDVProTar: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "white_space": "collapse",
            "pattern": r"[0-9]",
        },
    )
    iForProPa: TiForProPa = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )
    dCodAuOpe: None | int = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "total_digits": 10,
        },
    )
    dNomTit: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 4,
            "max_length": 30,
            "white_space": "preserve",
            "pattern": r".*[^\s].*",
        },
    )
    dNumTarj: None | int = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "total_digits": 4,
        },
    )


@dataclass(kw_only=True)
class TgVehNuevo(CommonMixin):
    """
    Detalle de vehiculos nuevos.

    :ivar iTipOpVN:
    :ivar dDesTipOpVN:
    :ivar dChasis:
    :ivar dColor:
    :ivar dPotencia: Potencia del motor (CV)
    :ivar dCapMot: Capacidad del motor (cc)
    :ivar dPNet: Peso Neto (Toneladas)
    :ivar dPBruto: Peso bruto (Toneladas)
    :ivar iTipCom:
    :ivar dDesTipCom:
    :ivar dNroMotor: Numero de motor
    :ivar dCapTracc: Capacidad maxima de traccion
    :ivar dAnoFab: Anho de fabricacion
    :ivar cTipVeh:
    :ivar dCapac: Capacidad máxima de pasajeros
    """

    class Meta:
        name = "tgVehNuevo"

    iTipOpVN: None | TiTipOpVn = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )
    dDesTipOpVN: None | str | TdDesTipOpVnValue = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )
    dChasis: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"[0-9A-Za-z]{17}",
        },
    )
    dColor: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "max_length": 10,
        },
    )
    dPotencia: None | int = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "total_digits": 4,
        },
    )
    dCapMot: None | int = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "total_digits": 4,
        },
    )
    dPNet: None | Decimal = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("999999.9999"),
            "total_digits": 10,
            "fraction_digits": 4,
        },
    )
    dPBruto: None | Decimal = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("999999.9999"),
            "total_digits": 10,
            "fraction_digits": 4,
        },
    )
    iTipCom: None | TiTipCom = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )
    dDesTipCom: None | str | TdDesTipComValue = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r".+",
        },
    )
    dNroMotor: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "max_length": 21,
        },
    )
    dCapTracc: None | Decimal = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("999999.9999"),
            "total_digits": 10,
            "fraction_digits": 4,
        },
    )
    dAnoFab: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"[0-9]{4}",
        },
    )
    cTipVeh: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 4,
            "max_length": 10,
        },
    )
    dCapac: None | int = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "total_digits": 3,
        },
    )


@dataclass(kw_only=True)
class TgVehTras(CommonMixin):
    """
    Campos que identifican el vehículo de traslado de mercaderías.

    :ivar dTiVehTras:
    :ivar dMarVeh: Marca
    :ivar dNroIDVeh: Número de identificación del vehículo
    :ivar dAdicVeh: Datos adicionales del vehículo
    :ivar dNroVuelo: Tipo de vehiculo
    """

    class Meta:
        name = "tgVehTras"

    dTiVehTras: TdDesModTrans = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )
    dMarVeh: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "max_length": 10,
            "white_space": "preserve",
            "pattern": r".*[^\s].*",
        }
    )
    dNroIDVeh: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "max_length": 20,
            "white_space": "preserve",
            "pattern": r".*[^\s].*",
        }
    )
    dAdicVeh: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "max_length": 20,
        },
    )
    dNroVuelo: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "length": 6,
        },
    )


@dataclass(kw_only=True)
class TgCamEsp(CommonMixin):
    """
    Campos complementarios comerciales de uso especifico.
    """

    class Meta:
        name = "tgCamEsp"

    gVehNuevo: None | TgVehNuevo = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )
    gGrupEner: None | TgGrupEner = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )
    gGrupSeg: None | TgGrupSeg = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )
    gGrupSup: None | TgGrupSup = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )
    gGrupAdi: None | TgGrupAdi = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )


@dataclass(kw_only=True)
class TgCamItem(CommonMixin):
    """
    Campos que describen los items de la operacion.
    """

    class Meta:
        name = "tgCamItem"

    dCodInt: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "max_length": 20,
        }
    )
    dParAranc: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"[0-9]{4}",
        },
    )
    dNCM: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"[0-9]{6,8}",
        },
    )
    dDncpG: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"[0-9]{8}",
        },
    )
    dDncpE: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"[0-9]{3,4}",
        },
    )
    dGtin: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"[0-9]{8,14}",
        },
    )
    dGtinPq: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"[0-9]{8,14}",
        },
    )
    dDesProSer: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "max_length": 120,
        }
    )
    cUniMed: TcUniMed = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )
    dDesUniMed: TdDesUniMed = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )
    dCantProSer: Decimal = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("9999999999.9999"),
            "total_digits": 14,
            "fraction_digits": 4,
        }
    )
    cPaisOrig: None | PaisType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )
    dDesPaisOrig: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 4,
            "max_length": 30,
            "white_space": "preserve",
            "pattern": r".*[^\s].*",
        },
    )
    dInfItem: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "max_length": 500,
        },
    )
    gValorItem: None | TgValorItem = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )
    gCamIVA: None | TgCamIva = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )
    gCamISC: None | TgCamIsc = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )
    gRasMerc: None | TgRasMerc = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )


@dataclass(kw_only=True)
class TgDaGoc(CommonMixin):
    """
    Campos Generales del Documento Electrónico DE.
    """

    class Meta:
        name = "tgDaGOC"

    dFeEmiDE: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d",
        }
    )
    gOpeCom: None | TgOpeCom = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )
    gEmis: TgEmis = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )
    gDatRec: TgDatRec = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )


@dataclass(kw_only=True)
class TgPagCont(CommonMixin):
    """
    Campos que describen la forma de pago al contado.

    :ivar iTiPago:
    :ivar dDesTiPag:
    :ivar dMonTiPag:
    :ivar cMoneTiPag:
    :ivar dDMoneTiPag: Descripcion de la moneda por tipo de pago
    :ivar dTiCamTiPag: Tipo de cambio
    :ivar gPagTarCD:
    :ivar gPagCheq:
    """

    class Meta:
        name = "tgPagCont"

    iTiPago: TiTiPago = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )
    dDesTiPag: TdDesTiPag = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )
    dMonTiPag: Decimal = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("999999999999999.9999"),
            "total_digits": 19,
            "fraction_digits": 4,
        }
    )
    cMoneTiPag: CMondT = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )
    dDMoneTiPag: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 3,
            "max_length": 20,
            "white_space": "collapse",
        }
    )
    dTiCamTiPag: None | Decimal = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_inclusive": Decimal("0"),
            "max_inclusive": Decimal("99999.9999"),
            "total_digits": 9,
            "fraction_digits": 4,
        },
    )
    gPagTarCD: None | TgPagTarCd = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )
    gPagCheq: None | TgPagCheq = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )


@dataclass(kw_only=True)
class TgTransp(CommonMixin):
    """
    Campos que describen el transporte de mercaderias.

    :ivar iTipTrans:
    :ivar dDesTipTrans:
    :ivar iModTrans:
    :ivar dDesModTrans:
    :ivar iRespFlete:
    :ivar cCondNeg:
    :ivar dNuManif: Número de manifiesto o conocimiento de carga/
        declaración de tránsito aduanero/ Carta de porte internacional
    :ivar dNuDespImp: Numero de despacho de importación
    :ivar dIniTras:
    :ivar dFinTras:
    :ivar cPaisDest:
    :ivar dDesPaisDest:
    :ivar gCamSal:
    :ivar gCamEnt:
    :ivar gVehTras:
    :ivar gCamTrans:
    """

    class Meta:
        name = "tgTransp"

    iTipTrans: None | TiTtrans = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )
    dDesTipTrans: None | TdDesTtrans = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )
    iModTrans: TiModTrans = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )
    dDesModTrans: TdDesModTrans = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )
    iRespFlete: None | TiRespFlete = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )
    cCondNeg: None | TcCondNeg = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )
    dNuManif: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 1,
            "max_length": 15,
        },
    )
    dNuDespImp: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 16,
            "max_length": 16,
        },
    )
    dIniTras: None | XmlDate = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_inclusive": XmlDate(2018, 5, 1),
        },
    )
    dFinTras: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"[2-9][0-9]{3}-([0][1-9]|[1][0-2])-([0][0-9]|[1-2][0-9]|[3][0-1])",
        },
    )
    cPaisDest: None | PaisType = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )
    dDesPaisDest: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_length": 4,
            "max_length": 30,
            "white_space": "preserve",
            "pattern": r".*[^\s].*",
        },
    )
    gCamSal: None | TgCamSal = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )
    gCamEnt: list[TgCamEnt] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "max_occurs": 99,
        },
    )
    gVehTras: list[TgVehTras] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "max_occurs": 4,
        },
    )
    gCamTrans: None | TgCamTrans = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )


@dataclass(kw_only=True)
class TgCamCond(CommonMixin):
    """
    Campos que describen la condición de la operación.
    """

    class Meta:
        name = "tgCamCond"

    iCondOpe: TiCondOpe = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )
    dDCondOpe: TdDcondOpe = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )
    gPaConEIni: list[TgPagCont] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "max_occurs": 99,
        },
    )
    gPagCred: None | TgPagCred = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )


@dataclass(kw_only=True)
class TgDtipDe(CommonMixin):
    """
    Campos específicos por tipo de documento electronico.
    """

    class Meta:
        name = "tgDtipDE"

    gCamFE: None | TgCamFe = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )
    gCamFEE: None | TgCamFee = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )
    gCamFEI: None | TgCamFei = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )
    gCamAE: None | TgCamAe = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )
    gCamNCDE: None | TgCamNcde = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )
    gCamNRE: None | TgCamNre = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )
    gCamCond: None | TgCamCond = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )
    gCamItem: list[TgCamItem] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )
    gCamEsp: None | TgCamEsp = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )
    gTransp: None | TgTransp = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )


@dataclass(kw_only=True)
class TDe(CommonMixin):
    """
    Campos firmados del DE.
    """

    class Meta:
        name = "tDE"

    dDVId: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "white_space": "collapse",
            "pattern": r"[0-9]",
        }
    )
    dFecFirma: str = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "pattern": r"\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d",
        }
    )
    gOpeDE: TgCopeDe = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )
    gTimb: TgDtim = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )
    gDatGralOpe: TgDaGoc = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )
    gDtipDE: TgDtipDe = field(
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        }
    )
    gTotSub: None | TgTotSub = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )
    gCamGen: None | TgCamGen = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
        },
    )
    gCamDEAsoc: list[TgCamDeasoc] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "http://ekuatia.set.gov.py/sifen/xsd",
            "max_occurs": 99,
        },
    )
    Id: str = field(
        metadata={
            "type": "Attribute",
            "length": 44,
            "pattern": r"[0-9]{2}([0-9]{7}[0-9A-D])[0-9]{34}",
        }
    )


@dataclass(kw_only=True)
class RDe(CommonMixin):
    """
    :ivar dVerFor:
    :ivar DE:
    :ivar Signature: Firma Digital del DE
    :ivar gCamFuFD:
    """

    class Meta:
        name = "rDE"
        namespace = "http://ekuatia.set.gov.py/sifen/xsd"

    dVerFor: str = field(
        metadata={
            "type": "Element",
            "pattern": r"[1][4][1]",
        }
    )
    DE: TDe = field(
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
    gCamFuFD: TgCamFuFd = field(
        metadata={
            "type": "Element",
        }
    )
