# ---------------------------------------------------------------------------------
#  /\_/\  🌐 This module was loaded through https://t.me/hikkamods_bot
# ( o.o )  🔐 Licensed under the GNU AGPLv3.
#  > ^ <   ⚠️ Owner of heta.hikariatama.ru doesn't take any responsibilities or intellectual property rights regarding this script
# ---------------------------------------------------------------------------------
# Name: вахуи_пон
# Author: Den4ikSuperOstryyPer4ik
# Commands:
# .пон | .вахуи
# ---------------------------------------------------------------------------------

#
# 	 @@@@@@    @@@@@@   @@@@@@@  @@@@@@@    @@@@@@   @@@@@@@@@@    @@@@@@   @@@@@@@   @@@  @@@  @@@       @@@@@@@@   @@@@@@
# 	@@@@@@@@  @@@@@@@   @@@@@@@  @@@@@@@@  @@@@@@@@  @@@@@@@@@@@  @@@@@@@@  @@@@@@@@  @@@  @@@  @@@       @@@@@@@@  @@@@@@@
# 	@@!  @@@  !@@         @@!    @@!  @@@  @@!  @@@  @@! @@! @@!  @@!  @@@  @@!  @@@  @@!  @@@  @@!       @@!       !@@
# 	!@!  @!@  !@!         !@!    !@!  @!@  !@!  @!@  !@! !@! !@!  !@!  @!@  !@!  @!@  !@!  @!@  !@!       !@!       !@!
# 	@!@!@!@!  !!@@!!      @!!    @!@!!@!   @!@  !@!  @!! !!@ @!@  @!@  !@!  @!@  !@!  @!@  !@!  @!!       @!!!:!    !!@@!!
# 	!!!@!!!!   !!@!!!     !!!    !!@!@!    !@!  !!!  !@!   ! !@!  !@!  !!!  !@!  !!!  !@!  !!!  !!!       !!!!!:     !!@!!!
# 	!!:  !!!       !:!    !!:    !!: :!!   !!:  !!!  !!:     !!:  !!:  !!!  !!:  !!!  !!:  !!!  !!:       !!:            !:!
# 	:!:  !:!      !:!     :!:    :!:  !:!  :!:  !:!  :!:     :!:  :!:  !:!  :!:  !:!  :!:  !:!   :!:      :!:           !:!
# 	::   :::  :::: ::      ::    ::   :::  ::::: ::  :::     ::   ::::: ::   :::: ::  ::::: ::   :: ::::   :: ::::  :::: ::
# 	 :   : :  :: : :       :      :   : :   : :  :    :      :     : :  :   :: :  :    : :  :   : :: : :  : :: ::   :: : :
#
#                                             © Copyright 2023
#
#                                    https://t.me/Den4ikSuperOstryyPer4ik
#                                                  and
#                                          https://t.me/ToXicUse
#
#                                    🔒 Licensed under the GNU AGPLv3
#                                 https://www.gnu.org/licenses/agpl-3.0.html
#
# meta developer: @AstroModules
# scope: hikka_only
# scope: hikka_min 1.3.0

import random

from telethon.tl.types import Message

from .. import loader


@loader.tds
class ВахуиПонMod(loader.Module):
    """пон и вахуи"""

    strings = {"name": "ВАХУИ-ПОН", "pon": "пон", "vahui": "вахуи"}

    @loader.command()
    async def понcmd(self, message: Message):
        """--> пон"""
        reply = await message.get_reply_message()
        m = random.choice(await self.client.get_messages("@PON_STICKS", limit=100))
        if reply:
            await self.client.send_message(message.chat_id, file=m, reply_to=reply)
        else:
            await message.respond(file=m)

        if message.out:
            await message.delete()

    @loader.command()
    async def вахуиcmd(self, message: Message):
        """--> вахуи"""
        reply = await message.get_reply_message()
        m = random.choice(await self.client.get_messages("@VAHUI_STICKS", limit=100))
        if reply:
            await self.client.send_message(message.chat_id, file=m, reply_to=reply)
        else:
            await message.respond(file=m)

        if message.out:
            await message.delete()
