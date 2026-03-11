"""Testes de bindings de Web Services do SIFEN."""
import warnings

warnings.filterwarnings("ignore")


class TestWsRecepcion:
    """Testes de schemas de recepção."""

    def test_import_ws_recep_de(self):
        from sifenlib.de.bindings.v150.ws_si_recep_de_v150 import (
            REnviDe,
            RRetEnviDe,
        )

        assert hasattr(REnviDe, "__dataclass_fields__")
        assert hasattr(RRetEnviDe, "__dataclass_fields__")

    def test_import_ws_recep_evento(self):
        from sifenlib.de.bindings.v150.ws_si_recep_evento_v150 import (
            REnviEventoDe,
            RRetEnviEventoDe,
        )

        assert hasattr(REnviEventoDe, "__dataclass_fields__")
        assert hasattr(RRetEnviEventoDe, "__dataclass_fields__")

    def test_import_ws_recep_lote(self):
        from sifenlib.de.bindings.v150.ws_si_recep_lote_de_v141 import (
            REnvioLote,
            RResEnviLoteDe,
        )

        assert hasattr(REnvioLote, "__dataclass_fields__")
        assert hasattr(RResEnviLoteDe, "__dataclass_fields__")


class TestWsConsulta:
    """Testes de schemas de consulta."""

    def test_import_cons_de(self):
        from sifenlib.de.bindings.v150.ws_si_cons_de_v141 import (
            REnviConsDeRequest,
            REnviConsDeResponse,
        )

        assert hasattr(REnviConsDeRequest, "__dataclass_fields__")
        assert hasattr(REnviConsDeResponse, "__dataclass_fields__")

    def test_import_cons_lote(self):
        from sifenlib.de.bindings.v150.ws_si_cons_lote_v141 import (
            REnviConsLoteDe,
            RResEnviConsLoteDe,
        )

        assert hasattr(REnviConsLoteDe, "__dataclass_fields__")
        assert hasattr(RResEnviConsLoteDe, "__dataclass_fields__")

    def test_import_cons_ruc(self):
        from sifenlib.de.bindings.v150.ws_si_cons_ruc_v141 import (
            REnviConsRuc,
            RResEnviConsRuc,
        )

        assert hasattr(REnviConsRuc, "__dataclass_fields__")
        assert hasattr(RResEnviConsRuc, "__dataclass_fields__")

    def test_import_cons_dte(self):
        from sifenlib.de.bindings.v150.ws_si_cons_dte import (
            RConsDteRequest,
            RConsDteResponse,
        )

        assert hasattr(RConsDteRequest, "__dataclass_fields__")
        assert hasattr(RConsDteResponse, "__dataclass_fields__")


class TestWsProtocolo:
    """Testes de schemas de protocolo."""

    def test_import_prot_de(self):
        from sifenlib.de.bindings.v150.prot_proces_de_v150 import RProtDe

        assert hasattr(RProtDe, "__dataclass_fields__")

    def test_import_prot_eventos(self):
        from sifenlib.de.bindings.v150.prot_proces_eventos_v141 import (
            TgResProc,
            TgResProcEve,
        )

        assert hasattr(TgResProc, "__dataclass_fields__")
        assert hasattr(TgResProcEve, "__dataclass_fields__")


class TestWsMixin:
    """Verifica que CommonMixin está nas classes WS."""

    def test_ws_has_mixin(self):
        from sifenlib.de.bindings.v150.ws_si_recep_de_v150 import REnviDe

        assert hasattr(REnviDe, "from_xml")
        assert hasattr(REnviDe, "to_xml")
        assert hasattr(REnviDe, "from_path")
