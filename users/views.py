from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.views.generic.detail import DetailView

from users.forms import SignUpForm, UserProfileForm
<<<<<<< HEAD
from users.models import UserProfile 
from django.http import HttpResponse
=======
from rest_framework import generics
from users.serializers import BrowsingHistorySerializer
from users.models import InAppSearchHistory
>>>>>>> dev

for profile in UserProfile.objects.filter(user_id=2):
    print(profile.chosen_product)
class UserView(DetailView):
    template_name = 'user/profile.html'

    def get_object(self):
        return self.request.user


class StoreBrowsingHistoryAPIView(generics.CreateAPIView):
    serializer_class = BrowsingHistorySerializer

    def get_queryset(self):
        product_id = self.kwargs['product_id']
        user_id = self.kwargs['user_id']
        queryset = InAppSearchHistory.objects.create(user_id, product_id)
        print(queryset.objects.all())

        return queryset


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
