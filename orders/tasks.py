from celery import task
from django.core.mail import send_mail
from .models import Order

@task
def order_created(order_id):
    """
    Task to send an e-mail notification when an order is 
    successfully created.
    """
    order = Order.objects.get(id=order_id)
    subject = 'Order nr. {}'.format(order.id)
    message = 'Dear {},\n\nYou have successfully placed an order.\
                  Your order id is {}.'.format(order.first_name,
                                            order.id)
    mail_sent = send_mail(subject,
                          message,
                          'admin@myshop.com',
                          [order.email])
    return mail_sent


# amqp==2.6.1
# billiard==3.5.0.2
# celery==4.1.0
# click==8.1.3
# click-didyoumean==0.3.0
# click-plugins==1.1.1
# click-repl==0.2.0
# Django==2.1.5
# kombu==4.1.0
# Pillow==9.3.0
# prompt-toolkit==3.0.36
# pytz==2022.7
# six==1.16.0
# typing_extensions==4.4.0
# vine==1.3.0
# wcwidth==0.2.5