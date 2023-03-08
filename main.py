# from flask import Flask, jsonify
from typing import List
from instagrapi.types import Media, Usertag, Location, UserShort
from instagram_service import instagramlogin, getAllMedia, getMediaInfo

from typing import Union

from fastapi import FastAPI
from db.base import Base
from db.session import engine
from db.utils import check_db_connected, check_db_disconnected
from sqlalchemy.orm import Session
from fastapi import Depends
from db.schema.box import BoxCreate
from db.session import get_db
from db.repository.box import create_new_box,fetchall,getMediaId,updateMediaId



def create_tables():
    Base.metadata.create_all(bind=engine)


def start_application():
    app = FastAPI()
    create_tables()
    instagramlogin()
    return app

app = start_application()


@app.on_event("startup")
async def app_startup():
    await check_db_connected()


@app.on_event("shutdown")
async def app_shutdown():
    await check_db_disconnected()


@app.get("/mediainfo", response_model=List[Media])
def read_root():
    return getAllMedia()


# @app.get("/mediainfo/{id}")
# async def media_info(id):
#     return getMediaInfo(id)


@app.post("/boxes")
async def createBox(box: BoxCreate, db: Session = Depends(get_db)):
    return create_new_box(boxinfo= box, db=db)


@app.get("/boxes")
async def getallboxes(db: Session = Depends(get_db)):
    return fetchall(db=db)


@app.get("/boxes/{id}")
async def getBox(id, db:Session = Depends(get_db)):
    boxinfo = getMediaId(id,db=db)
    if not boxinfo:
        return {"success":False, "error": 'Invalid Box Id'}
    return getMediaInfo(boxinfo['media_id'])


@app.put("/boxes/{id}")
async def updatebox(id, box:BoxCreate, db: Session = Depends(get_db)):
    return updateMediaId(id,box,db=db)