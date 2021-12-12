from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .models import Profile
from apps.feed.models import Category, Bookmark

from .forms import ProfileForm
from apps.feed.forms import CategoryForm







def profile(request, username):
    user = get_object_or_404(User, username=username)
    user_bookmarks = Bookmark.objects.filter(user=user).select_related('user', 'category')

    categories = Category.objects.filter(user=user).select_related('user')

    number_of_votes = 0

    for bookmark in user.bookmarks.all():
        number_of_votes = number_of_votes + (bookmark.number_of_votes - 1)

    if request.method == 'POST' and 'btnformprofile' in request.POST:
        UserEditForm = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if UserEditForm.is_valid():
            UserEditForm.save() 
            return redirect('profile', username=request.user.username)
    else:
        UserEditForm = ProfileForm(instance=user.profile)
   


    AddCategoryForm = CategoryForm(request.POST, request.FILES)
    if AddCategoryForm.is_valid():
        category = AddCategoryForm.save(commit=False)
        category.user = request.user
        category.save()
        return redirect('category_lists')

    context = { 
        'user': user,
        'number_of_votes': number_of_votes,
        'categories': categories,
        'user_bookmarks': user_bookmarks,
        'UserEditForm': UserEditForm,
        'AddCategoryForm': AddCategoryForm,
    }

    return render(request, 'profiles/profile.html', context)



@login_required
def edit_profile(request):
    if request.method == 'POST':
        UserEditForm = ProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if UserEditForm.is_valid():
            UserEditForm.save()
            return redirect('profile', username=request.user.username)
    else:
        UserEditForm = ProfileForm(instance=request.user.profile)
    
    context = {
        'user': request.user,
        'UserEditForm': UserEditForm
    }

    return render(request, 'profiles/edit_profile.html', context)



@login_required
def follow_user(request, username):
    user = get_object_or_404(User, username=username)
    request.user.profile.follows.add(user.profile)

    return redirect('profile', username=username)


@login_required
def unfollow_user(request, username):
    user = get_object_or_404(User, username=username)

    request.user.profile.follows.remove(user.profile)

    return redirect('profile', username=username)

@login_required
def followers(request, username):
    user = get_object_or_404(User, username=username)
    bookmarks = user.bookmarks.all().select_related('user')
    categories = Category.objects.filter(user=user)


    if request.method == 'POST' and 'btnformprofile' in request.POST:
        UserEditForm = ProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if UserEditForm.is_valid():
            UserEditForm.save()
            return redirect('profile', username=request.user.username)
    else:
        UserEditForm = ProfileForm(instance=user.profile)

    AddCategoryForm = CategoryForm(request.POST, request.FILES)
    if AddCategoryForm.is_valid():
        category = AddCategoryForm.save(commit=False)
        category.user = request.user
        category.save()
        return redirect('dashboard')

    context = {
        'user': user,
        'bookmarks': bookmarks,
        'categories': categories,
        'UserEditForm': UserEditForm,
        'AddCategoryForm': AddCategoryForm,
    }

    return render(request, 'profiles/followers.html', context)

@login_required
def follows(request, username):
    user = get_object_or_404(User, username=username)
    profiles = Profile.objects.all().order_by("-created")  # [0:3]
    bookmarks = user.bookmarks.all().order_by("-created_at")#[0:5]
    categories = Category.objects.filter(user=user)

    if request.method == 'POST' and 'btnformprofile' in request.POST:
        UserEditForm = ProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if UserEditForm.is_valid():
            UserEditForm.save()
            return redirect('profile', username=request.user.username)
    else:
        UserEditForm = ProfileForm(instance=user.profile)

    AddCategoryForm = CategoryForm(request.POST, request.FILES)
    if AddCategoryForm.is_valid():
        category = AddCategoryForm.save(commit=False)
        category.user = request.user
        category.save()
        return redirect('dashboard')

    context = {
        'user': user,
        'profiles': profiles,
        'bookmarks': bookmarks,
        'categories': categories,
        'UserEditForm': UserEditForm,
        'AddCategoryForm': AddCategoryForm,
    }
    
    return render(request, 'profiles/following.html', context)



@login_required
def categories(request, username):
    user = get_object_or_404(User, username=username)
    profiles = Profile.objects.all().order_by("-created")[0:3]
    bookmarks = user.bookmarks.all()
    categories = Category.objects.filter(user=user)

    number_of_votes = 0
    for bookmark in user.bookmarks.all():
        number_of_votes = number_of_votes + (bookmark.number_of_votes - 1)

    if request.method == 'POST' and 'btnformprofile' in request.POST:
        UserEditForm = ProfileForm(request.POST, request.FILES, instance=request.user.profile)

        if UserEditForm.is_valid():
            UserEditForm.save()
            return redirect('profile', username=request.user.username)
    else:
        UserEditForm = ProfileForm(instance=user.profile)

    AddCategoryForm = CategoryForm(request.POST, request.FILES)
    if AddCategoryForm.is_valid():
        category = AddCategoryForm.save(commit=False)
        category.user = request.user
        category.save()
        return redirect('dashboard')

    context = {
        'number_of_votes': number_of_votes,
        'user': user,
        'profiles': profiles,
        'bookmarks': bookmarks,
        'categories': categories,
        'UserEditForm': UserEditForm,
        'AddCategoryForm': AddCategoryForm,
    }
    return render(request, 'profiles/categories.html', context)

