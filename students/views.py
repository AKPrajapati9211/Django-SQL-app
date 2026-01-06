from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from .models import Student
from django.contrib.auth import logout
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.password = make_password(form.cleaned_data['password'])
            student.save()
            messages.success(request, 'Registration successful. Please log in.')
            return redirect('student_login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def student_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            try:
                student = Student.objects.get(email=email)
                if check_password(password, student.password):
                    request.session['student_id'] = student.id
                    return redirect('student_dashboard')
                else:
                    messages.error(request, 'Invalid password.')
            except Student.DoesNotExist:
                messages.error(request, 'Email not registered.')
    else:
        form = LoginForm()
    return render(request, 'student_login.html', {'form': form})

def admin_login(request):
    return redirect('/admin/login/')


def admin_logout(request):
    logout(request)
    return redirect('student_login')

def student_dashboard(request):
    student_id = request.session.get('student_id')
    if not student_id:
        return redirect('student_login')
    student = Student.objects.get(id=student_id)
    return render(request, 'student_dashboard.html', {'student': student })

def is_admin(user):
    return user.is_staff

@user_passes_test(is_admin)
def admin_dashboard(request):
    students = Student.objects.all()
    return render(request, 'admin_dashboard.html', {'students': students})  