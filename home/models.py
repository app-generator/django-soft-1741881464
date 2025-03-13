# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Contact(models.Model):

    #__Contact_FIELDS__
    companyname = models.CharField(max_length=255, null=True, blank=True)
    contact_name = models.CharField(max_length=255, null=True, blank=True)
    phone_no = models.CharField(max_length=255, null=True, blank=True)
    email = models.CharField(max_length=255, null=True, blank=True)

    #__Contact_FIELDS__END

    class Meta:
        verbose_name        = _("Contact")
        verbose_name_plural = _("Contact")


class Contracts(models.Model):

    #__Contracts_FIELDS__
    contract_name = models.CharField(max_length=255, null=True, blank=True)
    startdate = models.DateTimeField(blank=True, null=True, default=timezone.now)
    enddate = models.DateTimeField(blank=True, null=True, default=timezone.now)
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE)

    #__Contracts_FIELDS__END

    class Meta:
        verbose_name        = _("Contracts")
        verbose_name_plural = _("Contracts")


class Contract_Docs(models.Model):

    #__Contract_Docs_FIELDS__
    contract = models.ForeignKey(Contracts, on_delete=models.CASCADE)
    doc_name = models.CharField(max_length=255, null=True, blank=True)
    doc_attach = models.TextField(max_length=255, null=True, blank=True)

    #__Contract_Docs_FIELDS__END

    class Meta:
        verbose_name        = _("Contract_Docs")
        verbose_name_plural = _("Contract_Docs")



#__MODELS__END
