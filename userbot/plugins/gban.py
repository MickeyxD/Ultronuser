from userbot import bot, CMD_HELP, ALIVE_NAME
from telethon.tl.functions.contacts import BlockRequest, UnblockRequest
from userbot.utils import admin_cmd, sudo_cmd, edit_or_reply
from userbot.cmdhelp import CmdHelp
import html
from telethon import events
from telethon.tl.functions.photos import GetUserPhotosRequest
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.types import MessageEntityMentionName
from telethon.utils import get_input_location
from telethon.events import ChatAction

HELLBOY = str(ALIVE_NAME) if ALIVE_NAME else "Baap"
papa = borg.uid



async def get_full_user(event):  
    args = event.pattern_match.group(1).split(':', 1)
    extra = None
    if event.reply_to_msg_id and not len(args) == 2:
        previous_message = await event.get_reply_message()
        user_obj = await event.client.get_entity(previous_message.from_id)
        extra = event.pattern_match.group(1)
    elif len(args[0]) > 0:
        user = args[0]
        if len(args) == 2:
            extra = args[1]
        if user.isnumeric():
            user = int(user)
        if not user:
            await edit_or_reply(event, "**𝙎𝙤𝙢3𝙩𝙝𝙞𝙣𝙜 𝙒3𝙉𝙏 𝙒𝙧0𝙣𝙜**\n`Can you please provide me a user id`")
            return
        if event.message.entities is not None:
            probable_user_mention_entity = event.message.entities[0]
            if isinstance(probable_user_mention_entity,
                          MessageEntityMentionName):
                user_id = probable_user_mention_entity.user_id
                user_obj = await event.client.get_entity(user_id)
                return user_obj
        try:
            user_obj = await event.client.get_entity(user)
        except Exception as err:
            return await edit_or_reply(event, "**𝙎𝙤𝙢3𝙩𝙝𝙞𝙣𝙜 𝙒3𝙉𝙏 𝙒𝙧0𝙣𝙜**\n", str(err))           
    return user_obj, extra


async def get_user_from_id(user, event):
    if isinstance(user, str):
        user = int(user)
    try:
        user_obj = await event.client.get_entity(user)
    except (TypeError, ValueError) as err:
        await edit_or_reply(event, str(err))
        return None
    return user_obj

