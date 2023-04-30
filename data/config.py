# - *- coding: utf- 8 - *-
import configparser
import requests





config = configparser.ConfigParser()
tt = config.read("settings.ini")
if len(tt) <= 1:
    tok = input("\nВведи Токен Бота:  ")
    id_adm = input("\nВведи id Администратора:    ")
    gggg = f"[settings]\ntoken = {tok}\nadmin_id = {id_adm}\nsms = 0\nra = 150\ngor = 80\nver = 160\nr = lime"
    with open('settings.ini', "w") as f:
        f.write(gggg)
config.read("settings.ini")
BOT_TOKEN = config["settings"]["token"]
adm = config["settings"]["admin_id"]
sms_api = config['settings']['sms']
tt = config["settings"]["admin_id"]
MethodGetMe = (f'''https://api.telegram.org/bot{BOT_TOKEN}/GetMe''')

response = requests.post(MethodGetMe)
tttm = response.json()


id_us = (tttm['result']['id'])
first_name = (tttm['result']['first_name'])
username = (tttm['result']['username'])
if "," in adm:
    adm = adm.split(",")
else:
    if len(adm) >= 1:
        adm = [adm]
    else:
        adm = []
        print("***** Вы не указали админ ID *****")

bot_version = "2.9"
bot_description = f"<b>♻ Bot создал Cicada3301</b>\n" \
                  f"<b>⚜ Bot Version:</b> {bot_version}\n" \
                  f"<b>🔗Для выдачи доступов на сутки</b>\n"\
                  f"<b>🎫В случае их нехватки писать ▶️:</b> <a href='https://t.me/satanasat'><b>Cicada</b></a>"
sozdatel = adm[0]
