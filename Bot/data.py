from Bot.models import User, Chat


def get_user_details(name, email):
    try:
        user_instance = User.objects.get(username=name, email=email)
    except User.DoesNotExist:
        user_instance = User.objects.create(username=name, email=email)
        user_instance.save()
    return user_instance


def save_chat(message, timestamp, user_instance):
    chat = Chat.objects.create(message=message, timestamp=timestamp, user_id=user_instance)
    chat.save()

