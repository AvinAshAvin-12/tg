"""command: .heroku"""


from telethon import events
from datetime import datetime
from uniborg.util import admin_cmd
import subprocess
import importlib.util
import asyncio
import random
import importlib.util
from datetime import datetime
from random import randint
from asyncio import sleep
from os import execl
from asyncio import create_subprocess_shell as asyncrunapp
from asyncio.subprocess import PIPE as asyncPIPE
import asyncio
from asyncio import create_subprocess_shell as asyncrunapp
from asyncio.subprocess import PIPE as asyncPIPE
from platform import python_version, uname
from shutil import which, rmtree
from telethon import version
from os import remove, execle, path, makedirs, getenv, environ
from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError, NoSuchPathError
import distutils
from uniborg.util import admin_cmd
from collections import deque
import sys
import os
import io
import git
import heroku3
import json
from sample_config import Config
from datetime import datetime
from random import randint
from asyncio import sleep
from os import execl
import sys
import os
import io
import heroku3
import asyncio
import sys
import json
from speedtest import Speedtest
from telethon import functions
from os import remove, execle, path, makedirs, getenv, environ
from shutil import rmtree
import asyncio
import json
from asyncio import sleep
from telethon.errors import rpcbaseerrors
import os
import subprocess
import time
import math
from pySmartDL import SmartDL
import asyncio
from hachoir.metadata import extractMetadata
from hachoir.parser import createParser
from telethon.tl.types import DocumentAttributeVideo
import sys
from git import Repo
from git.exc import GitCommandError, InvalidGitRepositoryError, NoSuchPathError
from asyncio import create_subprocess_shell as asyncrunapp
from asyncio.subprocess import PIPE as asyncPIPE
from platform import python_version, uname
from shutil import which
from os import remove
from telethon import version


# ================= CONSTANT =================
HEROKU_API_KEY = Config.HEROKU_API_KEY
HEROKU_APP_NAME = Config.HEROKU_APP_NAME

DEFAULTUSER = Config.ALIVE_NAME if Config.ALIVE_NAME else uname().node
# ============================================

async def asyncrunapp_run(cmd, heroku):
    subproc = await asyncrunapp(cmd, stdout=asyncPIPE, stderr=asyncPIPE)
    stdout = await subproc.communicate()
    stderr = await subproc.communicate()
    exitCode = subproc.returncode
    if exitCode != 0:
        await heroku.edit(
            '**An error was detected while running subprocess**\n'
            f'```exitCode: {exitCode}\n'
            f'stdout: {stdout.decode().strip()}\n'
            f'stderr: {stderr.decode().strip()}```')
        return exitCode
    return stdout.decode().strip(), stderr.decode().strip(), exitCode

  
@borg.on(admin_cmd(pattern="heroku ?(.*)"))
async def heroku(event):
    await event.edit("`Processing...`")
    await asyncio.sleep(3)
    conf = event.pattern_match.group(1)
    result = await asyncrunapp_run(f'heroku ps -a {HEROKU_APP_NAME}', event)
    if result[2] != 0:
        return
    hours_remaining = result[0]
    await event.edit('`' + hours_remaining + '`')
    return
