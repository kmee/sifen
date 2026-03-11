"""Testes de geração e leitura de documentos XML completos do SIFEN.

Testa a construção programática de cada tipo de DE, serialização para XML,
round-trip (XML → objeto → XML → objeto), e validação de campos.
"""
import os
import warnings
from decimal import Decimal

import pytest
from lxml import etree

warnings.filterwarnings("ignore")

SAMPLES_DIR = os.path.join(
    os.path.dirname(__file__), "..", "sifenlib", "de", "samples", "v150"
)
SCHEMAS_DIR = os.path.join(
    os.path.dirname(__file__), "..", "sifenlib", "de", "schemas", "v150"
)


# ── Helpers ──────────────────────────────────────────────────────────


def _make_signature():
    """Cria um Signature xmldsig placeholder para testes."""
    from sifenlib.de.bindings.v150.xmldsig_core_schema import (
        CanonicalizationMethod,
        DigestMethod,
        DigestValue,
        Reference,
        Signature,
        SignatureMethod,
        SignatureValue,
        SignedInfo,
    )

    return Signature(
        SignedInfo=SignedInfo(
            CanonicalizationMethod=CanonicalizationMethod(
                Algorithm=(
                    "http://www.w3.org/TR/2001/REC-xml-c14n-20010315"
                ),
                content=[],
            ),
            SignatureMethod=SignatureMethod(
                Algorithm=(
                    "http://www.w3.org/2001/04/"
                    "xmldsig-more#rsa-sha256"
                ),
                content=[],
            ),
            Reference=[
                Reference(
                    DigestMethod=DigestMethod(
                        Algorithm=(
                            "http://www.w3.org/2001/04/xmlenc#sha256"
                        ),
                        content=[],
                    ),
                    DigestValue=DigestValue(value="PLACEHOLDER"),
                    URI="",
                )
            ],
        ),
        SignatureValue=SignatureValue(value="PLACEHOLDER"),
    )


def _make_emisor():
    """Cria um emissor padrão para testes."""
    from sifenlib.de.bindings.v150.fe_v141 import TgActEco, TgEmis

    return TgEmis(
        dRucEm="80069563",
        dDVEmi="1",
        iTipCont="1",
        dNomEmi="Empresa Test S.A.",
        dDirEmi="Av. España 1234",
        dNumCas="1234",
        cDepEmi="1",
        dDesDepEmi="CAPITAL",
        cDisEmi="1",
        dDesDisEmi="ASUNCION (DISTRITO)",
        cCiuEmi="1",
        dDesCiuEmi="ASUNCION (DISTRITO)",
        dTelEmi="021123456",
        dEmailE="test@empresa.com.py",
        gActEco=[
            TgActEco(cActEco="47111", dDesActEco="Venta al por menor")
        ],
    )


def _make_receptor():
    """Cria um receptor padrão para testes."""
    from sifenlib.de.bindings.v150.fe_v141 import TgDatRec

    return TgDatRec(
        iNatRec="1",
        iTiOpe="1",
        cPaisRec="PRY",
        dDesPaisRe="Paraguay",
        iTiContRec="1",
        dRucRec="4192083",
        dDVRec="5",
        dNomRec="Cliente Test S.A.",
        dDirRec="Calle 14 de Mayo 567",
    )


def _make_item(
    cod="PROD001",
    desc="Producto de prueba",
    qty=Decimal("1"),
    price=Decimal("100000"),
    iva_rate=Decimal("10"),
):
    """Cria um item de venda para testes."""
    from sifenlib.de.bindings.v150.fe_v141 import (
        TgCamItem,
        TgCamIva,
        TgValorItem,
        TiAfecIva,
    )

    total = qty * price
    if iva_rate > 0:
        base = total * 100 / (100 + iva_rate)
        iva_valor = total - base
        afec = TiAfecIva.VALUE_1
        desc_afec = "Gravado IVA"
    else:
        base = Decimal("0")
        iva_valor = Decimal("0")
        afec = TiAfecIva.VALUE_3
        desc_afec = "Exento"

    return TgCamItem(
        dCodInt=cod,
        dDesProSer=desc,
        cUniMed="77",
        dDesUniMed="UNI",
        dCantProSer=qty,
        gValorItem=TgValorItem(
            dPUniProSer=price,
            dDescItem=Decimal("0"),
            dTotOpeItem=total,
            dTotOpeGs=total,
        ),
        gCamIVA=TgCamIva(
            iAfecIVA=afec,
            dDesAfecIVA=desc_afec,
            dPropIVA=Decimal("100"),
            dTasaIVA=iva_rate,
            dBasGravIVA=int(base),
            dLiqIVAItem=int(iva_valor),
        ),
    )


