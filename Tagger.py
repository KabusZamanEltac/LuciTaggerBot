import random, os, logging, asyncio

from telethon import Button

from telethon import TelegramClient, events

from telethon.sessions import StringSession

from telethon.tl.types import ChannelParticipantsAdmins



logging.basicConfig(

    level=logging.INFO,

    format='%(name)s - [%(levelname)s] - %(message)s'

)

LOGGER = logging.getLogger(__name__)



api_id = int(os.environ.get("APP_ID"))

api_hash = os.environ.get("API_HASH")

bot_token = os.environ.get("TOKEN")

client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)





anlik_calisan = []



tekli_calisan = []







@client.on(events.NewMessage(pattern="^/start$"))

async def start(event):

  await event.reply("**🇦🇿 ASO tagger bot**\n ile Qrupunuzdakı Bütün Userlərə Tağ Ata bilərəm \nMəlumat üçün =======> /kömək yazın @ASOSONZİRVE **",

                    buttons=(

                   

		      [Button.url('Beni Gruba Ekle ➕', 'https://t.me/ASOtagger_bot?startgroup=a')],
                      [Button.url('ASO Söhbət Qrupu', 'https://t.me/ASOSONZİRVE')],

                      [Button.url('ASO Rəsmi📣', 'https://t.me/ASOresmi')],

		      [Button.url('Sahibim👨🏻‍💻', 'https://t.me/ismiyev95')],

                    ),

                    link_preview=False

                   )

@client.on(events.NewMessage(pattern="^/komek$"))

async def help(event):

  helptext = "**🇦🇿 ASO tagger bot Komutları**\n\n**/tag <səbəb> - 5-li tağ Atar**\n\n**/etag <səbəb> - Emoji ile tağ edər**\n\n**/1tag səbəb - Useleri Tək Tək tağ edər**\n\n**/admins səbəb - Adminlri Tək Tək Tağ Eder**\n\n**/start - botu başladar**"

  await event.reply(helptext,

                    buttons=(

                      [Button.url('Beni Gruba Ekle➕', 'https://t.me/werab_tag_bot?startgroup=a')],

                      [Button.url('ASO Söhbət Qrupu👨‍💻', 'https://t.me/WerabliAnlar')],

                      [ Düymə . url ( 'ASO Rəsmi 🔖' , 'https://t.me/ASOresmi' )],
. U
		      [ Düymə . url ( 'Sahibim🧑‍🔧' , 'https://t.me/ismiyev95' )],

                    ),

                    link_preview=False

                   )

	

@client.on(events.NewMessage(pattern="^/reklam$"))

async def help(event):

  helptext = "**Çok özellikleri User Botu Tapmaqa Çalışan Grub Sahibleri









ASOtagger_Bot Size Göre:\n\n📌 5-li etiket\n📌 Emoji etiket\n📌 Tek Tag\n📌 Yalnız Yöneticileri tag etmek\n📌\n\n Belə Çox özellikli @Werab_Tag_Bot 'u grubunuza Admin olarak ekleyip rahatlıqla , tağ ata bilərsiz **"

  await event.reply(helptext,

                    buttons=(

                      [Button.url('Botu Gruba Ekle➕', 'https://t.me/ASOtagger_bot?startgroup=a')],

                    ),

                    link_preview=False

                   )

	

	



@client.on(events.NewMessage(pattern='^(?i)/dur'))

async defe(event):

  global anlik_calisan

  anlik_calisan.remove(event.chat_id)





emoji = "🐵 🦁 🐯 🐱 🐶 🐺 🐻 🐨 🐼 🐹 🐭 🐰 🦊 🦝 🐮 🐷 🐽 🐗 🦓 🦄 🐴 🐸 🐲 🦎 🐉 🦖 🦕 🐢 🐊 🐍 🐁 🐀 🐇 🐈 🐩 🐕 🦮 🐕‍🦺 🐅 🐆 🐎 🐖 🐄 🐂 🐃 🐏 🐑 🐐 🦌 🦙 🦥 🦘 🐘 🦏 🦛 🦒 🐒 🦍 🦧 🐪 🐫 🐿️ 🦨 🦡 🦔 🦦 🦇 🐓 🐔 🐣 🐤 🐥 🐦 🦉 🦅 🦜 🕊️ 🦢 🦩 🦚 🦃 🦆 🐧🦈 🐬 🐋 🐳 🐟 🐠 🐡 🦐 🦞 🦀 🦑 🐙 🦪 🦂 🕷️ 🦋 🐞 🐝 🦟 🦗 🐜 🐌 🐚 🕸️ 🐛 🐾 😀 😃 😄 😁 😆 😅 😂 🤣 😭 😗 😙 😚 😘 🥰 😍 🤩 🥳 🤗 🙃 🙂 ☺️ 😊 😏 😌 😉 🤭 😶 😐 😑 😔 😋 😛 😝 😜 🤪 🤔 🤨 🧐 🙄 😒 😤 😠 🤬 ☹️ 🙁 😕 😟 🥺 😳 😬 🤐 🤫 😰 😨 😧 😦 😮 😯 😲 😱 🤯 😢 😥 😓 😞 😖 😣 😩 😫 🤤 🥱 😴 😪 🌛 🌜 🌚 🌝 🌞 🤢 🤮 🤧 🤒 🍓 🍒 🍎 🍉 🍑 🍊 🥭 🍍 🍌 🌶 🍇 🥝 🍐 🍏 🍈 🍋 🍄 🥕 🍠 🧅 🌽 🥦 🥒 🥬 🥑 🥯 🥖 🥐 🍞 🥜 🌰 🥔 🧄 🍆 🧇 🥞 🥚 🧀 🥓 🥩 🍗 🍖 🥙 🌯 🌮 🍕 🍟 🥨 🥪 🌭 🍔 🧆 🥘 🍝 🥫 🥣 🥗 🍲 🍛 🍜 🍢 🥟 🍱 🍚 🥡 🍤 🍣 🦞 🦪 🍘 🍡 🥠 🥮 🍧 🍧 🍨".split(" ")





