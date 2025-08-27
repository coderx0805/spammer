from telethon import __version__, events, Button

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10


START_BUTTON = [
    [
        Button.url("𓆩〬 🍹𝆺𝅥⃝🤍 ‌‌ ●𝐌ᴀ꯭ᴛ꯭ʟ꯭ᴀ꯭ʙ꯭ɪ꯭ 𝗗꯭ᴜ꯭ɴ꯭ɪ꯭ʏ꯭ᴀ꯭🤍𝆺꯭𝅥⎯꯭‌⎯꯭", "https://t.me/Matlabi_Duniyah"),
        Button.url("𝐎ᴡɴᴇʀ", "https://t.me/veron_deva")
    ],
    [
        Button.url(" 𝐂н𝙰𝙽𝙽𝙴𝙻 ", "https://t.me/Veron_bots"),
        Button.url(" 𝐒𝚄𝙿𝙿𝙾𝚃  ", "https://t.me/VERON_SUPPORTS")
    ],
]


@X1.on(events.NewMessage(pattern="/start"))
@X2.on(events.NewMessage(pattern="/start"))
@X3.on(events.NewMessage(pattern="/start"))
@X4.on(events.NewMessage(pattern="/start"))
@X5.on(events.NewMessage(pattern="/start"))
@X6.on(events.NewMessage(pattern="/start"))
@X7.on(events.NewMessage(pattern="/start"))
@X8.on(events.NewMessage(pattern="/start"))
@X9.on(events.NewMessage(pattern="/start"))
@X10.on(events.NewMessage(pattern="/start"))
async def start(event):
    if event.is_private:
        AltBot = await event.client.get_me()
        bot_name = AltBot.first_name
        bot_id = AltBot.id
        TEXT = f"**ʜᴇʏ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nɪ ᴀᴍ [{bot_name}](tg://user?id={bot_id})**\n"
        await event.client.send_file(
            event.chat_id,
            "https://files.catbox.moe/m37bvo.jpg",
            caption=TEXT,
            buttons=START_BUTTON
        )
