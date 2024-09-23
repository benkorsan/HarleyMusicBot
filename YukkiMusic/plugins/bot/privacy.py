from pyrogram import filters
from pyrogram.enums import ParseMode
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

import config
from YukkiMusic import app

TEXT = f"""
**{app.mention} için Gizlilik Politikası!**

Gizliliğiniz bizim için önemlidir. Verilerinizi nasıl topladığımız, kullandığımız ve koruduğumuz hakkında daha fazla bilgi edinmek için lütfen Gizlilik Politikamızı buradan inceleyin: [Gizlilik Politikası]({config.PRIVACY_LINK}).

Herhangi bir sorunuz veya endişeniz varsa, [Destek Ekibimize]({config.SUPPORT_GROUP}) ulaşmaktan çekinmeyin.
"""


@app.on_message(filters.command("privacy"))
async def privacy(client, message: Message):
    keyboard = InlineKeyboardMarkup(
        [[InlineKeyboardButton("Gizlilik Politikasını Görüntüle", url=config.PRIVACY_LINK)]]
    )
    await message.reply_text(
        TEXT,
        reply_markup=keyboard,
        parse_mode=ParseMode.MARKDOWN,
        disable_web_page_preview=True,
    )
