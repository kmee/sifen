"""Testes unitários do módulo de transmissão SIFEN."""
import warnings
from decimal import Decimal
from unittest.mock import MagicMock, patch

import pytest

pytest.importorskip("requests", reason="requests not installed")

warnings.filterwarnings("ignore")


# ── Config ────────────────────────────────────────────


class TestConfig:
    """Testes de configuração de endpoints."""

    def test_ambientes_existem(self):
        from pysifen.transmissao.config import (
            ENDPOINTS,
            PRODUCCION,
            TEST,
        )

        assert PRODUCCION in ENDPOINTS
        assert TEST in ENDPOINTS

    def test_endpoints_produccion(self):
        from pysifen.transmissao.config import (
            ENDPOINTS,
            PRODUCCION,
        )

        endpoints = ENDPOINTS[PRODUCCION]
        servicos = [
            "recep_de",
            "recep_lote",
            "cons_de",
            "cons_lote",
            "cons_ruc",
            "evento",
            "cons_dte",
        ]
        for servico in servicos:
            assert servico in endpoints
            assert endpoints[servico].startswith("https://")

    def test_endpoints_test(self):
        from pysifen.transmissao.config import (
            ENDPOINTS,
            TEST,
        )

        endpoints = ENDPOINTS[TEST]
        for url in endpoints.values():
            assert "sifen-test" in url

    def test_get_endpoint_produccion(self):
        from pysifen.transmissao.config import (
            PRODUCCION,
            get_endpoint,
        )

        url = get_endpoint(PRODUCCION, "recep_de")
        assert "sifen.set.gov.py" in url

    def test_get_endpoint_test(self):
        from pysifen.transmissao.config import (
            TEST,
            get_endpoint,
        )

        url = get_endpoint(TEST, "recep_de")
        assert "sifen-test" in url

    def test_get_endpoint_ambiente_invalido(self):
        from pysifen.transmissao.config import get_endpoint

        with pytest.raises(ValueError, match="Ambiente inválido"):
            get_endpoint(99, "recep_de")

    def test_get_endpoint_servico_invalido(self):
        from pysifen.transmissao.config import (
            PRODUCCION,
            get_endpoint,
        )

        with pytest.raises(ValueError, match="Serviço inválido"):
            get_endpoint(PRODUCCION, "servico_fake")


# ── Imports ───────────────────────────────────────────


class TestImports:
    """Testa que todos os módulos importam corretamente."""

    def test_import_transmissao(self):
        from pysifen.transmissao import (
            PRODUCCION,
            TEST,
            ConsultaSIFEN,
            TransmissaoDE,
            TransmissaoEvento,
        )

        assert PRODUCCION == 1
        assert TEST == 2
        assert ConsultaSIFEN is not None
        assert TransmissaoDE is not None
        assert TransmissaoEvento is not None

    def test_import_config(self):
        from pysifen.transmissao.config import (
            ENDPOINTS,
            PRODUCCION,
            TEST,
            get_endpoint,
        )

        assert callable(get_endpoint)
        assert isinstance(ENDPOINTS, dict)
        assert PRODUCCION == 1
        assert TEST == 2

    def test_import_base(self):
        from pysifen.transmissao.base import TransmissaoBase

        assert TransmissaoBase is not None

    def test_import_de(self):
        from pysifen.transmissao.de import TransmissaoDE

        assert TransmissaoDE is not None

    def test_import_consulta(self):
        from pysifen.transmissao.consulta import ConsultaSIFEN

        assert ConsultaSIFEN is not None

    def test_import_evento(self):
        from pysifen.transmissao.evento import TransmissaoEvento

        assert TransmissaoEvento is not None


# ── TransmissaoDE ─────────────────────────────────────


