from userbot import *
from userbot.utils import *
from userbot.cmdhelp import CmdHelp
from userbot.uniborgConfig import Config
from telethon.events import NewMessage
from telethon.tl.custom import Dialog
from telethon.tl.types import Channel, Chat, User

DEFAULTUSER = str(ALIVE_NAME) if ALIVE_NAME else "UltronUserBot User"

PM_IMG = Config.ALIVE_PIC

ludosudo = Config.SUDO_USERS

if ludosudo:
    sudou = "True"
else:
    sudou = "False"

kraken = bot.uid

pm_caption = "__**๐ฅ๐ฅ๐ณ๐๐๐๐ ฯัััะฒฯั ฮนั ฯฮท ฦฮนัั๐ฅ๐ฅ**__\n\n"

pm_caption += (
    f"               __โผ๐ผ๐ฐ๐๐๐ด๐โ__\n**ใ[{DEFAULTUSER}](tg://user?id={kraken})ใ**\n\n"
)

pm_caption += "โ รชlรชโ hรฐรฑ Vรชrยงรฏรฐรฑ: `1.15.0` \n"

pm_caption += "๊ฃ๊ฆ๊๊ป๊ฒ๊ ๊ฆ๊๊ช๊๊๊ฒ๊:      `3.7.4` \n"

pm_caption += f"ฤษVลโฑ เธฟรโฎ Vษโฑคโดลรโฆ:  __**D.0**__\n"

pm_caption += f"sแดแดแด            : `{sudou}`\n"

pm_caption += "๊๊ค๊ฃ๊ฃ๊ฒ๊ช๊ ๊๊ช๊ฒ๊ค๊ฃ  : [แดแดษชษด](https://t.me/ultronuserbot)\n"

pm_caption += "๐ฒ๐๐๐๐๐๐    : [Click Here](https://t.me/MickeyxD)\n\n"

pm_caption += "    [โจREPOโจ](https://github.com/MickeyxD/ultronuserbot) ๐น [๐License๐](https://github.com/MickeyxD/ultronuserbot/blob/master/LICENSE)"



@bot.on(admin_cmd(outgoing=True, pattern="alive$"))
@bot.on(sudo_cmd(pattern="alive$", allow_sudo=True))
async def amireallyalive(alive):
    await alive.get_chat()
    await alive.delete()
    """ For .alive command, check if the bot is running.  """
    await borg.send_file(alive.chat_id, PM_IMG, caption=pm_caption)
    await alive.delete()

CmdHelp("alive").add_command(
  'alive', None, 'Check weather the bot is alive or not'
).add_command(
  'devil', None, 'Check weather yhe bit is alive or not. In your custom Alive Pic and Alive Msg if in Heroku Vars'
).add()
