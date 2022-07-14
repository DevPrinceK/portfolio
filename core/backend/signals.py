from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Contact, Subscriber
# ...................
import requests
import array

ARKESEL_API_KEY = "OkhnOUlLV1FhSlpLQktXN0M="


@receiver(post_save, sender=Contact)
def notify_devprincek(sender, instance, created, **kwargs):
    if created:
        contact = instance.contact if instance.contact is not None else ''
        name = instance.name if instance.name is not None else ''
        email = instance.email if instance.email is not None else ''
        subject = instance.subject if instance.subject is not None else ''
        message = instance.message if instance.message is not None else ''

        sender_info = name + ' ' + contact + ' ' + email + ' \n'
        body = subject.upper() + ' \n\n' + message
        content = body + ' \n\n' + 'FROM: \n' + sender_info

        send_sms("devprincek", content, ["0558366133"])


# @receiver(post_save, sender=Subscriber)
# def subscription_notification(sender, instance, created, **kwargs):
#     if created:
#         message = 'Hello there! \n Thanks for subscribing to my weekly blogpost. \n'
#         pass


def send_sms(sender: str, message: str, recipients: array.array):
    header = {"api-key": ARKESEL_API_KEY, 'Content-Type': 'application/json',
              'Accept': 'application/json'}
    SEND_SMS_URL = "https://sms.arkesel.com/api/v2/sms/send"
    payload = {
        "sender": sender,
        "message": message,
        "recipients": recipients
    }
    response = requests.post(SEND_SMS_URL, headers=header, json=payload)
    return response.json()


# subscription confirmation mail
def confirmation_mail():
    pass


# new blog notification mail
def notification_mail():
    pass