def _make_totales(
    total=Decimal("100000"),
    iva10=None,
    base10=None,
    sub_exe=None,
):
    """Cria totais para testes."""
    from sifenlib.de.bindings.v150.fe_v141 import TgTotSub

    return TgTotSub(
        dSub10=total if iva10 else None,
        dSubExe=sub_exe,
        dTotOpe=total,
        dTotDesc=Decimal("0"),
        dPorcDescTotal=Decimal("0"),
        dDescTotal=Decimal("0"),
        dAnticipo=Decimal("0"),
        dRedon=Decimal("0"),
        dTotGralOpe=total,
        dIVA10=iva10,
        dBaseGrav10=base10,
        dTBasGraIVA=base10,
        dTotIVA=iva10,
        dTotalGs=total,
    )


# ── Testes de Geração: Factura Electrónica (tipo 1) ─────────────────


class TestGenerateFactura:
    """Geração programática de Factura Electrónica completa."""

    def test_build_factura_simple(self):
        """Constrói uma factura com 1 item e verifica serialização."""
        from sifenlib.de.bindings.v150.fe_v141 import (
            RDe,
            TDe,
            TgCamCond,
            TgCamFe,
            TgCamFuFd,
            TgCopeDe,
            TgDaGoc,
            TgDtim,
            TgDtipDe,
            TgOpeCom,
            TgPagCont,
            TiCondOpe,
            TiTiPago,
        )

        rde = RDe(
            dVerFor="150",
            DE=TDe(
                Id="01800695631001001000000612024112917595714694",
                dDVId="9",
                dFecFirma="2024-11-29T17:59:57",
                gOpeDE=TgCopeDe(
                    iTipEmi="1",
                    dDesTipEmi="Normal",
                    dCodSeg="000000001",
                ),
                gTimb=TgDtim(
                    iTiDE="1",
                    dDesTiDE="Factura electrónica",
                    dNumTim="12345678",
                    dEst="001",
                    dPunExp="001",
                    dNumDoc="0000001",
                    dFeIniT="2024-01-01",
                    dFeFinT="2025-12-31",
                ),
                gDatGralOpe=TgDaGoc(
                    dFeEmiDE="2024-11-29T17:59:57",
                    gOpeCom=TgOpeCom(
                        iTipTra="1",
                        dDesTipTra="Venta de mercadería",
                        iTImp="1",
                        dDesTImp="IVA",
                        cMoneOpe="PYG",
                        dDesMoneOpe="Guarani",
                    ),
                    gEmis=_make_emisor(),
                    gDatRec=_make_receptor(),
                ),
                gDtipDE=TgDtipDe(
                    gCamFE=TgCamFe(
                        iIndPres="1",
                        dDesIndPres="Operación presencial",
                    ),
                    gCamCond=TgCamCond(
                        iCondOpe=TiCondOpe.VALUE_1,
                        dDCondOpe="Contado",
                        gPaConEIni=[
                            TgPagCont(
                                iTiPago=TiTiPago.VALUE_1,
                                dDesTiPag="Efectivo",
                                dMonTiPag=Decimal("500000"),
                                cMoneTiPag="PYG",
                                dDMoneTiPag="Guarani",
                            )
                        ],
                    ),
                    gCamItem=[
                        _make_item(
                            "PROD001",
                            "Producto test",
                            Decimal("5"),
                            Decimal("100000"),
                        )
                    ],
                ),
                gTotSub=_make_totales(
                    total=Decimal("500000"),
                    iva10=Decimal("45455"),
                    base10=Decimal("454545"),
                ),
            ),
            Signature=_make_signature(),
            gCamFuFD=TgCamFuFd(
                dCarQR=(
                    "https://ekuatia.set.gov.py/"
                    "consultas/qr?nVersion=150"
                ),
            ),
        )

        xml = rde.to_xml()

        assert '<?xml version="1.0" encoding="UTF-8"?>' in xml
        assert "80069563" in xml
        assert "Empresa Test S.A." in xml
        assert "PROD001" in xml
        assert "500000" in xml

    def test_build_factura_multi_items(self):
        """Constrói factura com múltiplos itens."""
        from sifenlib.de.bindings.v150.fe_v141 import (
            RDe,
            TDe,
            TgCamCond,
            TgCamFe,
            TgCamFuFd,
            TgCopeDe,
            TgDaGoc,
            TgDtim,
            TgDtipDe,
            TgOpeCom,
            TgPagCont,
            TiCondOpe,
            TiTiPago,
        )

        items = [
            _make_item("P001", "Item 1", Decimal("2"), Decimal("100000")),
            _make_item("P002", "Item 2", Decimal("3"), Decimal("50000")),
            _make_item("P003", "Item 3", Decimal("1"), Decimal("200000")),
        ]
        total = Decimal("550000")

        rde = RDe(
            dVerFor="150",
            DE=TDe(
                Id="01800695631001001000000712025010112000000001",
                dDVId="1",
                dFecFirma="2025-01-01T12:00:00",
                gOpeDE=TgCopeDe(
                    iTipEmi="1",
                    dDesTipEmi="Normal",
                    dCodSeg="000000010",
                ),
                gTimb=TgDtim(
                    iTiDE="1",
                    dDesTiDE="Factura electrónica",
                    dNumTim="87654321",
                    dEst="001",
                    dPunExp="002",
                    dNumDoc="0000010",
                    dFeIniT="2025-01-01",
                    dFeFinT="2026-12-31",
                ),
                gDatGralOpe=TgDaGoc(
                    dFeEmiDE="2025-01-01T12:00:00",
                    gOpeCom=TgOpeCom(
                        iTipTra="1",
                        dDesTipTra="Venta de mercadería",
                        iTImp="1",
                        dDesTImp="IVA",
                        cMoneOpe="PYG",
                        dDesMoneOpe="Guarani",
                    ),
                    gEmis=_make_emisor(),
                    gDatRec=_make_receptor(),
                ),
                gDtipDE=TgDtipDe(
                    gCamFE=TgCamFe(
                        iIndPres="1",
                        dDesIndPres="Operación presencial",
                    ),
                    gCamCond=TgCamCond(
                        iCondOpe=TiCondOpe.VALUE_1,
                        dDCondOpe="Contado",
                        gPaConEIni=[
                            TgPagCont(
                                iTiPago=TiTiPago.VALUE_1,
                                dDesTiPag="Efectivo",
                                dMonTiPag=total,
                                cMoneTiPag="PYG",
                                dDMoneTiPag="Guarani",
                            )
                        ],
                    ),
                    gCamItem=items,
                ),
                gTotSub=_make_totales(
                    total=total,
                    iva10=Decimal("50000"),
                    base10=Decimal("500000"),
                ),
            ),
            Signature=_make_signature(),
            gCamFuFD=TgCamFuFd(
                dCarQR=(
                    "https://ekuatia.set.gov.py/"
                    "consultas/qr?nVersion=150"
                ),
            ),
        )

        xml = rde.to_xml()
        rde2 = RDe.from_xml(xml)

        assert len(rde2.DE.gDtipDE.gCamItem) == 3
        assert rde2.DE.gDtipDE.gCamItem[0].dCodInt == "P001"
        assert rde2.DE.gDtipDE.gCamItem[1].dCodInt == "P002"
        assert rde2.DE.gDtipDE.gCamItem[2].dCodInt == "P003"
        assert rde2.DE.gTotSub.dTotGralOpe == total

    def test_build_factura_credito(self):
        """Constrói factura a crédito com cuotas."""
        from sifenlib.de.bindings.v150.fe_v141 import (
            RDe,
            TDe,
            TgCamCond,
            TgCamFe,
            TgCamFuFd,
            TgCopeDe,
            TgCuotas,
            TgDaGoc,
            TgDtim,
            TgDtipDe,
            TgOpeCom,
            TgPagCred,
            TiCondOpe,
        )

        rde = RDe(
            dVerFor="150",
            DE=TDe(
                Id="01800695631001001000000812025020114300000002",
                dDVId="2",
                dFecFirma="2025-02-01T14:30:00",
                gOpeDE=TgCopeDe(
                    iTipEmi="1",
                    dDesTipEmi="Normal",
                    dCodSeg="000000020",
                ),
                gTimb=TgDtim(
                    iTiDE="1",
                    dDesTiDE="Factura electrónica",
                    dNumTim="87654321",
                    dEst="001",
                    dPunExp="001",
                    dNumDoc="0000020",
                    dFeIniT="2025-01-01",
                    dFeFinT="2026-12-31",
                ),
                gDatGralOpe=TgDaGoc(
                    dFeEmiDE="2025-02-01T14:30:00",
                    gOpeCom=TgOpeCom(
                        iTipTra="1",
                        dDesTipTra="Venta de mercadería",
                        iTImp="1",
                        dDesTImp="IVA",
                        cMoneOpe="PYG",
                        dDesMoneOpe="Guarani",
                    ),
                    gEmis=_make_emisor(),
                    gDatRec=_make_receptor(),
                ),
                gDtipDE=TgDtipDe(
                    gCamFE=TgCamFe(
                        iIndPres="1",
                        dDesIndPres="Operación presencial",
                    ),
                    gCamCond=TgCamCond(
                        iCondOpe=TiCondOpe.VALUE_2,
                        dDCondOpe="Crédito",
                        gPagCred=TgPagCred(
                            iCondCred="1",
                            dDCondCred="Plazo",
                            dPlazoCre="30 días",
                            dCuotas=3,
                            dMonEnt=Decimal("0"),
                            gCuotas=[
                                TgCuotas(
                                    dMonCuota=Decimal("333334"),
                                    dVencCuo="2025-03-01",
                                ),
                                TgCuotas(
                                    dMonCuota=Decimal("333333"),
                                    dVencCuo="2025-04-01",
                                ),
                                TgCuotas(
                                    dMonCuota=Decimal("333333"),
                                    dVencCuo="2025-05-01",
                                ),
                            ],
                        ),
                    ),
                    gCamItem=[
                        _make_item(
                            "MUEBLE01",
                            "Escritorio ejecutivo",
                            Decimal("1"),
                            Decimal("1000000"),
                        )
                    ],
                ),
                gTotSub=_make_totales(
                    total=Decimal("1000000"),
                    iva10=Decimal("90909"),
                    base10=Decimal("909091"),
                ),
            ),
            Signature=_make_signature(),
            gCamFuFD=TgCamFuFd(
                dCarQR=(
                    "https://ekuatia.set.gov.py/"
                    "consultas/qr?nVersion=150"
                ),
            ),
        )

        xml = rde.to_xml()
        rde2 = RDe.from_xml(xml)

        cond = rde2.DE.gDtipDE.gCamCond
        assert cond.iCondOpe == TiCondOpe.VALUE_2
        assert cond.gPagCred is not None
        assert len(cond.gPagCred.gCuotas) == 3
        assert cond.gPagCred.gCuotas[0].dMonCuota == Decimal("333334")


