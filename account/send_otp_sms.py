import random
import requests


def send_otp(phone_number):
    try:
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

        response = requests.post(
            "https://portal.amootsms.com/rest/SendQuickOTP", headers=headers, data=data)
        response.raise_for_status()  # Raise an error for bad status codes
        data_dict = response.json()  # Use .json() instead of ast.literal_eval

        return data_dict["Data"]["Code"], data_dict
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return "Error", {"Status": "Failed", "Message": str(e)}
    except KeyError as e:
        print(f"Key error: {e}")
        return "Error", {"Status": "Failed", "Message": f"Missing key in response: {e}"}
    except Exception as e:
        print(f"An error occurred: {e}")
        return "Error", {"Status": "Failed", "Message": str(e)}
