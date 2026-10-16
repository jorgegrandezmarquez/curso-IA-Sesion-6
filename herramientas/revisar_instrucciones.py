"""Revisa context/*.md y avisa si alguna línea contiene "ignora las reglas" (gratis, sin IA).

Uso:
    python herramientas/revisar_instrucciones.py
    python herramientas/revisar_instrucciones.py otra_carpeta
"""
import sys
from pathlib import Path

FRASE = "ignora las reglas"


def revisar(texto):
    return [
        (n, linea.strip())
        for n, linea in enumerate(texto.splitlines(), 1)
        if FRASE in " ".join(linea.lower().split())
    ]


def main():
    carpeta = Path(sys.argv[1] if len(sys.argv) > 1 else "context")
    total = 0
    for archivo in sorted(carpeta.glob("*.md")):
        for n, linea in revisar(archivo.read_text(encoding="utf8")):
            total += 1
            print(f"AVISO {archivo.name}, línea {n}: {linea}")
    if total:
        print(f'\nSe encontraron {total} línea(s) con la frase "{FRASE}". Revísalas antes de publicar.')
        return 1
    print(f'Bien: ningún documento de {carpeta} contiene "{FRASE}".')
    return 0


if __name__ == "__main__":
    sys.exit(main())