class TestTransmissaoDE:
    """Testes de transmissão de DE."""

    def _make_transmissao(self):
        from pysifen.transmissao.config import TEST
        from pysifen.transmissao.de import TransmissaoDE

        return TransmissaoDE(
            ambiente=TEST,
            pkcs12_data=b"fake-cert",
            pkcs12_password="fake-pass",
        )

    def test_instancia(self):
        t = self._make_transmissao()
        assert t.ambiente == 2
        assert t.pkcs12_data == b"fake-cert"
        assert t.pkcs12_password == "fake-pass"

    @patch(
        "pysifen.transmissao.base.TransmissaoBase._get_client"
    )
    @patch(
        "pysifen.transmissao.base.TransmissaoBase._sign_xml"
    )
    @patch(
        "pysifen.transmissao.base.TransmissaoBase._serialize"
    )
    def test_enviar_de_mock(
        self, mock_serialize, mock_sign, mock_client
    ):
        from pysifen.de.bindings.v150.prot_proces_de_v150 import (
            RProtDe,
        )
        from pysifen.de.bindings.v150.prot_proces_eventos_v141 import (
            TgResProc,
        )
        from pysifen.de.bindings.v150.ws_si_recep_de_v150 import (
            RRetEnviDe,
        )

        mock_serialize.return_value = "<rDE>xml</rDE>"
        mock_sign.return_value = "<rDE>signed</rDE>"

        mock_response = RRetEnviDe(
            rProtDe=RProtDe(
                Id="01800695631001001000000612024112917595714694",
                dFecProc="2024-11-29T18:00:00-03:00",
                dEstRes="Aprobado",
                dProtAut=123456789,
                gResProc=[
                    TgResProc(
                        dCodRes="0260",
                        dMsgRes="DE aprobado",
                    )
                ],
            )
        )
        client_mock = MagicMock()
        client_mock.send.return_value = mock_response
        mock_client.return_value = client_mock

        t = self._make_transmissao()

        rde_mock = MagicMock()
        rde_mock.DE.Id = (
            "01800695631001001000000612024112917595714694"
        )

        result = t.enviar_de(rde_mock)

        assert isinstance(result, RRetEnviDe)
        assert result.rProtDe.dEstRes == "Aprobado"
        assert result.rProtDe.dProtAut == 123456789
        assert result.rProtDe.gResProc[0].dCodRes == "0260"
        mock_sign.assert_called_once()

    def test_enviar_lote_max_excedido(self):
        t = self._make_transmissao()
        with pytest.raises(ValueError, match="não pode exceder"):
            t.enviar_lote([MagicMock()] * 51)

    def test_enviar_lote_vazio(self):
        t = self._make_transmissao()
        with pytest.raises(ValueError, match="não pode ser vazia"):
            t.enviar_lote([])

    @patch(
        "pysifen.transmissao.base.TransmissaoBase._get_client"
    )
    @patch(
        "pysifen.transmissao.base.TransmissaoBase._sign_xml"
    )
    @patch(
        "pysifen.transmissao.base.TransmissaoBase._serialize"
    )
    def test_enviar_lote_mock(
        self, mock_serialize, mock_sign, mock_client
    ):
        from pysifen.de.bindings.v150.ws_si_recep_lote_de_v141 import (
            RResEnviLoteDe,
        )

        mock_serialize.return_value = "<rDE>xml</rDE>"
        mock_sign.return_value = "<rDE>signed</rDE>"

        mock_response = RResEnviLoteDe(
            dFecProc="2024-11-29T18:00:00-03:00",
            dCodRes="0300",
            dMsgRes="Lote recibido",
            dProtConsLote=Decimal("123456"),
            dTpoProces=30,
        )
        client_mock = MagicMock()
        client_mock.send.return_value = mock_response
        mock_client.return_value = client_mock

        t = self._make_transmissao()

        rdes = []
        for i in range(3):
            rde = MagicMock()
            rde.DE.Id = f"0180069563100100100000061202411291759571469{i}"
            rdes.append(rde)

        result = t.enviar_lote(rdes, lote_id=999)

        assert isinstance(result, RResEnviLoteDe)
        assert result.dCodRes == "0300"
        assert result.dProtConsLote == Decimal("123456")
        assert mock_sign.call_count == 3

    def test_enviar_de_sem_assinatura(self):
        """Testa enviar_de com sign=False."""
        t = self._make_transmissao()

        with patch.object(t, "_get_client") as mock_client, \
             patch.object(t, "_sign_xml") as mock_sign, \
             patch.object(t, "_serialize") as mock_serialize:
            from pysifen.de.bindings.v150.prot_proces_de_v150 import (
                RProtDe,
            )
            from pysifen.de.bindings.v150.prot_proces_eventos_v141 import (
                TgResProc,
            )
            from pysifen.de.bindings.v150.ws_si_recep_de_v150 import (
                RRetEnviDe,
            )

            mock_serialize.return_value = "<rDE>xml</rDE>"
            client_mock = MagicMock()
            client_mock.send.return_value = RRetEnviDe(
                rProtDe=RProtDe(
                    dFecProc="2024-11-29T18:00:00-03:00",
                    gResProc=[
                        TgResProc(
                            dCodRes="0260",
                            dMsgRes="OK",
                        )
                    ],
                )
            )
            mock_client.return_value = client_mock

            rde_mock = MagicMock()
            result = t.enviar_de(rde_mock, sign=False)

            mock_sign.assert_not_called()
            assert isinstance(result, RRetEnviDe)


