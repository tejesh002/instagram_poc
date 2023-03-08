
from pydantic import BaseModel
from pydantic import EmailStr


# properties required during user creation
class BoxCreate(BaseModel):
    media_id: int
    media_url: str
