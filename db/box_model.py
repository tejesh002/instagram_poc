from sqlalchemy import Column,Integer, String

from db.base_class import Base

class Box(Base):
    id = Column(Integer,primary_key=True,index=True)
    media_id = Column(Integer,nullable = False)
    media_url = Column(String,nullable = False)