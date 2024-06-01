import random
import requests
import ast


def send_otp(phone_number):
    token = "3FBAD97E4B297C34714A0139A3992DB80E75A24E"
    mobile = phone_number
    code_length = 4
    optional_code = str(random.randint(1000, 9999))
    headers = {
        "Authorization": token,
    }

    data = {
        "Mobile": mobile,
        "CodeLength": code_length,
        "optional_code": optional_code,
    }

    response = requests.post("https://portal.amootsms.com/rest/SendQuickOTP", headers=headers, data=data)
    data_dict = ast.literal_eval(response.text)

    return data_dict["Data"]["Code"], data_dict

