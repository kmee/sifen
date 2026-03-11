"""Testes de integridade dos schemas e detecção de atualizações."""
import os
import warnings

import pytest

warnings.filterwarnings("ignore")

SCHEMAS_DIR = os.path.join(
    os.path.dirname(__file__), "..", "sifenlib", "de", "schemas", "v150"
)


class TestSchemaIntegrity:
    """Verifica integridade dos schemas locais."""

    def test_schemas_dir_exists(self):
        assert os.path.isdir(SCHEMAS_DIR)

    def test_main_schemas_present(self):
        expected = [
            "DE_v150.xsd",
            "DE_Types_v150.xsd",
            "Evento_v150.xsd",
            "Paises_v100.xsd",
            "Unidades_Medida_v141.xsd",
            "xmldsig-core-schema.xsd",
        ]
        for schema in expected:
            path = os.path.join(SCHEMAS_DIR, schema)
            assert os.path.isfile(path), f"Missing schema: {schema}"

    def test_ws_schemas_present(self):
        expected = [
            "siRecepDE_v150.xsd",
            "siRecepRDE_v150.xsd",
            "siRecepEvento_v150.xsd",
            "protProcesDE_v150.xsd",
        ]
        for schema in expected:
            path = os.path.join(SCHEMAS_DIR, schema)
            assert os.path.isfile(path), f"Missing WS schema: {schema}"

    def test_no_remote_schema_locations(self):
        """Verifica que nenhum XSD referencia URLs remotas."""
        for filename in os.listdir(SCHEMAS_DIR):
            if not filename.endswith(".xsd"):
                continue
            path = os.path.join(SCHEMAS_DIR, filename)
            with open(path, "r", encoding="utf-8") as f:
                content = f.read()
            assert "ekuatia.set.gov.py/sifen/xsd/" not in content, (
                f"{filename} still has remote schemaLocation references"
            )

    def test_schema_count(self):
        """Verifica quantidade mínima de schemas."""
        xsd_files = [f for f in os.listdir(SCHEMAS_DIR) if f.endswith(".xsd")]
        assert len(xsd_files) >= 40, (
            f"Expected at least 40 XSD files, found {len(xsd_files)}"
        )


class TestBindingsIntegrity:
    """Verifica integridade dos bindings gerados."""

    def test_bindings_importable(self):
        from sifenlib.de.bindings.v150 import fe_v141

        assert hasattr(fe_v141, "RDe")

    def test_all_binding_modules_importable(self):
        import importlib
        import pkgutil

        import sifenlib.de.bindings.v150 as pkg

        for importer, modname, ispkg in pkgutil.iter_modules(pkg.__path__):
            mod = importlib.import_module(
                f"sifenlib.de.bindings.v150.{modname}"
            )
            assert mod is not None, f"Failed to import {modname}"

    def test_binding_count(self):
        """Verifica quantidade mínima de módulos de bindings."""
        import pkgutil

        import sifenlib.de.bindings.v150 as pkg

        modules = list(pkgutil.iter_modules(pkg.__path__))
        assert len(modules) >= 20, (
            f"Expected at least 20 binding modules, found {len(modules)}"
        )


@pytest.mark.skipif(
    not os.environ.get("CHECK_SCHEMA_UPDATES"),
    reason="Set CHECK_SCHEMA_UPDATES=1 to check for schema updates",
)
class TestSchemaUpdates:
    """Detecta se há novos schemas disponíveis na SET."""

    def test_check_remote_schemas(self):
        import re
        import ssl
        import urllib.request

        ctx = ssl.create_default_context()
        ctx.check_hostname = False
        ctx.verify_mode = ssl.CERT_NONE

        url = "https://ekuatia.set.gov.py/sifen/xsd/"
        req = urllib.request.Request(
            url, headers={"User-Agent": "Mozilla/5.0"}
        )
        resp = urllib.request.urlopen(req, context=ctx, timeout=30)
        html = resp.read().decode()

        remote_files = set(re.findall(r'href="([^"]+\.xsd)"', html))
        local_files = set(
            f for f in os.listdir(SCHEMAS_DIR) if f.endswith(".xsd")
        )

        new_schemas = remote_files - local_files
        if new_schemas:
            pytest.fail(
                f"New schemas available on SET: {sorted(new_schemas)}"
            )
