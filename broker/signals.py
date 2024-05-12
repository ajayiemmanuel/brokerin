from django.db.models.signals import post_save
from django.contrib.auth.models import Group
from django.contrib.auth.models import User

from .models import *

def customer_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='customer')
        instance.groups.add(group)
        Customer.objects.create(
            user=instance,
            name=instance.username,
            )
        print('profile Created!')

post_save.connect(customer_profile, sender=User)


def deposit(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='deposit')
        instance.groups.add(group)
        Deposit.objects.create(
            user=instance,
            name=instance.username,
            )
        print('profile Created!')

post_save.connect(deposit, sender=User)


def profile_profile(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='profile')
        instance.groups.add(group)
        Profile.objects.create(
            user=instance,
            name=instance.username,
            )
        print('profile Created!')

post_save.connect(profile_profile, sender=User)



def account(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='account')
        instance.groups.add(group)
        Account.objects.create(
            user=instance,
            name=instance.username,
            )
        print('profile Created!')

post_save.connect(account, sender=User)


def transaction(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='transaction')
        instance.groups.add(group)
        Transaction.objects.create(
            user=instance,
            name=instance.username,
            )
        print('profile Created!')

post_save.connect(transaction, sender=User)

def transactionone(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='transactionone')
        instance.groups.add(group)
        Transactionone.objects.create(
            user=instance,
            name=instance.username,
            )
        print('profile Created!')

post_save.connect(transactionone, sender=User)


def transactiontwo(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='transactiontwo')
        instance.groups.add(group)
        Transactiontwo.objects.create(
            user=instance,
            name=instance.username,
            )
        print('profile Created!')

post_save.connect(transactiontwo, sender=User)


def transactionthree(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='transactionthree')
        instance.groups.add(group)
        Transactionthree.objects.create(
            user=instance,
            name=instance.username,
            )
        print('profile Created!')

post_save.connect(transactionthree, sender=User)

def wallet(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='wallet')
        instance.groups.add(group)
        Wallet.objects.create(
            user=instance,
            name=instance.username,
            )
        print('profile Created!')

post_save.connect(wallet, sender=User)


def pin(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='pin')
        instance.groups.add(group)
        Pin.objects.create(
            user=instance,
            name=instance.username,
            )
        print('profile Created!')

post_save.connect(pin, sender=User)


def alert(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='alert')
        instance.groups.add(group)
        Alert.objects.create(
            user=instance,
            name=instance.username,
            )
        print('profile Created!')

post_save.connect(alert, sender=User)


def verify(sender, instance, created, **kwargs):
    if created:
        group = Group.objects.get(name='verify')
        instance.groups.add(group)
        Verify.objects.create(
            user=instance,
            first_name=instance.username,
            )
        print('profile Created!')

post_save.connect(verify, sender=User)