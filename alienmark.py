"""
AlienMark - Convertidor de Documentos a Markdown
Creado por Cristian Novoa - DMT Consultora

Convierte PDF, Word, Excel, PowerPoint, imagenes, HTML y mas a formato Markdown.
Basado en Microsoft MarkItDown.

Uso:
  - Doble clic: Abre un selector de archivos para elegir que convertir.
  - Arrastrar archivos: Arrastra 1 o mas archivos encima del icono de AlienMark.
"""
import sys
import os
import time

__version__ = "1.0.0"
__author__ = "Cristian Novoa - DMT Consultora"

BANNER = r"""
     _    _ _            __  __            _    
    / \  | (_) ___ _ __ |  \/  | __ _ _ __| | __
   / _ \ | | |/ _ \ '_ \| |\/| |/ _` | '__| |/ /
  / ___ \| | |  __/ | | | |  | | (_| | |  |   < 
 /_/   \_\_|_|\___|_| |_|_|  |_|\__,_|_|  |_|\_\
"""

SUPPORTED_EXTENSIONS = (
    ".pdf", ".docx", ".xlsx", ".xls", ".pptx",
    ".html", ".htm", ".csv", ".json", ".xml",
    ".jpg", ".jpeg", ".png", ".gif", ".bmp",
    ".wav", ".mp3", ".epub", ".zip", ".msg",
    ".txt", ".md", ".rst", ".rtf",
)


def print_header(total=None):
    """Muestra el banner de AlienMark."""
    print(BANNER)
    print(f"  Version {__version__}")
    print(f"  {__author__}")
    print()
    if total and total > 1:
        print(f"  Conversion Masiva - {total} archivos")
    else:
        print("  Convertidor de Documentos a Markdown")
    print("  ========================================================")
    print()


def select_files_dialog():
    """Abre un cuadro de dialogo de Windows para seleccionar archivos."""
    import tkinter as tk
    from tkinter import filedialog

    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)
    root.update()

    files = filedialog.askopenfilenames(
        title="AlienMark - Selecciona archivos para convertir a Markdown",
        filetypes=[
            ("Todos los soportados",
             "*.pdf;*.docx;*.xlsx;*.xls;*.pptx;"
             "*.html;*.htm;*.csv;*.json;*.xml;"
             "*.jpg;*.jpeg;*.png;*.gif;*.bmp;"
             "*.wav;*.mp3;*.epub;*.zip;*.msg;"
             "*.txt;*.rst;*.rtf"),
            ("PDF", "*.pdf"),
            ("Word", "*.docx"),
            ("Excel", "*.xlsx;*.xls"),
            ("PowerPoint", "*.pptx"),
            ("HTML", "*.html;*.htm"),
            ("Imagenes", "*.jpg;*.jpeg;*.png;*.gif;*.bmp"),
            ("Audio", "*.wav;*.mp3"),
            ("Todos los archivos", "*.*"),
        ]
    )
    root.destroy()
    return list(files)


def convert_file(md, input_file, output_file):
    """Convierte un archivo a Markdown y lo guarda."""
    try:
        result = md.convert(input_file)
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(result.text_content)
        return True, None
    except Exception as e:
        return False, str(e)


def main():
    # Recoger archivos desde argumentos (drag & drop) o selector
    files = [f for f in sys.argv[1:] if os.path.exists(f)]

    if not files:
        print("\n  Abriendo selector de archivos...")
        files = select_files_dialog()

    if not files:
        print("\n  No se selecciono ningun archivo.")
        time.sleep(2)
        return

    # Filtrar archivos validos
    valid_files = []
    skipped = []
    for f in files:
        if os.path.exists(f):
            valid_files.append(f)
        else:
            skipped.append(f)

    if not valid_files:
        print("\n  [!] Ningun archivo valido encontrado.")
        input("\n  Presiona ENTER para cerrar...")
        return

    total = len(valid_files)
    is_batch = total > 1

    # Header
    print_header(total)

    # Crear convertidor (una sola instancia reutilizable)
    from markitdown import MarkItDown
    md = MarkItDown(enable_plugins=False)
    print("  Modo: Conversion local")
    print()

    # Informar archivos omitidos
    for s in skipped:
        print(f"  [!] Omitido (no encontrado): {s}")
    if skipped:
        print()

    # Convertir archivos
    exitosos = 0
    fallidos = 0
    resultados = []
    start_total = time.time()

    for i, input_file in enumerate(valid_files, 1):
        base_name = os.path.splitext(input_file)[0]
        output_file = base_name + ".md"
        file_name = os.path.basename(input_file)

        if is_batch:
            print(f"  [{i}/{total}] {file_name}", end="", flush=True)
        else:
            print(f"  Convirtiendo: {file_name}")

        start = time.time()
        success, error = convert_file(md, input_file, output_file)
        elapsed = time.time() - start

        if success:
            exitosos += 1
            resultados.append((file_name, "OK", f"{elapsed:.1f}s", output_file))
            if is_batch:
                print(f" ... OK ({elapsed:.1f}s)")
            else:
                print()
                print("  ========================================================")
                print("        Conversion exitosa!")
                print("  ========================================================")
                print()
                print(f"  Guardado en: {output_file}")
        else:
            fallidos += 1
            resultados.append((file_name, "ERROR", error, None))
            if is_batch:
                print(f" ... ERROR")
                print(f"         {error}")
            else:
                print(f"\n  [ERROR] {error}")

    elapsed_total = time.time() - start_total

    # Resumen
    print()
    if is_batch:
        print("  ========================================================")
        print("        RESUMEN")
        print("  ========================================================")
        print()
        print(f"  Total:    {total} archivos")
        print(f"  Exitosos: {exitosos}")
        if fallidos > 0:
            print(f"  Fallidos: {fallidos}")
        print(f"  Tiempo:   {elapsed_total:.1f}s")
        print()
        print("  --------------------------------------------------------")
        for nombre, estado, detalle, _ in resultados:
            icono = "+" if estado == "OK" else "X"
            print(f"  [{icono}] {nombre} - {detalle}")
        print("  --------------------------------------------------------")
        print()
        print("  Los archivos .md se guardaron junto a los originales.")
    else:
        # Si fue un solo archivo exitoso, abrirlo
        if exitosos > 0 and resultados[0][3]:
            print()
            print("  Abriendo archivo convertido...")
            try:
                os.startfile(resultados[0][3])
            except Exception:
                pass

    print()
    print(f"  AlienMark v{__version__} - {__author__}")
    print()
    input("  Presiona ENTER para cerrar...")


if __name__ == "__main__":
    main()
