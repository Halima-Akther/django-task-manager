from django.shortcuts import render, redirect, get_object_or_404
from .models import Task
from .forms import TaskForm, RegisterForm
from django.contrib.auth import authenticate, login


# ---------------------------------------
# ✅ TASK LIST (SHOW ALL TASKS)
# ---------------------------------------
def task_list(request):
    tasks = Task.objects.all()

    completed_tasks = tasks.filter(is_completed=True)
    pending_tasks = tasks.filter(is_completed=False)

    print("✅ TOTAL TASKS:", tasks.count())  # DEBUG

    return render(request, 'task_list.html', {
        'completed_tasks': completed_tasks,
        'pending_tasks': pending_tasks,
    })


# ---------------------------------------
# ✅ TASK DETAIL
# ---------------------------------------
def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, 'task_detail.html', {'task': task})


# ---------------------------------------
# ✅ TASK CREATE (FULL DEBUG + SAFE SAVE)
# ---------------------------------------
def task_create(request):
    print("👉 REQUEST METHOD:", request.method)

    if request.method == 'POST':
        form = TaskForm(request.POST)

        print("👉 FORM IS VALID:", form.is_valid())

        if not form.is_valid():
            print("❌ FORM ERRORS:", form.errors)

        if form.is_valid():
            task = form.save(commit=False)

            if request.user.is_authenticated:
                task.user = request.user
                print("✅ USER SET:", request.user.username)
            else:
                print("⚠️ USER NOT LOGGED IN — Saving with NULL USER")

            task.save()
            print("✅✅✅ TASK SAVED SUCCESSFULLY:", task.title)

            return redirect('task_list')
    else:
        form = TaskForm()

    return render(request, 'task_form.html', {'form': form})


# ---------------------------------------
# ✅ TASK UPDATE
# ---------------------------------------
def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            print("✅ TASK UPDATED:", task.title)
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)

    return render(request, 'task_form.html', {'form': form})


# ---------------------------------------
# ✅ TASK DELETE
# ---------------------------------------
def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.method == 'POST':
        print("🗑 DELETING TASK:", task.title)
        task.delete()
        return redirect('task_list')

    return render(request, 'delete.html', {'task': task})


# ---------------------------------------
# ✅ TASK TOGGLE COMPLETE
# ---------------------------------------
def task_toggle_complete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    task.is_completed = not task.is_completed
    task.save()
    print("🔁 TOGGLED TASK:", task.title, "→", task.is_completed)
    return redirect('task_list')


# ---------------------------------------
# ✅ USER REGISTER
# ---------------------------------------
def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()

            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")

            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)

            print("✅ USER REGISTERED:", username)
            return redirect("task_list")
    else:
        form = RegisterForm()

    return render(request, "register.html", {"form": form})









 
   



