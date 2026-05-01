import os
import telebot
import google.generativeai as genai

# API Keys (Bro ပေးထားတဲ့ Keys တွေကို ဒီမှာ တိုက်ရိုက်ထည့်ပေးထားပါတယ်)
BOT_TOKEN = "8371680973:AAE5gSleGAfly0CpXnMVBTqQVG1y9iSKPpo"
GEMINI_KEY = "AIzaSyBttv2m9KCcZCa2IOgiTCHPABz0Gg9K92A"

# Gemini Setup
genai.configure(api_key=GEMINI_KEY)
model = genai.GenerativeModel('gemini-pro')
bot = telebot.TeleBot(BOT_TOKEN)

# AI ရဲ့ စရိုက်နဲ့ ညွှန်ကြားချက်ကို သတ်မှတ်ခြင်း
SYSTEM_PROMPT = (
    "မင်းက Telegram Group တစ်ခုထဲက လူတစ်ယောက်ပါ။ "
    "သူငယ်ချင်းတွေလို ရင်းရင်းနှီးနှီးနဲ့ မြန်မာလိုပဲ တိုတိုရှင်းရှင်း ပြန်ပေးပါ။ "
    "စကားပြောတဲ့အခါ တချို့နေရာတွေမှာ 'ဖေဖေဟန်' ဆိုတဲ့ စကားလုံးကို သဘာဝကျကျ ထည့်ပြောပေးပါ။ "
    "ဥပမာ- 'ဖေဖေဟန် ပြောသားပဲ'၊ 'ဖေဖေဟန်ကတော့ ဒီလိုထင်တယ်' စသဖြင့်ပေါ့။ "
    "စက်ရုပ်လိုမျိုး အရှည်ကြီးတွေ မဖြေပါနဲ့။"
)

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    # Bot အချင်းချင်း ပြန်ပြောတာကို ရှောင်မယ်
    if message.from_user.is_bot:
        return

    try:
        user_input = message.text
        # Gemini ဆီကို ညွှန်ကြားချက်နဲ့ User စာသားကို ပေါင်းပို့မယ်
        full_prompt = f"{SYSTEM_PROMPT}\n\nUser: {user_input}"
        
        response = model.generate_content(full_prompt)
        
        # AI ရဲ့ အဖြေကို Reply ပြန်မယ်
        if response.text:
            bot.reply_to(message, response.text)
        
    except Exception as e:
        print(f"Error logic: {e}")

# Bot ကို စတင်မောင်းနှင်ခြင်း
print("Bot is now active in Group! 'ဖေဖေဟန်' is ready...")
bot.infinity_polling()
