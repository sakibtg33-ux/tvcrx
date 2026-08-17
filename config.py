# Paste your BotFather token between the quotation marks.
# Never share the completed file publicly.
BOT_TOKEN = "8281237118:AAE0MoKYVcLTvDYfTN-bQuufuTAkSWbXmQg"

# Get these from https://my.telegram.org -> API development tools.
API_ID = 23274996  # Replace locally/Railway with your new API ID
API_HASH = "7fa0c48ef9e57f8d92dba33ed6771e64"

# Safety and resource limits for a personal local bot.
MAX_MINUTES = 180
# Local Bot API server supports large uploads; 1950 MB leaves a small safety margin below 2000 MB.
MAX_UPLOAD_MB = 1950
FFMPEG_TIMEOUT_BUFFER_SECONDS = 120

# Required for files larger than the standard Telegram Bot API limit.
# Run the official local Bot API server on this address before starting the bot.
USE_LOCAL_BOT_API = True
# Railway service name; for local Docker use http://127.0.0.1:8081 instead.
BOT_API_HOST = "http://telegram-api:8081"

# Optional: restrict usage to specific Telegram user IDs.
# Leave empty to allow anyone who can message the bot.
ALLOWED_USER_IDS = set()
