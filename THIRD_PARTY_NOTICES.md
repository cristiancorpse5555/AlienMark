# Componentes de terceros

AlienMark se distribuye bajo la licencia MIT (ver `LICENSE`). El instalador de Windows incluye los siguientes componentes
de terceros, cada uno bajo su propia licencia:

| Componente | Uso en AlienMark | Licencia | Sitio |
|---|---|---|---|
| **Microsoft MarkItDown** | Motor de conversión a Markdown | MIT | <https://github.com/microsoft/markitdown> |
| **Magika** (Google) | Detección del tipo de archivo | Apache 2.0 | <https://github.com/google/magika> |
| **pdfminer.six**, **mammoth**, **python-pptx**, **openpyxl**, **pandas** y otras dependencias de MarkItDown | Lectura de PDF, Word, PowerPoint y Excel | MIT / BSD / Apache 2.0 | ver cada paquete |
| **ONNX Runtime** (Microsoft) | Modelo de Magika | MIT | <https://github.com/microsoft/onnxruntime> |
| **Python** y **Tcl/Tk** | Intérprete y selector de archivos | PSF / BSD | <https://www.python.org> |

Las licencias de los paquetes de Python se incluyen en la carpeta de instalación (`_internal`).