@client.on(events.NewMessage(pattern="^/etag ?(.*)"))

async def mentionall(event):

  global anlik_calisan

  if event.is_private:

    return await event.respond("**Bu Bot gruplar ve kanallar üçün Keçerli❗**")

  

  admins = []

  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):

    admins.append(admin.id)

  if not event.sender_id in admins:

    return await event.respond("**Bu Tağı Sadece Admins İşlədə bilər〽️**")

  

  if event.pattern_match.group(1):

    mode = "text_on_cmd"

    msg = event.pattern_match.group(1)

  elif event.reply_to_msg_id:

    mode = "text_on_reply"

    msg = event.reply_to_msg_id

    if msg == None:

        return await event.respond("** Keçmiş mesajlar üçün tağ ede bilmirəm**")

  elif event.pattern_match.group(1) and event.reply_to_msg_id:

    return await event.respond("Tağ Etmək üçün səbəb yaz❗️")

  else:

    return await event.respond("**Tağ Etməyə Başlamağ Üçün Səbəb yazın...!**")

  

  if mode == "text_on_cmd":

    anlik_calisan.append(event.chat_id)

    usrnum = 0

    usrtxt = ""

    async for usr in client.iter_participants(event.chat_id):

      usrnum += 1

      usrtxt += f"[{random.choice(emoji)}](tg://user?id={usr.id}) "

      if event.chat_id not in anlik_calisan:

        await event.respond("**durdum🙄 @ASOresmi**")

        return

      if usrnum == 5:

        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")

        await asyncio.sleep(2)

        usrnum = 0

        usrtxt = ""

        

  

  if mode == "text_on_reply":

    anlik_calisan.append(event.chat_id)

 

    usrnum = 0

    usrtxt = ""

    async for usr in client.iter_participants(event.chat_id):

      usrnum += 1

      usrtxt += f"[{random.choice(emoji)}](tg://user?id={usr.id}) "

      if event.chat_id not in anlik_calisan:

        await event.respond("Işlem Başarıyla Durdum\n\n**Burda sizin reklamınız ola bilər 👉 @ASOSONZİRVE **✅")

        return

      if usrnum == 5:

        await client.send_message(event.chat_id, usrtxt, reply_to=msg)

        await asyncio.sleep(2)

        usrnum = 0

        usrtxt = ""





@client.on(events.NewMessage(pattern='^(?i)/dur'))

async def dur(event):

  global anlik_calisan

  anlik_calisan.remove(event.chat_id)





@client.on(events.NewMessage(pattern="^/tag ?(.*)"))

