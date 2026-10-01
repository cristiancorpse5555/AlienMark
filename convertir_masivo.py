"""
MarkItDown - Conversion Masiva
Abre una ventana para seleccionar multiples archivos y los convierte todos.
"""
import sys
import os
import tkinter as tk
from tkinter import filedialog

def main():
    # Si se pasaron archivos como argumentos, usarlos directamente
    files_from_args = [f for f in sys.argv[1:] if f != "--ai" and os.path.exists(f)]

    if files_from_args:
        files = files_from_args
    else:
        # Abrir dialogo para seleccionar archivos
        root = tk.Tk()
        root.withdraw()
        root.attributes('-topmost', True)

        files = filedialog.askopenfilenames(
            title="Selecciona los archivos a convertir a Markdown",
            filetypes=[
                ("Todos los soportados", "*.pdf;*.docx;*.xlsx;*.xls;*.pptx;*.html;*.htm;*.csv;*.json;*.xml;*.jpg;*.jpeg;*.png;*.gif;*.bmp;*.wav;*.mp3;*.epub;*.zip"),
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

        if not files:
            print("\n  No se seleccionaron archivos.")
            return

    # Construir comando con todos los archivos
    use_ai = "--ai" in sys.argv
    script_dir = os.path.dirname(os.path.abspath(__file__))
    convertir_script = os.path.join(script_dir, "convertir.py")

    args = [sys.executable, convertir_script] + list(files)
    if use_ai:
        args.append("--ai")

    import subprocess
    subprocess.call(args)

    print()
    input("  Presiona ENTER para cerrar...")

if __name__ == "__main__":
    main()
