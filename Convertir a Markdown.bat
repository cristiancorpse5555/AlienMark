@echo off
setlocal enabledelayedexpansion
title MarkItDown - Convertidor a Markdown

echo.
echo  ========================================================
echo        MarkItDown - Convertidor a Markdown
echo   Convierte PDF, Word, Excel, PowerPoint y mas
echo  ========================================================
echo.

REM Verificar si se arrastro un archivo
if "%~1"=="" (
    echo  [!] No arrastraste ningun archivo.
    echo.
    echo  --------------------------------------------------------
    echo   COMO USAR:
    echo  --------------------------------------------------------
    echo.
    echo   1. Arrastra cualquier archivo encima de:
    echo.
    echo      "Convertir a Markdown.bat"     - Conversion basica
    echo      "Convertir con Gemini AI.bat"  - Usa IA para imagenes
    echo.
    echo   2. El archivo convertido se guardara en la misma
    echo      carpeta del archivo original, con extension .md
    echo.
    echo   Formatos soportados:
    echo     - PDF, Word, Excel, PowerPoint
    echo     - Imagenes, Audio, HTML, CSV, JSON
    echo     - Y muchos mas...
    echo.
    echo  --------------------------------------------------------
    echo.
    pause
    exit /b
)

echo  Archivo recibido: "%~nx1"
echo  Procesando...
echo.

REM Ejecutar el script de Python
"%~dp0.venv\Scripts\python.exe" "%~dp0convertir.py" "%~1"

echo.
echo  --------------------------------------------------------
echo  Presiona cualquier tecla para cerrar esta ventana...
echo  --------------------------------------------------------
pause >nul