async def mentionall(event):

  global anlik_calisan

  if event.is_private:

    return await event.respond("Bu bot sadəcə gruplar ve kanallar üçün keçerli❗️**")

  

  admins = []

  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):

    admins.append(admin.id)

  if not event.sender_id in admins:

    return await event.respond("**Bu botu sadace admins işlədə bilər〽️**")

  

  if event.pattern_match.group(1):

    mode = "text_on_cmd"

    msg = event.pattern_match.group(1)

  elif event.reply_to_msg_id:

    mode = "text_on_reply"

    msg = event.reply_to_msg_id

    if msg == None:

        return await event.respond("Əvvəlki Mesajlara Cavab Verməyin")

  elif event.pattern_match.group(1) and event.reply_to_msg_id:

    return await event.respond("Başladmağ üçün səbəb yaz❗️")

  else:

    return await event.respond("Tağa başlamağ üçün səbəb yaz")

  

  if mode == "text_on_cmd":

    anlik_calisan.append(event.chat_id)

    usrnum = 0

    usrtxt = ""

    async for usr in client.iter_participants(event.chat_id):

      usrnum += 1

      usrtxt += f"👥 - [{usr.first_name}](tg://user?id={usr.id}) \n"

      if event.chat_id not in anlik_calisan:

        await event.respond("Durdum🌹\n\n**Burda sizində reklamınız ola bilər 👉 @ASOSONZİRVE**✅")

        return

      if usrnum == 5:

        await client.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")

        await asyncio.sleep(2)

        usrnum = 0

        usrtxt = ""

        

  

  if mode == "text_on_reply":

    anlik_calisan.append(event.chat_id)

 

    usrnum = 0

    usrtxt = ""

    async for usr in client.iter_participants(event.chat_id):

      usrnum += 1

      usrtxt += f"👥 - [{usr.first_name}](tg://user?id={usr.id}) \n"

      if event.chat_id not in anlik_calisan:

        await event.respond("Durdum👀 @ASOresmi")

        return

      if usrnum == 5:

        await client.send_message(event.chat_id, usrtxt, reply_to=msg)

        await asyncio.sleep(2)

        usrnum = 0

        usrtxt = ""



@client.on(events.NewMessage(pattern='^(?i)/dur'))

async def cancel(event):

  global anlik_calisan

  anlik_calisan.remove(event.chat_id)

	



@client.on(events.NewMessage(pattern="^/tektag ?(.*)"))

async def mentionall(event):

  global tekli_calisan

  if event.is_private:

    return await event.respond("**Bu bot gruplar ve kanallar için keçerli❗️**")

  

  admins = []

  async for admin in client.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):

    admins.append(admin.id)

  if not event.sender_id in admins:

    return await event.respond("**Bu botu sadace admins işlədə bilər〽**")

  

  if event.pattern_match.group(1):

    mode = "text_on_cmd"

    msg = event.pattern_match.group(1)

  elif event.reply_to_msg_id:

    mode = "text_on_reply"

    msg = event.reply_to_msg_id

    if msg == None:

        return await event.respond("**əvvlki mesajı tağ edə bilmirəm*")

  elif event.pattern_match.group(1) and event.reply_to_msg_id:

    return await event.respond("Xaiş Edirəm Başlamaq Üçün Bir Səbəb Yaz ❗️")

  else:

    return await event.respond("**Gozunu Sevim Bir Səbəb Yaz🙈..**")

  

  if mode == "text_on_cmd":

    tekli_calisan.append(event.chat_id)

    usrnum = 0

    usrtxt = ""

    async for usr in client.iter_participants(event.chat_id):

      usrnum += 1

      usrtxt += f"**👤 - [{usr.first_name}](tg://user?id={usr.id}) \n**"

      if event.chat_id not in tekli_calisan:

        await event.respond("**Dayandırıldı\n\n**Burda sizin reklamınız ola bilir @ASOSONZİRVE **✅****")

        return

      if usrnum == 1:

        await client.send_message(event.chat_id, f"{usrtxt} {msg}")

        await asyncio.sleep(2)

        usrnum = 0

        usrtxt = ""

        

  

  if mode == "text_on_reply":

    tekli_calisan.append(event.chat_id)

 

    usrnum = 0

    usrtxt = ""

    async for usr in client.iter_participants(event.chat_id):

      usrnum += 1

      usrtxt += f"👤 - [{usr.first_name}](tg://user?id={usr.id}) \n"

      if event.chat_id not in tekli_calisan:

        await event.respond("Durdum🙈\n\n**Burda sizində reklamınız ola bilər 👉 @ASOSONZİRVE**✅**")

        return

      if usrnum == 1:

        await client.send_message(event.chat_id, usrtxt, reply_to=msg)

        await asyncio.sleep(2)

        usrnum = 0

        usrtxt = ""



@client.on(events.NewMessage(pattern='^(?i)/dur'))

async def cancel(event):

  global tekli_calisan

  tekli_calisan.remove(event.chat_id)

	





@client.on(events.NewMessage(pattern="^/admins?(.*)"))

async def mentionall(tagadmin):



	if tagadmin.pattern_match.group(1):

		seasons = tagadmin.pattern_match.group(1)

	else:

		seasons = ""



	chat = await tagadmin.get_input_chat()

	a_=0

	await tagadmin.delete()

	async for i in client.iter_participants(chat, filter=cp):

		if a_ == 500:

			break

		a_+=5

		await tagadmin.client.send_message(tagadmin.chat_id, "**[{}](tg://user?id={}) {}**".format(i.first_name, i.id, seasons))

		sleep(0.5)





print(">> Bot işləyir narahat olma 🚀 @ismiyev95 məlumat ala bilərsiniz <<")

client.run_until_disconnected()
