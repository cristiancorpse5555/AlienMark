<p align="center">
  <img src="assets/icon/AlienMark-256.png" alt="AlienMark" width="120"/>
</p>

<h1 align="center">AlienMark</h1>

<p align="center">
  <b>Convert PDF, Word, Excel, PowerPoint and more to Markdown in one click. Free, on your PC, no internet needed.</b><br/>
  Perfect for feeding documents to ChatGPT, Claude or Gemini, or keeping them in Obsidian or Notion.
</p>

<p align="center">
  <a href="README.md">🇪🇸 Español</a> · 🇬🇧 English
</p>

<p align="center">
  <a href="https://github.com/cristiancorpse5555/AlienMark/releases/latest"><img alt="Download" src="https://img.shields.io/github/v/release/cristiancorpse5555/AlienMark?label=download&color=2ea44f"/></a>
  <img alt="Windows" src="https://img.shields.io/badge/Windows-10%20%7C%2011-0078D6"/>
  <a href="LICENSE"><img alt="MIT License" src="https://img.shields.io/badge/license-MIT-blue"/></a>
</p>

---

## What does it do?

AlienMark takes your documents and converts them to **Markdown** (`.md`): clean text that keeps headings, lists and
tables. It's the format AI assistants and note-taking apps understand best.

- 📄 **PDF, Word (`.docx`), Excel (`.xlsx`, `.xls`), PowerPoint (`.pptx`)**
- 🌐 **HTML, CSV, JSON, XML, EPUB, Outlook (`.msg`)**, and **`.zip`** files (converts what's inside)
- 🖼️ **Images** (extracts their metadata)
- 📚 **Many files at once:** select or drag in dozens of files and they're converted in a queue, with a final summary.
- 🔒 **100% local:** your documents never leave your PC.
- 🛡️ **Never overwrites your files:** if `report.md` already exists, it saves `report (2).md`.

Built on **[Microsoft MarkItDown](https://github.com/microsoft/markitdown)**.

> [!NOTE]
> AlienMark's messages are in **Spanish**, but it converts documents in any language.

## 📥 Installation (for anyone)

1. Go to **[Downloads (Releases)](https://github.com/cristiancorpse5555/AlienMark/releases/latest)** and download
   **`AlienMark_Setup_v1.1.0.exe`** (under *Assets*).
2. Double-click the downloaded file.
3. **If Windows shows "Windows protected your PC"** (this happens with new programs that haven't bought a code-signing
   certificate): click **"More info"** and then **"Run anyway"**.
4. Follow the wizard (*Next → Install*). Tick **"Create a desktop shortcut"**: it's the handiest way to use it.

You don't need to install Python or anything else. **Requirements:** 64-bit Windows 10 or 11.

## 🚀 How to use it

**Option 1 — Drag and drop (fastest)**
Drag one or more files **onto the AlienMark icon** on your Desktop.

**Option 2 — Pick files**
Double-click AlienMark, choose the files in the window (hold `Ctrl` to select several) and click **Open**.

**Where's the result?**
The `.md` is saved **in the same folder as the original**, with the same name. If you convert a single file, it opens
automatically when done. To view it you can use Notepad, VS Code, Obsidian, or just drag it into an AI chat.

## 🛠️ Troubleshooting

| Problem | Solution |
|---|---|
| A PDF comes out empty or nearly empty | It's a **scanned** PDF (a photo of paper): there's no text to extract. Run it through OCR first. |
| `[ERROR]` on a file | It may be damaged, password-protected or open in another program. Close it and try again. |
| The black window closes too fast | That's normal: at the end it waits for you to press **ENTER**. If it closed by itself, run it again and read the message. |

## 👩‍💻 For developers

Built with **Python 3.13** on top of [MarkItDown](https://github.com/microsoft/markitdown).

```bash
git clone https://github.com/cristiancorpse5555/AlienMark.git
cd AlienMark
py -3.13 -m venv .venv
.venv\Scripts\pip install -r requirements.txt
.venv\Scripts\python alienmark.py file.pdf
```

### AI mode (optional, from source)
`convertir.py` can use **Google Gemini** to describe images and better understand tables and diagrams:

1. Get your free key → **[step-by-step guide](docs/GET_API_KEY.md)**.
2. Copy `config.example.txt` to `config.txt` and paste the key after `GEMINI_API_KEY=`.
3. Run `python convertir.py file.pdf --ai`, or drag files onto **`Convertir con Gemini AI.bat`**.

In this mode the content **is sent to Google** for analysis. The installer only uses local mode.

### Build the installer
```bash
.venv\Scripts\pyinstaller --onedir --console --name AlienMark --icon assets/icon/AlienMark.ico --version-file version_info.py --distpath dist\AlienMark_dir_parent --collect-all magika --collect-all markitdown --clean --noconfirm alienmark.py
iscc alienmark_installer.iss
```
Requires [Inno Setup 6](https://jrsoftware.org/isinfo.php). Output: `dist\AlienMark_Setup_v1.1.0.exe`.

Found a bug or have an idea? Open an **[Issue](https://github.com/cristiancorpse5555/AlienMark/issues)** (English or
Spanish). Pull requests are welcome.

## 📄 License

Code under the **[MIT](LICENSE)** license © 2026 DMT Consultora. Third-party components in
[`THIRD_PARTY_NOTICES.md`](THIRD_PARTY_NOTICES.md). Not affiliated with Microsoft or Google.
