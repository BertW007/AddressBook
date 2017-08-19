from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=64)
    surname = models.CharField(max_length=64)
    description = models.TextField(blank=True)


class Address(models.Model):
    city = models.CharField(max_length=64)
    street = models.CharField(max_length=64)
    house_number = models.CharField(max_length=16)
    flat_number = models.CharField(max_length=16)
    person = models.ForeignKey(Person)


class Phone(models.Model):
    phone_number = models.CharField(max_length=32)
    type = models.CharField(max_length=32)
    person = models.ForeignKey(Person)


class Email(models.Model):
    email = models.CharField(max_length=64)
    person = models.ForeignKey(Person)


class Group(models.Model):
    name = models.CharField(max_length=32)
    member = models.ManyToManyField(Person, related_name='groups')