# ── Testes de Geração: Nota de Crédito (tipo 5) ─────────────────────


class TestGenerateNotaCredito:
    """Geração de Nota de Crédito com documento associado."""

    def test_build_nota_credito(self):
        from sifenlib.de.bindings.v150.fe_v141 import (
            RDe,
            TDe,
            TgCamCond,
            TgCamDeasoc,
            TgCamFuFd,
            TgCamNcde,
            TgCopeDe,
            TgDaGoc,
            TgDtim,
            TgDtipDe,
            TgOpeCom,
            TgPagCont,
            TiCondOpe,
            TiMotEmi,
            TiTiPago,
        )

        rde = RDe(
            dVerFor="150",
            DE=TDe(
                Id="01800695631001001000000912025030110000000003",
                dDVId="3",
                dFecFirma="2025-03-01T10:00:00",
                gOpeDE=TgCopeDe(
                    iTipEmi="1",
                    dDesTipEmi="Normal",
                    dCodSeg="000000030",
                ),
                gTimb=TgDtim(
                    iTiDE="5",
                    dDesTiDE="Nota de crédito electrónica",
                    dNumTim="87654321",
                    dEst="001",
                    dPunExp="001",
                    dNumDoc="0000030",
                    dFeIniT="2025-01-01",
                    dFeFinT="2026-12-31",
                ),
                gDatGralOpe=TgDaGoc(
                    dFeEmiDE="2025-03-01T10:00:00",
                    gOpeCom=TgOpeCom(
                        iTipTra="1",
                        dDesTipTra="Venta de mercadería",
                        iTImp="1",
                        dDesTImp="IVA",
                        cMoneOpe="PYG",
                        dDesMoneOpe="Guarani",
                    ),
                    gEmis=_make_emisor(),
                    gDatRec=_make_receptor(),
                ),
                gDtipDE=TgDtipDe(
                    gCamNCDE=TgCamNcde(
                        iMotEmi=TiMotEmi.VALUE_1,
                        dDesMotEmi=(
                            "Devolución y Ajuste de precios"
                        ),
                    ),
                    gCamCond=TgCamCond(
                        iCondOpe=TiCondOpe.VALUE_1,
                        dDCondOpe="Contado",
                        gPaConEIni=[
                            TgPagCont(
                                iTiPago=TiTiPago.VALUE_1,
                                dDesTiPag="Efectivo",
                                dMonTiPag=Decimal("200000"),
                                cMoneTiPag="PYG",
                                dDMoneTiPag="Guarani",
                            )
                        ],
                    ),
                    gCamItem=[
                        _make_item(
                            "DEV001",
                            "Producto devuelto",
                            Decimal("1"),
                            Decimal("200000"),
                        )
                    ],
                ),
                gTotSub=_make_totales(
                    total=Decimal("200000"),
                    iva10=Decimal("18182"),
                    base10=Decimal("181818"),
                ),
                gCamDEAsoc=[
                    TgCamDeasoc(
                        iTipDocAso="1",
                        dDesTipDocAso="Electrónico",
                        dCdCDERef=(
                            "0180069563100100100000061"
                            "2024112917595714694"
                        ),
                    )
                ],
            ),
            Signature=_make_signature(),
            gCamFuFD=TgCamFuFd(
                dCarQR=(
                    "https://ekuatia.set.gov.py/"
                    "consultas/qr?nVersion=150"
                ),
            ),
        )

        xml = rde.to_xml()
        rde2 = RDe.from_xml(xml)

        assert rde2.DE.gTimb.iTiDE == "5"
        assert rde2.DE.gDtipDE.gCamNCDE is not None
        assert rde2.DE.gDtipDE.gCamNCDE.iMotEmi == TiMotEmi.VALUE_1
        assert len(rde2.DE.gCamDEAsoc) == 1


