from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings

from .forms import SignUpForm, ContactForm
from .models import SignUp


def contact(request):

    form = ContactForm(request.POST or None)
    if form.is_valid():
        # for key in form.cleaned_data:
        #     print(key, form.cleaned_data.get(key))
        email = form.cleaned_data.get("email")
        message = form.cleaned_data.get("message")
        full_name = form.cleaned_data.get("full_name")

        send_mail(
            subject='Site contact form',
            message="%s: %s via %s" % (full_name, message, email),
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.EMAIL_HOST_USER, 'strmatvey@yandex.ru'],
            #html_message="<h2>Yo!</h2>",
            fail_silently=False
        )

    context = {
        'form': form,
        'title': 'Would you like something to write?',
        'title_center': True,
    }
    return render(request, 'forms.html', context)


def home(request):
    title = 'Welcome'

    # if request.method == 'POST':
    #     print(request.POST)

    form = SignUpForm(request.POST or None)

    context = {
        'title': title,
        'form': form,
    }

    if form.is_valid():
        form.save()
        # instance = form.save(commit=False)
        # if instance.full_name == None:
        #     instance.full_name = "Justin"
        # instance.save()
        # print(instance)
        context = {
            'title': 'Thank you!',
        }

    if request.user.is_authenticated() and request.user.is_staff:
        for instance in SignUp.objects.all().order_by('-timestamp'):
            print(instance.full_name)
        context = {
            'queryset': SignUp.objects.all().order_by('-timestamp').filter(full_name__icontains='att')
        }

    return render(request, 'home.html', context)


def home__(request):
    title = 'Welcome'
    if request.user.is_authenticated():
        title = "My title %s" % request.user
    context = {
        'title': title,
    }
    return render(request, 'home.html', context)
