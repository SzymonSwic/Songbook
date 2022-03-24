from django.shortcuts import render

from .forms import UserRegistrationForm


def register_new_user(request):
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            # new_user = user_form.save(commit=False)
            # new_user.set_password(user_form.cleaned_data['password'])
            user_form.save()
            return render(request,
                          'registration/register_confirm.html',
                          {'user_form': user_form})
    else:
        user_form = UserRegistrationForm()
    return render(request,
                  'registration/register.html',
                  {'user_form': user_form})
