"""Consultas ao SIFEN (DE, lote, RUC, DTE)."""
from __future__ import annotations

from decimal import Decimal

from sifenlib.de.bindings.v150.ws_si_cons_de_v141 import (
    REnviConsDeRequest,
    REnviConsDeResponse,
)
from sifenlib.de.bindings.v150.ws_si_cons_dte import (
    RConsDteRequest,
    RConsDteResponse,
)
from sifenlib.de.bindings.v150.ws_si_cons_lote_v141 import (
    REnviConsLoteDe,
    RResEnviConsLoteDe,
)
from sifenlib.de.bindings.v150.ws_si_cons_ruc_v141 import (
    REnviConsRuc,
    RResEnviConsRuc,
)
from sifenlib.transmissao.base import TransmissaoBase


class ConsultaSIFEN(TransmissaoBase):
    """Consultas aos web services do SIFEN."""

    def consultar_de(self, cdc: str) -> REnviConsDeResponse:
        """Consulta DE por CDC (44 dígitos).

        Args:
            cdc: Código de Control (44 dígitos numéricos)

        Returns:
            REnviConsDeResponse com resultado da consulta
        """
        if len(cdc) != 44 or not cdc.isdigit():
            raise ValueError(
                f"CDC deve ter 44 dígitos numéricos. "
                f"Recebido: '{cdc}' ({len(cdc)} chars)"
            )

        request = REnviConsDeRequest(
            dId=_generate_id(),
            dCDC=cdc,
        )

        client = self._get_client("cons_de")
        response = client.send(request)

        if isinstance(response, REnviConsDeResponse):
            return response

        return self._parse(
            response if isinstance(response, str)
            else response.decode(),
            REnviConsDeResponse,
        )

    def consultar_lote(
        self, prot_lote: int | Decimal
    ) -> RResEnviConsLoteDe:
        """Consulta resultado de lote pelo protocolo.

        Args:
            prot_lote: número de protocolo do lote

        Returns:
            RResEnviConsLoteDe com resultado por DE
        """
        request = REnviConsLoteDe(
            dId=_generate_id(),
            dProtConsLote=Decimal(str(prot_lote)),
        )

        client = self._get_client("cons_lote")
        response = client.send(request)

        if isinstance(response, RResEnviConsLoteDe):
            return response

        return self._parse(
            response if isinstance(response, str)
            else response.decode(),
            RResEnviConsLoteDe,
        )

    def consultar_ruc(self, ruc: str) -> RResEnviConsRuc:
        """Consulta dados de contribuinte por RUC.

        Args:
            ruc: número de RUC (5-8 caracteres)

        Returns:
            RResEnviConsRuc com dados do contribuinte
        """
        if not (5 <= len(ruc) <= 8):
            raise ValueError(
                f"RUC deve ter entre 5 e 8 caracteres. "
                f"Recebido: '{ruc}' ({len(ruc)} chars)"
            )

        request = REnviConsRuc(
            dId=_generate_id(),
            dRUCCons=ruc,
        )

        client = self._get_client("cons_ruc")
        response = client.send(request)

        if isinstance(response, RResEnviConsRuc):
            return response

        return self._parse(
            response if isinstance(response, str)
            else response.decode(),
            RResEnviConsRuc,
        )

    def consultar_dte(
        self, consulta_dte
    ) -> RConsDteResponse:
        """Consulta DTE (Documento Tributário Eletrônico).

        Args:
            consulta_dte: instância de RConsultaDte

        Returns:
            RConsDteResponse com resultado
        """
        request = RConsDteRequest(
            rConsultaDTE=consulta_dte,
        )

        client = self._get_client("cons_dte")
        response = client.send(request)

        if isinstance(response, RConsDteResponse):
            return response

        return self._parse(
            response if isinstance(response, str)
            else response.decode(),
            RConsDteResponse,
        )


def _generate_id() -> int:
    """Gera ID de controle de envio baseado em timestamp."""
    import time

    return int(time.time() * 1000) % 999999999999999
