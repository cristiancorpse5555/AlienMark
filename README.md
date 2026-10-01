# 👽 AlienMark

> **Convertidor de Documentos a Markdown para Windows**  
> *Desarrollado por **Cristian Novoa — DMT Consultora***  
> Basado en la tecnología de **Microsoft MarkItDown**.

<p align="center">
  <img src="assets/icon/AlienMark-256.png" alt="AlienMark Logo" width="160"/>
</p>

---

## 📌 ¿Qué es AlienMark?

**AlienMark** es una herramienta de escritorio diseñada para convertir documentos de múltiples formatos a Markdown (`.md`) limpio, estructurado y listo para usar en bases de conocimiento, modelos LLM, Obsidian, Notion o archivado digital.

Incluye dos modalidades:
1. **Conversión Local Ultrarrápida:** 100% offline, privada y sin costo alguno.
2. **Conversión Potenciada por IA (Opcional):** Integrada con Google Gemini (Flash) para describir imágenes y procesar tablas o diagramas complejos dentro de documentos.

---

## ✨ Características Principales

- **Doble modo de ejecución:**
  - **Arrastrar y Soltar (Drag & Drop):** Arrastra 1 o hasta 50 archivos simultáneamente sobre el ejecutable.
  - **Selector Visual:** Al hacer doble clic sobre la aplicación, se despliega una ventana de Windows para explorar carpetas y elegir los archivos.
- **Conversión Masiva en Cola:** Procesa múltiples documentos consecutivamente mostrando una barra de progreso (`[1/10]`, `[2/10]...`) y un resumen final con tiempos de ejecución.
- **Formatos Compatibles:**
  - Documentos: PDF, Word (`.docx`), Rich Text (`.rtf`, `.txt`).
  - Hojas de Cálculo: Excel (`.xlsx`, `.xls`), CSV.
  - Presentaciones: PowerPoint (`.pptx`).
  - Web & Datos: HTML, JSON, XML.
  - Multimedia: Imágenes (`.jpg`, `.png`, `.bmp`), Audio (`.wav`, `.mp3`).
  - Archivos Comprimidos: `.zip`.
- **Distribuible:** Se puede compilar como un `.exe` portable independiente o como instalador oficial (`Setup.exe`) con Inno Setup.

---

## 🚀 Uso Rápido (Desde Código Fuente)

### 1. Clonar el repositorio
```bash
git clone https://github.com/cristiancorpse5555/AlienMark.git
cd AlienMark
```

### 2. Crear entorno virtual e instalar dependencias
```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

*(O instalar directamente `pip install "markitdown[all]" openai Pillow pyinstaller`)*

### 3. Configuración de IA (Opcional)
Si deseas usar la conversión con Gemini:
1. Copia `config.example.txt` como `config.txt`:
   ```bash
   copy config.example.txt config.txt
   ```
2. Añade tu API Key de **Google AI Studio** en `config.txt`.

### 4. Ejecución
- **Modo Local:**
  ```bash
  python alienmark.py archivo.pdf
  ```
- **Modo IA con Gemini:**
  ```bash
  python convertir.py archivo.pdf --ai
  ```

---

## 🛠️ Compilación de Ejecutables (.exe)

Para generar la versión portable y el instalador:

### Versión Portable (un solo archivo `.exe`):
```bash
pyinstaller --onefile --console --name AlienMark --icon assets/icon/AlienMark.ico --version-file version_info.py --collect-all magika --collect-all markitdown --clean --noconfirm alienmark.py
```

### Versión Instalador (Inno Setup):
1. Compilar primero en modo carpeta:
   ```bash
   pyinstaller --onedir --console --name AlienMark --icon assets/icon/AlienMark.ico --version-file version_info.py --distpath dist\AlienMark_dir_parent --collect-all magika --collect-all markitdown --noconfirm alienmark.py
   ```
2. Compilar el instalador con Inno Setup:
   ```bash
   iscc alienmark_installer.iss
   ```

---

## 👤 Autor

* **Cristian Novoa**  
* **DMT Consultora**  

---

## 📄 Licencia

Este proyecto utiliza componentes de [Microsoft MarkItDown](https://github.com/microsoft/markitdown) bajo la licencia MIT.
