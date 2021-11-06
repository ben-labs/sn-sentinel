#!/bin/env python3
'''Example code to detect new SN Quebec patches for ServiceNow'''

import os
import dotenv
import re
from blab.sentinel import Ftp


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

ftp.disconnect()
