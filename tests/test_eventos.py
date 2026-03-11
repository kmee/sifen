"""Testes de bindings de eventos do SIFEN."""
import warnings

warnings.filterwarnings("ignore")


class TestEventoBindings:
    """Verifica que os bindings de evento são importáveis e usáveis."""

    def test_import_evento_v150(self):
        from pysifen.de.bindings.v150.evento_v150 import TrEve

        assert hasattr(TrEve, "__dataclass_fields__")

    def test_import_evento_types(self):
        from pysifen.de.bindings.v150.evento_types_v150 import TiTipEve

        assert TiTipEve is not None

    def test_evento_cancelacion(self):
        from pysifen.de.bindings.v150.evento_v150 import TrGeVeCan

        fields = list(TrGeVeCan.__dataclass_fields__.keys())
        assert len(fields) > 0

    def test_evento_inutilizacion(self):
        from pysifen.de.bindings.v150.evento_v150 import TrGeVeInu

        fields = list(TrGeVeInu.__dataclass_fields__.keys())
        assert len(fields) > 0

    def test_evento_conformidad(self):
        from pysifen.de.bindings.v150.evento_v150 import TrGeVeConf

        fields = list(TrGeVeConf.__dataclass_fields__.keys())
        assert len(fields) > 0

    def test_evento_disconformidad(self):
        from pysifen.de.bindings.v150.evento_v150 import TrGeVeDisconf

        fields = list(TrGeVeDisconf.__dataclass_fields__.keys())
        assert len(fields) > 0

    def test_evento_nominacion(self):
        from pysifen.de.bindings.v150.evento_v150 import TrGeveNom

        fields = list(TrGeveNom.__dataclass_fields__.keys())
        assert len(fields) > 0

    def test_evento_mixin(self):
        from pysifen.de.bindings.v150.evento_v150 import TrEve

        assert hasattr(TrEve, "from_xml")
        assert hasattr(TrEve, "to_xml")
