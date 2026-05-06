TENANTS = {
    "client_1": {
        "WHATSAPP_TOKEN": "",
        "PHONE_NUMBER_ID": "",
        "SHEET_NAME": ""
    }
}

def get_tenant(phone_number_id):
    for tenant in TENANTS.values():
        if tenant["PHONE_NUMBER_ID"] == phone_number_id:
            return tenant
    return None

