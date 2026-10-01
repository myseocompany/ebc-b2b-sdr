#!/usr/bin/env bash
set -euo pipefail

required=(AGENTS.md SOUL.md MYSEO.md POLICIES.md MEMORY.md SOURCES.md TASKS.md DECISIONS.md README.md)
for file in "${required[@]}"; do
  if [[ ! -s "$file" ]]; then
    echo "Falta archivo requerido o está vacío: $file" >&2
    exit 1
  fi
done

required_dirs=(context clients workflows templates progress evals)
for dir in "${required_dirs[@]}"; do
  if [[ ! -d "$dir" ]]; then
    echo "Falta directorio requerido: $dir" >&2
    exit 1
  fi
done

if [[ $(wc -l < AGENTS.md) -gt 200 ]]; then
  echo "AGENTS.md supera 200 líneas; mover detalle a archivos bajo demanda." >&2
  exit 1
fi

echo "MySEO harness: estructura base válida."
