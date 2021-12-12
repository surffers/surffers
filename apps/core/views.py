from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator


from apps.feed.models import Category, Bookmark, Tag, Vote

from apps.feed.forms import CategoryForm
from apps.profiles.models import Profile
import datetime





from django.views.generic import TemplateView
from djpaddle.models import Plan


class Checkout(TemplateView):
    template_name = 'checkout.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['paddle_plan'] = Plan.objects.get(pk=kwargs['plan_id'])
        # If you have not added 'djpaddle.context_processors.vendor_id' as a template context processors
        context['DJPADDLE_VENDOR_ID'] = settings.DJPADDLE_VENDOR_ID
        # If you have not added 'djpaddle.context_processors.sandbox' as a template context processors
        context['DJPADDLE_SANDBOX'] = settings.DJPADDLE_SANDBOX


        if self.request.user.has_subscription:
            active_subscription = self.request.user.subscriptions.get(status='active')
            context['subscription'] = active_subscription

        return context

def blog(request):

    context = {

    }
    return render(request, 'core/blog.html', context)



def error_404_view(request, exception):
    return render(request, 'core/404.html')


def test(request):
    date_from = datetime.datetime.now() - datetime.timedelta(days=3)
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


def home(request):
    # date_from = datetime.datetime.now() - datetime.timedelta(days=3)
    # user_bookmarks = Bookmark.objects.filter(created_at__gte=date_from).order_by("-number_of_votes")
    tags = Tag.objects.all()[0:35]
    userids = [request.user.id]
    categories = Category.objects.filter(user_id__in=userids).select_related('user')
    user_bookmarks = Bookmark.objects.all().select_related('user', 'category').order_by("-number_of_votes")[0:3]
    popular_categories = Category.objects.all().select_related('user').order_by("-created_at")[0:3]


    if request.method == 'POST' and 'btnaddcategory' in request.POST:
        form = CategoryForm(request.POST, request.FILES)

        if form.is_valid():
            category = form.save(commit=False)
            category.user = request.user
            category.save()
            return redirect('category_lists')
    else:
        form = CategoryForm()

    AddCategoryForm = CategoryForm(request.POST, request.FILES)
    if AddCategoryForm.is_valid():
        category = AddCategoryForm.save(commit=False)
        category.user = request.user
        category.save()
        return redirect('category_lists')

    context = {
        'tags': tags,
        'user_bookmarks': user_bookmarks,
        'popular_categories': popular_categories,
        'categories': categories,
        'form': form,
        'AddCategoryForm': AddCategoryForm,
    }
    return render(request, 'core/home.html', context)


def followslists(request):
    userids = [request.user.id]
    categories = Category.objects.filter(user_id__in=userids).select_related('user')
    for bookmark in request.user.profile.follows.all():
        userids.append(bookmark.user.id)
    user_bookmarks = Bookmark.objects.filter(user_id__in=userids).select_related('user', 'category')

    AddCategoryForm = CategoryForm(request.POST, request.FILES)
    if AddCategoryForm.is_valid():
        category = AddCategoryForm.save(commit=False)
        category.user = request.user
        category.save()
        return redirect('category_lists')

    paginator = Paginator(user_bookmarks, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'user_bookmarks': user_bookmarks,
        'categories': categories,
        'AddCategoryForm': AddCategoryForm,
    }
    return render(request, 'core/follows-lists.html', context)

def bookmarklists(request):
    userids = [request.user.id]
    categories = Category.objects.filter(user_id__in=userids).select_related('user')
    user_bookmarks = Bookmark.objects.all().select_related('user', 'category', ).order_by("-created_at")

    AddCategoryForm = CategoryForm(request.POST, request.FILES)
    if AddCategoryForm.is_valid():
        category = AddCategoryForm.save(commit=False)
        category.user = request.user
        category.save()
        return redirect('category_lists')

    paginator = Paginator(user_bookmarks, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'user_bookmarks': user_bookmarks,
        'categories': categories,
        'AddCategoryForm': AddCategoryForm,
    }
    return render(request, 'core/bookmarklists.html', context)

def toplists(request):
    user_bookmarks = Bookmark.objects.all().order_by("-number_of_votes")
    userids = [request.user.id]
    categories = Category.objects.filter(user_id__in=userids).select_related('user')

    AddCategoryForm = CategoryForm(request.POST, request.FILES)
    if AddCategoryForm.is_valid():
        category = AddCategoryForm.save(commit=False)
        category.user = request.user
        category.save()
        return redirect('category_lists')

    paginator = Paginator(user_bookmarks, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'user_bookmarks': user_bookmarks,
        'categories': categories,
        'AddCategoryForm': AddCategoryForm,
    }
    return render(request, 'core/toplists.html', context)

def categorylists(request):
    all_categories = Category.objects.all().select_related('user')
    userids = [request.user.id]

    categories = Category.objects.filter(user_id__in=userids).select_related('user')

    AddCategoryForm = CategoryForm(request.POST, request.FILES)
    if AddCategoryForm.is_valid():
        category = AddCategoryForm.save(commit=False)
        category.user = request.user
        category.save()
        return redirect('category_lists')

    paginator = Paginator(all_categories, 30)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'all_categories': all_categories,
        'page_obj': page_obj,

        'categories': categories,
        'AddCategoryForm': AddCategoryForm,
    }
    return render(request, 'core/categorylists.html', context)


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
        return redirect('category_lists')

    context = {
        'user_bookmarks': user_bookmarks,
        'profiles': profiles,
        'categories': categories,
        'AddCategoryForm': AddCategoryForm,
    }
    return render(request, 'core/users.html', context)




