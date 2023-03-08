from dotenv import load_dotenv
import os
load_dotenv()

INSTAGRAM_USERNAME= os.environ["INSTA_USERNAME"]
INSTAGRAM_PASSWSORD=os.environ["INSTA_PASSWORD"]
DATABASE="sqlite:///instagram.db"