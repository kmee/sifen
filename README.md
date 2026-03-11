# sifen

Bindings Python para leer y generar XML del **SIFEN** (Sistema Integrado de Facturación Electrónica Nacional) de Paraguay.

Generados automáticamente a partir de los XSD oficiales de la SET usando [xsdata](https://xsdata.readthedocs.io/), siguiendo el mismo enfoque de [nfelib](https://github.com/akretion/nfelib).

## Instalación

```bash
pip install sifen
```

Con firma digital (RSA-SHA256):

```bash
pip install sifen[sign]
```

Con transmisión SOAP (envío al SIFEN):

```bash
pip install sifen[transmissao]
```

Para desarrollo:

```bash
pip install -e ".[sign,test]"
```

## Uso

### Leer un Documento Electrónico (DE)

```python
from pysifen.de.bindings.v150.fe_v141 import RDe

# Leer desde archivo
rde = RDe.from_path("factura.xml")

# Leer desde string
rde = RDe.from_xml(xml_string)

# Navegar los datos
print(rde.DE.gDatGralOpe.gEmis.dRucEm)       # RUC del emisor
print(rde.DE.gDatGralOpe.gEmis.dNomEmi)       # Nombre del emisor
print(rde.DE.gDtipDE.gCamFE.iIndPres)         # Indicador de presencia
print(len(rde.DE.gDtipDE.gCamItem))            # Cantidad de ítems
```

### Serializar a XML

```python
xml = rde.to_xml()
print(xml)
```

### Round-trip (leer y escribir)

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

### Firmar XML (RSA-SHA256)

```bash
pip install sifen[sign]
```

```python
with open("certificado.pfx", "rb") as f:
    cert_data = f.read()
signed = rde.sign_xml(xml, cert_data, "password", rde.DE.Id)
```

Usa `signxml` directamente con RSA-SHA256 y C14N, conforme lo exigido por el SIFEN.
La función centralizada también está disponible en:

```python
from pysifen.assinatura import sign_xml

signed = sign_xml(xml, cert_data, "password", doc_id)
```

### Transmisión SOAP al SIFEN

```bash
pip install sifen[transmissao]
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
print(resultado.rProtDe.dProtAut)     # Protocolo de autorización
```

#### Enviar lote de DEs (asíncrono)

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
print(resultado.xContRUC.dRazCons)      # Razón social
print(resultado.xContRUC.dRUCFactElec)  # "S" = habilitado para FE
```

#### Enviar eventos (cancelación, inutilización, etc.)

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

| Tipo | Código | Descripción |
|------|--------|-------------|
| Factura Electrónica | 1 | Factura electrónica estándar |
| FE Exportación | 2 | Factura de exportación |
| FE Importación | 3 | Factura de importación |
| Autofactura | 4 | Autofactura |
| Nota de Crédito | 5 | Nota de crédito electrónica |
| Nota de Débito | 6 | Nota de débito electrónica |
| Nota de Remisión | 7 | Nota de remisión electrónica |
| Comprobante de Retención | 8 | Comprobante de retención |

## Módulos

### Bindings (generados automáticamente)

| Módulo | Descripción |
|--------|-------------|
| `fe_v141` | Documento Electrónico principal (RDe, TDe, TgEmis, ...) |
| `de_v150` | Tipos adicionales del DE v150 |
| `de_types_v150` | Tipos base (enums, restricciones) |
| `evento_v150` | Eventos (cancelación, inutilización, conformidad, ...) |
| `evento_types_v150` | Tipos de eventos |
| `ws_si_recep_de_v150` | WS Recepción DE |
| `ws_si_recep_evento_v150` | WS Recepción Evento |
| `ws_si_cons_de_v141` | WS Consulta DE |
| `ws_si_cons_ruc_v141` | WS Consulta RUC |
| `prot_proces_de_v150` | Protocolo de procesamiento |
| `xmldsig_core_schema` | Firma digital XML |

### Firma (`pysifen.assinatura`)

| Función | Descripción |
|---------|-------------|
| `sign_xml()` | Firma XML con PKCS12/RSA-SHA256 usando `signxml` |

### Transmisión (`pysifen.transmissao`)

| Clase | Descripción |
|-------|-------------|
| `TransmissaoDE` | Envío de DEs (síncrono y lote) con mTLS |
| `ConsultaSIFEN` | Consultas (DE por CDC, lote, RUC, DTE) |
| `TransmissaoEvento` | Envío de eventos (cancelación, inutilización, etc.) |
| `TransmissaoBase` | Clase base con SOAP client, mTLS y serialización |

### Ambientes

| Constante | Valor | Descripción |
|-----------|-------|-------------|
| `PRODUCCION` | 1 | Ambiente de producción (`sifen.set.gov.py`) |
| `TEST` | 2 | Ambiente de pruebas (`sifen-test.set.gov.py`) |

## Dependencias Opcionales

| Extra | Paquetes | Uso |
|-------|----------|-----|
| `sign` | `signxml`, `cryptography`, `lxml` | Firma digital RSA-SHA256 |
| `transmissao` | `xsdata[soap]`, `signxml`, `cryptography`, `requests`, `lxml` | Transmisión SOAP con mTLS |
| `soap` | `xsdata[soap]` | Solo cliente SOAP |
| `test` | `pytest`, `pytest-cov`, `xmldiff`, `lxml` | Tests |

## Regenerar Bindings

Si los XSD se actualizan:

```bash
pip install xsdata[cli,lxml]
./script.sh
```

## Desarrollo

```bash
git clone https://github.com/kmee/sifen.git
cd sifen
python -m venv .venv
source .venv/bin/activate
pip install -e ".[sign,test]" "xsdata[cli,lxml]"
pytest tests/ -v
ruff check pysifen/ tests/
```

## Referencias

- [XSD oficiales SIFEN](https://ekuatia.set.gov.py/sifen/xsd/)
- [Manual Técnico v150](https://www.dnit.gov.py/documents/20123/420592/Manual+T%C3%A9cnico+Versi%C3%B3n+150.pdf)
- [Portal e-Kuatia](https://ekuatia.set.gov.py)
- [nfelib (referencia)](https://github.com/akretion/nfelib)
- [xsdata](https://xsdata.readthedocs.io/)

## Licencia

MIT License - Copyright (c) KMEE
