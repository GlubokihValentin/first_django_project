from django.shortcuts import render, redirect

from myapp.views import menu
from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # create a new user object but avoid saving it yet
            new_user = user_form.save(commit=False)
            # set the chosen password
            new_user.set_password(user_form.cleaned_data['password'])
            # save the User object
            new_user.save()
            return render(request, 'users/register_done.html', {'new_user': new_user, 'menu': menu})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'users/register.html', {'user_form': user_form, 'menu': menu})
    # так внутри создается пользователь - создается запись во встроенной таблицк User
    # user = User.objects.create_user('johm', 'lennon@thebeatles,com', 'johnpassword')
# Create your views here.
