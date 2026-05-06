import time

last_messages = {}

def is_spam(phone):
    now = time.time()
    if phone in last_messages and now - last_messages[phone] < 2:
        return True
    last_messages[phone] = now
    return False

