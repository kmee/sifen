#!/bin/bash
set -e

echo "=== Gerando bindings do SIFEN ==="

# Documento Electrónico v150
echo "Gerando DE v150..."
xsdata generate pysifen/de/schemas/v150 \
    --package pysifen.de.bindings.v150

echo "=== Bindings gerados com sucesso ==="