@bot.on(admin_cmd(pattern="gban ?(.*)"))
@bot.on(sudo_cmd(pattern="gban ?(.*)", allow_sudo=True))
async def gban(userbot):
    ids = userbot
    sender = await ids.get_sender()
    hum = await ids.client.get_me()
    if not sender.id == hum.id:
        hellbot = await edit_or_reply(ids, "𝙏𝙧𝙮𝙞𝙣𝙜 𝙩𝙤 𝙜𝙗𝙖𝙣 𝙩𝙝𝙞𝙨 𝙧𝙚𝙩𝙖𝙧𝙙!")
    else:
        hellbot = await edit_or_reply(ids, "`σк! ɢɴᴀɴɴɪɴɢ ᴛʜɪs ᴘɪᴇᴄᴇ ᴏғ sʜɪᴛ....`")
    hum = await userbot.client.get_me()
    await hellbot.edit(f"`🔥𝗚𝗹𝗼𝗯𝗮𝗹 𝗕𝗮𝗻𝗻𝗶𝗻𝗴 𝗧𝗵𝗶𝘀 𝗨𝘀𝗲𝗿...𝗝𝘂𝘀𝘁 𝗪𝗮𝗶𝘁 𝗔𝗻𝗱 𝗪𝗮𝘁𝗰𝗵🚶`")
    my_mention = "[{}](tg://user?id={})".format(hum.first_name, hum.id)
    f"@{hum.username}" if hum.username else my_mention
    await userbot.get_chat()
    a = b = 0
    if userbot.is_private:
        user = userbot.chat
        reason = userbot.pattern_match.group(1)
    else:
        userbot.chat.title
    try:
        user, reason = await get_full_user(userbot)
    except:
        pass
    try:
        if not reason:
            reason = "Private"
    except:
        return await hellbot.edit(f"**𝙎𝙤𝙢3𝙩𝙝𝙞𝙣𝙜 𝙒3𝙉𝙏 𝙒𝙧0𝙣𝙜 🤔**")
    if user:
        if user.id == 1037581197:
            return await hellbot.edit(
                f"'𝘼𝙗𝙚 𝙂𝙖𝙣𝙙𝙪 𝙅𝙖 𝙠𝙚 𝙜𝙖𝙣𝙙 𝙢𝙧𝙖 𝙖𝙥𝙣𝙚 𝙗𝙖𝙖𝙥 𝙠𝙤 𝙜𝙗𝙖𝙣 𝙣𝙝𝙞 𝙠𝙧 𝙨𝙠𝙩𝙖 𝙝𝙪🤫🚶`"
            )
        try:
            from userbot.modules.sql_helper.gmute_sql import gmute
        except:
            pass
        try:
            await userbot.client(BlockRequest(user))
        except:
            pass
        testuserbot = [
            d.entity.id
            for d in await userbot.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        for i in testuserbot:
            try:
                await userbot.client.edit_permissions(i, user, view_messages=False)
                a += 1
                await hellbot.edit(f"𝙂𝙗𝙖𝙣𝙣𝙞𝙣𝙜 𝙏𝙝𝙞𝙨 𝙐𝙨𝙚𝙧🚶\n\n𝙏𝙤𝙩𝙖𝙡 𝘾𝙝𝙖𝙩𝙨 𝘼𝙛𝙛𝙚𝙘𝙩𝙚𝙙:- `{a}`")
            except:
                b += 1
    else:
        await hellbot.edit(f"`Either reply to a user or gib me user id/name`")
    try:
        if gmute(user.id) is False:
            return await hellbot.edit(f"**Error! User already gbanned.**")
    except:
        pass
    return await hellbot.edit(
        f"[{user.first_name}](tg://user?id={user.id}) 𝙗𝙚𝙩𝙖 𝙢𝙖𝙟𝙙𝙪𝙧 𝙠𝙤 𝙠𝙝𝙤𝙙𝙣𝙖 𝙖𝙪𝙧 [{Devil}](tg://user?id={papa}) 𝙠𝙤 𝙘𝙝𝙤𝙙𝙣𝙖 𝙠𝙖𝙗𝙝𝙞 𝙨𝙞𝙠𝙝𝙖na 𝙣𝙝i.\n\nGban 𝙎𝙪𝙘𝙘𝙚𝙨𝙨𝙛𝙪𝙡 🔥\n𝘼𝙛𝙛𝙚𝙘𝙩𝙚𝙙 𝘾𝙝𝙖𝙩𝙨😏 : {a} **"
    )

@bot.on(admin_cmd(pattern="ungban ?(.*)"))
@bot.on(sudo_cmd(pattern="ungban ?(.*)", allow_sudo=True))
async def gunban(userbot):
    ids = userbot
    sender = await ids.get_sender()
    hum = await ids.client.get_me()
    if not sender.id == hum.id:
        hellbot = await edit_or_reply(ids, "`𝙏𝙧𝙮𝙞𝙣𝙜 𝙩𝙤 𝙪𝙣𝙜𝙗𝙖𝙣 𝙩𝙝𝙞𝙨 𝙠𝙞𝙙. ..`")
    else:
        hellbot = await edit_or_reply(ids, "`𝙐𝙣𝙜𝙗𝙖𝙣 𝙞𝙣 𝙋𝙧𝙤𝙜𝙧𝙚𝙨𝙨...`")
    hum = await userbot.client.get_me()
    await hellbot.edit(f"`Trying to ungban this kiddo...`")
    my_mention = "[{}](tg://user?id={})".format(hum.first_name, hum.id)
    f"@{hum.username}" if hum.username else my_mention
    await userbot.get_chat()
    a = b = 0
    if userbot.is_private:
        user = userbot.chat
        reason = userbot.pattern_match.group(1)
    else:
        userbot.chat.title
    try:
        user, reason = await get_full_user(userbot)
    except:
        pass
    try:
        if not reason:
            reason = "Private"
    except:
        return await hellbot.edit("**Som3ting W3nt Wr0ng**")
    if user:
        if user.id == 1037581197:
            return await hellbot.edit("**You need to grow some balls to gban / ungban my creator**")
        try:
            from userbot.modules.sql_helper.gmute_sql import ungmute
        except:
            pass
        try:
            await userbot.client(UnblockRequest(user))
        except:
            pass
        testuserbot = [
            d.entity.id
            for d in await userbot.client.get_dialogs()
            if (d.is_group or d.is_channel)
        ]
        for i in testuserbot:
            try:
                await userbot.client.edit_permissions(i, user, send_messages=True)
                a += 1
                await hellbot.edit(f"Ok! Now Ungbaning this kiddo.\nChats:- `{a}`")
            except:
                b += 1
    else:
        await hellbot.edit("**Reply to a user**")
    try:
        if ungmute(user.id) is False:
            return await hellbot.edit("**Error! User already ungbanned.**")
    except:
        pass
    return await hellbot.edit(
        f"[{user.first_name}](tg://user?id={user.id}) Aur bhai.... Aagya swaad.\n\nUngban Successful 🔥\nChats :- `{a}`"
    )




@borg.on(ChatAction)
async def handler(kraken): 
   if kraken.user_joined or kraken.user_added:      
       try:       	
         from userbot.modules.sql_helper.gmute_sql import is_gmuted
         guser = await kraken.get_user()      
         gmuted = is_gmuted(guser.id)             
       except:      
          return
       if gmuted:
        for i in gmuted:
            if i.sender == str(guser.id):                                                                         
                chat = await kraken.get_chat()
                admin = chat.admin_rights
                creator = chat.creator   
                if admin or creator:
                 try:
                    await client.edit_permissions(kraken.chat_id, guser.id, view_messages=False)                              
                    await kraken.reply(
                     f"⚠️⚠️**Warning**⚠️⚠️\n\n`Gbanned User Joined the chat!!`\n"                      
                     f"**⚜️ Victim Id ⚜️**:\n[{guser.id}](tg://user?id={guser.id})\n"                   
                     f"**🔥 Action 🔥**  :\n`Banned this piece of shit....` **AGAIN!**")                                                
                 except:       
                    kraken.reply("`Sheit!! No permission to ban users.\n@admins ban this retard.\nGlobally Banned User And A Potential Spammer`\n**Make your group a safe place by cleaning this shit**")                   
                    return
                  
                  
CmdHelp("gban_gmute").add_command(
  'gban', '<reply> / <userid> / <username>', 'Gbans the targeted user and adds to gban watch list'
).add_command(
  'ungban', '<reply> / <userid> / <username>', 'Unbans the targeted user and removes them from gban watch list. Grants another Chance'
).add_command(
  'gmute', '<reply>/ <userid>/ <username>', 'Gmutes the targeted user. Works only if you have delete msg permission. (Works on admins too)'
).add_command(
  'ungmute', '<reply>/ <userid>/ <username>', 'Ungmutes the user. Now targeted user is free'
).add()
