# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔐 Licensed under the GNU GPLv3.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: afk
# Description: Provides a message saying that you are unavailable
# Author: HitaloSama
# Commands:
# .afk | .unafk
# ---------------------------------------------------------------------------------


#    Friendly Telegram (telegram userbot)
#    Copyright (C) 2018-2019 The Authors

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

import datetime
import logging
import time

from telethon import types

from .. import loader, utils

logger = logging.getLogger(__name__)


@loader.tds
class AFKMod(loader.Module):
    """Provides a message saying that you are unavailable"""

    strings = {
        "name": "AFK",
        "gone": "<b>I'm goin' AFK</b>",
        "back": "<b>I'm no longer AFK</b>",
        "afk": "<b>I'm AFK right now (since {} ago).</b>",
        "afk_reason": "<b>I'm AFK right now (since {} ago).\nReason:</b> <i>{}</i>",
    }

    async def client_ready(self, client, db):
        self._db = db
        self._me = await client.get_me()

    async def afkcmd(self, message):
        """.afk [message]"""
        if utils.get_args_raw(message):
            self._db.set(__name__, "afk", utils.get_args_raw(message))
        else:
            self._db.set(__name__, "afk", True)
        self._db.set(__name__, "gone", time.time())
        self._db.set(__name__, "ratelimit", [])
        await self.allmodules.log("afk", data=utils.get_args_raw(message) or None)
        await utils.answer(message, self.strings("gone", message))

    async def unafkcmd(self, message):
        """Remove the AFK status"""
        self._db.set(__name__, "afk", False)
        self._db.set(__name__, "gone", None)
        self._db.set(__name__, "ratelimit", [])
        await self.allmodules.log("unafk")
        await utils.answer(message, self.strings("back", message))

    async def watcher(self, message):
        if not isinstance(message, types.Message):
            return
        if message.mentioned or getattr(message.to_id, "user_id", None) == self._me.id:
            afk_state = self.get_afk()
            if not afk_state:
                return
            logger.debug("tagged!")
            ratelimit = self._db.get(__name__, "ratelimit", [])
            if utils.get_chat_id(message) in ratelimit:
                return
            else:
                self._db.setdefault(__name__, {}).setdefault("ratelimit", []).append(
                    utils.get_chat_id(message)
                )
                self._db.save()
            user = await utils.get_user(message)
            if user.is_self or user.bot or user.verified:
                logger.debug("User is self, bot or verified.")
                return
            if self.get_afk() is False:
                return
            now = datetime.datetime.now().replace(microsecond=0)
            gone = datetime.datetime.fromtimestamp(
                self._db.get(__name__, "gone")
            ).replace(microsecond=0)
            diff = now - gone
            if afk_state is True:
                ret = self.strings("afk", message).format(diff)
            elif afk_state is not False:
                ret = self.strings("afk_reason", message).format(diff, afk_state)
            await utils.answer(message, ret, reply_to=message)

    def get_afk(self):
        return self._db.get(__name__, "afk", False)
