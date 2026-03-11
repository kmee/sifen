"""Testes do módulo de assinatura digital XML."""
import os

import pytest

pytest.importorskip("signxml", reason="signxml not installed")
pytest.importorskip("cryptography", reason="cryptography not installed")

SAMPLES_DIR = os.path.join(
    os.path.dirname(__file__), "..", "pysifen", "de", "samples", "v150"
)


@pytest.fixture
def cert_path():
    return os.path.join(os.path.dirname(__file__), "test_cert.pfx")


@pytest.fixture
def cert_data(cert_path):
    if not os.path.exists(cert_path):
        pytest.skip("test_cert.pfx not found")
    with open(cert_path, "rb") as f:
        return f.read()


@pytest.fixture
def sample_xml():
    path = os.path.join(SAMPLES_DIR, "factura_electronica.xml")
    with open(path) as f:
        return f.read()


@pytest.fixture
def sample_rde():
    from pysifen.de.bindings.v150.fe_v141 import RDe

    path = os.path.join(SAMPLES_DIR, "factura_electronica.xml")
    return RDe.from_path(path)


class TestSignXml:
    """Testes de assinatura XML com signxml."""

    def test_sign_xml_with_test_cert(
        self, cert_data, sample_rde
    ):
        """Assina XML de amostra e verifica Signature."""
        from pysifen.assinatura import sign_xml

        xml = sample_rde.to_xml()
        signed = sign_xml(
            xml, cert_data, "test1234", sample_rde.DE.Id
        )

        assert "<ds:Signature" in signed or "<Signature" in signed
        assert "SignatureValue" in signed
        assert "SignedInfo" in signed

    def test_sign_xml_sha256(self, cert_data, sample_rde):
        """Verifica que usa SHA256 (não SHA1)."""
        from pysifen.assinatura import sign_xml

        xml = sample_rde.to_xml()
        signed = sign_xml(
            xml, cert_data, "test1234", sample_rde.DE.Id
        )

        assert "rsa-sha256" in signed or "sha256" in signed.lower()
        assert "rsa-sha1" not in signed

    def test_sign_xml_reference_uri(
        self, cert_data, sample_rde
    ):
        """Verifica que Reference URI aponta para o CDC."""
        from lxml import etree

        from pysifen.assinatura import sign_xml

        xml = sample_rde.to_xml()
        doc_id = sample_rde.DE.Id
        signed = sign_xml(xml, cert_data, "test1234", doc_id)

        root = etree.fromstring(signed.encode())
        ns = {"ds": "http://www.w3.org/2000/09/xmldsig#"}
        refs = root.findall(".//ds:Reference", ns)
        assert len(refs) >= 1

        uris = [r.get("URI", "") for r in refs]
        assert any(f"#{doc_id}" in uri for uri in uris)

    def test_sign_xml_roundtrip(self, cert_data, sample_rde):
        """Assina, parseia de volta, verifica estrutura."""
        from lxml import etree

        from pysifen.assinatura import sign_xml

        xml = sample_rde.to_xml()
        signed = sign_xml(
            xml, cert_data, "test1234", sample_rde.DE.Id
        )

        # Deve ser XML válido
        root = etree.fromstring(signed.encode())
        assert root is not None

        # Deve conter elemento Signature
        ns = {"ds": "http://www.w3.org/2000/09/xmldsig#"}
        sig = root.find(".//ds:Signature", ns)
        assert sig is not None

        # Deve conter SignedInfo, SignatureValue, KeyInfo
        assert sig.find("ds:SignedInfo", ns) is not None
        assert sig.find("ds:SignatureValue", ns) is not None

    def test_sign_xml_invalid_cert(self, sample_rde):
        """Testa erro com certificado inválido."""
        from pysifen.assinatura import sign_xml

        xml = sample_rde.to_xml()
        with pytest.raises(Exception):
            sign_xml(
                xml, b"invalid-pkcs12", "wrong", sample_rde.DE.Id
            )

    def test_sign_xml_bytes_input(
        self, cert_data, sample_rde
    ):
        """Aceita XML como bytes."""
        from pysifen.assinatura import sign_xml

        xml = sample_rde.to_xml().encode()
        signed = sign_xml(
            xml, cert_data, "test1234", sample_rde.DE.Id
        )
        assert "SignatureValue" in signed

    def test_sign_xml_bytes_password(
        self, cert_data, sample_rde
    ):
        """Aceita senha como bytes."""
        from pysifen.assinatura import sign_xml

        xml = sample_rde.to_xml()
        signed = sign_xml(
            xml, cert_data, b"test1234", sample_rde.DE.Id
        )
        assert "SignatureValue" in signed

    def test_sign_via_mixin(self, cert_data, sample_rde):
        """Testa assinatura via CommonMixin.sign_xml()."""
        xml = sample_rde.to_xml()
        signed = sample_rde.sign_xml(
            xml, cert_data, "test1234", sample_rde.DE.Id
        )
        assert "SignatureValue" in signed