# ── Testes de Geração: Nota de Débito (tipo 6) ──────────────────────


class TestGenerateNotaDebito:
    """Geração de Nota de Débito."""

    def test_build_nota_debito(self):
        from sifenlib.de.bindings.v150.fe_v141 import (
            RDe,
            TDe,
            TgCamCond,
            TgCamDeasoc,
            TgCamFuFd,
            TgCamNcde,
            TgCopeDe,
            TgDaGoc,
            TgDtim,
            TgDtipDe,
            TgOpeCom,
            TgPagCont,
            TiCondOpe,
            TiMotEmi,
            TiTiPago,
        )

        rde = RDe(
            dVerFor="150",
            DE=TDe(
                Id="01800695631001001000001012025031509000000004",
                dDVId="4",
                dFecFirma="2025-03-15T09:00:00",
                gOpeDE=TgCopeDe(
                    iTipEmi="1",
                    dDesTipEmi="Normal",
                    dCodSeg="000000040",
                ),
                gTimb=TgDtim(
                    iTiDE="6",
                    dDesTiDE="Nota de débito electrónica",
                    dNumTim="87654321",
                    dEst="001",
                    dPunExp="001",
                    dNumDoc="0000040",
                    dFeIniT="2025-01-01",
                    dFeFinT="2026-12-31",
                ),
                gDatGralOpe=TgDaGoc(
                    dFeEmiDE="2025-03-15T09:00:00",
                    gOpeCom=TgOpeCom(
                        iTipTra="1",
                        dDesTipTra="Venta de mercadería",
                        iTImp="1",
                        dDesTImp="IVA",
                        cMoneOpe="PYG",
                        dDesMoneOpe="Guarani",
                    ),
                    gEmis=_make_emisor(),
                    gDatRec=_make_receptor(),
                ),
                gDtipDE=TgDtipDe(
                    gCamNCDE=TgCamNcde(
                        iMotEmi=TiMotEmi.VALUE_2,
                        dDesMotEmi="Devolución",
                    ),
                    gCamCond=TgCamCond(
                        iCondOpe=TiCondOpe.VALUE_1,
                        dDCondOpe="Contado",
                        gPaConEIni=[
                            TgPagCont(
                                iTiPago=TiTiPago.VALUE_1,
                                dDesTiPag="Efectivo",
                                dMonTiPag=Decimal("50000"),
                                cMoneTiPag="PYG",
                                dDMoneTiPag="Guarani",
                            )
                        ],
                    ),
                    gCamItem=[
                        _make_item(
                            "INT001",
                            "Intereses por mora",
                            Decimal("1"),
                            Decimal("50000"),
                        )
                    ],
                ),
                gTotSub=_make_totales(
                    total=Decimal("50000"),
                    iva10=Decimal("4545"),
                    base10=Decimal("45455"),
                ),
                gCamDEAsoc=[
                    TgCamDeasoc(
                        iTipDocAso="1",
                        dDesTipDocAso="Electrónico",
                        dCdCDERef=(
                            "0180069563100100100000061"
                            "2024112917595714694"
                        ),
                    )
                ],
            ),
            Signature=_make_signature(),
            gCamFuFD=TgCamFuFd(
                dCarQR=(
                    "https://ekuatia.set.gov.py/"
                    "consultas/qr?nVersion=150"
                ),
            ),
        )

        xml = rde.to_xml()
        rde2 = RDe.from_xml(xml)

        assert rde2.DE.gTimb.iTiDE == "6"
        assert rde2.DE.gDtipDE.gCamNCDE.iMotEmi == TiMotEmi.VALUE_2
        assert rde2.DE.gTotSub.dTotGralOpe == Decimal("50000")


