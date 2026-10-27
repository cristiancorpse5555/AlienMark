# 🔑 Cómo obtener tu clave de Google Gemini (paso a paso)

El modo con IA de AlienMark usa **Gemini** de Google para describir imágenes y entender tablas y diagramas. Para eso
necesita una **clave de API**: un código largo que identifica tu cuenta. Es **gratis** para un uso normal y toma unos
3 minutos.

> El AlienMark del instalador **no la necesita**: convierte sin IA. La clave solo hace falta para el modo con IA, que se
> usa desde el código fuente.

> No necesitas tarjeta de crédito ni saber programar. Solo una cuenta de Google (la misma de Gmail).

---

## Paso 1 · Entra a Google AI Studio

1. Abre tu navegador (Chrome, Edge, etc.).
2. Ve a: **<https://aistudio.google.com/apikey>**
3. Si te lo pide, **inicia sesión** con tu cuenta de Google.

## Paso 2 · Acepta las condiciones (solo la primera vez)

La primera vez aparece una ventana con los términos de servicio de Google AI Studio.
Marca la casilla de aceptación y pulsa **Continuar**.

## Paso 3 · Crea la clave

1. Pulsa el botón **"Crear clave de API"** (*"Create API key"* si tu cuenta está en inglés).
2. Si te pregunta por un **proyecto**, elige el que aparece por defecto o pulsa **"Crear clave de API en un proyecto
   nuevo"**. Cualquiera de los dos sirve.
3. En unos segundos aparece tu clave: un texto largo que empieza por **`AIza`**.

## Paso 4 · Copia la clave

Pulsa el botón **Copiar** que está junto a la clave.

## Paso 5 · Pégala en AlienMark (modo con IA)

1. En la carpeta del proyecto, copia `config.example.txt` y renombra la copia a **`config.txt`**.
2. Ábrelo con el Bloc de notas y reemplaza `PEGA_TU_API_KEY_AQUI` por tu clave:
   ```
   GEMINI_API_KEY=AIza...tu clave...
   GEMINI_MODEL=gemini-3.6-flash
   ```
3. Guarda el archivo. Listo: ya puedes usar **`Convertir con Gemini AI.bat`**.

---

## ❓ Preguntas frecuentes

**¿Cuesta dinero?**
Google ofrece un **nivel gratuito** con un límite de uso diario que alcanza para un uso personal normal. Si un día lo
superas, espera al día siguiente. Solo pagarías si tú mismo activas la facturación en Google Cloud.

**¿Es segura mi clave?**
La clave se guarda **solo en tu PC**, en `config.txt` (ese archivo nunca se sube a GitHub). **No la compartas**: quien la
tenga puede usar tu cuota. Si crees que alguien la vio, bórrala en <https://aistudio.google.com/apikey> y crea una nueva.

**Dice que la clave no está configurada.**
Revisa que el archivo se llame exactamente `config.txt` (no `config.txt.txt`) y que la clave no tenga espacios.