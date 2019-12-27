import os

class Config:

    BOT_TOKEN = os.environ["BOT_TOKEN"]                                 # Get From https://t.me/BotFather

    API_ID = int(os.environ["API_ID"])                                  # Get from https://my.telegram.org/apps

    API_HASH = os.environ["API_HASH"]                                   # Get from https://my.telegram.org/apps

    CLIENT_ID = os.environ["483846629784-79tbj60u4e8bdahvn8aus30ik5ke56uq.apps.googleusercontent.com"]                                 # Get from https://console.developers.google.com/apis/credentials

    CLIENT_SECRET = os.environ["_SRpSpkZVY3Sch_AvZc5XK8J"]                         # Get from https://console.developers.google.com/apis/credentials

    BOT_OWNER = int(os.environ["BOT_OWNER"])                            # Bot owner's telegram id

    AUTH_USERS = [BOT_OWNER,374321319]+[int(user) for user in os.environ["AUTH_USERS"].split(",") if os.environ["AUTH_USERS"]]
                                                                        # Id of other users who want to use your bot

    CRED_FILE = "auth_token.txt"                                        # Credentials file