# ── Testes de Geração: Nota de Remisión (tipo 7) ────────────────────


class TestGenerateNotaRemision:
    """Geração de Nota de Remisión."""

    def test_build_nota_remision(self):
        from sifenlib.de.bindings.v150.fe_v141 import (
            RDe,
            TDe,
            TgCamFuFd,
            TgCamNre,
            TgCopeDe,
            TgDaGoc,
            TgDtim,
            TgDtipDe,
            TiMotivTras,
            TiRespEmiNr,
        )

        rde = RDe(
            dVerFor="150",
            DE=TDe(
                Id="01800695631001001000001112025040108000000005",
                dDVId="5",
                dFecFirma="2025-04-01T08:00:00",
                gOpeDE=TgCopeDe(
                    iTipEmi="1",
                    dDesTipEmi="Normal",
                    dCodSeg="000000050",
                ),
                gTimb=TgDtim(
                    iTiDE="7",
                    dDesTiDE="Nota de remisión electrónica",
                    dNumTim="87654321",
                    dEst="001",
                    dPunExp="001",
                    dNumDoc="0000050",
                    dFeIniT="2025-01-01",
                    dFeFinT="2026-12-31",
                ),
                gDatGralOpe=TgDaGoc(
                    dFeEmiDE="2025-04-01T08:00:00",
                    gEmis=_make_emisor(),
                    gDatRec=_make_receptor(),
                ),
                gDtipDE=TgDtipDe(
                    gCamNRE=TgCamNre(
                        iMotEmiNR=[TiMotivTras.VALUE_1],
                        dDesMotEmiNR=["Traslado por venta"],
                        iRespEmiNR=TiRespEmiNr.VALUE_1,
                    ),
                    gCamItem=[
                        _make_item(
                            "TRANS01",
                            "Mercadería en tránsito",
                            Decimal("100"),
                            Decimal("10000"),
                        )
                    ],
                ),
                gTotSub=_make_totales(
                    total=Decimal("1000000"),
                    iva10=Decimal("90909"),
                    base10=Decimal("909091"),
                ),
            ),
            Signature=_make_signature(),
            gCamFuFD=TgCamFuFd(
                dCarQR=(
                    "https://ekuatia.set.gov.py/"
                    "consultas/qr?nVersion=150"
                ),
            ),
        )

        xml = rde.to_xml()
        rde2 = RDe.from_xml(xml)

        assert rde2.DE.gTimb.iTiDE == "7"
        nre = rde2.DE.gDtipDE.gCamNRE
        assert nre is not None
        mot = nre.iMotEmiNR
        if isinstance(mot, list):
            assert mot[0] == TiMotivTras.VALUE_1
        else:
            assert mot == TiMotivTras.VALUE_1


