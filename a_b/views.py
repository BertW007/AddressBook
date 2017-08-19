from django.shortcuts import render
from django.core.exceptions import ObjectDoesNotExist
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from a_b.models import Person, Address, Phone, Email


class Main(View):

    def __init__(self):
        self.message = ''

    def get(self, request, *args, **kwargs):
        people = Person.objects.all()
        return render(request, 'main.html', {"people": people,
                                             "message": self.message})


class DeletePerson(Main):

    def get(self, request, id):
        try:
            person = Person.objects.get(id=id)
            person.delete()
            self.message = "Person {} was successfully deleted.".format(person.name)
        except ObjectDoesNotExist:
            self.message = "Person not found."
        finally:
            return super().get(request)


class EditPerson(Main):

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return render(request, 'editperson.html')


class EditName(Main):

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return render(request, 'edit-name.html')

    def post(self, request, id):
        try:
            name = request.POST.get("name")
            new_name = request.POST.get("new_name")

            surname = request.POST.get("surname")
            new_surname = request.POST.get("new_surname")

            desc = request.POST.get("desc")
            new_desc = request.POST.get("new_desc")

            if new_name == "SAVE":
                person = Person.objects.get(id=id)
                person.name = name
                person.save()
                self.message = "Person with ID {} was successfully edited.".format(person.id)
            elif new_surname == "SAVE":
                person = Person.objects.get(id=id)
                person.surname = surname
                person.save()
                self.message = "Person with ID {} was successfully edited.".format(person.id)
            elif new_desc == "SAVE":
                person = Person.objects.get(id=id)
                person.description = desc
                person.save()
                self.message = "Person with ID {} was successfully edited.".format(person.id)
            else:
                self.message = "Something is wrong"

        except ObjectDoesNotExist:
            self.message = "Person not found."

        finally:
            return super().get(request)


class EditAddress(Main):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return render(request, 'edit-address.html')

    def post(self, request, id):
        try:
            city = request.POST.get("city")
            new_city = request.POST.get("new_city")

            street = request.POST.get("street")
            new_street = request.POST.get("new_street")

            flat_number = request.POST.get("flat_number")
            new_flat_number = request.POST.get("new_flat_number")

            house_number = request.POST.get("house_number")
            new_house_number = request.POST.get("new_house_number")

            isCreate = Address.objects.get_or_create(person_id=id)

            if isCreate:
                person_address = Address.objects.get(person_id=id)

                if new_city == "SAVE":
                    person_address.city = city
                    person_address.save()
                    self.message = "Person with ID {} was successfully edited.".format(person_address.person_id)
                elif new_street == "SAVE":
                    person_address.street = street
                    person_address.save()
                    self.message = "Person with ID {} was successfully edited.".format(person_address.person_id)
                elif new_flat_number == "SAVE":
                    person_address.flat_number = flat_number
                    person_address.save()
                    self.message = "Person with ID {} was successfully edited.".format(person_address.person_id)
                elif new_house_number == "SAVE":
                    person_address.house_number = house_number
                    person_address.save()
                    self.message = "Person with ID {} was successfully edited.".format(person_address.person_id)
                else:
                    self.message = "Something is wrong"

        except ObjectDoesNotExist:
            self.message = "Person not found."
        finally:
            return super().get(request)


class EditPhone(Main):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return render(request, 'edit-phone.html')

    def post(self, request, id):
        try:
            phone = request.POST.get("phone")
            phone_type = request.POST.get("phone_type")
            new_phone = request.POST.get("new_phone")
            new_phone_type = request.POST.get("new_phone_type")

            isCreate = Phone.objects.get_or_create(person_id=id)

            if isCreate:
                person_phone = Phone.objects.get(person_id=id)
                if new_phone == "SAVE":
                    person_phone.phone_number = phone
                    person_phone.save()
                    self.message = "Person with ID {} was successfully edited.".format(person_phone.person_id)
                elif new_phone_type == "SAVE":
                    person_phone.type = phone_type
                    person_phone.save()
                    self.message = "Person with ID {} was successfully edited.".format(person_phone.person_id)
                else:
                    self.message = "Something is wrong"

        except ObjectDoesNotExist:
            self.message = "Person not found."
        finally:
            return super().get(request)


class EditEmail(Main):
    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return render(request, 'edit-email.html')

    def post(self, request, id):
        try:
            email = request.POST.get("email")
            new_email = request.POST.get("new_email")

            isCreate = Email.objects.get_or_create(person_id=id)

            if isCreate:
                person_email = Email.objects.get(person_id=id)
                if new_email == "SAVE":
                    person_email.email = email
                    person_email.save()
                    self.message = "Person with ID {} was successfully edited.".format(person_email.person_id)
                else:
                    self.message = "Something is wrong"

        except ObjectDoesNotExist:
            self.message = "Person not found."
        finally:
            return super().get(request)


class AddPerson(Main):

    @method_decorator(csrf_exempt)
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)

    def get(self, request, *args, **kwargs):
        return render(request, 'add_person.html')

    def post(self, request):
        try:
            name = request.POST.get("name")
            surname = request.POST.get("surname")
            desc = request.POST.get("desc")
            Person.objects.create(name=name, surname=surname, description=desc)
            self.message = "Person was successfully add"
        except Exception:
            self.message = "Something is wrong..."
        finally:
            return super().get(request)


class ShowPerson(View):
    def get(self, request, id):
        person = Person.objects.get(id=id)
        addresses = person.address_set.all()
        phones = person.phone_set.all()
        emails = person.email_set.all()
        return render(request, 'show_person.html',\
                      {"person": person, "addresses": addresses, "phones": phones, "emails": emails})
