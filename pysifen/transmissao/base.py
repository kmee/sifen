"""Classe base para transmissão SOAP ao SIFEN."""
from __future__ import annotations

import tempfile

from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import (
    SerializerConfig,
)

from pysifen.transmissao.config import get_endpoint


class TransmissaoBase:
    """Base para transmissão SOAP com mTLS ao SIFEN.

    Args:
        ambiente: PRODUCCION (1) ou TEST (2)
        pkcs12_data: bytes do certificado .pfx
        pkcs12_password: senha do certificado
    """

    def __init__(
        self,
        ambiente: int,
        pkcs12_data: bytes,
        pkcs12_password: str,
    ):
        self.ambiente = ambiente
        self.pkcs12_data = pkcs12_data
        self.pkcs12_password = pkcs12_password
        self._parser = XmlParser()
        self._serializer = XmlSerializer(
            config=SerializerConfig(
                xml_declaration=True,
                encoding="UTF-8",
            )
        )
        self._cert_files = None

    def _get_cert_files(self) -> tuple[str, str]:
        """Extrai cert e key do PKCS12 para arquivos temporários.

        Retorna tupla (cert_path, key_path) para uso com
        requests/httpx.
        """
        if self._cert_files is not None:
            return self._cert_files

        from cryptography.hazmat.primitives.serialization import (
            BestAvailableEncryption,
            Encoding,
            NoEncryption,
            pkcs12,
        )

        private_key, certificate, _ = pkcs12.load_key_and_certificates(
            self.pkcs12_data,
            self.pkcs12_password.encode()
            if isinstance(self.pkcs12_password, str)
            else self.pkcs12_password,
        )

        cert_file = tempfile.NamedTemporaryFile(
            suffix=".pem", delete=False
        )
        key_file = tempfile.NamedTemporaryFile(
            suffix=".pem", delete=False
        )

        cert_file.write(certificate.public_bytes(Encoding.PEM))
        cert_file.close()

        key_file.write(
            private_key.private_bytes(
                Encoding.PEM,
                BestAvailableEncryption(b"")
                if False
                else NoEncryption(),
            )
        )
        key_file.close()

        self._cert_files = (cert_file.name, key_file.name)
        return self._cert_files

    def _get_client(self, servico: str):
        """Retorna xsdata SOAP client para o serviço.

        O client é configurado com mTLS usando o certificado
        PKCS12.
        """
        from xsdata.formats.dataclass.client import Client, Config

        url = get_endpoint(self.ambiente, servico)
        cert_path, key_path = self._get_cert_files()

        config = Config.from_service(
            None,
            location=url,
        )
        transport = _create_transport(cert_path, key_path)
        return Client(config=config, transport=transport)

    def _sign_xml(self, xml: str, doc_id: str) -> str:
        """Assina XML com certificado PKCS12 (RSA-SHA256)."""
        from pysifen.assinatura import sign_xml

        return sign_xml(
            xml, self.pkcs12_data, self.pkcs12_password, doc_id
        )

    def _serialize(self, obj) -> str:
        """Serializa um objeto binding para XML string."""
        return self._serializer.render(obj)

    def _parse(self, xml: str, clazz):
        """Parseia XML string para objeto binding."""
        return self._parser.from_string(xml, clazz)

    def cleanup(self):
        """Remove arquivos temporários de certificado."""
        import os

        if self._cert_files:
            for path in self._cert_files:
                try:
                    os.unlink(path)
                except OSError:
                    pass
            self._cert_files = None

    def __del__(self):
        self.cleanup()


def _create_transport(cert_path: str, key_path: str):
    """Cria transport HTTP com mTLS para o SOAP client.

    Usa requests.Session com certificado cliente.
    """
    from requests import Session

    session = Session()
    session.cert = (cert_path, key_path)
    session.verify = True

    class RequestsTransport:
        """Transport adapter usando requests para mTLS."""

        def __init__(self, session):
            self._session = session

        def post(self, url, data, headers=None):
            response = self._session.post(
                url,
                data=data,
                headers=headers or {
                    "Content-Type": "text/xml; charset=utf-8"
                },
            )
            response.raise_for_status()
            return response.content

    return RequestsTransport(session)
