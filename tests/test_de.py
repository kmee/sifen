"""Testes de leitura e escrita de Documentos Electrónicos (DE)."""
import os
import warnings
from decimal import Decimal

import pytest

warnings.filterwarnings("ignore")

SAMPLES_DIR = os.path.join(
    os.path.dirname(__file__), "..", "pysifen", "de", "samples", "v150"
)


@pytest.fixture
def factura_path():
    return os.path.join(SAMPLES_DIR, "factura_electronica.xml")


@pytest.fixture
def nota_credito_path():
    return os.path.join(SAMPLES_DIR, "nota_credito.xml")


@pytest.fixture
def autofactura_path():
    return os.path.join(SAMPLES_DIR, "autofactura.xml")


@pytest.fixture
def nota_remision_path():
    return os.path.join(SAMPLES_DIR, "nota_remision.xml")


class TestReadFactura:
    """Testes de leitura de Factura Electrónica (tipo 1)."""

    def test_parse_factura(self, factura_path):
        from pysifen.de.bindings.v150.fe_v141 import RDe

        rde = RDe.from_path(factura_path)
        assert rde is not None
        assert rde.dVerFor == "150"

    def test_factura_tipo(self, factura_path):
        from pysifen.de.bindings.v150.fe_v141 import RDe

        rde = RDe.from_path(factura_path)
        assert rde.DE.gTimb.iTiDE == "1"

    def test_factura_emisor(self, factura_path):
        from pysifen.de.bindings.v150.fe_v141 import RDe

        rde = RDe.from_path(factura_path)
        emis = rde.DE.gDatGralOpe.gEmis
        assert emis.dRucEm == "80069563"
        assert emis.dNomEmi == "Empresa Demo S.A."
        assert emis.dDirEmi == "Av. España 1234"
        assert emis.dEmailE == "demo@empresa.com.py"

    def test_factura_receptor(self, factura_path):
        from pysifen.de.bindings.v150.fe_v141 import RDe

        rde = RDe.from_path(factura_path)
        rec = rde.DE.gDatGralOpe.gDatRec
        assert rec.dRucRec == "4192083"
        assert rec.dNomRec == "Cliente Demo S.A."

    def test_factura_items(self, factura_path):
        from pysifen.de.bindings.v150.fe_v141 import RDe

        rde = RDe.from_path(factura_path)
        items = rde.DE.gDtipDE.gCamItem
        assert len(items) == 2
        assert items[0].dCodInt == "PROD001"
        assert items[0].dDesProSer == "Producto de prueba"
        assert items[1].dCodInt == "SERV001"

    def test_factura_totales(self, factura_path):
        from pysifen.de.bindings.v150.fe_v141 import RDe

        rde = RDe.from_path(factura_path)
        totais = rde.DE.gTotSub
        assert totais.dTotGralOpe == Decimal("1150000")
        assert totais.dSub10 == Decimal("1150000")
        assert totais.dIVA10 == Decimal("104545")

    def test_factura_iva(self, factura_path):
        from pysifen.de.bindings.v150.fe_v141 import RDe, TiAfecIva

        rde = RDe.from_path(factura_path)
        item = rde.DE.gDtipDE.gCamItem[0]
        assert item.gCamIVA.iAfecIVA == TiAfecIva.VALUE_1
        assert item.gCamIVA.dTasaIVA == Decimal("10")

    def test_factura_condicion_pago(self, factura_path):
        from pysifen.de.bindings.v150.fe_v141 import RDe, TiCondOpe

        rde = RDe.from_path(factura_path)
        cond = rde.DE.gDtipDE.gCamCond
        assert cond.iCondOpe == TiCondOpe.VALUE_1
        assert len(cond.gPaConEIni) == 1
        assert cond.gPaConEIni[0].dMonTiPag == Decimal("1150000")

    def test_factura_campos_futuro(self, factura_path):
        from pysifen.de.bindings.v150.fe_v141 import RDe

        rde = RDe.from_path(factura_path)
        assert rde.gCamFuFD is not None
        assert "ekuatia.set.gov.py" in rde.gCamFuFD.dCarQR


class TestReadNotaCredito:
    """Testes de leitura de Nota de Crédito (tipo 5)."""

    def test_parse_nota_credito(self, nota_credito_path):
        from pysifen.de.bindings.v150.fe_v141 import RDe

        rde = RDe.from_path(nota_credito_path)
        assert rde.DE.gTimb.iTiDE == "5"

    def test_nota_credito_motivo(self, nota_credito_path):
        from pysifen.de.bindings.v150.fe_v141 import RDe, TiMotEmi

        rde = RDe.from_path(nota_credito_path)
        assert rde.DE.gDtipDE.gCamNCDE is not None
        assert rde.DE.gDtipDE.gCamNCDE.iMotEmi == TiMotEmi.VALUE_1

    def test_nota_credito_doc_associado(self, nota_credito_path):
        from pysifen.de.bindings.v150.fe_v141 import RDe

        rde = RDe.from_path(nota_credito_path)
        assoc = rde.DE.gCamDEAsoc
        assert assoc is not None
        assert len(assoc) > 0


