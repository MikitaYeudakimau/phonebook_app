from django.contrib import messages
from django.contrib.auth import login, logout
from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, TemplateView
from models import Person, Phone

from .forms import ContactForm, CreatePersonForm, UserLoginForm, UserRegisterForm


class AddPhoneFormView(CreateView):
    template_name = 'phonebook/add_person.html'
    form_class = CreatePersonForm
    success_url = reverse_lazy('home')

    def get_success_url(self):
        phone_numbers = self.request.POST.get("phones")
        for phone_number in phone_numbers.split("\n"):
            Phone.objects.create(phone=phone_number, contact=self.object)
        return super().get_success_url()


class HomePage(TemplateView):
    template_name = "phonebook/home.html"


class AllContacts(TemplateView):
    template_name = "phonebook/all_contacts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_by = self.request.GET.get('search_by')
        query = self.request.GET.get('query')
        search_mes = "All phones"
        if search_by in ["name", "phone"] and query:
            if search_by == "name":
                context['persons'] = Person.objects.filter(name__icontains=query)
            else:
                context['persons'] = Person.objects.filter(phones__phone__icontains=query)
            search_mes = f"All coincidences by request '{query}'"
            context['search_mes'] = search_mes
            return context
        context['search_mes'] = search_mes
        context['persons'] = Person.objects.all()
        return context


class DeletePhoneView(DeleteView):
    model = Person
    template_name = "phonebook/delete_contact.html"
    success_url = reverse_lazy("all_contacts")


def user_login(request):
    if request.method == "POST":
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("home")
    else:
        form = UserLoginForm()
    return render(request, "phonebook/login.html", {"form": form})


def user_logout(request):
    logout(request)
    return redirect("login")


def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Вы успешно зарегестрированы")
            return redirect("home")
        else:
            messages.error(request, "Ошибка регистрации")
    form = UserRegisterForm()
    return render(request, "phonebook/register.html", {"form": form})


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            mail = send_mail(form.cleaned_data['subject'], form.cleaned_data['content'], "nik1807@tut.by",
                             ['nikevdokimovv@gmail.com'], fail_silently=False)
            if mail:
                messages.success(request, "Mail is sent")
                return redirect("home")
            else:
                messages.error(request, "Ошибка в отправке письма")
        else:
            messages.error(request, "Ошибка валидации")
    else:
        form = ContactForm()
    return render(request, "phonebook/contact.html", {"form": form})
