from django.shortcuts import render, get_object_or_404, redirect, HttpResponse
from django.contrib.auth.models import User
from django.utils.timezone import now
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import PetForm, CareGiverForm
from .models import Pet, CareGiver
from .models import Pet, VetAppointment


def index(request):
    pets = Pet.objects.all()
    caregivers = CareGiver.objects.all()  # Query all CareGiver objects
    return render(request, 'index.html', {'pets': pets, 'caregivers': caregivers})


@login_required(login_url='login')
def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Your password and confirm password are not Same!!")
        else:

            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login')

    return render(request, 'signup.html')


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return HttpResponse("Username or Password is incorrect!!!")

    return render(request, 'login.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')


def pet_details(request, pet_id):
    pet = get_object_or_404(Pet, id=pet_id)
    return render(request, 'petdetails.html', {'pet': pet})

def confirm_adoption(request, pet_id):
    if request.method == 'POST':
        pet = get_object_or_404(Pet, id=pet_id)
        pet.is_available_for_adoption = False
        pet.save()
        return redirect('index')

def giver_details(request, caregiver_id):
    caregiver = get_object_or_404(CareGiver, id=caregiver_id)
    return render(request, 'cgdetails.html', {'caregiver': caregiver})

def giver_details_static(request):
    # Fetch the first caregiver as an example (you can customize this logic)
    caregiver = CareGiver.objects.first()
    if not caregiver:
        return render(request, 'cgdetails.html', {'error': 'No caregiver found.'})
    return render(request, 'cgdetails.html', {'caregiver': caregiver})

def add_pet(request):
    if request.method == 'POST':
        form = PetForm(request.POST, request.FILES)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.owner = request.user
            pet.save()
            return redirect('/')
    else:
        form = PetForm()
    return render(request, 'add_pet.html', {'form': form})


def add_caregiver(request):

    if request.method == "POST":
        form = CareGiverForm(request.POST, request.FILES)
        if form.is_valid():
            caregiver = form.save(commit=False)
            caregiver.user = request.user
            caregiver.save()
            return redirect('/')
    else:
        form = CareGiverForm()
    return render(request, 'add_caregiver.html', {'form': form})

def book_appointment(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        pet_name = request.POST.get('pet_name')
        contact_number = request.POST.get('contact_number')
        date = request.POST.get('date')
        time = request.POST.get('time')
        reason = request.POST.get('reason')

        # Save the appointment
        VetAppointment.objects.create(
            user_name=user_name,
            pet_name=pet_name,
            contact_number=contact_number,
            date=date,
            time=time,
            reason=reason
        )
        return redirect('index')  # Redirect to the homepage after booking

    return render(request, 'book_appointment.html')