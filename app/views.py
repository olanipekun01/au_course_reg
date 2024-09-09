from django.shortcuts import render,redirect
from .forms import UserSignupForm, StudentSignupForm, InstructorSignupForm
from .models import User, Student, Instructor

# Create your views here.
def index(request):
    return render(request, 'index.html')


def courseMain(request):
    return render(request, 'coursemain.html')

def register(request):
    if request.method == 'POST':
        user_form = UserSignupForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()  # Save the user instance
            user_type = user.user_type
            
            if user_type == 'student':
                student_form = StudentSignupForm(request.POST)
                if student_form.is_valid():
                    student = student_form.save(commit=False)
                    student.user = user  # Link student to user
                    student.save()
            elif user_type == 'instructor':
                instructor_form = InstructorSignupForm(request.POST)
                if instructor_form.is_valid():
                    instructor = instructor_form.save(commit=False)
                    instructor.user = user  # Link instructor to user
                    instructor.save()
            
            return redirect('success_page')  # Redirect to success page after signup
    else:
        user_form = UserSignupForm()
        student_form = StudentSignupForm()
        instructor_form = InstructorSignupForm()
    
    return render(request, 'signup.html', {
        'user_form': user_form,
        'student_form': student_form,
        'instructor_form': instructor_form,
    })