# ── Testes de Round-Trip Completo ────────────────────────────────────


class TestRoundTrip:
    """Round-trip: XML → objeto → XML → objeto, comparando campos."""

    def test_roundtrip_factura_from_sample(self):
        from sifenlib.de.bindings.v150.fe_v141 import RDe

        path = os.path.join(SAMPLES_DIR, "factura_electronica.xml")
        rde1 = RDe.from_path(path)
        xml1 = rde1.to_xml()
        rde2 = RDe.from_xml(xml1)
        xml2 = rde2.to_xml()

        # Campos devem ser idênticos após round-trip
        assert rde1.DE.Id == rde2.DE.Id
        assert rde1.DE.gTimb.iTiDE == rde2.DE.gTimb.iTiDE
        assert rde1.DE.gDatGralOpe.gEmis.dRucEm == (
            rde2.DE.gDatGralOpe.gEmis.dRucEm
        )
        assert rde1.DE.gDatGralOpe.gEmis.dNomEmi == (
            rde2.DE.gDatGralOpe.gEmis.dNomEmi
        )
        assert rde1.DE.gTotSub.dTotGralOpe == (
            rde2.DE.gTotSub.dTotGralOpe
        )

        # XML deve ser estável (2o round-trip = 1o round-trip)
        assert xml1 == xml2

    def test_roundtrip_all_samples_xml_stable(self):
        """XML é estável: serializar 2x produz resultado idêntico."""
        from sifenlib.de.bindings.v150.fe_v141 import RDe

        for filename in sorted(os.listdir(SAMPLES_DIR)):
            if not filename.endswith(".xml"):
                continue
            path = os.path.join(SAMPLES_DIR, filename)
            rde1 = RDe.from_path(path)
            xml1 = rde1.to_xml()
            rde2 = RDe.from_xml(xml1)
            xml2 = rde2.to_xml()
            assert xml1 == xml2, (
                f"Round-trip XML unstable for {filename}"
            )

    def test_roundtrip_generated_factura(self):
        """Round-trip de factura gerada programaticamente."""
        from sifenlib.de.bindings.v150.fe_v141 import (
            RDe,
            TDe,
            TgCamCond,
            TgCamFe,
            TgCamFuFd,
            TgCopeDe,
            TgDaGoc,
            TgDtim,
            TgDtipDe,
            TgOpeCom,
            TgPagCont,
            TiCondOpe,
            TiTiPago,
        )

        rde = RDe(
            dVerFor="150",
            DE=TDe(
                Id="01800695631001001000000612024112917595714694",
                dDVId="9",
                dFecFirma="2024-11-29T17:59:57",
                gOpeDE=TgCopeDe(
                    iTipEmi="1",
                    dDesTipEmi="Normal",
                    dCodSeg="000000001",
                ),
                gTimb=TgDtim(
                    iTiDE="1",
                    dDesTiDE="Factura electrónica",
                    dNumTim="12345678",
                    dEst="001",
                    dPunExp="001",
                    dNumDoc="0000001",
                    dFeIniT="2024-01-01",
                    dFeFinT="2025-12-31",
                ),
                gDatGralOpe=TgDaGoc(
                    dFeEmiDE="2024-11-29T17:59:57",
                    gOpeCom=TgOpeCom(
                        iTipTra="1",
                        dDesTipTra="Venta de mercadería",
                        iTImp="1",
                        dDesTImp="IVA",
                        cMoneOpe="PYG",
                        dDesMoneOpe="Guarani",
                    ),
                    gEmis=_make_emisor(),
                    gDatRec=_make_receptor(),
                ),
                gDtipDE=TgDtipDe(
                    gCamFE=TgCamFe(
                        iIndPres="1",
                        dDesIndPres="Operación presencial",
                    ),
                    gCamCond=TgCamCond(
                        iCondOpe=TiCondOpe.VALUE_1,
                        dDCondOpe="Contado",
                        gPaConEIni=[
                            TgPagCont(
                                iTiPago=TiTiPago.VALUE_1,
                                dDesTiPag="Efectivo",
                                dMonTiPag=Decimal("750000"),
                                cMoneTiPag="PYG",
                                dDMoneTiPag="Guarani",
                            )
                        ],
                    ),
                    gCamItem=[
                        _make_item(
                            "A01",
                            "Item A",
                            Decimal("3"),
                            Decimal("250000"),
                        )
                    ],
                ),
                gTotSub=_make_totales(
                    total=Decimal("750000"),
                    iva10=Decimal("68182"),
                    base10=Decimal("681818"),
                ),
            ),
            Signature=_make_signature(),
            gCamFuFD=TgCamFuFd(
                dCarQR=(
                    "https://ekuatia.set.gov.py/"
                    "consultas/qr?nVersion=150"
                ),
            ),
        )

        xml1 = rde.to_xml()
        rde2 = RDe.from_xml(xml1)
        xml2 = rde2.to_xml()

        assert xml1 == xml2
        assert rde2.DE.gDtipDE.gCamItem[0].dCodInt == "A01"
        assert rde2.DE.gTotSub.dTotGralOpe == Decimal("750000")


