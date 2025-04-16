from telethon import TelegramClient, events, Button

bot = TelegramClient(None, 6, "eb06d4abfb49dc3eeb1aeb98ae0f581e").start(bot_token="7316320223:AAFdH2UCQv1A1NFxmxjTxypSH2iN7-Hwlrw")

@bot.on(events.NewMessage(pattern="/start"))
async def _start(event):
    txt = """
**Welcome In 11xGame 💙**

__• Smooth Touch Website__
__• Your Data Is Safe__
__• Cricket Bets__
__• Casino Games , Skill Games__
__• Safe Banks Withdrawal__ 

**Play With 11x And Make Safe Money 🪙**
    """
    return await event.reply(txt, buttons=[[Button.url("Play", url="https://t.me/Game11xBot/play")]])

bot.loop.run_forever()
