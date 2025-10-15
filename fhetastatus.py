# NOT OFFICIAL FHeta MODULE
# meta developer: @mikhaylodm && @FHeta_Updates

from herokutl.tl.types import Message
from .. import loader, utils
import requests

@loader.tds
class DeleteLinuxMod(loader.Module):
    """NOT OFFICIAL FHeta MODULE\nCheck fheta status"""

    strings = {
        "name": "FHetaStatus",
        "working": "<b><emoji document_id=5427009714745517609>✅</emoji>FHeta is working</b>",
        "not_working": "<b><emoji document_id=5465665476971471368>❌</emoji>Fheta is unavailable</b>", 
        "_cmd_doc_fping": "check fheta status."
    }
    
    strings_ru = {
        "working": "<b><emoji document_id=5427009714745517609>✅</emoji>FHeta работает</b>",
        "not_working": "<b><emoji document_id=5465665476971471368>❌</emoji>Fheta недоступна</b>", 
        "_cmd_doc_fping": "проверить статус FHeta."
    }

    async def fpingcmd(self, message: Message):
        """check fheta status"""

        url = "https://api.fixyres.com/search?query=z" # Не ии это мне на будущее если менять
        response = requests.get(url)
        if response.status_code == 200 and response.text != "[]":
            meassage = await utils.answer(message, self.strings("working"))
        else:
            meassage = await utils.answer(message, self.strings("not_working"))