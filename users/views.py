from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic.detail import DetailView

from users.forms import SignUpForm, UserProfileForm
from users.models import UserProfile 
from django.http import HttpResponse

for profile in UserProfile.objects.filter(user_id=2):
    print(profile.chosen_product)
class UserView(DetailView):
    template_name = 'profile.html'

    def get_object(self):
        return self.request.user


def register(request):
    if request.method == 'POST':
          
        form = SignUpForm(request.POST)
        user_profile_form = UserProfileForm(request.POST)
        print(form.is_valid())
        print(form)
        if form.is_valid() and user_profile_form.is_valid():
            user = form.save()
            user_profile_form.save(user)
            password = form.cleaned_data.get('password1')
            email = request.POST["email"]
            user = authenticate(request, email=email, password=password)
            login(request, user)
            return redirect('/')
        else:
            print("Invalid form data")
    #         raw_password = form.cleaned_data.get('password1')
    #         user = authenticate(request,
    #                             email=user.email,
    #                             password=raw_password)
    #         if user is not None:
    #             login(request, user)
    #         else:
    #             print("user is not authenticated")
    #         return redirect('users:profile')
    # else:
    #     form = SignUpForm()
    return render(request, 'user/register.html')
def log_searched(request):
    #Make it post
    user_id = int(request.GET["id"])
    product_slug = request.GET["product_slug"]
    
    # profiles = []
    
    profiles = UserProfile.objects.filter(user_id=user_id)
    # print(profiles)
    for profile in profiles:
        profile.chosen_product = product_slug
        profile.save()
    return HttpResponse("Success")