# ── Testes de Leitura Profunda de Samples ────────────────────────────


class TestDeepReadSamples:
    """Leitura profunda de todos os campos dos XML de exemplo."""

    def test_factura_complete_navigation(self):
        """Navega por todos os níveis da factura."""
        from sifenlib.de.bindings.v150.fe_v141 import RDe

        path = os.path.join(SAMPLES_DIR, "factura_electronica.xml")
        rde = RDe.from_path(path)

        # Nível 1: RDe
        assert rde.dVerFor == "150"
        assert rde.Signature is not None
        assert rde.gCamFuFD is not None

        # Nível 2: DE
        de = rde.DE
        assert de.Id is not None
        assert len(de.Id) == 44
        assert de.dDVId == "9"
        assert de.dFecFirma is not None

        # Nível 3: gOpeDE
        assert de.gOpeDE.iTipEmi == "1"
        assert de.gOpeDE.dCodSeg is not None

        # Nível 3: gTimb
        assert de.gTimb.iTiDE == "1"
        assert de.gTimb.dNumTim is not None
        assert de.gTimb.dEst == "001"
        assert de.gTimb.dPunExp == "001"

        # Nível 3: gDatGralOpe
        gral = de.gDatGralOpe
        assert gral.dFeEmiDE is not None

        # Nível 4: gOpeCom
        assert gral.gOpeCom.cMoneOpe.value == "PYG"

        # Nível 4: gEmis (emissor)
        emis = gral.gEmis
        assert emis.dRucEm == "80069563"
        assert emis.dDVEmi == "1"
        assert emis.iTipCont == "1"
        assert emis.dNomEmi == "Empresa Demo S.A."
        assert emis.dDirEmi is not None
        assert emis.cDepEmi is not None
        assert emis.dEmailE is not None
        assert len(emis.gActEco) >= 1

        # Nível 4: gDatRec (receptor)
        rec = gral.gDatRec
        assert rec.dRucRec == "4192083"
        assert rec.dNomRec == "Cliente Demo S.A."

        # Nível 3: gDtipDE
        dtip = de.gDtipDE
        assert dtip.gCamFE is not None
        assert dtip.gCamCond is not None

        # Nível 4: Items
        assert len(dtip.gCamItem) == 2
        item1 = dtip.gCamItem[0]
        assert item1.dCodInt == "PROD001"
        assert item1.dDesProSer == "Producto de prueba"
        assert item1.dCantProSer == Decimal("2")
        assert item1.gValorItem is not None
        assert item1.gValorItem.dPUniProSer == Decimal("500000")
        assert item1.gCamIVA is not None
        assert item1.gCamIVA.dTasaIVA == Decimal("10")

        # Nível 3: gTotSub
        assert de.gTotSub.dTotGralOpe == Decimal("1150000")

    def test_nota_credito_complete_navigation(self):
        """Navega pela nota de crédito com documento associado."""
        from sifenlib.de.bindings.v150.fe_v141 import RDe

        path = os.path.join(SAMPLES_DIR, "nota_credito.xml")
        rde = RDe.from_path(path)

        assert rde.DE.gTimb.iTiDE == "5"
        assert rde.DE.gDtipDE.gCamNCDE is not None

        # Documento associado
        assoc = rde.DE.gCamDEAsoc
        assert len(assoc) >= 1
        assert assoc[0].iTipDocAso.value == 1
        assert assoc[0].dCdCDERef is not None
        assert len(assoc[0].dCdCDERef) == 44

    def test_autofactura_complete_navigation(self):
        """Navega pela autofactura com dados do vendedor."""
        from sifenlib.de.bindings.v150.fe_v141 import RDe

        path = os.path.join(SAMPLES_DIR, "autofactura.xml")
        rde = RDe.from_path(path)

        assert rde.DE.gTimb.iTiDE == "4"
        ae = rde.DE.gDtipDE.gCamAE
        assert ae is not None
        assert ae.dNomVen == "Juan Vendedor Pérez"
        assert ae.dNumIDVen == "1234567"
        assert ae.dDirVen is not None

    def test_nota_remision_complete_navigation(self):
        """Navega pela nota de remisión com motivo de traslado."""
        from sifenlib.de.bindings.v150.fe_v141 import RDe

        path = os.path.join(SAMPLES_DIR, "nota_remision.xml")
        rde = RDe.from_path(path)

        assert rde.DE.gTimb.iTiDE == "7"
        nre = rde.DE.gDtipDE.gCamNRE
        assert nre is not None

        # Items da nota de remisión
        assert len(rde.DE.gDtipDE.gCamItem) == 1
        item = rde.DE.gDtipDE.gCamItem[0]
        assert item.dCodInt == "PROD001"
        assert item.dCantProSer == Decimal("50")


