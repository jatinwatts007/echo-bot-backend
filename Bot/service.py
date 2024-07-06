from datetime import datetime

import pytz

from Bot.data import get_user_details, save_chat


def chat_with_echo_bot(data):
    name = data.get('name')
    message = data.get('message')
    email = data.get('email')
    timestamp = data.get('timestamp')
    tz = pytz.timezone('Asia/Kolkata')
    # here dividing by 1000 to convert milliseconds to seconds
    date_time = datetime.fromtimestamp(timestamp/1000, tz).isoformat()
    user_instance = get_user_details(name=name, email=email)
    save_chat(message=message, timestamp=date_time, user_instance=user_instance)
    return True


