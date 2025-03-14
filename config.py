import os
import logging
from logging.handlers import RotatingFileHandler



#Bot token @Botfather
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

#Your API ID from my.telegram.org
APP_ID = int(os.environ.get("APP_ID", ""))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "")

#Your db channel Id
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1001995978690"))

# NAMA OWNER
OWNER = os.environ.get("OWNER", "sewxiy")

#OWNER ID
OWNER_ID = int(os.environ.get("OWNER_ID", "6497757690"))

#Port
PORT = os.environ.get("PORT", "8030")

#Database
DB_URI = os.environ.get("DATABASE_URL", "")
DB_NAME = os.environ.get("DATABASE_NAME", "Cluster0")

#force sub channel id, if you want enable force sub
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1001473043276"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1001644866777"))

TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

START_PIC = os.environ.get("START_PIC", "https://graph.org/file/f295fd496ad3b13119bae-abef89a82d0a379171.jpg")
FORCE_PIC = os.environ.get("FORCE_PIC", "https://graph.org/file/114a36349c7b77b6dcadb-9f85e281fb1a6d1663.jpg")

FILE_AUTO_DELETE = int(os.getenv("FILE_AUTO_DELETE", "10")) # auto delete in seconds

#start message
START_MSG = os.environ.get("START_MESSAGE", "<b>Hello 💕 {mention} \n\n ɪ ᴀᴍ ғɪʟᴇ sᴛᴏʀᴇ ʙᴏᴛ, ɪ ᴄᴀɴ sᴛᴏʀᴇ ᴘʀɪᴠᴀᴛᴇ ғɪʟᴇs ɪɴ sᴘᴇᴄɪғɪᴇᴅ ᴄʜᴀɴɴᴇʟ ᴀɴᴅ ᴏᴛʜᴇʀ ᴜsᴇʀs ᴄᴀɴ ᴀᴄᴄᴇss ɪᴛ ғʀᴏᴍ sᴘᴇᴄɪᴀʟ ʟɪɴᴋ.\n\n <blockquote>ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : <a href='https://telegram.me/Sitaratoons_Support_bot'>ᴀᴄxᴀɴɪᴍᴇ</a></blockquote></b>")
try:
    ADMINS=[6376328008]
    for x in (os.environ.get("ADMINS", "5115691197 6273945163 6103092779 5231212075").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")

#Force sub message 
FORCE_MSG = os.environ.get("FORCE_SUB_MESSAGE", "<b>ʜᴇʟʟᴏ {mention} \nᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʜᴇɴ ᴄʟɪᴄᴋ ᴏɴ ʀᴇʟᴏᴀᴅ button ᴛᴏ ɢᴇᴛ ʏᴏᴜʀ ʀᴇǫᴜᴇꜱᴛᴇᴅ ꜰɪʟᴇ.\n\n <blockquote>ᴍᴀɪɴᴛᴀɪɴᴇᴅ ʙʏ : <a href='https://telegram.me/Sitaratoons_Support_bot'>ᴀᴄxᴀɴɪᴍᴇ</a></blockquote></b>")

#set your Custom Caption here, Keep None for Disable Custom Caption
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

#set True if you want to prevent users from forwarding files from bot
PROTECT_CONTENT = True if os.environ.get('PROTECT_CONTENT', "False") == "True" else False

#Set true if you want Disable your Channel Posts Share button
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", None) == 'True'

BOT_STATS_TEXT = "<b>BOT UPTIME</b>\n{uptime}"
USER_REPLY_TEXT = "ʙᴀᴋᴋᴀ ! ʏᴏᴜ ᴀʀᴇ ɴᴏᴛ ᴍʏ ꜱᴇɴᴘᴀɪ!!"

ADMINS.append(OWNER_ID)
ADMINS.append(6497757690)

LOG_FILE_NAME = "filesharingbot.txt"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(
            LOG_FILE_NAME,
            maxBytes=50000000,
            backupCount=10
        ),
        logging.StreamHandler()
    ]
)
logging.getLogger("pyrogram").setLevel(logging.WARNING)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
   
