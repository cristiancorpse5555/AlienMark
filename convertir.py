"""
MarkItDown - Convertidor inteligente a Markdown
Usa Gemini Flash para describir imagenes y mejorar conversiones.
Soporta conversion individual y masiva (drag & drop o selector de archivos).
"""
import sys
import os
import time

def load_config():
    """Carga la API key y modelo desde config.txt"""
    config_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config.txt")
    config = {}
    if os.path.exists(config_path):
        with open(config_path, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if "=" in line and not line.startswith("#"):
                    key, value = line.split("=", 1)
                    config[key.strip()] = value.strip()
    return config

def create_converter(use_ai=False):
    """Crea una instancia del convertidor (reutilizable para multiples archivos)."""
    from markitdown import MarkItDown

    config = load_config()
    api_key = config.get("GEMINI_API_KEY", "")
    model = config.get("GEMINI_MODEL", "gemini-3.6-flash")

    if use_ai and api_key and api_key != "PEGA_TU_API_KEY_AQUI":
        from openai import OpenAI

        client = OpenAI(
            api_key=api_key,
            base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
        )
        md = MarkItDown(
            llm_client=client,
            llm_model=model,
            enable_plugins=False
        )
        print(f"  Modo: IA activada (Gemini {model})")
    else:
        md = MarkItDown(enable_plugins=False)
        if use_ai:
            if not api_key or api_key == "PEGA_TU_API_KEY_AQUI":
                print("  [!] API key no configurada. Usando modo basico.")
                print("      Edita config.txt para agregar tu API key de Google AI Studio.")
        print("  Modo: Conversion local (sin IA)")

    return md

def convert_file(md, input_file, output_file):
    """Convierte un archivo a Markdown."""
    try:
        result = md.convert(input_file)
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(result.text_content)
        return True, None
    except Exception as e:
        return False, str(e)

def select_files_dialog(use_ai=False):
    """Abre un cuadro de dialogo para seleccionar uno o varios archivos si no se arrastro ninguno."""
    import tkinter as tk
    from tkinter import filedialog

    root = tk.Tk()
    root.withdraw()
    root.attributes('-topmost', True)

    title = "Selecciona archivos a convertir a Markdown (Gemini AI)" if use_ai else "Selecciona archivos a convertir a Markdown"
    
    files = filedialog.askopenfilenames(
        title=title,
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
    return list(files)

if __name__ == "__main__":
    use_ai = "--ai" in sys.argv
    files = [f for f in sys.argv[1:] if f != "--ai"]

    # Si no se arrastraron archivos, abrir selector de archivos
    if not files:
        print("\n  No se especificaron archivos. Abriendo selector...")
        files = select_files_dialog(use_ai)

    # Filtrar archivos validos
    valid_files = []
    for f in files:
        if os.path.exists(f):
            valid_files.append(f)
        else:
            print(f"  [!] No encontrado, se omite: {f}")

    if not valid_files:
        print("\n  [!] No se selecciono ningun archivo valido.")
        time.sleep(2)
        sys.exit(0)

    total = len(valid_files)
    is_batch = total > 1

    print()
    print("  ========================================================")
    if is_batch:
        modo_str = " (Con Gemini 3.6 Flash)" if use_ai else ""
        print(f"   MarkItDown - Conversion Masiva ({total} archivos){modo_str}")
    else:
        modo_str = " (Gemini AI)" if use_ai else ""
        print(f"        MarkItDown - Convertidor a Markdown{modo_str}")
    print("  ========================================================")
    print()

    # Crear convertidor una sola vez (reutilizable)
    md = create_converter(use_ai)
    print()

    exitosos = 0
    fallidos = 0
    resultados = []
    start_total = time.time()

    for i, input_file in enumerate(valid_files, 1):
        base_name = os.path.splitext(input_file)[0]
        output_file = base_name + ".md"
        file_name = os.path.basename(input_file)

        if is_batch:
            print(f"  [{i}/{total}] {file_name}")
        else:
            print(f"  Convirtiendo: {file_name}")

        start = time.time()
        success, error = convert_file(md, input_file, output_file)
        elapsed = time.time() - start

        if success:
            exitosos += 1
            resultados.append((file_name, "OK", f"{elapsed:.1f}s"))
            if is_batch:
                print(f"         OK ({elapsed:.1f}s)")
            else:
                print()
                print("  ========================================================")
                print("        Conversion exitosa!")
                print("  ========================================================")
                print()
                print(f"  Archivo guardado en:")
                print(f"  {output_file}")
        else:
            fallidos += 1
            resultados.append((file_name, "ERROR", error))
            print(f"         ERROR: {error}")

    elapsed_total = time.time() - start_total

    # Resumen final
    if is_batch:
        print()
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
        for nombre, estado, detalle in resultados:
            icono = "+" if estado == "OK" else "X"
            print(f"  [{icono}] {nombre} - {detalle}")
        print("  --------------------------------------------------------")
        print()
        print(f"  Los archivos .md se guardaron junto a los originales.")
    else:
        if exitosos > 0:
            print()
            print("  Abriendo archivo...")
            try:
                os.startfile(output_file)
            except Exception:
                pass

    print()
    input("  Presiona ENTER para cerrar...")
