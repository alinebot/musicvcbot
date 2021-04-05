from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>👋🏻 Hi {message.from_user.first_name}!</b>

I am Denvil Music Bot, an open-source bot that lets you play music in your Telegram groups voice chat.
This bot is based on su music project and hamkers vc bot. 

To add in your group contact us at @Anierosupport

Use the buttons below to know more about me.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Add me to group", url="https://t.me/URLmusicbot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💬 Music Group", url="https://t.me/AnieRoSupport"
                    ),
                    InlineKeyboardButton(
                        "Channel 🔈", url="https://t.me/MusicBotEnjoy_group"
                    ),
                    InlineKeyboardButton(
                        " support chat", url="https://t.me/Anierosupport" )
                ],
                [
                    InlineKeyboardButton(
                        "Donate the coder", url="https://t.me/@noobviral"
                    )
                ]
            ]
        )
    )


@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "💁🏻‍♂️ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
