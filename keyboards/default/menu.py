# - *- coding: utf- 8 - *-
from aiogram.types import ReplyKeyboardMarkup
from aiogram.types.inline_keyboard import InlineKeyboardButton, InlineKeyboardMarkup

from data.config import adm


def check_user_out_func(user_id):
    menu_default = ReplyKeyboardMarkup(resize_keyboard=True)
    menu_default.row("🔐 Акаунты", "📱 Профиль", "ℹ FAQ")
    menu_default.row("📯 Функции", "📦 Анонимный Файлообменик", '📶 Номера')#📲 ProtonMail")
    menu_default.row("📸 Штамп на фото", "📞 Подмена номера")
    if str(user_id) in adm:
        menu_default.row("🔐 Управление  🖍", "📰 Информация о боте")
        menu_default.row("⚙ Настройки", "🔆 Общие функции", "👤 Добавление Администраторов ⚜️")
        menu_default.row("🔗 Одн. ссылка для входа")
    return menu_default


all_back_to_main_default = ReplyKeyboardMarkup(resize_keyboard=True)
all_back_to_main_default.row("⬅ На главную")

ssaa = InlineKeyboardMarkup(row_width=2)
ssaa.add(
    InlineKeyboardButton("✅ Добавить ", callback_data='yes_add')
)

lic = InlineKeyboardMarkup()
lic.add(
    InlineKeyboardButton("✅ let's go", callback_data='pr')
)

reg_back = InlineKeyboardMarkup()
reg_back.add(
    InlineKeyboardButton('❌ Отмена', callback_data='otm')
)



virtualsim = InlineKeyboardMarkup(row_width=2)
virtualsim.add(
    InlineKeyboardButton('📲 Telegram',callback_data='proton'),
    InlineKeyboardButton('📲 Signal', callback_data='sig')
    )

virtualsimadm = InlineKeyboardMarkup(row_width=2)
virtualsimadm.add(
    InlineKeyboardButton('📲 Telegram',callback_data='proton'),
    InlineKeyboardButton('📲 Signal', callback_data='sig'),
    InlineKeyboardButton('Баланс', callback_data='BBB')
    )




pon = InlineKeyboardMarkup(row_width=2)
pon.add(
    InlineKeyboardButton("Я Все Понял", callback_data="ponyal_vega")
)

dano = InlineKeyboardMarkup(row_width=2)
dano.add(
    InlineKeyboardButton("ДА ✅", callback_data="da_vega"),
    InlineKeyboardButton("Нет ❌", callback_data="no_vega")
)


sit = InlineKeyboardMarkup()
sit.add(
    InlineKeyboardButton(text="vegaswork.cc", callback_data="vg"),
    InlineKeyboardButton(text="pzhtop.ru", callback_data="pz"),
    InlineKeyboardButton(text="pzhtopl.ru", callback_data="pzl")
)
sit.add(
    InlineKeyboardButton(text="kdrtop.ru", callback_data="kdrtop"),
    InlineKeyboardButton(text="kdrtopl.ru", callback_data="kdrtopl"),
    InlineKeyboardButton(text="amzntop.ru", callback_data="amzntop")
)
sit.add(
    InlineKeyboardButton(text="arizonel.ru", callback_data="arizonel"),
    InlineKeyboardButton(text="arizone.ru", callback_data="arizone"),
    InlineKeyboardButton(text="chizhtopl.ru", callback_data="chizhtopl"),
)
sit.add(
    InlineKeyboardButton(text="chizhtop.ru", callback_data="chizhtop"),
    InlineKeyboardButton(text="abawork.cc", callback_data="abawork"),
    InlineKeyboardButton(text="murmur48.cc", callback_data="murmur48"),
)
sit.add(
    InlineKeyboardButton(text="lok-work.cc", callback_data="lokwork"),
    InlineKeyboardButton(text="lok-shop.ru", callback_data="lokshop"),
    InlineKeyboardButton(text="amzntopl.ru", callback_data="amzntopl"),
    InlineKeyboardButton(text="bestcrown.cc", callback_data="bbe"),
)



pravila = InlineKeyboardMarkup()
pravila.add(
    InlineKeyboardButton(text="✅ Я Все Понял", callback_data="pon")
)


otm = InlineKeyboardMarkup()
otm.add(
    InlineKeyboardButton(text="❌ Назад В Меню", callback_data="pr")
)