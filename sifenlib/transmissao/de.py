"""Transmissão de Documentos Eletrônicos ao SIFEN."""
from __future__ import annotations

import base64

from sifenlib.de.bindings.v150.ws_si_recep_de_v150 import (
    REnviDe,
    RRetEnviDe,
)
from sifenlib.de.bindings.v150.ws_si_recep_lote_de_v141 import (
    REnvioLote,
    RResEnviLoteDe,
)
from sifenlib.transmissao.base import TransmissaoBase

MAX_LOTE = 50


class TransmissaoDE(TransmissaoBase):
    """Transmissão de DE (síncrono e lote) ao SIFEN."""

    def enviar_de(self, rde, sign: bool = True) -> RRetEnviDe:
        """Envia um DE de forma síncrona.

        Args:
            rde: instância de RDe (documento eletrônico)
            sign: se True, assina o XML antes de enviar

        Returns:
            RRetEnviDe contendo RProtDe com resultado
        """
        xml_de = self._serialize(rde)

        if sign:
            doc_id = rde.DE.Id if hasattr(rde, "DE") else None
            if doc_id:
                xml_de = self._sign_xml(xml_de, doc_id)

        envi_de = REnviDe(
            dId=_generate_id(),
            xDE=REnviDe.XDe(),
        )

        client = self._get_client("recep_de")
        response = client.send(
            envi_de,
            headers={"xml_de": xml_de},
        )

        if isinstance(response, RRetEnviDe):
            return response

        return self._parse(
            response if isinstance(response, str)
            else response.decode(),
            RRetEnviDe,
        )

    def enviar_lote(
        self,
        lista_rde: list,
        lote_id: int | None = None,
        sign: bool = True,
    ) -> RResEnviLoteDe:
        """Envia lote de DEs (assíncrono).

        Args:
            lista_rde: lista de RDe (máximo 50)
            lote_id: identificador do lote (gerado se None)
            sign: se True, assina cada XML antes de enviar

        Returns:
            RResEnviLoteDe com dProtConsLote para consulta

        Raises:
            ValueError: se lote exceder MAX_LOTE (50) DEs
        """
        if len(lista_rde) > MAX_LOTE:
            raise ValueError(
                f"Lote não pode exceder {MAX_LOTE} DEs. "
                f"Recebido: {len(lista_rde)}"
            )
        if not lista_rde:
            raise ValueError("Lista de DEs não pode ser vazia.")

        xmls = []
        for rde in lista_rde:
            xml_de = self._serialize(rde)
            if sign:
                doc_id = (
                    rde.DE.Id if hasattr(rde, "DE") else None
                )
                if doc_id:
                    xml_de = self._sign_xml(xml_de, doc_id)
            xmls.append(xml_de)

        xml_concatenado = "\n".join(xmls)
        xde_base64 = base64.b64encode(
            xml_concatenado.encode("utf-8")
        )

        envio_lote = REnvioLote(
            dId=lote_id or _generate_id(),
            xDE=xde_base64,
        )

        client = self._get_client("recep_lote")
        response = client.send(envio_lote)

        if isinstance(response, RResEnviLoteDe):
            return response

        return self._parse(
            response if isinstance(response, str)
            else response.decode(),
            RResEnviLoteDe,
        )


def _generate_id() -> int:
    """Gera ID de controle de envio baseado em timestamp."""
    import time

    return int(time.time() * 1000) % 999999999999999
