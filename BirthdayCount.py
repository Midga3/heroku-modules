# Free to use | MIDGA3
# meta developer: @mikhaylodm

from herokutl.tl.types import Message
from .. import loader, utils
import requests

@loader.tds
class BirthdayCount(loader.Module):
    """Counter to birthday\nVia @birthdaycountbot"""

    strings = {
        "name": "BirthdayCount",
        "fail": "<b><emoji document_id=5465665476971471368>❌</emoji>First, register at @birthdaycountbot</b>", 
        "_cmd_doc_bcount": "check how many days left."
    }
    
    strings_ru = {
        "fail": "<b><emoji document_id=5465665476971471368>❌</emoji></b>", 
        "_cmd_doc_bcount": "проверьте сколько дней осталось.", 
        "_cls_doc": "Счёт до др\nЧерез бота @birthdaycountbot"
    }

    async def bcountcmd(self, message):
        """check how many days left."""     
        async with self._client.conversation("@birthdaycountbot") as conv:
			msg = await conv.send_message("/start")
			r = await conv.get_response()
			if ":" in r.text:
				text = r.text
			else:
				text = self.strings("fail")
			await msg.delete()
			await r.delete()
		await answer(message, text)