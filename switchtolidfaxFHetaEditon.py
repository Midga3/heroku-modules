# ---------------------------------------------------------------------------------
# Name: switchtolidfax
# Description: Switch your hikka to lidfax
# Author: @DepositUser
# ---------------------------------------------------------------------------------
# 🔒    Licensed under the GNU AGPLv3
# 🌐 https://www.gnu.org/licenses/agpl-3.0.html
# ---------------------------------------------------------------------------------
# Author: @deposituser
# Commands: switchtolidfax
# meta developer: @DepositUser
# meta_desc: Switch your hikka to lidfax
# meta banner: https://envs.sh/3Wd.jpg
# meta pic: https://kappa.lol/2Z_Q-
# ---------------------------------------------------------------------------------

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from hikkatl.types import Message
from .. import loader, utils
import asyncio

@loader.tds
class SwitchToLidFax(loader.Module):
    """Auto switching from Hikka to LidFax"""

    strings = {"name": "SwitchToLidFax"}

    async def client_ready(self, client, db):
        self._db = db

        if self.get("done"):
            keyboard = InlineKeyboardMarkup(inline_keyboard=[[
                InlineKeyboardButton(text='🥷 Support chat', url='https://t.me/lidfax_talks')],[
                InlineKeyboardButton(text='📖 Github', url='https://github.com/sz3333/LidFax-userbot')
            ]]
            )
            await self.inline._bot.send_photo(
                self.tg_id, 
                "https://envs.sh/K1p.png",
                caption="<b>Hello, you switched to a LidFax, a Heroku Userbot fork with some improvements.</b>"
                "\nModule for switching is unloaded.",
                reply_markup=keyboard,
            )

            self.set("done", None) # db need to be clear, for case if user backup db and switches once more

            await self.invoke('unloadmod', 'SwitchToLidFax', self.inline.bot_id)

    async def _run_git_command(self, command):
        """Helper function to run git commands and wait for completion"""
        process = await asyncio.create_subprocess_shell(
            command,
            stdin=asyncio.subprocess.PIPE,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
            cwd=utils.get_base_dir(),
        )
        await process.communicate()
        return process.returncode

    @loader.command()
    async def switchtolidfax(self, message: Message):
        """ - Automatically switch to lidfax"""

        await utils.answer(message, "Compatibility check... Wait")

        if "sz3333" in utils.get_git_info()[1]:
            return await utils.answer(message, "You`re already running fork.")

        await utils.answer(message, "Everything is okay, I started switching...")

        # Git config
        await self._run_git_command("git config --global user.email 'you@example.com'")
        await self._run_git_command("git config --global user.name 'Your Name'")

        # Create stable branch (ignore if exists)
        await self._run_git_command("git branch stable 2>/dev/null || true")

        # Switch to stable branch
        await self._run_git_command("git switch stable || git checkout stable")

        # Remove old origin (ignore if doesn't exist)
        await self._run_git_command("git remote remove origin 2>/dev/null || true")

        # Add new origin
        await self._run_git_command("git remote add origin https://github.com/sz3333/LidFax-userbot.git")

        # Fetch from new origin
        await self._run_git_command("git fetch origin")

        # Checkout stable branch from origin
        await self._run_git_command("git checkout -B stable origin/stable")

        peer_id = self.inline.bot_id

        await self.invoke('fconfig', 'updater GIT_ORIGIN_URL https://github.com/sz3333/LidFax-userbot', peer_id)

        await utils.answer(message, "Automatically restarting. (after restart, it's all done)")

        self.set("done", True)

        await self.invoke('update', '-f', peer_id)