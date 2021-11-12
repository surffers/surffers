from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages

import datetime
from .models import Category, Bookmark, Vote
from apps.profiles.models import Profile
from .forms import CategoryForm, BookmarkForm



@login_required
def vote(request, bookmark_id):
    bookmarks = get_object_or_404(Bookmark, pk=bookmark_id)

    next_page = request.GET.get('next_page', '')

    if bookmarks.user != request.user and not Vote.objects.filter(user=request.user, bookmark=bookmarks):
        vote = Vote.objects.create(bookmark=bookmarks, user=request.user)

    if next_page == 'detail':
        return redirect('detail', bookmark_id=bookmark_id)
    else:
        return redirect('/')


def detail(request, bookmark_id):
    bookmark = get_object_or_404(Bookmark, pk=bookmark_id)
    userids = [request.user.id]
    category = Category.objects.filter(user_id__in=userids).select_related('user')

    context = {
        'bookmark': bookmark,
        'category': category,
    }

    return render(request, 'feed/detail.html', context)


def category(request, category_id):
    bookmarks = Bookmark.objects.all()
    category = Category.objects.get(id=category_id)

    profiles = Profile.objects.all().order_by("-created")[0:3]

    userids = [request.user.id]
    categories = Category.objects.filter(user_id__in=userids).order_by("-created_at")  # [0:3]
    # for bookmark in request.user.profile.follows.all():
    #     userids.append(bookmark.user.id)


    if request.method == 'POST':
        form = BookmarkForm(request.POST, request.FILES)
        if form.is_valid():
            bookmark = form.save(commit=False)
            bookmark.user = request.user
            bookmark.category_id = category_id
            bookmark.save()
            form.save_m2m()
            return redirect('category', category_id=category_id)
    else:
        form = BookmarkForm()



    if request.method == 'POST' and 'btnedit' in request.POST:
        FormEdit = CategoryForm(request.POST, request.FILES, instance=category)
        if FormEdit.is_valid():
            FormEdit.save()
            return redirect('category', category_id=category_id)
    else:
        FormEdit = CategoryForm(instance=category)



    AddCategoryForm = CategoryForm(request.POST, request.FILES)
    if AddCategoryForm.is_valid():
        category = AddCategoryForm.save(commit=False)
        category.user = request.user
        category.save()
        return redirect('category', category_id=category_id)

    context = {
        'profiles': profiles,
        'categories': categories,
        'bookmarks': bookmarks,
        'category': category,
        'form': form,
        'AddCategoryForm': AddCategoryForm,
        'FormEdit': FormEdit,
    }

    return render(request, 'feed/category.html', context)


@login_required
def category_add(request, category_id):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)

        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()   

            messages.success(request, 'Category created!')

            return redirect('category', category_id=category_id)
    else:
        form = CategoryForm()

    context = {
        'form':form,
    }

    return render(request, 'feed/category_add.html', context)

        

@login_required
def category_edit(request, category_id):

    if request.method == 'POST':
        FormEdit = CategoryForm(request.POST, request.FILES, instance=category)
        if FormEdit.is_valid():
            FormEdit.save()
            messages.success(request, 'Changes saved!')
            return redirect('category', category_id=category_id)
    else:
        FormEdit = CategoryForm(instance=category)

    context = {
        'FormEdit': FormEdit,
    }

    return render(request, 'feed/category_edit.html', context)


@login_required
def category_delete(request, category_id):
    category = Category.objects.filter(user=request.user).get(id=category_id)
    category.delete(request.POST, request.FILES)

    messages.success(request, 'Category removed!')

    return redirect('/')



@login_required
def bookmark_add(request, category_id):
    if request.method == 'POST':
        form = BookmarkForm(request.POST, request.FILES)

        if form.is_valid():
            bookmark = form.save(commit=False)
            bookmark.user = request.user
            bookmark.category_id = category_id
            bookmark.save()
            form.save_m2m()

            messages.success(request, 'Bookmark added!')

            return redirect('category', category_id=category_id)
    else:
        form = BookmarkForm()

    context = {
        'form': form,
    }

    return render(request, 'feed/add_bookmark.html', context)


@login_required
def bookmark_delete(request, category_id, bookmark_id):
    bookmark = Bookmark.objects.filter(user=request.user).get(pk=bookmark_id)
    bookmark.delete(request.FILES)

    messages.success(request, 'Bookmark deleted!')

    return redirect('category', category_id=category_id)






