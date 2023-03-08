from db.box_model import Box
from sqlalchemy.orm import Session
from db.box_model import Box
from db.schema.box import BoxCreate


def create_new_box(boxinfo: BoxCreate, db: Session):
    try:        
        box = Box(
            media_id=boxinfo.media_id,
            media_url=boxinfo.media_url
        )
        db.add(box)
        db.commit()
        db.refresh(box)
        return box
    except Exception as ex:
        print(str(ex))
        return {"success":False, "error":ex}

def fetchall(db: Session):
    return db.query(Box).all()


def getMediaId(boxid: int, db: Session):
    boxinfo = db.query(Box).filter(Box.id == boxid).first()
    if not boxinfo:
        return False
    return boxinfo.__dict__


def updateMediaId(boxid, boxinfo: BoxCreate, db: Session):
    try:
        boxexists = getMediaId(boxid, db)
        if not boxexists:
            return {"success": False, "error": "Invalid Box Id"}
        db.query(Box).filter(Box.id == boxid).update(
            {"media_id": boxinfo.media_id, "media_url": boxinfo.media_url})
        db.commit()
        return getMediaId(boxid=boxid, db=db)
    except Exception as ex:
        print(ex)
        return {"success":False, "error":str(ex)}
