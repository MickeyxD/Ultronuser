import asyncio

from userbot.utils import admin_cmd, sudo_cmd, edit_or_reply
from userbot.cmdhelp import CmdHelp


@bot.on(admin_cmd(pattern=r"gandu$", outgoing=True))
@bot.on(sudo_cmd(pattern=r"gandu$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    animation_interval = 5
    animation_ttl = range(0, 21)
    animation_chars = [
        "`abe gandu,Ruk abhi teri gand marta hu lodu`",
        "`Dekh sale Teri gand me dal diya lund`",
        "`now twisting my lund in your gand`",
        "`Your Gand Fat giye Successfully`",
        "`es Gandu Ka Gand Fat gye a`",
        "`Gandu Asking again to taste my DICKπ`",
        "`Requested acceptedπ»π, Ready to taste my DICKπ`",
        "`Getting again with fati hoi gand ready to fuck π`",
        "`You Gandu Is Ready To Fuck`",
        "`Fucking Your ππ\n\n\nYour  Ass Get Red\nTrying new SEX position to make u Squirt\n\nAlmost Done. 0%\nβββββββββββββββββββββββββ `",
        "`Fucking Your ππ\n\n\nYour Gand Get White\nu squirted like a showerπ§π¦π\n\nAlmost Done..\n\nFucked Percentage... 4%\nβββββββββββββββββββββββββ `",
        "`Fucking Your ππ\n\n\nYour gand Get Red\nDoing Extreme SEX with uπ\n\nAlmost Done...\n\nFucked Percentage... 8%\nβββββββββββββββββββββββββ `",
        "`Fucking Your ππ\n\n\nYour gand Get Red\nWarming ur Assπ to Fuck!ππ\n\nAlmost Done....\n\nFucked Percentage... 20%\nβββββββββββββββββββββββββ `",
        "`Fucking Your ππ\n\n\nYour ASSπ Get Red\nInserted my Penisπ in ur ASSπ\n\nAlmost Done.....\n\nFucked Percentage... 36%\nβββββββββββββββββββββββββ `",
        "`Fucking Your ππ\n\n\nYour ASSπ Get Red\ndoing extreme sex with u\n\nAlmost Done......\n\nFucked Percentage... 52%\nβββββββββββββββββββββββββ `",
        "`Fucking Your ππ\n\n\nYour Boobsπ€π are Awesome\nPressing u tight Nipplesπ€π\n\nAlmost Done.......\n\nFucked Percentage... 84%\nβββββββββββββββββββββββββ `",
        "`Fucking Your ππ\n\n\nYour Gand Get Horny\nDoing Gandsex with youππ\n\nAlmost Done........\n\nFucked Percentage... 89%\nβββββββββββββββββββββββββ `",
        "`Fucking Your ππ\n\n\nYour Boobsπ€π are Awesome\nI am getting ready to cum in ur Mouthπ\n\nAlmost Done.......\n\nFucked Percentage... 90%\nβββββββββββββββββββββββββ `",
        "`Fucking Your ππ\n\n\nYour  Boobsπ€π are Awesome\nFinally, I have cummed in ur Mouthππ\n\nAlmost Done.......\n\nFucked Percentage... 96%\nβββββββββββββββββββββββββ `",
        "`Fucking Your ππ\n\n\nYour ur Gand is Awesome\nyou is Licking my Dickπ in the Awesome Wayβπ€π€ππ\n\nAlmost Done.......\n\nFucked Percentage... 100%\nβββββββββββββββββββββββββ `",
        "`Fucking Your ππ\n\n\nYour  ASSπ Get Red\nCummed On ur Mouthππ\n\nYou got Pleasure\n\nResult: Now I Have 1 More SEX Partner ππ abh ja ki kise aur se chuda gandu`",
    ]

    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await event.edit(animation_chars[i % 21])


CmdHelp("Gandu").add_command(
  "gandu", None, "Uhhhh... Try it and see"
)