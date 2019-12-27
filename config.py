import os

class Config:

    BOT_TOKEN = os.environ['1043241288:AAF7cNXrdFmG0wMRj1AQJczInr9fB32SXdY']                                 # Get From https://t.me/BotFather

    API_ID = int(os.environ["965018"])                                  # Get from https://my.telegram.org/apps

    API_HASH = os.environ["6cd1a0cfc1a3e76076a8331c4319e97c"]                                   # Get from https://my.telegram.org/apps

    CLIENT_ID = os.environ["483846629784-79tbj60u4e8bdahvn8aus30ik5ke56uq.apps.googleusercontent.com"]                                 # Get from https://console.developers.google.com/apis/credentials

    CLIENT_SECRET = os.environ["_SRpSpkZVY3Sch_AvZc5XK8J"]                         # Get from https://console.developers.google.com/apis/credentials

    BOT_OWNER = int(os.environ["491634139"])                            # Bot owner's telegram id

    AUTH_USERS = [BOT_OWNER,705138975]+[int(user) for user in os.environ["AUTH_USERS"].split(",") if os.environ["AUTH_USERS"]]
                                                                        # Id of other users who want to use your bot

    CRED_FILE = "auth_token.txt"                                        # Credentials file