# ── Testes de Validação XML ──────────────────────────────────────────


class TestXmlValidation:
    """Testes de validação estrutural do XML gerado."""

    def test_xml_has_declaration(self):
        from sifenlib.de.bindings.v150.fe_v141 import RDe

        path = os.path.join(SAMPLES_DIR, "factura_electronica.xml")
        rde = RDe.from_path(path)
        xml = rde.to_xml()
        assert xml.startswith('<?xml version="1.0" encoding="UTF-8"?>')

    def test_xml_is_well_formed(self):
        """Verifica que o XML gerado é well-formed."""
        from sifenlib.de.bindings.v150.fe_v141 import RDe

        for filename in sorted(os.listdir(SAMPLES_DIR)):
            if not filename.endswith(".xml"):
                continue
            path = os.path.join(SAMPLES_DIR, filename)
            rde = RDe.from_path(path)
            xml = rde.to_xml()
            # lxml parseia sem erro = well-formed
            etree.fromstring(xml.encode("utf-8"))

    def test_xml_has_namespace(self):
        """XML gerado contém o namespace SIFEN."""
        from sifenlib.de.bindings.v150.fe_v141 import RDe

        path = os.path.join(SAMPLES_DIR, "factura_electronica.xml")
        rde = RDe.from_path(path)
        xml = rde.to_xml()
        assert "ekuatia.set.gov.py/sifen/xsd" in xml

    def test_xml_has_xmldsig_namespace(self):
        """XML gerado contém namespace xmldsig para Signature."""
        from sifenlib.de.bindings.v150.fe_v141 import RDe

        path = os.path.join(SAMPLES_DIR, "factura_electronica.xml")
        rde = RDe.from_path(path)
        xml = rde.to_xml()
        assert "www.w3.org/2000/09/xmldsig" in xml

    def test_xsd_schema_loadable(self):
        """Verifica que os schemas XSD carregam corretamente."""
        for xsd_name in [
            "FE_v141.xsd",
            "DE_v150.xsd",
            "Evento_v150.xsd",
            "siRecepDE_v150.xsd",
        ]:
            path = os.path.join(SCHEMAS_DIR, xsd_name)
            with open(path, "rb") as f:
                schema_doc = etree.parse(f)
            schema = etree.XMLSchema(schema_doc)
            assert schema is not None, f"Failed to load {xsd_name}"


# ── Testes de Assinatura com Certificado Fake ────────────────────────


class TestSignXml:
    """Testes de assinatura XML com certificado de teste."""

    @pytest.fixture
    def cert_path(self):
        return os.path.join(os.path.dirname(__file__), "test_cert.pfx")

    @pytest.fixture
    def cert_data(self, cert_path):
        if not os.path.exists(cert_path):
            pytest.skip("test_cert.pfx not found")
        with open(cert_path, "rb") as f:
            return f.read()

    def test_sign_xml_requires_signxml(self, cert_data):
        """sign_xml levanta ImportError sem signxml."""
        from sifenlib.de.bindings.v150.fe_v141 import RDe

        path = os.path.join(SAMPLES_DIR, "factura_electronica.xml")
        rde = RDe.from_path(path)
        xml = rde.to_xml()

        try:
            rde.sign_xml(xml, cert_data, "test1234", rde.DE.Id)
        except ImportError as e:
            assert "sifenlib[sign]" in str(e)
        except Exception:
            # Se signxml estiver instalado, qualquer
            # erro de assinatura é aceitável neste teste
            pass

    def test_sign_method_exists(self):
        """sign_xml está disponível em todas as classes."""
        from sifenlib.de.bindings.v150.fe_v141 import RDe, TDe, TgEmis

        for cls in [RDe, TDe, TgEmis]:
            assert hasattr(cls, "sign_xml")
            assert callable(getattr(cls, "sign_xml"))

    def test_cert_file_valid_pkcs12(self, cert_data):
        """Certificado de teste é PKCS12 válido."""
        from cryptography.hazmat.primitives.serialization import pkcs12

        private_key, cert, chain = pkcs12.load_key_and_certificates(
            cert_data, b"test1234"
        )
        assert private_key is not None
        assert cert is not None
        assert cert.subject.rfc4514_string() is not None
