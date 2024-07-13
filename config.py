import os, time, re

id_pattern = re.compile(r'^.\d+$') 


class Config(object):

    # Client Config 
    API_ID = int(os.environ.get('API_ID', '21189715')) # ⚠️ Required
    API_HASH = os.environ.get('API_HASH', '988a9111105fd2f0c5e21c2c2449edfd') # ⚠️ Required
    BOT_TOKEN = os.environ.get('BOT_TOKEN', '7421052524:AAFcKa0yuQ8Q2oZVPiBSZL-J3rcujrCSrHk') # ⚠️ Required

    # database config
    DB_URL  = os.environ.get("DB_URL","mongodb+srv://ayanosuvii0925:subhichiku123@cluster0.uw8yxkl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # ⚠️ Required

    # Other Config 
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "https://t.me/sifrapprovalbot") # ⚠️ Required
    BOT_UPTIME  = time.time()
    OWNER = int(os.environ.get('OWNER', '6798912985')) # ⚠️ Required
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002149291828")) # ⚠️ Required
    APPROVED_WELCOME_TEXT = os.environ.get("APPROVED_WELCOME_TEXT", "Hello {mention}\nWelcome To {title}\n\nYou're Auto Approved. ✅")
    LEAVING_BY_TEXT = os.environ.get("APPROVED_WELCOME_TEXT", "👋 Bye {mention} !\nSee You Soon by {title}\n\nYou Left. ⛔")
    FORCE_SUB = os.environ.get('FORCE_SUB', '1002149291828') # ⚠️ Required
    AUTH_CHANNEL = int(FORCE_SUB) if FORCE_SUB and id_pattern.search(
    FORCE_SUB) else None 

    # Web response configuration
    WEBHOOK = bool(os.environ.get("WEBHOOK", True))
    PORT = int(os.environ.get("PORT", "8080"))

class Txt(object):

    START_MSG = """
🦁 Hᴇʟʟᴏ {} !,
I'ᴍ ᴀɴ ᴀᴜᴛᴏ Aᴘᴘʀᴏᴠᴀʟ Bᴏᴛ (Aᴅᴍɪɴ Jᴏɪɴ Rᴇǫᴜᴇsᴛ)

I ᴄᴀɴ ᴀᴘᴘʀᴏᴠᴇ ᴜsᴇʀs ɪɴ Gʀᴏᴜᴘ ᴏʀ Cʜᴀɴɴᴇʟs. Aᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀᴛ 💬
"""
