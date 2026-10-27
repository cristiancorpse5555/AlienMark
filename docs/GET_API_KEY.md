# 🔑 How to get your Google Gemini key (step by step)

<p><a href="OBTENER_API_KEY.md">🇪🇸 Español</a> · 🇬🇧 English</p>

AlienMark's AI mode uses Google's **Gemini** to describe images and understand tables and diagrams. To do that it needs
an **API key**: a long code that identifies your account. It's **free** for normal use and takes about 3 minutes.

> The AlienMark you get from the installer **doesn't need it**: it converts without AI. The key is only needed for the
> AI mode, which runs from the source code.

> You don't need a credit card or any programming knowledge. Just a Google account (the same one you use for Gmail).

---

## Step 1 · Go to Google AI Studio

1. Open your browser (Chrome, Edge, etc.).
2. Go to: **<https://aistudio.google.com/apikey>**
3. If asked, **sign in** with your Google account.

## Step 2 · Accept the terms (first time only)

The first time, a window with the Google AI Studio terms of service appears.
Tick the checkbox to accept and click **Continue**.

## Step 3 · Create the key

1. Click the **"Create API key"** button.
2. If it asks you for a **project**, choose the one shown by default or click **"Create API key in new project"**.
   Either works.
3. After a few seconds your key appears: a long piece of text starting with **`AIza`**.

## Step 4 · Copy the key

Click the **Copy** button next to the key.

## Step 5 · Paste it into AlienMark (AI mode)

1. In the project folder, copy `config.example.txt` and rename the copy to **`config.txt`**.
2. Open it with Notepad and replace `PEGA_TU_API_KEY_AQUI` with your key:
   ```
   GEMINI_API_KEY=AIza...your key...
   GEMINI_MODEL=gemini-3.6-flash
   ```
3. Save the file. Done: you can now use **`Convertir con Gemini AI.bat`**.

---

## ❓ Frequently asked questions

**Does it cost money?**
Google offers a **free tier** with a daily usage limit that's enough for normal personal use. If you go over it one
day, wait until the next day. You'd only pay if you yourself enable billing in Google Cloud.

**Is my key safe?**
The key is stored **only on your PC**, in `config.txt` (that file is never uploaded to GitHub). **Don't share it**:
whoever has it can use your quota. If you think someone saw it, delete it at <https://aistudio.google.com/apikey> and
create a new one.

**It says the key isn't configured.**
Check that the file is named exactly `config.txt` (not `config.txt.txt`) and that the key has no spaces.
