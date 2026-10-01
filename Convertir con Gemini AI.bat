@echo off
setlocal

REM === LOG DE DIAGNOSTICO ===
set "LOGFILE=%~dp0ultimo_log.txt"

echo ======================================== > "%LOGFILE%"
echo DIAGNOSTICO MarkItDown >> "%LOGFILE%"
echo Fecha: %date% %time% >> "%LOGFILE%"
echo ======================================== >> "%LOGFILE%"
echo. >> "%LOGFILE%"
echo Argumento recibido raw: %1 >> "%LOGFILE%"
echo Argumento recibido limpio: %~1 >> "%LOGFILE%"
echo Nombre archivo: %~nx1 >> "%LOGFILE%"
echo Ruta del bat: %~dp0 >> "%LOGFILE%"
echo. >> "%LOGFILE%"

title MarkItDown + Gemini AI - Convertidor Inteligente

echo.
echo  ========================================================
echo        MarkItDown + Gemini AI
echo   Conversion inteligente con IA para imagenes y mas
echo  ========================================================
echo.

REM Verificar si se arrastro un archivo
if "%~1"=="" (
    echo  [!] No arrastraste ningun archivo.
    echo SIN ARCHIVO - no se recibio argumento >> "%LOGFILE%"
    echo.
    echo  Arrastra un archivo encima de este icono para convertirlo.
    echo.
    pause
    exit /b
)

echo  Archivo recibido: "%~nx1"
echo  Procesando...
echo.

echo Ejecutando Python... >> "%LOGFILE%"
echo Comando: "%~dp0.venv\Scripts\python.exe" "%~dp0convertir.py" "%~1" --ai >> "%LOGFILE%"
echo. >> "%LOGFILE%"

REM Ejecutar el script de Python con IA activada
"%~dp0.venv\Scripts\python.exe" "%~dp0convertir.py" "%~1" --ai 2>> "%LOGFILE%"

echo. >> "%LOGFILE%"
echo Codigo de salida: %ERRORLEVEL% >> "%LOGFILE%"

echo.
echo  --------------------------------------------------------
echo  Presiona cualquier tecla para cerrar esta ventana...
echo  --------------------------------------------------------
pause >nul
