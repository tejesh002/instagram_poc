from db.box_model import Box
from sqlalchemy.orm import Session
from db.box_model import Box
from db.schema.box import BoxCreate

def create_new_box(boxinfo : BoxCreate, db: Session):
    box = Box(
        media_id = boxinfo.media_id,
        media_url = boxinfo.media_url
    )
    db.add(box)
    db.commit()
    db.refresh(box)
    return box


def fetchall(db: Session):
    return db.query(Box).all()

def getMediaId(boxid: int, db:Session):
    return db.query(Box).filter(Box.id==boxid).first().__dict__