import requests
import env_config


def create_pass(
    email,
    name,
    roll_number,
    allowed,
    day_1_validity="",
    day_2_validity="",
    phone_number="",
):
    url = env_config.create_pass_api

    data = {
        "name": name,
        "email": email,
        "phone_number": phone_number,
        "roll_number": roll_number,
        "allowed": allowed,
        "day_1_validity": day_1_validity,
        "day_2_validity": day_2_validity,
    }

    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer " + env_config.token,
    }

    response = requests.post(url, json=data, headers=headers)

    print("\n***create_pass_section***\nstatus_code > ", response.status_code)
    print("response > ", response.json(), "\n***create_pass_section***\n")

    return response.json()
