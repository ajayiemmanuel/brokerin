from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_save
from django.db import models

# Create your models here.
class Customer (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    email = models.CharField (max_length = 200, null = True)
    phone_number = models.CharField (max_length = 200, null = True)
    country = models.CharField (max_length = 200, null = True)
    gender = models.CharField (max_length = 200, null = True)

    def __str__(self):
        return str(self.name)

class Deposit (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    capital_balance = models.CharField (max_length = 200, default = "0.00",)
    btc = models.CharField (max_length = 200,  null = True, default = "0.00",)
    usd = models.CharField (max_length = 200, default = "0.00",)
    bonus_usd = models.CharField (max_length = 200, default = "0.00",)
    plan = models.CharField (max_length = 200, default = "Silver",)
    verify = models.CharField (max_length = 200, default = "Unverified",)
    currency = models.CharField (max_length = 200, default = "$",)



    def __str__(self):
        return str(self.name)


class Profile (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    profile_pic = models.ImageField (default = "avater.png", null = True, blank = True)


    def __str__(self):
        return str(self.name)


class Account (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    account_number = models.CharField (max_length = 200,  null = True, default = "0.00",)
    account_name = models.CharField (max_length = 200, default = "0.00",)
    bank_name = models.CharField (max_length = 200, default = "0.00",)
    swift_code = models.CharField (max_length = 200, default = "0.00",)
    bitcoin_address = models.CharField (max_length = 200,  null = True, default = "0.00",)
    ethereum_address = models.CharField (max_length = 200, default = "0.00",)
    cashapp_tag = models.CharField (max_length = 200, default = "0.00",)
    paypal_email = models.CharField (max_length = 200, default = "0.00",)


    def __str__(self):
        return str(self.name)


class Transaction (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    number = models.CharField (max_length = 200, default = "1",)
    tf_type = models.CharField (max_length = 200, default = "-",)
    amount = models.CharField (max_length = 200, default = "-",)
    status = models.CharField (max_length = 200, default = "-",)
    date_time = models.CharField (max_length = 200, default = "-",)


    def __str__(self):
        return str(self.name)

class Transactionone (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    number = models.CharField (max_length = 200, default = "2",)
    tf_type = models.CharField (max_length = 200, default = "-",)
    amount = models.CharField (max_length = 200, default = "-",)
    status = models.CharField (max_length = 200, default = "-",)
    date_time = models.CharField (max_length = 200, default = "-",)


    def __str__(self):
        return str(self.name)

class Transactiontwo (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    number = models.CharField (max_length = 200, default = "3",)
    tf_type = models.CharField (max_length = 200, default = "-",)
    amount = models.CharField (max_length = 200, default = "-",)
    status = models.CharField (max_length = 200, default = "-",)
    date_time = models.CharField (max_length = 200, default = "-",)


    def __str__(self):
        return str(self.name)


class Transactionthree (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    number = models.CharField (max_length = 200, default = "4",)
    tf_type = models.CharField (max_length = 200, default = "-",)
    amount = models.CharField (max_length = 200, default = "-",)
    status = models.CharField (max_length = 200, default = "-",)
    date_time = models.CharField (max_length = 200, default = "-",)


    def __str__(self):
        return str(self.name)

class Wallet (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    btc = models.CharField (max_length = 200, default = "4",)
    eth = models.CharField (max_length = 200, default = "-",)
    usdt = models.CharField (max_length = 200, default = "-",)
    usdc = models.CharField (max_length = 200, default = "-",)


    def __str__(self):
        return str(self.name)



class Pin (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    pin = models.CharField (max_length = 200, null = True, default = "0000")


    def __str__(self):
        return str(self.name)


class Report (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    Report = models.CharField (max_length = 200, null = True)


    def __str__(self):
        return str(self.name)

choices = [
    ('sweetAlert', 'sweetAlert'),
    ('paid',"paid"),
]
    
STATUS = (
    ('You need to have a Withdrawal Pin in order to facilitate your withdrawal request. Please contact an agent for help on how to get one.', 'You need to have a Withdrawal Pin in order to facilitate your withdrawal request. Please contact an agent for help on how to get one.'),
    ('Please upgrade your account, your current investment plan does not support this action, the company will email you shortly or contact customer care for more info', 'Please upgrade your account, your current investment plan does not support this action, the company will email you shortly or contact customer care for more info'),
    ('KYC has not been uploaded kindly fill in your details on your kyc data table', 'KYC has not been uploaded kindly fill in your details on your kyc data table'),
    )

kyc = (
    ('swal-2', 'swal-2'),
    ('swal-4', 'swal-4'),
    )

class Alert (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    name = models.CharField (max_length = 200,  null = True)
    alert = models.CharField (max_length=24, choices=choices, default='sweetAlert')
    status = models.CharField (max_length=200, null=True, choices=STATUS, default='You need to have a Withdrawal Pin in order to facilitate your withdrawal request. Please contact an agent for help on how to get one.')
    kyc = models.CharField (max_length=24, choices=kyc, default='#swal-4')

    def __str__(self):
        return str(self.name)


class Verify (models.Model):
    user = models.OneToOneField (User, null = True, blank = True, on_delete = models.CASCADE)
    first_name = models.CharField (max_length = 200,  null = True)
    last_name = models.CharField (max_length = 200, null = True,)
    email = models.CharField (max_length = 200, null = True,)
    gender = models.CharField (max_length = 200, null = True,)
    country_code = models.CharField (max_length = 200, null = True,)
    country = models.CharField (max_length = 200, null = True,)
    phone_number = models.CharField (max_length = 200, null = True,)
    year = models.CharField (max_length = 200, null = True,)
    month = models.CharField (max_length = 200, null = True,)
    day = models.CharField (max_length = 200, null = True,)
    profile_pic = models.ImageField (null = True, blank = True)

    def __str__(self):
        return str(self.first_name)