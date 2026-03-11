"""Assinatura digital XML para SIFEN (RSA-SHA256)."""


def sign_xml(xml_input, pkcs12_data, pkcs12_password, doc_id):
    """Assina XML usando certificado PKCS12 com RSA-SHA256.

    Args:
        xml_input: XML string ou lxml Element
        pkcs12_data: bytes do .pfx
        pkcs12_password: senha (str ou bytes)
        doc_id: ID do elemento a referenciar (CDC)

    Returns:
        XML assinado como string
    """
    from cryptography.hazmat.primitives.serialization import (
        Encoding,
        NoEncryption,
        PrivateFormat,
        pkcs12,
    )
    from lxml import etree
    from signxml import XMLSigner, methods

    password = (
        pkcs12_password.encode()
        if isinstance(pkcs12_password, str)
        else pkcs12_password
    )
    private_key, certificate, _ = (
        pkcs12.load_key_and_certificates(pkcs12_data, password)
    )
    key_pem = private_key.private_bytes(
        Encoding.PEM, PrivateFormat.TraditionalOpenSSL, NoEncryption()
    )
    cert_pem = certificate.public_bytes(Encoding.PEM)

    # Parsear XML se string
    if isinstance(xml_input, (str, bytes)):
        xml_bytes = (
            xml_input.encode()
            if isinstance(xml_input, str)
            else xml_input
        )
        root = etree.fromstring(xml_bytes)
    else:
        root = xml_input

    # Limpar whitespace (necessário para C14N consistente)
    for el in root.iter("*"):
        if el.text is not None and not el.text.strip():
            el.text = None
        if el.tail is not None and not el.tail.strip():
            el.tail = None

    # Assinar com signxml
    signer = XMLSigner(
        method=methods.enveloped,
        signature_algorithm="rsa-sha256",
        digest_algorithm="sha256",
        c14n_algorithm=(
            "http://www.w3.org/TR/2001/REC-xml-c14n-20010315"
        ),
    )
    ref_uri = f"#{doc_id}" if doc_id else None
    signed = signer.sign(
        root, key=key_pem, cert=cert_pem,
        reference_uri=ref_uri,
    )

    # Reposicionar Signature para parent do elemento assinado
    if doc_id:
        element = signed.find(f".//*[@Id='{doc_id}']")
        signature = signed.find(
            ".//{http://www.w3.org/2000/09/xmldsig#}Signature"
        )
        if element is not None and signature is not None:
            parent = element.getparent()
            if parent is not None:
                parent.append(signature)

    return etree.tostring(signed, encoding="unicode")
