# sifenlib — Diretrizes do Projeto

## Visão Geral

Biblioteca Python que gera automaticamente bindings (dataclasses) a partir dos schemas XSD oficiais do **SIFEN** (Sistema Integrado de Facturación Electrónica Nacional) do Paraguai, usando **xsdata**, no mesmo padrão da [nfelib](https://github.com/akretion/nfelib) da Akretion.

**Princípio central:** Zero código manual para o schema. Todo binding é gerado pelo xsdata a partir dos XSD oficiais da SET. Código escrito à mão se limita ao `CommonMixin`, testes e scripts de geração.

## Metadados

- **Licença:** MIT
- **Copyright:** KMEE
- **Autor:** mileo
- **GitHub:** `KMEE/sifenlib`
- **Python:** >=3.9
- **Dependência principal:** xsdata

## Estrutura do Projeto

```
sifenlib/
├── .xsdata.xml                    # Configuração do xsdata (originalCase, CommonMixin extension)
├── pyproject.toml                 # Build config (setuptools)
├── script.sh                      # Script de geração de bindings
├── README.md
├── MIT-LICENSE
├── sifenlib/
│   ├── __init__.py                # __version__ = "0.1.0"
│   ├── CommonMixin.py             # Mixin: from_xml, to_xml, from_path, validate_xml, sign_xml
│   └── de/                        # Documento Electrónico
│       ├── schemas/v150/          # XSD originais da SET (com schemaLocation local)
│       ├── bindings/v150/         # Bindings gerados pelo xsdata (NÃO editar manualmente)
│       └── samples/v150/          # XMLs de exemplo para testes
├── tests/
│   ├── test_de.py                 # Testes de leitura/escrita DE
│   ├── test_eventos.py            # Testes de eventos
│   ├── test_ws.py                 # Testes de schemas WS
│   └── test_schema_versions.py    # Detecta novas versões de schemas
└── .github/workflows/tests.yml    # CI: pytest + ruff
```

## Comandos Frequentes

```bash
# Instalar em modo dev
pip install -e ".[test]"

# Gerar/regenerar bindings (após alterar XSD ou .xsdata.xml)
./script.sh

# Rodar testes
pytest tests/ -v

# Lint
ruff check sifenlib/ tests/
```

## Convenções

### Código
- **Bindings são gerados automaticamente** — NUNCA editar arquivos em `sifenlib/de/bindings/` manualmente
- **FieldName originalCase** — campos mantêm nomes do XSD (ex: `iTipEmi`, `dDesTipEmi`, `gOpeDE`)
- **CommonMixin** é injetado em todas as classes via `.xsdata.xml` Extension
- **Um arquivo .py por arquivo .xsd** (Structure: filenames)

### Schemas XSD
- Fonte oficial: `https://ekuatia.set.gov.py/sifen/xsd/`
- Namespace: `http://ekuatia.set.gov.py/sifen/xsd`
- Todos os `schemaLocation` devem usar paths relativos locais (`./DE_Types_v150.xsd`)
- Versão na pasta usa 3 dígitos: `v150` = versão 1.50 do Manual Técnico

### Versionamento de Schemas
- v150 = Manual Técnico versão 1.50
- Schemas de versões mistas coexistem na mesma pasta (DE_Types_v150, SIFEN_Types_v141, Paises_v100)
- Nova versão major (2.00) ganha pasta `v200/`

### Testes
- Framework: pytest
- Cada tipo de DE deve ter teste de leitura (parsing) e escrita (serialização)
- Testes de round-trip: XML → objeto → XML → comparar
- Samples XML em `sifenlib/de/samples/v150/`

### Estilo
- Ruff para lint (rules: E, F, I, W)
- Target: Python 3.9
- Max line length: 79 (para bindings gerados)

## Tipos de Documento Electrónico (DE)

| Tipo | Código | Descrição |
|------|--------|-----------|
| Factura Electrónica | 1 | Fatura eletrônica padrão |
| FE Exportación | 2 | Fatura de exportação |
| FE Importación | 3 | Fatura de importação |
| Autofactura | 4 | Autofatura |
| Nota de Crédito | 5 | Nota de crédito eletrônica |
| Nota de Débito | 6 | Nota de débito eletrônica |
| Nota de Remisión | 7 | Nota de remissão eletrônica |
| Comprobante de Retención | 8 | Comprovante de retenção |

## API Esperada

```python
# Ler XML
from sifenlib.de.bindings.v150.de_v150 import Rde
rde = Rde.from_path("factura.xml")
rde = Rde.from_xml(xml_string)

# Navegar
rde.DE.gDatGralOpe.gEmis.dRucEm
rde.DE.gDatGralOpe.gEmis.dNomEm

# Serializar
xml = rde.to_xml()

# Validar contra XSD
errors = rde.validate_xml()

# Assinar (requer signxml + cryptography)
signed = rde.sign_xml(xml, cert_data, password, doc_id)
```

## Dependências Opcionais

- `sign`: `signxml` + `cryptography` — assinatura digital XML (RSA-SHA256)
- `soap`: `xsdata[soap]` — cliente SOAP para WS da SET
- `test`: `pytest`, `pytest-cov`, `xmldiff`, `lxml`

## Referências

- XSD oficiais: https://ekuatia.set.gov.py/sifen/xsd/
- Manual Técnico v150: https://www.dnit.gov.py/documents/20123/420592/Manual+T%C3%A9cnico+Versi%C3%B3n+150.pdf
- nfelib (referência): https://github.com/akretion/nfelib
- xsdata docs: https://xsdata.readthedocs.io/
- jsifenlib (Java): https://github.com/roshkadev/rshk-jsifenlib

## Plano de Sprints

O plano detalhado está em `plano-sifenlib.md`. Resumo:

0. Setup inicial (git, pyproject.toml, .xsdata.xml)
1. Download e organização dos XSD (ajustar schemaLocation para paths relativos)
2. Geração dos bindings com xsdata
3. XMLs de exemplo para cada tipo de DE
4. Testes de leitura (parsing)
5. Testes de escrita (serialização + round-trip)
6. Detecção automática de atualizações de schema
7. Documentação, README, CI/CD, publicação PyPI
8. Funcionalidades avançadas (CDC, QR Code, KuDE, SOAP, integração Odoo)
