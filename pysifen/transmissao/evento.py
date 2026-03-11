"""Transmissão de eventos ao SIFEN."""
from __future__ import annotations

from pysifen.de.bindings.v150.ws_si_recep_evento_v150 import (
    REnviEventoDe,
    RRetEnviEventoDe,
)
from pysifen.transmissao.base import TransmissaoBase


class TransmissaoEvento(TransmissaoBase):
    """Transmissão de eventos de DE ao SIFEN."""

    def enviar_evento(
        self, evento
    ) -> RRetEnviEventoDe:
        """Envia evento (cancelamento, inutilização, etc).

        Args:
            evento: instância de TgGroupGesEve (grupo de
                gestão de eventos)

        Returns:
            RRetEnviEventoDe com resultado do processamento
        """
        envi_evento = REnviEventoDe(
            dId=_generate_id(),
            dEvReg=REnviEventoDe.DEvReg(
                gGroupGesEve=evento,
            ),
        )

        client = self._get_client("evento")
        response = client.send(envi_evento)

        if isinstance(response, RRetEnviEventoDe):
            return response

        return self._parse(
            response if isinstance(response, str)
            else response.decode(),
            RRetEnviEventoDe,
        )


def _generate_id() -> int:
    """Gera ID de controle de envio baseado em timestamp."""
    import time

    return int(time.time() * 1000) % 999999999999999
