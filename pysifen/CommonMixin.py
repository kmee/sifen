"""Mixin comum para todos os bindings do SIFEN."""
import os
from pathlib import Path

from xsdata.formats.dataclass.parsers import XmlParser
from xsdata.formats.dataclass.serializers import XmlSerializer
from xsdata.formats.dataclass.serializers.config import SerializerConfig


class CommonMixin:
    """Mixin adicionado automaticamente pelo xsdata a todas as classes."""

    @classmethod
    def from_xml(cls, xml_string: str):
        """Deserializa um XML string em objeto Python."""
        parser = XmlParser()
        return parser.from_string(xml_string, cls)

    @classmethod
    def from_path(cls, file_path: str):
        """Deserializa um arquivo XML em objeto Python."""
        parser = XmlParser()
        return parser.from_path(Path(file_path), cls)

    def to_xml(self, pretty_print: bool = True) -> str:
        """Serializa o objeto Python em XML string."""
        config = SerializerConfig(
            pretty_print=pretty_print,
            xml_declaration=True,
            encoding="UTF-8",
        )
        serializer = XmlSerializer(config=config)
        return serializer.render(self)

    def validate_xml(self) -> list:
        """Valida o XML contra o schema XSD correspondente."""
        from lxml import etree

        xml_string = self.to_xml()
        xml_doc = etree.fromstring(xml_string.encode())

        module = self.__class__.__module__
        parts = module.split(".")
        # pysifen.de.bindings.v150.de_v150 -> pysifen/de/schemas/v150/
        schema_dir = os.path.join(
            os.path.dirname(os.path.abspath(__file__)),
            parts[1],  # "de"
            "schemas",
            parts[3],  # "v150"
        )
        schema_files = [f for f in os.listdir(schema_dir) if f.endswith(".xsd")]
        errors = []
        for schema_file in schema_files:
            try:
                schema_path = os.path.join(schema_dir, schema_file)
                with open(schema_path, "rb") as f:
                    schema_doc = etree.parse(f)
                schema = etree.XMLSchema(schema_doc)
                schema.assertValid(xml_doc)
                return []
            except etree.DocumentInvalid as e:
                errors = [str(err) for err in e.error_log]
            except Exception:
                continue
        return errors

    def sign_xml(self, xml, pkcs12_data, pkcs12_password, doc_id):
        """Assina o XML usando certificado PKCS12 (RSA-SHA256)."""
        try:
            from pysifen.assinatura import sign_xml
        except ImportError:
            raise ImportError(
                "Para assinar XML, instale: "
                "pip install sifen[sign]"
            )
        return sign_xml(xml, pkcs12_data, pkcs12_password, doc_id)
