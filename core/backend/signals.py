from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Contact, Subscriber, Blog
from core import settings
import requests
import array


from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


# ARKESEL_API_KEY = "OkhnOUlLV1FhSlpLQktXN0M="


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


@receiver(post_save, sender=Subscriber)
def subscription_notification(sender, instance, created, **kwargs):
    if created:
        confirmation_mail(instance)
    pass


@receiver(post_save, sender=Blog)
def notifify_subscribers(sender, instance, created, **kwargs):
    if created:
        if instance.is_published:
            notification_mail(instance)
            print('New Blogs: Mail Sent to subscribers')
    if instance.is_published:
        notification_mail(instance)
        print('Old blog: Mail sent to subscribers')


def send_sms(sender: str, message: str, recipients: array.array):
    header = {"api-key": settings.ARKESEL_API_KEY, 'Content-Type': 'application/json',
              'Accept': 'application/json'}
    SEND_SMS_URL = "https://sms.arkesel.com/api/v2/sms/send"
    payload = {
        "sender": sender,
        "message": message,
        "recipients": recipients
    }
    response = requests.post(SEND_SMS_URL, headers=header, json=payload)
    print(response.json())
    return response.json()


# subscription confirmation mail
def confirmation_mail(SUBSCRIBER):
    confirmation_template = 'website/notification/confirmation_mail.html'
    text = render_to_string(confirmation_template, {
        'subscriber': SUBSCRIBER,
    })
    msg = EmailMultiAlternatives(
        'Subscription Confirmation', text,
        settings.EMAIL_HOST_USER, [SUBSCRIBER.email])
    msg.attach_alternative(text, "text/html")
    try:
        msg.send()
    except Exception as err:
        print(err)
    else:
        print("Successful....Email sent!")


# new blog notification mail
def notification_mail(BLOG):
    confirmation_template = 'website/notification/notification_mail.html'

    sent_mails = 0
    not_sent_mails = 0
    for subscriber in Subscriber.objects.all():
        if subscriber.email:
            text = render_to_string(confirmation_template, {
                'blog': BLOG,
            })
            msg = EmailMultiAlternatives(
                'New Blog Post', text,
                settings.EMAIL_HOST_USER, [subscriber.email])
            msg.attach_alternative(text, "text/html")
            try:
                msg.send()
            except Exception as err:
                not_sent_mails += 1
                print(err)
            else:
                sent_mails += 1
                print("Successful....Email sent!")
            pass
