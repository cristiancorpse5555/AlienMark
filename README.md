<p align="center">
  <img src="assets/icon/AlienMark-256.png" alt="AlienMark" width="120"/>
</p>

<h1 align="center">AlienMark</h1>

<p align="center">
  <b>Convierte PDF, Word, Excel, PowerPoint y más a Markdown con un clic. Gratis, en tu PC y sin internet.</b><br/>
  Ideal para darle documentos a ChatGPT, Claude o Gemini, o para guardarlos en Obsidian o Notion.
</p>

<p align="center">
  <a href="https://github.com/cristiancorpse5555/AlienMark/releases/latest"><img alt="Descargar" src="https://img.shields.io/github/v/release/cristiancorpse5555/AlienMark?label=descargar&color=2ea44f"/></a>
  <img alt="Windows" src="https://img.shields.io/badge/Windows-10%20%7C%2011-0078D6"/>
  <a href="LICENSE"><img alt="Licencia MIT" src="https://img.shields.io/badge/licencia-MIT-blue"/></a>
</p>

---

## ¿Qué hace?

AlienMark toma tus documentos y los convierte a **Markdown** (`.md`): texto limpio que conserva títulos, listas y tablas.
Es el formato que mejor entienden las inteligencias artificiales y las apps de notas.

- 📄 **PDF, Word (`.docx`), Excel (`.xlsx`, `.xls`), PowerPoint (`.pptx`)**
- 🌐 **HTML, CSV, JSON, XML, EPUB, Outlook (`.msg`)**, archivos **`.zip`** (convierte lo que tengan dentro)
- 🖼️ **Imágenes** (extrae sus metadatos)
- 📚 **Varios archivos a la vez:** selecciona o arrastra hasta decenas de archivos y los convierte en cola, con resumen final.
- 🔒 **100% local:** los documentos no salen de tu PC.
- 🛡️ **Nunca sobrescribe tus archivos:** si ya existe `informe.md`, guarda `informe (2).md`.

Basado en **[Microsoft MarkItDown](https://github.com/microsoft/markitdown)**.

## 📥 Instalación (para cualquier persona)

1. Ve a **[Descargas (Releases)](https://github.com/cristiancorpse5555/AlienMark/releases/latest)** y descarga
   **`AlienMark_Setup_v1.1.0.exe`** (en la sección *Assets*).
2. Haz doble clic en el archivo descargado.
3. **Si Windows muestra "Windows protegió su PC"** (pasa con programas nuevos que no compraron un certificado de firma):
   pulsa **"Más información"** y luego **"Ejecutar de todas formas"**.
4. Sigue el asistente (*Siguiente → Instalar*). Marca **"Crear un acceso directo en el Escritorio"**: es la forma más
   cómoda de usarlo.

No necesitas instalar Python ni nada más. **Requisitos:** Windows 10 u 11 de 64 bits.

## 🚀 Cómo se usa

**Opción 1 — Arrastrar y soltar (la más rápida)**
Arrastra uno o varios archivos **encima del ícono de AlienMark** en el Escritorio.

**Opción 2 — Elegir archivos**
Haz doble clic en AlienMark, elige los archivos en la ventana (puedes marcar varios con `Ctrl`) y pulsa **Abrir**.

**¿Dónde queda el resultado?**
El `.md` se guarda **en la misma carpeta que el original**, con el mismo nombre. Si conviertes un solo archivo, se abre
solo al terminar. Para verlo con formato puedes usar el Bloc de notas, VS Code, Obsidian o arrastrarlo a un chat de IA.

## 🛠️ Solución de problemas

| Problema | Solución |
|---|---|
| Un PDF sale vacío o casi vacío | Es un PDF **escaneado** (una foto de papel): no tiene texto que extraer. Pásalo antes por un OCR. |
| `[ERROR]` con un archivo | Puede estar dañado, protegido con contraseña o abierto en otro programa. Ciérralo y reintenta. |
| La ventana negra se cierra muy rápido | Es normal: al final espera que pulses **ENTER**. Si se cerró sola, ejecútala de nuevo y lee el mensaje. |

## 👩‍💻 Para desarrolladores

Hecho en **Python 3.13** sobre [MarkItDown](https://github.com/microsoft/markitdown).

```bash
git clone https://github.com/cristiancorpse5555/AlienMark.git
cd AlienMark
py -3.13 -m venv .venv
.venv\Scripts\pip install -r requirements.txt
.venv\Scripts\python alienmark.py archivo.pdf
```

### Modo con IA (opcional, desde el código)
`convertir.py` puede usar **Google Gemini** para describir imágenes y entender mejor tablas y diagramas:

1. Consigue tu clave gratis → **[guía paso a paso](docs/OBTENER_API_KEY.md)**.
2. Copia `config.example.txt` como `config.txt` y pega la clave en `GEMINI_API_KEY=`.
3. Ejecuta `python convertir.py archivo.pdf --ai`, o arrastra archivos sobre **`Convertir con Gemini AI.bat`**.

En este modo el contenido **sí se envía a Google** para analizarlo. El instalador usa solo el modo local.

### Generar el instalador
```bash
.venv\Scripts\pyinstaller --onedir --console --name AlienMark --icon assets/icon/AlienMark.ico --version-file version_info.py --distpath dist\AlienMark_dir_parent --collect-all magika --collect-all markitdown --clean --noconfirm alienmark.py
iscc alienmark_installer.iss
```
Requiere [Inno Setup 6](https://jrsoftware.org/isinfo.php). Resultado: `dist\AlienMark_Setup_v1.1.0.exe`.

¿Encontraste un error o tienes una idea? Abre un **[Issue](https://github.com/cristiancorpse5555/AlienMark/issues)**.
Las contribuciones (*pull requests*) son bienvenidas.

## 📄 Licencia

Código bajo licencia **[MIT](LICENSE)** © 2026 DMT Consultora. Componentes de terceros en
[`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md). No está afiliado a Microsoft ni a Google.
