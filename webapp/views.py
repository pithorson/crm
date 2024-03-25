from django.shortcuts import render, redirect
from .forms import CreateUserForm, LoginForm, CreateRecordForm,UpdateRecordForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Record

def home(request):
    return render(request, 'webapp/index.html')

def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("my-login")
    context = {'form': form}
    return render(request, 'webapp/register.html', context=context)

def my_login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("dashboard")
    context = {'form': form}
    return render(request, 'webapp/my-login.html', context=context)

def user_logout(request):
    logout(request)
    return redirect("my-login")

@login_required(login_url='my-login')
def dashboard(request):
    records = Record.objects.all()
    return render(request, 'webapp/dashboard.html', {'records': records})

def create_record(request):
    if request.method == 'POST':
        form = CreateRecordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard')  # Redirect to the appropriate URL after saving
    else:
        form = CreateRecordForm()

    context = {'form': form}
    return render(request, 'webapp/create-record.html', context)


#update record

@login_required(login_url='my-login')
def update_record(request, pk):
    record_instance = Record.objects.get(id=pk)

    form = UpdateRecordForm(instance=record_instance)

    if request.method == 'POST':
        form = UpdateRecordForm(request.POST, instance=record_instance)

        if form.is_valid():
            form.save()
            return redirect("dashboard")

    context = {'form': form}

    return render(request, 'webapp/update-record.html', context=context)



# Read / view a singular record

@login_required(login_url='my-login')
def singular_record(request, pk):
    singular_record_instance = Record.objects.get(id=pk)

    context = {'record': singular_record_instance}

    return render(request, 'webapp/view-record.html', context=context)




# delete a record

@login_required(login_url='my-login')
def delete_record(request,pk):

    record = Record.objects.get(id=pk)

    record.delete()

    return redirect("dashboard")