from urllib import parse
from tinydb import TinyDB
import json

class ClientStorage:
    db = TinyDB('./db.json')

    def get(self):
        """Get client settings
        """
        # key = parse.unquote(sessionid.strip(" \""))
        try:
            return self.db.all()
        except IndexError:
            raise Exception('Session not found (e.g. after reload process), please relogin')

    def set(self, cl) -> bool:
        """Set client settings
        """
        key = parse.unquote(cl.sessionid.strip(" \""))
        self.db.truncate()
        self.db.insert({'sessionid': key, 'settings': json.dumps(cl.get_settings())})
        return True

    def close(self):
        pass
