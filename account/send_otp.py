import random

import requests
import datetime

Token = "3FBAD97E4B297C34714A0139A3992DB80E75A24E"
Mobile = '9162750548'
CodeLength = 4
OptionalCode = str(random.randint(1000, 9999))
headers = {
    "Authorization": Token,
}

data = {
    "Mobile": Mobile,
    "CodeLength": CodeLength,
    "OptionalCode": OptionalCode,
}

response = requests.post("https://portal.amootsms.com/rest/SendQuickOTP", headers=headers, data=data)

json_response = response.text
