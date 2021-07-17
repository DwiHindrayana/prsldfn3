# DAISYXMUSIC- Telegram bot project
# Copyright (C) 2021  Roj Serbest
# Copyright (C) 2021  Inuka Asith
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.
# Modified by Inukaasith

import os
from os import getenv

from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

que = {}
SESSION_NAME = getenv("BQCyJ8JyEypnOTSA0dRjkwMJonwNiZFJaUsuvjrW_WaXegYXnYeR1Q0d30HtcKFthoxyfshqdCpfTM70lrxrT4MeBgO-t2svNqLrqWoM-M5alosxvJ-FMc76LugQX65LrIX_CrdF6UhH_GcRRXKY2eMrzsz__2QyW3b7aOGkxY9LvmQs7D45V1VwrxXUX2KFJ1CtzpL66r53Plq79PDTXFEitwXdVV0ZMcCXEPbgEkifWo7cHtttoDxxN9MPmO_-yNVZCPnuJFOGvHES5M5XG5Gv0fd5mW0A3Vsgbay4LkrdCOnmN2fcHrSsHqRd_P5zlwXdg6gOvwUv4yBE-ABNfoxrYsOOWQA")
BOT_TOKEN = getenv("1881967077:AAHyWsmGKz9YYiUm1sTKfVhctOYKiXo1QHo")
BOT_NAME = getenv("Fricillia Defina")
UPDATES_CHANNEL = getenv("luftschl0ss")
BG_IMAGE = getenv("https://telegra.ph/file/661ab4453ed2e986a672d.png")
admins = {}
API_ID = int(getenv("6953926"))
API_HASH = getenv("745b753c78ccb58676733a10ac00b266")
BOT_USERNAME = getenv("prsldfnBot")
ASSISTANT_NAME = getenv("JotaroDioBrandoBot")
SUPPORT_GROUP = getenv("prsldfn")
PROJECT_NAME = getenv("JPE MK5")
SOURCE_CODE = getenv("SOURCE_CODE", "github.com/TeamOfDaisyX/DaisyXMusic")
DURATION_LIMIT = int(getenv("15"))
ARQ_API_KEY = getenv("VKSSQH-SRNJYZ-MSOJAI-QALESR-ARQ", None)
PMPERMIT = getenv("PMPERMIT", None)
LOG_GRP = getenv("LOG_GRP", None)
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ !").split())

SUDO_USERS = list(map(int, getenv("1656983129").split()))
