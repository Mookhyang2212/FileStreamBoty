from os import environ as env

class Telegram:
    API_ID = int(env.get("TELEGRAM_API_ID", 23908538))
    API_HASH = env.get("TELEGRAM_API_HASH", "600d68b2a9ab32ab116e9b32a89c46fd")
    OWNER_ID = int(env.get("OWNER_ID", 5107892950))
    ALLOWED_USER_IDS = env.get("ALLOWED_USER_IDS", "").split()
    BOT_USERNAME = env.get("TELEGRAM_BOT_USERNAME", "@Miririririririr_bot")
    BOT_TOKEN = env.get("TELEGRAM_BOT_TOKEN", "6039857845:AAHOnjuEUUDUszAzCt-klQAvOMSE5Irsjtk")
    CHANNEL_ID = int(env.get("TELEGRAM_CHANNEL_ID", -1002142370083))
    SECRET_CODE_LENGTH = int(env.get("SECRET_CODE_LENGTH", 12))

class Server:
    BASE_URL = env.get("BASE_URL", "https://testtiddaldl-970235d35086.herokuapp.com/")
    BIND_ADDRESS = env.get("BIND_ADDRESS", "0.0.0.0")
    PORT = int(env.get("PORT", 443))

# LOGGING CONFIGURATION
LOGGER_CONFIG_JSON = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '[%(asctime)s][%(name)s][%(levelname)s] -> %(message)s',
            'datefmt': '%d/%m/%Y %H:%M:%S'
        },
    },
    'handlers': {
        'file_handler': {
            'class': 'logging.FileHandler',
            'filename': 'event-log.txt',
            'formatter': 'default'
        },
        'stream_handler': {
            'class': 'logging.StreamHandler',
            'formatter': 'default'
        }
    },
    'loggers': {
        'uvicorn': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        },
        'uvicorn.error': {
            'level': 'WARNING',
            'handlers': ['file_handler', 'stream_handler']
        },
        'bot': {
            'level': 'INFO',
            'handlers': ['file_handler', 'stream_handler']
        }
    }
}