# ── ConsultaSIFEN ─────────────────────────────────────


class TestConsultaSIFEN:
    """Testes de consultas ao SIFEN."""

    def _make_consulta(self):
        from pysifen.transmissao.config import TEST
        from pysifen.transmissao.consulta import ConsultaSIFEN

        return ConsultaSIFEN(
            ambiente=TEST,
            pkcs12_data=b"fake-cert",
            pkcs12_password="fake-pass",
        )

    def test_consultar_de_cdc_invalido_curto(self):
        c = self._make_consulta()
        with pytest.raises(ValueError, match="44 dígitos"):
            c.consultar_de("123")

    def test_consultar_de_cdc_invalido_letras(self):
        c = self._make_consulta()
        with pytest.raises(ValueError, match="44 dígitos"):
            c.consultar_de("A" * 44)

    def test_consultar_ruc_invalido_curto(self):
        c = self._make_consulta()
        with pytest.raises(ValueError, match="entre 5 e 8"):
            c.consultar_ruc("123")

    def test_consultar_ruc_invalido_longo(self):
        c = self._make_consulta()
        with pytest.raises(ValueError, match="entre 5 e 8"):
            c.consultar_ruc("123456789")

    @patch(
        "pysifen.transmissao.base.TransmissaoBase._get_client"
    )
    def test_consultar_de_mock(self, mock_client):
        from pysifen.de.bindings.v150.ws_si_cons_de_v141 import (
            REnviConsDeResponse,
        )

        mock_response = REnviConsDeResponse(
            dFecProc="2024-11-29T18:00:00-03:00",
            dCodRes="0422",
            dMsgRes="CDC encontrado",
            xContenDE="<DE>...</DE>",
        )
        client_mock = MagicMock()
        client_mock.send.return_value = mock_response
        mock_client.return_value = client_mock

        c = self._make_consulta()
        cdc = "01800695631001001000000612024112917595714694"
        result = c.consultar_de(cdc)

        assert isinstance(result, REnviConsDeResponse)
        assert result.dCodRes == "0422"

    @patch(
        "pysifen.transmissao.base.TransmissaoBase._get_client"
    )
    def test_consultar_lote_mock(self, mock_client):
        from pysifen.de.bindings.v150.ws_si_cons_lote_v141 import (
            RResEnviConsLoteDe,
        )

        mock_response = RResEnviConsLoteDe(
            dFecProc="2024-11-29T18:00:00-03:00",
            dCodResLot="0362",
            dMsgResLot="Lote procesado",
        )
        client_mock = MagicMock()
        client_mock.send.return_value = mock_response
        mock_client.return_value = client_mock

        c = self._make_consulta()
        result = c.consultar_lote(123456)

        assert isinstance(result, RResEnviConsLoteDe)
        assert result.dCodResLot == "0362"

    @patch(
        "pysifen.transmissao.base.TransmissaoBase._get_client"
    )
    def test_consultar_ruc_mock(self, mock_client):
        from pysifen.de.bindings.v150.ws_si_cons_ruc_v141 import (
            RResEnviConsRuc,
            TContenedorRuc,
        )

        mock_response = RResEnviConsRuc(
            dCodRes="0502",
            dMsgRes="Contribuyente encontrado",
            xContRUC=TContenedorRuc(
                dRUCCons="80069563",
                dRazCons="Empresa Demo S.A.",
                dCodEstCons="ACT",
                dDesEstCons="Activo",
                dRUCFactElec="S",
            ),
        )
        client_mock = MagicMock()
        client_mock.send.return_value = mock_response
        mock_client.return_value = client_mock

        c = self._make_consulta()
        result = c.consultar_ruc("80069563")

        assert isinstance(result, RResEnviConsRuc)
        assert result.xContRUC.dRazCons == "Empresa Demo S.A."
        assert result.xContRUC.dRUCFactElec == "S"

    @patch(
        "pysifen.transmissao.base.TransmissaoBase._get_client"
    )
    def test_consultar_dte_mock(self, mock_client):
        from pysifen.de.bindings.v150.ws_si_cons_dte import (
            RConsDteResponse,
        )

        mock_response = RConsDteResponse(
            dFecProc="2024-11-29T18:00:00",
            dMsgRes="Consulta exitosa",
            rConsDte=b"zipdata",
        )
        client_mock = MagicMock()
        client_mock.send.return_value = mock_response
        mock_client.return_value = client_mock

        c = self._make_consulta()
        consulta_dte = MagicMock()
        result = c.consultar_dte(consulta_dte)

        assert isinstance(result, RConsDteResponse)
        assert result.dMsgRes == "Consulta exitosa"


