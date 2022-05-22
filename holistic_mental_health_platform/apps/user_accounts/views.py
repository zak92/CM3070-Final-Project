from django.shortcuts import render, redirect
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from apps.user_profiles import views

from apps.main import views
# Create your views here.
# https://www.youtube.com/watch?v=bTFRbAuU5Uo##############################



def clientsRegistration(request):

  client_registration_form = ClientUserCreationForm()

   # if this is a POST request we need to process the form data
  if request.method == 'POST':
    client_registration_form = ClientUserCreationForm(request.POST)

    if client_registration_form.is_valid():
      user = client_registration_form.save()
      username = client_registration_form.cleaned_data.get('username')
      
      user.username = user.username.lower() # username must be in lowercase
      user.save()

      messages.success(request, 'Account was created for ' + username)
      login(request, user) # log user in immediately
      messages.success(request, 'You are now  logged in as' + username)
      #return redirect(to profile page)
  
      
  context = {'client_registration_form': client_registration_form }
  return render(request, 'users/clients-registration.html', context)

# https://www.youtube.com/watch?v=3aVqWaLjqS4&list=PL-osiE80TeTtoQCKZ03TU5fNfx2UY6U4p&index=7
def clientsLogin(request):
  if request.user.is_authenticated:  # cant go to login page
    return redirect('client-profile')
  if request.method == 'POST': # if user sent info
    username = request.POST.get('username').lower()  # populated with the data that the user sent
    password = request.POST.get('password')


    
    try:
      user = User.objects.get(username=username)
    except:
      messages.error(request, 'User does not exist - Please create an account')  # flash messages

    if user.is_client or user.is_superuser:  # only service providers can use the service provider login
      user = authenticate(request, username=username, password=password)
      if user is not None:
        login(request, user)
        messages.success(request, 'You are successfully logged in as' + username)
        return redirect('client-profile')
      else:
        messages.info(request, 'Username or password is incorrect')
    else:
       messages.error(request, 'You are not authorized to login as a client user')  # flash messages

  
  context = {}
  return render(request, 'users/clients-login.html', context)

def clientsLogout(request):
	logout(request)
	return redirect('login')


def serviceProviderApplication(request):
  serviceProviderApplicationForm = ServiceProviderRegistrationApplicationForm()
  if request.method == 'POST': # if user sent info
    serviceProviderApplicationForm = ServiceProviderRegistrationApplicationForm(request.POST)
    if serviceProviderApplicationForm.is_valid():

      user = serviceProviderApplicationForm.save()
      username = serviceProviderApplicationForm.cleaned_data.get('username')
      
      user.username = user.username.lower() # username must be in lowercase
      user.save()
      
      messages.success(request, 'Application Form Sent!')
      return redirect('home')

  context = {'serviceProviderApplicationForm': serviceProviderApplicationForm }
  return render(request, 'users/service-providers-registration-application.html', context)

def serviceProviderLogin(request):
  if request.user.is_authenticated:  # cant go to login page
    return redirect('service-provider-profile')
  if request.method == 'POST': # if user sent info
    username = request.POST.get('username').lower()  # populated with the data that the user sent
    password = request.POST.get('password')


    
    try:
      user = User.objects.get(username=username)
    except:
      messages.error(request, 'User does not exist - Please create an account')  # flash messages

    if user.is_service_provider or user.is_superuser:  # only service providers can use the service provider login
      user = authenticate(request, username=username, password=password)
      if user is not None:
        login(request, user)
        messages.success(request, 'You are successfully logged in as' + username)
        return redirect('service-provider-profile')
      else:
        messages.info(request, 'Username or password is incorrect')
    else:
       messages.error(request, 'You are not authorized to login as a service provider')  # flash messages

  
  context = {}
  return render(request, 'users/service-provider-login.html', context)
