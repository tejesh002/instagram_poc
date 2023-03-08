
from instagrapi import Client
from local_database import ClientStorage
from settings import INSTAGRAM_PASSWSORD, INSTAGRAM_USERNAME
import json
from typing import List
import ast
db = ClientStorage()


def instagramlogin():
    try:
        cl = Client()
        settings = db.get()
        if not settings:
            login_response = cl.login(INSTAGRAM_USERNAME, INSTAGRAM_PASSWSORD)
            if login_response:
                db.set(cl)
                return True

        # if 'settings' in settings[0]:
        #     relogin_response = cl.login(
        #         INSTAGRAM_USERNAME, INSTAGRAM_PASSWSORD, relogin=True)
        #     print(relogin_response)
        #     if relogin_response:
        #         db.set(cl)
        #         return db.get()

        return True
    except Exception as ex:
        print(ex)
        return False


def getAllMedia():
    try:
        cl = Client()
        settings = db.get()
        if settings:
            cl.set_settings(json.loads(settings[0]['settings']))
        userid = json.loads(settings[0]['settings'])[
            'authorization_data']['ds_user_id']
        return cl.user_medias(int(userid))

    except Exception as ex:
        print(ex)
        return False

# 3026981649115911410
# 3026938334093871756


def getMediaInfo(pkid):
    try:
        cl = Client()
        settings = db.get()
        cl.set_settings(json.loads(settings[0]['settings']))
        mediaInfo = cl.media_info(pkid, False)

        return mediaInfo
    except Exception as ex:
        if str(ex) == "Media not found or unavailable":
            return {"success": False, "error": "Invalid Media Id"}
        return {"success": False, "error": str(ex)}
