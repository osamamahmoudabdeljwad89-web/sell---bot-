users = {}

def get_user(phone):
    if phone not in users:
        users[phone] = {
            "name": "",
            "cart": [],
            "address": ""
        }
    return users[phone]