# ── TransmissaoEvento ─────────────────────────────────


class TestTransmissaoEvento:
    """Testes de transmissão de eventos."""

    def _make_transmissao(self):
        from pysifen.transmissao.config import TEST
        from pysifen.transmissao.evento import TransmissaoEvento

        return TransmissaoEvento(
            ambiente=TEST,
            pkcs12_data=b"fake-cert",
            pkcs12_password="fake-pass",
        )

    @patch(
        "pysifen.transmissao.base.TransmissaoBase._get_client"
    )
    def test_enviar_evento_mock(self, mock_client):
        from pysifen.de.bindings.v150.prot_proces_eventos_v141 import (
            TgResProc,
            TgResProcEve,
        )
        from pysifen.de.bindings.v150.ws_si_recep_evento_v150 import (
            RRetEnviEventoDe,
        )

        mock_response = RRetEnviEventoDe(
            dFecProc="2024-11-29T18:00:00-03:00",
            gResProcEVe=[
                TgResProcEve(
                    dEstRes="Aprobado",
                    dProtAut=987654321,
                    id="0000000001",
                    gResProc=[
                        TgResProc(
                            dCodRes="0460",
                            dMsgRes="Evento aprobado",
                        )
                    ],
                )
            ],
        )
        client_mock = MagicMock()
        client_mock.send.return_value = mock_response
        mock_client.return_value = client_mock

        t = self._make_transmissao()
        evento_mock = MagicMock()
        result = t.enviar_evento(evento_mock)

        assert isinstance(result, RRetEnviEventoDe)
        assert result.gResProcEVe[0].dEstRes == "Aprobado"
        assert result.gResProcEVe[0].dProtAut == 987654321


# ── Base ──────────────────────────────────────────────


class TestTransmissaoBase:
    """Testes da classe base."""

    def test_serialize(self):
        from pysifen.de.bindings.v150.ws_si_cons_ruc_v141 import (
            REnviConsRuc,
        )
        from pysifen.transmissao.base import TransmissaoBase
        from pysifen.transmissao.config import TEST

        t = TransmissaoBase(
            ambiente=TEST,
            pkcs12_data=b"fake",
            pkcs12_password="fake",
        )
        request = REnviConsRuc(dId=1, dRUCCons="80069563")
        xml = t._serialize(request)

        assert "rEnviConsRUC" in xml
        assert "80069563" in xml

    def test_parse(self):
        from pysifen.de.bindings.v150.ws_si_cons_ruc_v141 import (
            REnviConsRuc,
        )
        from pysifen.transmissao.base import TransmissaoBase
        from pysifen.transmissao.config import TEST

        t = TransmissaoBase(
            ambiente=TEST,
            pkcs12_data=b"fake",
            pkcs12_password="fake",
        )
        request = REnviConsRuc(dId=1, dRUCCons="80069563")
        xml = t._serialize(request)
        parsed = t._parse(xml, REnviConsRuc)

        assert parsed.dId == 1
        assert parsed.dRUCCons == "80069563"

    def test_cleanup(self):
        from pysifen.transmissao.base import TransmissaoBase
        from pysifen.transmissao.config import TEST

        t = TransmissaoBase(
            ambiente=TEST,
            pkcs12_data=b"fake",
            pkcs12_password="fake",
        )
        t._cert_files = ("/tmp/fake_cert.pem", "/tmp/fake_key.pem")
        t.cleanup()
        assert t._cert_files is None
