
import os

class Config:

    BOT_TOKEN = os.environ.get('BOT_TOKEN', '5442493323:AAHPw8TNe0hh2zCAQKm_2O2o6KdmQ3Okgf8')
    APP_ID = os.environ.get('APP_ID', '6534707')
    API_HASH = os.environ.get('API_HASH', '4bcc61d959a9f403b2f20149cbbe627a')

    #comma seperated user id of users who are allowed to use
    ALLOWED_USERS = [x.strip(' ') for x in os.environ.get('ALLOWED_USERS','1098504493').split(',')]

    DOWNLOAD_DIR = 'downloads'
