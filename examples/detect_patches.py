#!/bin/env python3
'''Example code to detect new SN Quebec patches for ServiceNow'''

import os
import dotenv
import re
from blab.sentinel import Ftp, Telegram


dotenv.load_dotenv(os.path.join(os.path.dirname(__file__), '../.env'))
ftp = Ftp()
ftp.connect(os.environ.get('ftp_uid'), os.environ.get('ftp_pwd'))

quebec_patchs = ftp.list_patches("glide*quebec*.zip")

# Get the latest patch available
quebec_patchs.sort(reverse=True)
current_patch = quebec_patchs[0]

# Get checksum file
checksums = ftp.list_patches(f'{current_patch}*md5sum*')
if len(checksums) == 1:
    checksum_file = checksums[0]
else:
    ftp.disconnect()
    raise ValueError("Incorrect checksum files found "
                     f"using {current_patch}*md5sum*")

# extract checksum
md5sum = re.search('.*md5sum-(.*)', checksum_file).group(1)

# print results
print(current_patch)
print(checksum_file)
print(md5sum)

'''
Alert via telegram.

To use the Telegram Class you will need a bot and
it's token.

Also whomever you are trying to send an alert to
needs to be registered to the bot. ie: They need
to have communicated with the bot before.
'''
alerter = Telegram(os.environ.get('bot_token'))
alerter.send_message(
                     os.environ.get('ben_telegram_id'),
                     "<b><u>New patch files found:</u></b>\n "
                     f"<i>{current_patch} </i>\nYou got work to do!")

ftp.disconnect()
