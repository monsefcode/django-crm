from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import redirect
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm

# ! Create your CORE views here.
def register(request):
    if request.method == 'POST':
       form = UserRegisterForm(request.POST)
       if form.is_valid():
           form.save()
           username = form.cleaned_data.get('username')
           messages.success(request, f'Account created for {username}!')
           return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, 'auth/register.html', {'form': form})


@login_required
def profile(request):
    # If the request is a POST request, then create a new instance of the form
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        # If the forms are valid, then save the data
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()

            # Display a success message
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')
    # if the request is a GET request, then create a new instance of the form
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

        # dict to pass to the template to display the forms on the page
        context = {
            'u_form': u_form,
            'p_form': p_form
        }

    return render(request, 'auth/profile.html', context)


