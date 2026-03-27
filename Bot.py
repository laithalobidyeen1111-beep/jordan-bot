from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes
import requests

TOKEN = "8089421898:AAF7Rw7xDfwvuNqRuyjivKZbX_afdxdSejU"
API_KEY = "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"

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_text = update.message.text

    await update.message.reply_text("😎 استنى شوي...")

    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "openai/gpt-3.5-turbo",
            "messages": [
                {
                    "role": "system",
                    "content": "احكي باللهجة الأردنية وبأسلوب شب أردني خفيف دم"
                },
                {
                    "role": "user",
                    "content": user_text
                }
            ]
        }
    )

    data = response.json()

    try:
        reply = data["choices"][0]["message"]["content"]
    except:
        reply = "في اشي غلط يا زلمة 😅"

    await update.message.reply_text(reply)

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT, handle_message))

app.run_polling()
