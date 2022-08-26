import json
from unicodedata import category, name
from django.contrib import messages
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import context
from django.contrib.auth import authenticate, login
from .forms import LoginForm, EditBreakingNews, EditNews, EditYoutube, AddCategoryNepali, RenameCategory, \
    Advertisement_Form, AddSubTitle_Form
from apps_nepali.models import Advertisement, BreakingNews, Category, MainNews, LatestNews, YoutubeLink, StandardNews, \
    AddSubTitle


# Create your views here.

def index(request):
    form = LoginForm()
    context = {'form': form}
    return render(request, 'admin_pannel/login_page.html', context)


def admin_signup_post(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('ap_dashboard')
        else:
            messages.error(request, 'Invalid Credentials')
            return redirect('ap_index')


def ap_dashboard(request):
    return render(request, 'admin_pannel/AdminPanel_dashboard.html')


def ap_layout_page(request):
    category_query = Category.objects.all().order_by('-id')
    context = {'category_query': category_query}
    return render(request, 'admin_pannel/landing_page.html', context)


def ap_landing_page(request):
    category_query = Category.objects.all()
    context = {'category_query': category_query}
    return render(request, 'admin_pannel/AdminPanel_landingpage.html', context)


# Adding Category Starts


def ap_add_more_tittle(request):
    category_query = Category.objects.all()
    form = AddCategoryNepali()
    context = {'category_query': category_query, 'form': form}
    # context = {'category_query': category_query, 'form': form , 'category_id':ids}
    return render(request, 'admin_pannel/AdminPanel_addmoretitle.html', context)


def add_more_post(request):
    if request.method == 'POST':
        form = AddCategoryNepali(request.POST)
        if form.is_valid():
            category_name = form.cleaned_data.get('name')
            is_active = form.cleaned_data.get('is_active')
            section_num = request.POST.get('_section')

            print(section_num)
            if section_num == '':
                category_query = Category.objects.create(
                    name=category_name, is_active=is_active)
                category_query.save()
                return redirect('ap_layout_page')
            else:
                section_check = Category.objects.filter(section=section_num)
                if section_check:
                    return redirect('ap_layout_page')
                else:
                    category_query = Category.objects.create(
                        name=category_name, is_active=is_active, section=section_num)
                    category_query.save()
                    return redirect('ap_layout_page')

        else:
            print(form.errors)
            return redirect('ap_layout_page')


# Adding category ends

def ap_layout_page(request):
    category_query = Category.objects.filter(level=0).order_by('-id')
    context = {'category_query': category_query}

    return render(request, 'admin_pannel/landing_page.html', context)


def ap_sanghiya_page(request):
    category_query = Category.objects.all()
    context = {'category_query': category_query}
    return render(request, 'admin_pannel/into_sangiya.html', context)


# Youtube Section Starts


def ap_youtube(request):
    category_query = Category.objects.all().order_by('-id')
    youtube_query = YoutubeLink.objects.all().order_by('-id')
    context = {'youtube_query': youtube_query,
               'category_query': category_query}
    return render(request, 'admin_pannel/youtube/youtube_page.html', context)


# page to add youtube news


def ap_add_youtube(request):
    category_query = Category.objects.all()
    youtube_query = YoutubeLink.objects.all().order_by('-id')
    form = EditYoutube()
    context = {'category_query': category_query,
               'youtube_query': youtube_query, 'form': form}
    return render(request, 'admin_pannel/youtube/add_youtube_news.html', context)


# adding youtube news


def ap_add_youtube_news(request):
    if request.method == 'POST':
        form = EditYoutube(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            link = form.cleaned_data.get('link')
            is_active = form.cleaned_data.get('is_active')

            youtube_query = YoutubeLink.objects.create(
                title=title, link=link, is_active=is_active)
            youtube_query.save()
            return redirect('ap_youtube')
        else:
            print(form.errors)

            return redirect('ap_add_youtube')


def edit_youtube_page(request, ids):
    youtube_query = YoutubeLink.objects.get(id=ids)
    form = EditYoutube(instance=youtube_query)
    context = {'form': form, 'youtube_query': youtube_query}
    return render(request, 'admin_pannel/youtube/edit_youtube.html', context)


def edit_youtube_page_post(request, ids):
    if request.method == 'POST':
        form = EditYoutube(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            link = form.cleaned_data.get('link')
            is_active = form.cleaned_data.get('is_active')

            youtube_query = YoutubeLink.objects.get(id=ids)

            youtube_query.title = title
            youtube_query.link = link
            youtube_query.is_active = is_active

            youtube_query.save()

            return redirect('ap_adds_plus_breakingnews')

        else:
            print(form.errors)


def delete_youtube_page(request, ids):
    youtube_query = YoutubeLink.objects.get(id=ids)
    youtube_query.delete()
    return redirect('ap_adds_plus_breakingnews')


# Youtube Section Ends


def ap_edit_breaking_news_page(request, ids):
    category_query = Category.objects.all()
    breaking_news_query = BreakingNews.objects.get(id=ids)
    form = EditBreakingNews(instance=breaking_news_query)
    context = {'form': form, 'breaking_news_query': breaking_news_query,
               'category_query': category_query}
    return render(request, 'admin_pannel/breaking_news/edit_breaking_news.html', context)


def edit_breaking_news_page_post(request, ids):
    if request.method == 'POST':
        form = EditBreakingNews(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            is_active = form.cleaned_data.get('is_active')

            breaking_news_query = BreakingNews.objects.get(id=ids)

            breaking_news_query.title = title
            breaking_news_query.is_active = is_active

            breaking_news_query.save()

            return redirect('ap_breaking_news')

        else:
            print(form.errors)


def ap_main_news_page(request):
    category_query = Category.objects.all()

    main_news_query = MainNews.objects.all().order_by('-id')

    context = {'category_query': category_query,
               'main_news_query': main_news_query}
    return render(request, 'admin_pannel/main_news/index.html', context)

def ap_latest_news_page(request):
    news_query = StandardNews.objects.all().order_by('-time_uploaded')
    form = EditNews(request.POST)
    category_query = Category.objects.all()
    # latest_news_query = LatestNews.objects.all().order_by('-time_uploaded')
    # latest_news_query = LatestNews.objects.create(title=title, editor_name=editor_name, location=location,
    #                                               news_summary=news_summary, description=description,
    #                                               is_active=is_active, photo_img=photo_img)
    # standard_news_query = StandardNews.objects.all().order_by('-id')
    context = {'category_query': category_query, 'form': form, 'news_query': news_query,
               # 'latest_news_query': latest_news_query
               # 'standard_news_query': standard_news_query
               }
    return render(request, 'admin_pannel/latestnews/index.html', context)


def delete_latest_news_page(request, ids):
    latest_news_query = StandardNews.objects.get(id=ids)
    latest_news_query.delete()
    return redirect('ap_latest_news_page')


def ap_edit_news_page(request, ids):
    category_query = Category.objects.all()
    news_query = StandardNews.objects.get(id=ids)
    form = EditNews(instance=news_query)
    context = {'form': form, 'news_query': news_query,
               'category_query': category_query}
    return render(request, 'admin_pannel/edit_news.html', context)


# breaking_news
def ap_breaking_news_listpage(request):
    category_query = Category.objects.all()
    breaking_query = BreakingNews.objects.all().order_by('-id')
    context = {'category_query': category_query,
               'breaking_query': breaking_query}
    return render(request, 'admin_pannel/breaking_news/breaking_news_page.html', context)


def ap_add_breaking_news(request):
    category_query = Category.objects.all()
    breaking_query = BreakingNews.objects.all().order_by('-id')
    form = EditBreakingNews()
    context = {'category_query': category_query,
               'breaking_query': breaking_query, 'form': form}
    return render(request, 'admin_pannel/breaking_news/add_breaking_news.html', context)


# adding breaking new post
def ap_add_breaking_news_post(request):
    if request.method == 'POST':
        form = EditBreakingNews(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')

            breaking_news_query = BreakingNews.objects.create(title=title)

            breaking_news_query.save()

            return redirect('ap_breaking_news_listpage')

        else:
            print(form.errors)


def ap_edit_breaking_news_page(request, ids):
    category_query = Category.objects.all()
    breaking_news_query = BreakingNews.objects.get(id=ids)
    form = EditBreakingNews(instance=breaking_news_query)
    context = {'form': form, 'breaking_news_query': breaking_news_query,
               'category_query': category_query}
    return render(request, 'admin_pannel/breaking_news/edit_breaking_news.html', context)


def edit_breaking_news_page_post(request, ids):
    if request.method == 'POST':
        form = EditBreakingNews(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            is_active = form.cleaned_data.get('is_active')

            breaking_news_query = BreakingNews.objects.get(id=ids)

            breaking_news_query.title = title
            breaking_news_query.is_active = is_active

            breaking_news_query.save()

            return redirect('ap_breaking_news_listpage')

        else:
            print(form.errors)


def delete_breaking_news_page(request, ids):
    breaking_news_query = BreakingNews.objects.get(id=ids)
    breaking_news_query.delete()
    return redirect('ap_breaking_news_listpage')


def delete_main_news_page(request, ids):
    main_news_query = MainNews.objects.get(id=ids)
    main_news_query.delete()
    return redirect('ap_main_news_page')


# shift news to main news


def add_main_news_btn(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        product_id = data['mainnewsId']
        print(product_id)

        standard_query = StandardNews.objects.filter(id=product_id).last()
        print(standard_query)

        main_news_check = MainNews.objects.filter(
            standard_news=standard_query).last()
        if main_news_check:
            print('already exist')
        else:
            main_news_query = MainNews.objects.create(
                standard_news=standard_query)
            main_news_query.save()


# adding_adds
def edit_ads(request):
    category_query = Category.objects.all()
    context = {'category_query': category_query}
    return render(request, 'admin_pannel/ads/edit_ads.html', context)


def ads_list_page(request):
    category_query = Category.objects.all()
    ads_query = Advertisement.objects.all().order_by('-id')
    context = {'category_query': category_query, 'ads_query': ads_query}
    return render(request, 'admin_pannel/ads/for_adds.html', context)


def add_adds(request):
    category_query = Category.objects.all()
    ads_query = Advertisement.objects.all().order_by('-id')
    form = Advertisement_Form(request.POST)
    context = {'category_query': category_query,
               'ads_query': ads_query, 'form': form}
    return render(request, 'admin_pannel/ads/add_ads.html', context)


# adding new advertisement


def add_ads_post(request):
    if request.method == 'POST':
        form = Advertisement_Form(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            print(title, '................')
            photo_img = form.cleaned_data.get('photo_img')
            print(photo_img, '................')
            ads_query = Advertisement.objects.create(
                title=title, photo_img=photo_img)
            ads_query.save()
            return redirect('ads_list_page')
        else:
            print(form.errors)
            return redirect('ap_add_ads')


def edit_ads(request, ids):
    category_query = Category.objects.all()
    ads_query = Advertisement.objects.get(id=ids)
    form = Advertisement_Form(instance=ads_query)
    context = {'form': form, 'ads_query': ads_query,
               'category_query': category_query}
    return render(request, 'admin_pannel/ads/edit_ads.html', context)


def edit_ads_post(request, ids):
    if request.method == 'POST':
        form = Advertisement_Form(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            print(title, '................')
            photo_img = form.cleaned_data.get('photo_img')
            print(photo_img, '................')
            ads_query = Advertisement.objects.get(id=ids)
            ads_query.title = title
            ads_query.photo_img = photo_img
            ads_query.save()
            return redirect('ads_list_page')
        else:
            print(form.errors)
            return redirect('ap_add_ads')


def delete_ads_page(request, ids):
    ads_query = Advertisement.objects.get(id=ids)
    ads_query.delete()
    return redirect('ads_list_page')


# Category title name page starts


def ap_titles_name(request):
    category_query = Category.objects.all()
    form = RenameCategory()
    context = {'category_query': category_query, 'form': form}
    return render(request, 'admin_pannel/AdminPanel_titlesname.html', context)


# renaming category name
def ap_rename_category(request):
    form = RenameCategory()
    if request.method == 'POST':
        form = RenameCategory(request.POST)
        if form.is_valid():
            category_id = request.POST.get('category_ids')
            category_name = form.cleaned_data.get('name')
            print(category_name, '................')
            rename_query = Category.objects.filter(id=category_id).last()
            rename_query.name = category_name
            rename_query.save()
            return redirect('ap_titles_name')


# Subt_title_Section
def ap_into_samachar(request):
    category_query = Category.objects.all()
    context = {'category_query': category_query}
    return render(request, 'admin_pannel/into_samachar.html', context)


# add_news page
def ap_add_news(request):
    # category_query = Category.objects.filter(parent_id=ids)
    category_query = Category.objects.all()
    news_query = StandardNews.objects.all().order_by('-id')
    form = EditNews(request.POST)
    context = {'category_query': category_query,
               'news_query': news_query, 'form': form, }
    return render(request, 'admin_pannel/sub-category/add_news.html', context)


# add_news post


def ap_add_news_post(request):
    if request.method == 'POST':
        form = EditNews(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            print(title, '................')
            editor_name = form.cleaned_data.get('editor_name')
            print(editor_name, '................')
            location = form.cleaned_data.get('location')
            print(location, '................')
            news_summary = form.cleaned_data.get('news_summary')
            print(news_summary, '................')
            description = form.cleaned_data.get('description')
            category = form.cleaned_data.get('category')
            print(category, '................')
            is_active = form.cleaned_data.get('is_active')
            photo_img = form.cleaned_data.get('photo_img')
            date_time_picker = form.cleaned_data.get('date_time_picker')
            # time_uploaded = form.cleaned_data.get('time_uploaded')
            # number_of_views = form.cleaned_data.get('number_of_views')
            news_query = StandardNews.objects.create(title=title, editor_name=editor_name, location=location,
                                                     news_summary=news_summary, description=description,
                                                     is_active=is_active, category=category, photo_img=photo_img)
            # latest_news_query = LatestNews.objects.create(date_time_picker=date_time_picker,
            #                                               time_uploaded=time_uploaded, number_of_views=number_of_views)
            # print(latest_news_query)

            news_query.save()
            # latest_news_query.save()
            return redirect('ap_add_sub_title', ids=category.id)
        else:
            print(form.errors)


# edit_news page
def ap_edit_news(request, ids):
    category_query = Category.objects.all()
    news_query = StandardNews.objects.get(id=ids)
    form = EditNews(instance=news_query)
    context = {'form': form, 'news_query': news_query,
               'category_query': category_query}
    return render(request, 'admin_pannel/sub-category/edit_news.html', context)


def ap_edit_news_post(request, ids):
    if request.method == 'POST':
        form = EditNews(request.POST, request.FILES)
        if form.is_valid():
            title = form.cleaned_data.get('title')
        print(title, '................')
        editor_name = form.cleaned_data.get('editor_name')
        location = form.cleaned_data.get('location')
        news_summary = form.cleaned_data.get('news_summary')
        print(news_summary, '................')
        description = form.cleaned_data.get('description')
        category = form.cleaned_data.get('category')
        print(category, '................')
        is_active = form.cleaned_data.get('is_active')
        photo_img = form.cleaned_data.get('photo_img')
        news_query = StandardNews.objects.get(id=ids)
        news_query.title = title
        news_query.editor_name = editor_name
        news_query.location = location
        news_query.news_summary = news_summary
        news_query.description = description
        news_query.category = category
        news_query.is_active = is_active
        news_query.photo_img = photo_img
        news_query.save()
        return redirect('ap_add_sub_title', news_query.category.id)
    else:

        print("error")
        return redirect('ap_dashboard')


# delete news page


def delete_news_page(request, ids):
    news_query = StandardNews.objects.get(id=ids)
    news_query.delete()
    return redirect('ap_add_sub_title', ids=news_query.category.id)


def ap_add_sub_title(request, ids):
    current_query = Category.objects.filter(id=ids).last()
    category_query = Category.objects.filter(parent_id=ids).order_by('-id')

    news_query = StandardNews.objects.filter(category=current_query)
    print(category_query, '................')
    form = AddSubTitle()
    print(ids, '................')
    context = {'category_query': category_query, 'form': form, 'category_id': ids,
               'news_query': news_query, 'current_query': current_query}
    return render(request, 'admin_pannel/sub-category/Add_sub_title.html', context)


# adding new sub-title


def ap_add_sub_title_post(request, ids):
    if request.method == 'POST':
        form = AddSubTitle_Form(request.POST)
        if form.is_valid():
            name = form.cleaned_data.get('title')
            print(name, '......t..........')
            current_catergory = Category.objects.get(id=ids)
            sub_title_query = Category.objects.create(name=name, parent=current_catergory)
            sub_title_query.save()
            print(ids)
            return redirect('ap_add_sub_title', ids)
        else:
            print(form.errors)
