# Plano de Desenvolvimento: pysifen

**Bindings Python para ler e gerar XML do SIFEN (Paraguay) — usando xsdata, no formato nfelib**

---

## 1. Visão Geral do Projeto

### O que é

A **pysifen** será uma biblioteca Python que gera automaticamente bindings (dataclasses) a partir dos schemas XSD oficiais do SIFEN (Sistema Integrado de Facturación Electrónica Nacional) do Paraguai, usando a mesma abordagem comprovada da [nfelib](https://github.com/akretion/nfelib) da Akretion.

### Por que fazer

- **Não existe** uma biblioteca Python equivalente para o SIFEN — a única lib open source conhecida é a [rshk-jpysifen](https://github.com/roshkadev/rshk-jpysifen), escrita em Java.
- O SIFEN é **obrigatório** para cada vez mais contribuintes no Paraguai (desde 2026, para provedores do Estado), gerando demanda crescente.
- O padrão nfelib com xsdata provou ser extremamente eficiente: os bindings são gerados automaticamente, eliminando milhares de linhas de código manual.

### Princípio central

> **Zero código manual para o schema.** Todo binding é gerado pelo xsdata a partir dos XSD oficiais da SET. O código "escrito à mão" se limita ao `CommonMixin`, testes e scripts de geração.

---

## 2. Análise dos Schemas XSD do SIFEN

### Fonte oficial dos XSD

Os schemas estão publicados em: `https://ekuatia.set.gov.py/sifen/xsd/`

Além disso, o portal disponibiliza um RAR com a estrutura completa: `https://ekuatia.set.gov.py/documents/371863/0/Estructura+xml_DE.rar/`

### Namespace

Todos os schemas usam o namespace: `http://ekuatia.set.gov.py/sifen/xsd`

### Inventário dos XSD (versão 150)

**Schemas de Tipos (fundação):**

| Schema | Descrição |
|--------|-----------|
| `DE_Types_v150.xsd` | Tipos base do Documento Electrónico (tCDC, tEmail, etc.) |
| `SIFEN_Types_v141.xsd` | Tipos do sistema SIFEN |
| `Paises_v100.xsd` | Codificação de países (ISO 3166) |
| `Unidades_Medida_v141.xsd` | Unidades de medida |
| `xmldsig-core-schema.xsd` | Assinatura digital XML (W3C) |

**Schema principal:**

| Schema | Descrição |
|--------|-----------|
| `DE_v150.xsd` | **Documento Electrónico** — o schema principal com toda a estrutura do DE |
| `Evento_v150.xsd` | Formato de evento do emissor |

**Schemas de Serviços Web (envio/recepção):**

| Schema | Descrição |
|--------|-----------|
| `siRecepDE_v150.xsd` | WS Recepção de DE |
| `siRecepDE_v141.xsd` | WS Recepção DE (v141) |
| `siRecepRDE_v150.xsd` | WS Recepção Resposta DE |
| `siRecepDE_Ekuatiai_v150.xsd` | WS Recepção DE (e-Kuatia'i) |
| `siRecepRDE_Ekuatiai_v150.xsd` | WS Recepção Resposta (e-Kuatia'i) |
| `siRecepEvento_v150.xsd` | WS Recepção Evento |
| `siRecepEventoEmisor_v150.xsd` | WS Recepção Evento Emissor |
| `siRecepEventoReceptor_v150.xsd` | WS Recepção Evento Receptor |
| `siRecepEventoSet_v150.xsd` | WS Recepção Evento SET |

**Schemas de Protocolo/Resposta:**

| Schema | Descrição |
|--------|-----------|
| `protProcesDE_v150.xsd` | Protocolo de processamento DE |
| `protProcesEventos_v141.xsd` | Protocolo de processamento eventos |

**Schemas de Consulta:**

| Schema | Descrição |
|--------|-----------|
| `WS_SiConsDE_v141.xsd` | WS Consulta DE |
| `WS_SiConsLote_v141.xsd` | WS Consulta Lote |
| `WS_SiConsRUC_v141.xsd` | WS Consulta RUC |
| `WS_SiConsDTE.xsd` | WS Consulta DTE |
| `WS_SiConsDTEAsync.xsd` | WS Consulta DTE Assíncrono |
| `WS_ConsultaArchivoRuc.xsd` | WS Consulta Arquivo RUC |

**Schemas WSDL:**

| Schema | Descrição |
|--------|-----------|
| `WS_SiRecepDE_v141.xsd` | WSDL Recepção DE |
| `WS_SiRecepDE_v150.xsd` | WSDL Recepção DE v150 |
| `WS_SiRecepEvento_v141.xsd` | WSDL Recepção Evento |
| `WS_SiRecepEvento_v150.xsd` | WSDL Recepção Evento v150 |
| `WS_SiRecepLoteDE_v141.xsd` | WSDL Recepção Lote DE |

---

## 3. Arquitetura do Projeto (espelho da nfelib)

### Estrutura de diretórios

```
pysifen/
├── .xsdata.xml                          # Configuração do xsdata
├── .gitignore
├── .pre-commit-config.yaml
├── pyproject.toml
├── script.sh                            # Script de geração de todos os bindings
├── README.md
├── MIT-LICENSE
├── ext/
│   └── pysifen.jpg                     # Logo/imagem do projeto
├── pysifen/
│   ├── __init__.py                      # __version__ = "0.1.0"
│   ├── CommonMixin.py                   # Mixin com from_xml, to_xml, from_path, validate_xml, sign_xml
│   └── de/                              # Documento Electrónico
│       ├── __init__.py
│       ├── schemas/
│       │   └── v150/                    # XSD originais da SET
│       │       ├── DE_v150.xsd
│       │       ├── DE_Types_v150.xsd
│       │       ├── Evento_v150.xsd
│       │       ├── Paises_v100.xsd
│       │       ├── Unidades_Medida_v141.xsd
│       │       ├── xmldsig-core-schema.xsd
│       │       ├── siRecepDE_v150.xsd
│       │       ├── siRecepRDE_v150.xsd
│       │       ├── siRecepEvento_v150.xsd
│       │       ├── siRecepEventoEmisor_v150.xsd
│       │       ├── siRecepEventoReceptor_v150.xsd
│       │       ├── siRecepEventoSet_v150.xsd
│       │       ├── protProcesDE_v150.xsd
│       │       ├── WS_SiConsDE_v141.xsd
│       │       ├── WS_SiConsLote_v141.xsd
│       │       ├── WS_SiConsRUC_v141.xsd
│       │       ├── WS_SiConsDTE.xsd
│       │       └── ... (todos os XSD)
│       ├── bindings/
│       │   └── v150/                    # Bindings gerados automaticamente
│       │       ├── __init__.py
│       │       ├── de_v150.py           # Classes do DE
│       │       ├── de_types_v150.py     # Tipos base
│       │       ├── evento_v150.py       # Eventos
│       │       ├── paises_v100.py       # Países
│       │       └── ... (gerados pelo xsdata)
│       └── samples/
│           └── v150/                    # XMLs de exemplo para testes
│               ├── factura_electronica.xml
│               ├── nota_credito.xml
│               ├── autofactura.xml
│               └── ... (amostras reais)
├── tests/
│   ├── __init__.py
│   ├── test_de.py                       # Testes de leitura/escrita DE
│   ├── test_eventos.py                  # Testes de eventos
│   ├── test_ws.py                       # Testes de schemas WS
│   └── test_schema_versions.py          # Detecta novas versões de schemas
└── .github/
    └── workflows/
        └── tests.yml                    # CI com GitHub Actions
```

### Convenção de versionamento

Seguindo a nfelib, usar apenas **2 dígitos** para a versão do schema na pasta: v150 corresponde à versão 1.50 do Manual Técnico. Se a SET lançar uma versão 1.51 que mantém os mesmos 2 primeiros dígitos, os XSD se sobrepõem na mesma pasta. Uma eventual versão 2.00 ganharia uma pasta `v200/`.

---

## 4. Configuração do xsdata (`.xsdata.xml`)

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Config xmlns="http://pypi.org/project/xsdata" version="22.7">
  <Output maxLineLength="79">
    <Package>generated</Package>
    <Format repr="true" eq="true" order="false" unsafeHash="false"
            frozen="false" slots="false" kwOnly="false">dataclasses</Format>
    <Structure>filenames</Structure>
    <DocstringStyle>reStructuredText</DocstringStyle>
    <RelativeImports>false</RelativeImports>
    <CompoundFields defaultName="choice" forceDefaultName="false">false</CompoundFields>
    <PostponedAnnotations>false</PostponedAnnotations>
    <UnnestClasses>false</UnnestClasses>
  </Output>
  <Extensions>
    <Extension type="class" class=".*"
               import="pysifen.CommonMixin"
               prepend="false" applyIfDerived="false"/>
  </Extensions>
  <Conventions>
    <ClassName case="pascalCase" safePrefix="type"/>
    <FieldName case="originalCase" safePrefix="value"/>
    <ConstantName case="screamingSnakeCase" safePrefix="value"/>
    <ModuleName case="snakeCase" safePrefix="mod"/>
    <PackageName case="snakeCase" safePrefix="pkg"/>
  </Conventions>
  <Substitutions>
    <Substitution type="package"
                  search="http://ekuatia.set.gov.py/sifen/xsd"
                  replace="sifen"/>
    <Substitution type="package"
                  search="http://www.w3.org/2000/09/xmldsig#"
                  replace="xmldsig"/>
  </Substitutions>
</Config>
```

### Pontos-chave da configuração

- **`FieldName case="originalCase"`**: Mantém os nomes dos campos XSD exatamente como estão (ex.: `iTipEmi`, `dDesTipEmi`, `gOpeDE`), o que é fundamental para compatibilidade com o Manual Técnico.
- **`Extension CommonMixin`**: Injeta os métodos `from_xml()`, `to_xml()`, `from_path()`, `validate_xml()` e `sign_xml()` em todas as classes geradas.
- **`Structure filenames`**: Gera um arquivo Python por arquivo XSD, mantendo a correspondência clara.

---

## 5. CommonMixin

O `CommonMixin` é o único arquivo de código "manual" significativo e deve oferecer a mesma API que a nfelib:

```python
"""Mixin comum para todos os bindings do SIFEN."""
import os
from pathlib import Path
from lxml import etree
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
        xml_string = self.to_xml()
        xml_doc = etree.fromstring(xml_string.encode())

        # Localizar o XSD baseado no módulo da classe
        module = self.__class__.__module__
        parts = module.split(".")
        # pysifen.de.bindings.v150.de_v150 -> pysifen/de/schemas/v150/
        schema_dir = os.path.join(
            os.path.dirname(__file__),
            parts[1],  # "de"
            "schemas",
            parts[3],  # "v150"
        )
        # Encontrar o XSD principal
        schema_files = [f for f in os.listdir(schema_dir) if f.endswith(".xsd")]
        errors = []
        for schema_file in schema_files:
            try:
                schema_path = os.path.join(schema_dir, schema_file)
                with open(schema_path, "rb") as f:
                    schema_doc = etree.parse(f)
                schema = etree.XMLSchema(schema_doc)
                schema.assertValid(xml_doc)
                return []  # válido
            except etree.DocumentInvalid as e:
                errors = [str(err) for err in e.error_log]
            except Exception:
                continue
        return errors

    def sign_xml(self, xml, pkcs12_data, pkcs12_password, doc_id):
        """Assina o XML usando certificado PKCS12."""
        try:
            from erpbrasil.assinatura import assinatura
        except ImportError:
            raise ImportError(
                "Para assinar XML, instale: pip install erpbrasil.assinatura"
            )
        return assinatura.Assinatura(
            pkcs12_data, pkcs12_password
        ).assina_xml2(xml, doc_id)
```

### Nota sobre assinatura

O SIFEN usa assinatura XML com RSA-SHA256 no elemento `<DE>` referenciado pelo atributo `Id` (que é o CDC). A lib de assinatura pode ser reutilizada da `erpbrasil.assinatura` ou adaptada com `signxml`. A assinatura é um **requisito obrigatório** para envio ao SIFEN.

---

## 6. Script de Geração (`script.sh`)

```bash
#!/bin/bash
set -e

echo "=== Gerando bindings do SIFEN ==="

# Documento Electrónico v150
echo "Gerando DE v150..."
xsdata generate pysifen/de/schemas/v150 \
    --package pysifen.de.bindings.v150

echo "=== Bindings gerados com sucesso ==="
```

Para rodar: `chmod +x script.sh && ./script.sh`

---

## 7. Configuração do Projeto (`pyproject.toml`)

```toml
[build-system]
requires = ["setuptools>=45", "wheel"]
build-backend = "setuptools.backends._legacy:_Backend"

[project]
name = "pysifen"
description = "Bindings Python para ler e gerar XML do SIFEN (Paraguay)"
readme = "README.md"
license = "MIT"
requires-python = ">=3.9"
authors = [
    { name = "Seu Nome", email = "seu@email.com" },
]
keywords = [
    "sifen", "factura-electronica", "paraguay", "ekuatia",
    "xml", "xsdata", "documento-electronico", "set",
]
classifiers = [
    "Development Status :: 3 - Alpha",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Topic :: Office/Business :: Financial",
]
dependencies = [
    "xsdata",
]
dynamic = ["version"]

[project.urls]
Homepage = "https://github.com/SEU_USER/pysifen"
Source = "https://github.com/SEU_USER/pysifen"

[project.optional-dependencies]
sign = ["erpbrasil.assinatura"]
soap = ["xsdata[soap]"]
test = [
    "pytest",
    "pytest-cov",
    "xmldiff",
    "pre-commit",
    "lxml",
]

[tool.setuptools]
include-package-data = true

[tool.setuptools.dynamic]
version = {attr = "pysifen.__version__"}

[tool.ruff]
target-version = "py39"

[tool.ruff.lint]
select = ["E", "F", "I", "W"]
```

---

## 8. Plano de Execução em Sprints

### Sprint 0 — Setup Inicial (1-2 dias)

**Objetivo:** Projeto configurado, repositório criado, xsdata instalado.

- [ ] Criar repositório GitHub `pysifen`
- [ ] Criar estrutura de diretórios conforme seção 3
- [ ] Configurar `pyproject.toml`, `.gitignore`, `.pre-commit-config.yaml`
- [ ] Instalar xsdata: `pip install xsdata[cli,lxml]`
- [ ] Criar `.xsdata.xml` com a configuração da seção 4
- [ ] Criar `pysifen/__init__.py` com `__version__`

**Verificação:** `pip install -e .` funciona sem erros.

---

### Sprint 1 — Download e Organização dos XSD (1-2 dias)

**Objetivo:** Todos os XSD oficiais baixados e organizados.

- [ ] Baixar todos os XSD de `https://ekuatia.set.gov.py/sifen/xsd/`
- [ ] Baixar o RAR com a estrutura completa da SET
- [ ] Organizar em `pysifen/de/schemas/v150/`
- [ ] Verificar integridade: todos os `xs:include` e `xs:import` resolvem localmente
- [ ] **Ajustar schemaLocation** nos XSD para usar caminhos relativos locais (os schemas originais referenciam URLs remotas como `https://ekuatia.set.gov.py/sifen/xsd/...` — precisam ser convertidos para caminhos relativos como `./DE_Types_v150.xsd`)
- [ ] Commitar os XSD originais (com ajustes de path) no repositório

**Verificação:** `xmllint --schema pysifen/de/schemas/v150/DE_v150.xsd` valida um XML de exemplo.

**Atenção:** Este é o passo mais crítico. Os XSD da SET podem ter referências cruzadas complexas que precisam ser resolvidas localmente para o xsdata funcionar.

---

### Sprint 2 — Geração dos Bindings (2-3 dias)

**Objetivo:** Bindings Python gerados e importáveis.

- [ ] Criar o `CommonMixin.py` (seção 5)
- [ ] Criar `script.sh` (seção 6)
- [ ] Executar: `xsdata generate pysifen/de/schemas/v150 --package pysifen.de.bindings.v150`
- [ ] Resolver erros de geração (tipos conflitantes, imports circulares, etc.)
- [ ] Ajustar `Substitutions` no `.xsdata.xml` se necessário
- [ ] Verificar que os bindings são importáveis: `from pysifen.de.bindings.v150.de_v150 import Rde`
- [ ] Commitar os bindings gerados

**Verificação:**
```python
from pysifen.de.bindings.v150.de_v150 import Rde
print(Rde.__dataclass_fields__.keys())
```

**Problemas esperados:**
- `xs:include` com URLs absolutas — solução: baixar todos os XSD localmente e ajustar paths
- Tipos com nomes que colidem com palavras reservadas Python — solução: `safePrefix` no xsdata
- Schemas WSDL podem precisar tratamento especial com `xsdata[soap]`

---

### Sprint 3 — Obtenção de XMLs de Exemplo (1-2 dias)

**Objetivo:** Ter XMLs reais ou realistas para testes.

- [ ] Buscar XMLs de exemplo no Manual Técnico do SIFEN
- [ ] Buscar XMLs de teste na jpysifen (repo roshkadev)
- [ ] Buscar XMLs na documentação da FacturaSend
- [ ] Criar XMLs de exemplo "à mão" seguindo o Manual Técnico para cada tipo de DE:
  - Factura Electrónica (tipo 1)
  - Factura Electrónica de Exportación (tipo 2)
  - Factura Electrónica de Importación (tipo 3)
  - Autofactura (tipo 4)
  - Nota de Crédito Electrónica (tipo 5)
  - Nota de Débito Electrónica (tipo 6)
  - Nota de Remisión Electrónica (tipo 7)
  - Comprobante de Retención Electrónico (tipo 8)
- [ ] Salvar em `pysifen/de/samples/v150/`

**Verificação:** Cada XML valida contra o XSD com `xmllint`.

---

### Sprint 4 — Testes de Leitura (parsing) (2-3 dias)

**Objetivo:** Ler qualquer XML do SIFEN e navegar nos objetos Python.

- [ ] Criar `tests/test_de.py` com testes de leitura para cada tipo de DE
- [ ] Testar acesso a campos profundos (ex.: `rde.DE.gDatGralOpe.gOpeCom.iTipTra`)
- [ ] Testar que enums são corretamente mapeados (ex.: `iTipEmi` = 1 ou 2)
- [ ] Testar leitura de campos opcionais (ex.: dados de exportação)
- [ ] Verificar que `from_xml()` e `from_path()` funcionam

**Verificação:** `pytest tests/test_de.py -v` passa.

Exemplo de teste:
```python
def test_read_factura():
    from pysifen.de.bindings.v150.si_recep_de_v150 import Rde
    rde = Rde.from_path("pysifen/de/samples/v150/factura_electronica.xml")
    assert rde.DE.gOpeDE.iTipEmi == "1"
    assert rde.DE.gDatGralOpe.gEmis.dRucEm is not None
```

---

### Sprint 5 — Testes de Escrita (serialização) (2-3 dias)

**Objetivo:** Gerar XML válido do SIFEN a partir de objetos Python.

- [ ] Testar serialização: `rde.to_xml()` produz XML válido
- [ ] Testar round-trip: ler XML → objeto → XML → comparar com original
- [ ] Testar construção de DE do zero:

```python
from pysifen.de.bindings.v150.de_v150 import Rde, TgOpeDE, TgDatGralOpe
rde = Rde(
    dVerFor=150,
    DE=TDE(
        Id="01800695631001001000000312024112917595714694",
        gOpeDE=TgOpeDE(iTipEmi=1),
        gDatGralOpe=TgDatGralOpe(...)
    )
)
xml = rde.to_xml()
```

- [ ] Testar `validate_xml()` — deve retornar lista vazia para XML válido
- [ ] Usar `xmldiff` para comparar XML gerado vs. original

**Verificação:** `pytest tests/ -v` passa 100%.

---

### Sprint 6 — Validação de Schema e Detecção de Atualizações (1 dia)

**Objetivo:** Detectar automaticamente quando a SET publica novos schemas.

- [ ] Criar `tests/test_schema_versions.py` que baixa o index de `https://ekuatia.set.gov.py/sifen/xsd/` e compara com os schemas locais
- [ ] Alertar quando há schemas novos que não existem localmente
- [ ] Configurar no CI para rodar periodicamente

---

### Sprint 7 — Documentação e Publicação (2-3 dias)

**Objetivo:** Projeto publicado e documentado.

- [ ] Escrever README.md completo com exemplos de uso (espelhar formato nfelib)
- [ ] Configurar GitHub Actions para CI (testes + lint)
- [ ] Configurar publicação no PyPI
- [ ] Criar tag de release `v0.1.0`
- [ ] Publicar: `pip install pysifen`

---

### Sprint 8 — Funcionalidades Avançadas (contínuo)

**Objetivo:** Recursos adicionais de valor.

- [ ] **Assinatura digital**: Integrar com `signxml` ou `erpbrasil.assinatura` para assinar o elemento `<DE>` com RSA-SHA256
- [ ] **Geração do CDC**: Implementar helper para gerar o Código de Control do Documento Electrónico (44 dígitos)
- [ ] **Geração do QR Code**: Implementar helper para gerar a URL do QR conforme Manual Técnico seção 13.7.2
- [ ] **Geração do KuDE**: Representação gráfica (PDF) do DTE para receptores não-eletrônicos
- [ ] **Cliente SOAP**: Usando `xsdata[soap]`, gerar bindings para os WSDL dos serviços web da SET
- [ ] **Integração Odoo**: Usando `xsdata-odoo`, gerar modelos abstratos Odoo automaticamente (seguindo a abordagem `akretion/xsdata-odoo`)

---

## 9. Desafios Técnicos Esperados

### 9.1 Resolução de `schemaLocation`

Os XSD da SET referenciam URLs absolutas (`https://ekuatia.set.gov.py/sifen/xsd/...`). É necessário baixar todos localmente e reescrever os `schemaLocation` para paths relativos antes de rodar o xsdata.

**Solução:** Script Python que percorre todos os XSD e substitui:
```python
# Exemplo de ajuste
content = content.replace(
    'schemaLocation="https://ekuatia.set.gov.py/sifen/xsd/',
    'schemaLocation="./'
)
```

### 9.2 Versionamento misto nos schemas

O SIFEN tem schemas em versões diferentes no mesmo "pacote" (DE_Types_v150, SIFEN_Types_v141, Paises_v100). Todos precisam estar na mesma pasta para resolver as dependências.

### 9.3 Nomes de campos em espanhol

Diferente da nfelib (português), os campos do SIFEN estão em espanhol abreviado (ex.: `iTipEmi`, `dDesTipEmi`, `gOpeDE`). Manter `originalCase` é importante para correspondência com o Manual Técnico.

### 9.4 Assinatura XML

O SIFEN exige assinatura enveloped no nó `<DE>` usando o atributo `Id` como referência. Isso é similar à NF-e brasileira, mas com namespace diferente. Pode-se reutilizar lógica de assinatura existente com ajustes mínimos.

### 9.5 Tamanho dos schemas

O `DE_v150.xsd` é um schema muito extenso com dezenas de grupos (gOpeDE, gDatGralOpe, gEmis, gDest, gItDe, etc.), totalizando centenas de campos. Os bindings gerados serão grandes, mas isso é esperado e gerenciado automaticamente pelo xsdata.

---

## 10. API de Uso Esperada (objetivo final)

```python
# === Ler um Documento Electrónico (DE) ===
from pysifen.de.bindings.v150.si_recep_de_v150 import Rde
rde = Rde.from_path("factura.xml")
# ou: rde = Rde.from_xml(xml_string)

# Navegar nos dados
print(rde.DE.gDatGralOpe.gEmis.dRucEm)       # RUC do emissor
print(rde.DE.gDatGralOpe.gEmis.dNomEm)       # Nome do emissor
print(rde.DE.gDtipDE.gCamFE.iIndPres)         # Indicador de presença
print(len(rde.DE.gDtipDE.gCamItem))            # Quantidade de itens

# === Serializar ===
xml = rde.to_xml()

# === Validar ===
errors = rde.validate_xml()
if not errors:
    print("XML válido!")

# === Construir do zero ===
from pysifen.de.bindings.v150.de_v150 import *
de = TDE(
    Id="01800695631001001000000312024112917595714694",
    dDVId=9,
    gOpeDE=TgOpeDE(iTipEmi=1, dDesTipEmi="Normal"),
    gDatGralOpe=TgDatGralOpe(
        dFeEmiDE="2024-11-29T17:59:57",
        gEmis=TgEmis(
            dRucEm="80069563",
            dDVEmi=1,
            iTipCont=1,
            dNomEm="Mi Empresa S.A.",
        ),
    ),
)
rde = Rde(dVerFor=150, DE=de)
print(rde.to_xml())

# === Assinar ===
with open("certificado.pfx", "rb") as f:
    cert_data = f.read()
signed = rde.sign_xml(xml, cert_data, "password", rde.DE.Id)
```

---

## 11. Referências

| Recurso | URL |
|---------|-----|
| XSD oficiais SIFEN | https://ekuatia.set.gov.py/sifen/xsd/ |
| Manual Técnico SIFEN v150 | https://www.dnit.gov.py/documents/20123/420592/Manual+T%C3%A9cnico+Versi%C3%B3n+150.pdf |
| Portal e-Kuatia | https://ekuatia.set.gov.py |
| nfelib (referência) | https://github.com/akretion/nfelib |
| xsdata (gerador de bindings) | https://xsdata.readthedocs.io/ |
| xsdata-odoo (integração Odoo) | https://github.com/akretion/xsdata-odoo |
| jpysifen (lib Java SIFEN) | https://github.com/roshkadev/rshk-jpysifen |
| FacturaSend (API SIFEN) | https://docs.facturasend.com.py/ |

---

## 12. Estimativa de Esforço

| Sprint | Descrição | Esforço |
|--------|-----------|---------|
| 0 | Setup inicial | 1-2 dias |
| 1 | Download e organização dos XSD | 1-2 dias |
| 2 | Geração dos bindings | 2-3 dias |
| 3 | XMLs de exemplo | 1-2 dias |
| 4 | Testes de leitura | 2-3 dias |
| 5 | Testes de escrita | 2-3 dias |
| 6 | Detecção de atualizações | 1 dia |
| 7 | Documentação e publicação | 2-3 dias |
| **Total MVP** | **Sprints 0-7** | **~12-19 dias úteis** |
| 8 | Funcionalidades avançadas | Contínuo |

O MVP (ler, escrever e validar XML do SIFEN) pode estar pronto em **2-3 semanas** de trabalho focado, com funcionalidades avançadas (assinatura, QR, KuDE, cliente SOAP) sendo adicionadas incrementalmente.