class TestReadAutofactura:
    """Testes de leitura de Autofactura (tipo 4)."""

    def test_parse_autofactura(self, autofactura_path):
        from pysifen.de.bindings.v150.fe_v141 import RDe

        rde = RDe.from_path(autofactura_path)
        assert rde.DE.gTimb.iTiDE == "4"

    def test_autofactura_campos(self, autofactura_path):
        from pysifen.de.bindings.v150.fe_v141 import RDe

        rde = RDe.from_path(autofactura_path)
        ae = rde.DE.gDtipDE.gCamAE
        assert ae is not None
        assert ae.dNomVen == "Juan Vendedor Pérez"


class TestReadNotaRemision:
    """Testes de leitura de Nota de Remisión (tipo 7)."""

    def test_parse_nota_remision(self, nota_remision_path):
        from pysifen.de.bindings.v150.fe_v141 import RDe

        rde = RDe.from_path(nota_remision_path)
        assert rde.DE.gTimb.iTiDE == "7"

    def test_nota_remision_motivo(self, nota_remision_path):
        from pysifen.de.bindings.v150.fe_v141 import RDe

        rde = RDe.from_path(nota_remision_path)
        nre = rde.DE.gDtipDE.gCamNRE
        assert nre is not None
        # iMotEmiNR pode ser lista de enum ou enum direto
        mot = nre.iMotEmiNR
        if isinstance(mot, list):
            assert mot[0].value == 1
        else:
            assert mot.value == 1


class TestFromXml:
    """Testes de from_xml (string)."""

    def test_from_xml_string(self, factura_path):
        from pysifen.de.bindings.v150.fe_v141 import RDe

        with open(factura_path) as f:
            xml_string = f.read()
        rde = RDe.from_xml(xml_string)
        assert rde.DE.gDatGralOpe.gEmis.dRucEm == "80069563"


class TestSerialization:
    """Testes de serialização (to_xml) e round-trip."""

    def test_to_xml(self, factura_path):
        from pysifen.de.bindings.v150.fe_v141 import RDe

        rde = RDe.from_path(factura_path)
        xml = rde.to_xml()
        assert '<?xml version="1.0" encoding="UTF-8"?>' in xml
        assert "80069563" in xml
        assert "Empresa Demo" in xml

    def test_round_trip(self, factura_path):
        from pysifen.de.bindings.v150.fe_v141 import RDe

        rde1 = RDe.from_path(factura_path)
        xml = rde1.to_xml()
        rde2 = RDe.from_xml(xml)

        assert rde1.dVerFor == rde2.dVerFor
        assert rde1.DE.Id == rde2.DE.Id
        assert rde1.DE.gDatGralOpe.gEmis.dRucEm == rde2.DE.gDatGralOpe.gEmis.dRucEm
        assert rde1.DE.gDatGralOpe.gEmis.dNomEmi == rde2.DE.gDatGralOpe.gEmis.dNomEmi
        assert len(rde1.DE.gDtipDE.gCamItem) == len(rde2.DE.gDtipDE.gCamItem)
        assert rde1.DE.gTotSub.dTotGralOpe == rde2.DE.gTotSub.dTotGralOpe

    def test_round_trip_all_samples(self):
        from pysifen.de.bindings.v150.fe_v141 import RDe

        for filename in os.listdir(SAMPLES_DIR):
            if not filename.endswith(".xml"):
                continue
            path = os.path.join(SAMPLES_DIR, filename)
            rde1 = RDe.from_path(path)
            xml = rde1.to_xml()
            rde2 = RDe.from_xml(xml)
            assert rde1.DE.Id == rde2.DE.Id, f"Round-trip failed for {filename}"

    def test_to_xml_compact(self, factura_path):
        from pysifen.de.bindings.v150.fe_v141 import RDe

        rde = RDe.from_path(factura_path)
        xml_pretty = rde.to_xml(pretty_print=True)
        xml_compact = rde.to_xml(pretty_print=False)
        assert len(xml_compact) < len(xml_pretty)


class TestCommonMixin:
    """Testes do CommonMixin."""

    def test_mixin_methods_exist(self):
        from pysifen.de.bindings.v150.fe_v141 import RDe

        assert hasattr(RDe, "from_xml")
        assert hasattr(RDe, "from_path")
        assert hasattr(RDe, "to_xml")
        assert hasattr(RDe, "validate_xml")
        assert hasattr(RDe, "sign_xml")

    def test_mixin_on_sub_classes(self):
        from pysifen.de.bindings.v150.fe_v141 import TgEmis

        assert hasattr(TgEmis, "from_xml")
        assert hasattr(TgEmis, "to_xml")
