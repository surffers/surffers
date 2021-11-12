from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator
from apps.feed.models import Category, Bookmark, Vote

from apps.feed.forms import CategoryForm
from apps.profiles.models import Profile
import datetime

from django.http import JsonResponse
from django.contrib.auth.models import User
import json
from apps.core.serializers import UserSerailizer


def userSettings(request):
    user, created = User.objects.get_or_create(id=1)
    setting = user.setting

    seralizer = UserSerailizer(setting, many=False)

    return JsonResponse(seralizer.data, safe=False)


def updateTheme(request):
    data = json.loads(request.body)
    theme = data['theme']

    user, created = User.objects.get_or_create(id=1)
    user.setting.value = theme
    user.setting.save()
    print('Request:', theme)
    return JsonResponse('Updated..', safe=False)

def error_404_view(request, exception):
    return render(request, 'core/404.html')


def settings(request):
    users_list = Profile.objects.all()
    profiles = Profile.objects.filter()

    form = CategoryForm(request.POST, request.FILES)

    if form.is_valid():
        category = form.save(commit=False)
        category.user = request.user
        category.save()  
        return redirect('/')

    context = {
        'profiles': profiles,
        "title": "ListUser",
        "users_list": users_list,
        'form': form,
    }
    return render(request, 'core/settings.html', context)


def test(request):
    date_from = datetime.datetime.now() - datetime.timedelta(days=1)
    user_bookmarks = Bookmark.objects.filter(created_at__gte=date_from).order_by("-number_of_votes")


    userids = [request.user.id]
    categories = Category.objects.filter(user_id__in=userids)

    paginator = Paginator(user_bookmarks, 30)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'categories': categories,
        'user_bookmarks': user_bookmarks,
    }
    return render(request, 'core/tests.html', context)


def sponsor(request):

    context = {

    }
    return render(request, 'core/sponsor.html', context)



@login_required
def dashboard(request):
    # date_from = datetime.datetime.now() - datetime.timedelta(days=1)
    # user_bookmarks = Bookmark.objects.filter(created_at__gte=date_from).order_by("-number_of_votes")

    userids = [request.user.id]
    categories = Category.objects.filter(user_id__in=userids).select_related('user')
    for bookmark in request.user.profile.follows.all():
        userids.append(bookmark.user.id)
    bookmarks = Bookmark.objects.filter(user_id__in=userids).select_related('user', 'category').order_by("-number_of_votes")


    AddCategoryForm = CategoryForm(request.POST, request.FILES)
    if AddCategoryForm.is_valid():
        category = AddCategoryForm.save(commit=False)
        category.user = request.user
        category.save()
        return redirect('dashboard')

    paginator = Paginator(bookmarks, 30)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'bookmarks': bookmarks,
        'categories': categories,
        'AddCategoryForm': AddCategoryForm,
    }
    return render(request, 'core/dashboard.html', context)



def home(request):
    date_from = datetime.datetime.now() - datetime.timedelta(days=1)
    user_bookmarks = Bookmark.objects.filter(created_at__gte=date_from).order_by("-number_of_votes").select_related('user', 'category')

    userids = [request.user.id]
    categories = Category.objects.filter(user_id__in=userids).select_related('user')

    AddCategoryForm = CategoryForm(request.POST, request.FILES)
    if AddCategoryForm.is_valid():
        category = AddCategoryForm.save(commit=False)
        category.user = request.user
        category.save()
        return redirect('category', category_id=userids)

    paginator = Paginator(user_bookmarks, 30)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)



    context = {
        'page_obj': page_obj,
        'user_bookmarks': user_bookmarks,
        'categories': categories,
        'AddCategoryForm': AddCategoryForm,
    }
    return render(request, 'core/home.html', context)





@login_required
def users(request):
    profiles = Profile.objects.all().order_by("-created")  # [0:3]

    userids = [request.user.id]
    categories = Category.objects.filter(user_id__in=userids)

    for bookmark in request.user.profile.follows.all():
        userids.append(bookmark.user.id)
    user_bookmarks = Bookmark.objects.filter(user_id__in=userids).order_by("-created_at")  # [0:3]

    AddCategoryForm = CategoryForm(request.POST, request.FILES)
    if AddCategoryForm.is_valid():
        category = AddCategoryForm.save(commit=False)
        category.user = request.user
        category.save()
        return redirect('dashboard')

    context = {
        'user_bookmarks': user_bookmarks,
        'profiles': profiles,
        'categories': categories,
        'AddCategoryForm': AddCategoryForm,
    }
    return render(request, 'core/users.html', context)




def blog(request):

    context = {


    }
    return render(request, 'core/blog.html', context)