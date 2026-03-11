# pysifen

Bindings Python para ler e gerar XML do **SIFEN** (Sistema Integrado de Facturación Electrónica Nacional) do Paraguai.

Gerados automaticamente a partir dos XSD oficiais da SET usando [xsdata](https://xsdata.readthedocs.io/), seguindo a mesma abordagem da [nfelib](https://github.com/akretion/nfelib).

## Instalação

```bash
pip install pysifen
```

Com assinatura digital (RSA-SHA256):

```bash
pip install pysifen[sign]
```

Com transmissão SOAP (envio ao SIFEN):

```bash
pip install pysifen[transmissao]
```

Para desenvolvimento:

```bash
pip install -e ".[sign,test]"
```

## Uso

### Ler um Documento Electrónico (DE)

```python
from pysifen.de.bindings.v150.fe_v141 import RDe

# Ler de arquivo
rde = RDe.from_path("factura.xml")

# Ler de string
rde = RDe.from_xml(xml_string)

# Navegar nos dados
print(rde.DE.gDatGralOpe.gEmis.dRucEm)       # RUC do emissor
print(rde.DE.gDatGralOpe.gEmis.dNomEmi)       # Nome do emissor
print(rde.DE.gDtipDE.gCamFE.iIndPres)         # Indicador de presença
print(len(rde.DE.gDtipDE.gCamItem))            # Quantidade de itens
```

### Serializar para XML

```python
xml = rde.to_xml()
print(xml)
```

### Round-trip (ler e escrever)

```python
rde = RDe.from_path("factura.xml")
xml = rde.to_xml()
rde2 = RDe.from_xml(xml)
assert rde.DE.Id == rde2.DE.Id
```

### Validar contra XSD

```python
errors = rde.validate_xml()
if not errors:
    print("XML válido!")
else:
    for error in errors:
        print(error)
```

### Assinar XML (RSA-SHA256)

```bash
pip install pysifen[sign]
```

```python
with open("certificado.pfx", "rb") as f:
    cert_data = f.read()
signed = rde.sign_xml(xml, cert_data, "password", rde.DE.Id)
```

Usa `signxml` diretamente com RSA-SHA256 e C14N, conforme exigido pelo SIFEN.
A função centralizada também está disponível em:

```python
from pysifen.assinatura import sign_xml

signed = sign_xml(xml, cert_data, "password", doc_id)
```

### Transmissão SOAP ao SIFEN

```bash
pip install pysifen[transmissao]
```

#### Enviar DE (síncrono)

```python
from pysifen.transmissao import TransmissaoDE, TEST

transmissao = TransmissaoDE(
    ambiente=TEST,
    pkcs12_data=cert_data,
    pkcs12_password="password",
)
resultado = transmissao.enviar_de(rde)
print(resultado.rProtDe.dEstRes)      # "Aprobado"
print(resultado.rProtDe.dProtAut)     # Protocolo de autorização
```

#### Enviar lote de DEs (assíncrono)

```python
resultado = transmissao.enviar_lote([rde1, rde2, rde3])
print(resultado.dProtConsLote)  # Protocolo para consulta posterior
```

#### Consultar DE por CDC

```python
from pysifen.transmissao import ConsultaSIFEN, TEST

consulta = ConsultaSIFEN(
    ambiente=TEST,
    pkcs12_data=cert_data,
    pkcs12_password="password",
)
resultado = consulta.consultar_de("01800695631001001000000612024112917595714694")
```

#### Consultar RUC

```python
resultado = consulta.consultar_ruc("80069563")
print(resultado.xContRUC.dRazCons)      # Razão social
print(resultado.xContRUC.dRUCFactElec)  # "S" = habilitado para FE
```

#### Enviar eventos (cancelamento, inutilização, etc.)

```python
from pysifen.transmissao import TransmissaoEvento, TEST

evento_transmissao = TransmissaoEvento(
    ambiente=TEST,
    pkcs12_data=cert_data,
    pkcs12_password="password",
)
resultado = evento_transmissao.enviar_evento(evento)
```

## Tipos de Documento Electrónico

| Tipo | Código | Descrição |
|------|--------|-----------|
| Factura Electrónica | 1 | Fatura eletrônica |
| FE Exportación | 2 | Fatura de exportação |
| FE Importación | 3 | Fatura de importação |
| Autofactura | 4 | Autofatura |
| Nota de Crédito | 5 | Nota de crédito |
| Nota de Débito | 6 | Nota de débito |
| Nota de Remisión | 7 | Nota de remissão |
| Comprobante de Retención | 8 | Comprovante de retenção |

## Módulos

### Bindings (gerados automaticamente)

| Módulo | Descrição |
|--------|-----------|
| `fe_v141` | Documento Electrónico principal (RDe, TDe, TgEmis, ...) |
| `de_v150` | Tipos adicionais do DE v150 |
| `de_types_v150` | Tipos base (enums, restrições) |
| `evento_v150` | Eventos (cancelação, inutilização, conformidade, ...) |
| `evento_types_v150` | Tipos de eventos |
| `ws_si_recep_de_v150` | WS Recepção DE |
| `ws_si_recep_evento_v150` | WS Recepção Evento |
| `ws_si_cons_de_v141` | WS Consulta DE |
| `ws_si_cons_ruc_v141` | WS Consulta RUC |
| `prot_proces_de_v150` | Protocolo de processamento |
| `xmldsig_core_schema` | Assinatura digital XML |

### Assinatura (`pysifen.assinatura`)

| Função | Descrição |
|--------|-----------|
| `sign_xml()` | Assina XML com PKCS12/RSA-SHA256 usando `signxml` |

### Transmissão (`pysifen.transmissao`)

| Classe | Descrição |
|--------|-----------|
| `TransmissaoDE` | Envio de DEs (síncrono e lote) com mTLS |
| `ConsultaSIFEN` | Consultas (DE por CDC, lote, RUC, DTE) |
| `TransmissaoEvento` | Envio de eventos (cancelamento, inutilização, etc.) |
| `TransmissaoBase` | Classe base com SOAP client, mTLS e serialização |

### Ambientes

| Constante | Valor | Descrição |
|-----------|-------|-----------|
| `PRODUCCION` | 1 | Ambiente de produção (`sifen.set.gov.py`) |
| `TEST` | 2 | Ambiente de testes (`sifen-test.set.gov.py`) |

## Dependências Opcionais

| Extra | Pacotes | Uso |
|-------|---------|-----|
| `sign` | `signxml`, `cryptography`, `lxml` | Assinatura digital RSA-SHA256 |
| `transmissao` | `xsdata[soap]`, `signxml`, `cryptography`, `requests`, `lxml` | Transmissão SOAP com mTLS |
| `soap` | `xsdata[soap]` | Apenas cliente SOAP |
| `test` | `pytest`, `pytest-cov`, `xmldiff`, `lxml` | Testes |

## Regenerar Bindings

Se os XSD forem atualizados:

```bash
pip install xsdata[cli,lxml]
./script.sh
```

## Desenvolvimento

```bash
git clone https://github.com/KMEE/pysifen.git
cd pysifen
python -m venv .venv
source .venv/bin/activate
pip install -e ".[sign,test]" "xsdata[cli,lxml]"
pytest tests/ -v
ruff check pysifen/ tests/
```

## Referências

- [XSD oficiais SIFEN](https://ekuatia.set.gov.py/sifen/xsd/)
- [Manual Técnico v150](https://www.dnit.gov.py/documents/20123/420592/Manual+T%C3%A9cnico+Versi%C3%B3n+150.pdf)
- [Portal e-Kuatia](https://ekuatia.set.gov.py)
- [nfelib (referência)](https://github.com/akretion/nfelib)
- [xsdata](https://xsdata.readthedocs.io/)

## Licença

MIT License - Copyright (c) KMEE
