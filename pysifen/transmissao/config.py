"""Configuração de ambientes e endpoints do SIFEN."""

PRODUCCION = 1
TEST = 2

ENDPOINTS = {
    PRODUCCION: {
        "recep_de": (
            "https://sifen.set.gov.py/de/ws/sync/recibe.wsdl"
        ),
        "recep_lote": (
            "https://sifen.set.gov.py/de/ws/async/recibe-lote.wsdl"
        ),
        "cons_de": (
            "https://sifen.set.gov.py/de/ws/consultas/consulta.wsdl"
        ),
        "cons_lote": (
            "https://sifen.set.gov.py/"
            "de/ws/consultas/consulta-lote.wsdl"
        ),
        "cons_ruc": (
            "https://sifen.set.gov.py/consultas/ruc.wsdl"
        ),
        "evento": (
            "https://sifen.set.gov.py/de/ws/eventos/"
            "recibe-evento.wsdl"
        ),
        "cons_dte": (
            "https://sifen.set.gov.py/"
            "de/ws/consultas/consulta-dte.wsdl"
        ),
    },
    TEST: {
        "recep_de": (
            "https://sifen-test.set.gov.py/"
            "de/ws/sync/recibe.wsdl"
        ),
        "recep_lote": (
            "https://sifen-test.set.gov.py/"
            "de/ws/async/recibe-lote.wsdl"
        ),
        "cons_de": (
            "https://sifen-test.set.gov.py/"
            "de/ws/consultas/consulta.wsdl"
        ),
        "cons_lote": (
            "https://sifen-test.set.gov.py/"
            "de/ws/consultas/consulta-lote.wsdl"
        ),
        "cons_ruc": (
            "https://sifen-test.set.gov.py/consultas/ruc.wsdl"
        ),
        "evento": (
            "https://sifen-test.set.gov.py/"
            "de/ws/eventos/recibe-evento.wsdl"
        ),
        "cons_dte": (
            "https://sifen-test.set.gov.py/"
            "de/ws/consultas/consulta-dte.wsdl"
        ),
    },
}


def get_endpoint(ambiente: int, servico: str) -> str:
    """Retorna a URL do endpoint para o ambiente e serviço."""
    if ambiente not in ENDPOINTS:
        raise ValueError(
            f"Ambiente inválido: {ambiente}. "
            f"Use PRODUCCION ({PRODUCCION}) ou TEST ({TEST})."
        )
    endpoints = ENDPOINTS[ambiente]
    if servico not in endpoints:
        raise ValueError(
            f"Serviço inválido: {servico}. "
            f"Serviços disponíveis: {list(endpoints.keys())}"
        )
    return endpoints[servico]
