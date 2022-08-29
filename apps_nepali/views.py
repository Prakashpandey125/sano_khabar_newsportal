from datetime import datetime, date
from django.db.models import Q

import adbs
import nepali_datetime

from django.shortcuts import render,redirect
#import paginator
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .models import (BreakingNews, Category, StandardNews, MainNews, LatestNews, YoutubeLink, NewsComment)
from  admin_pannel.forms import NewsCommentform


def latest_dates_np(value):
    value = value.strftime('%Y/%m/%d')
    given_date = value
    np_list = adbs.ad_to_bs(given_date)
    np_date = np_list['ne']['year'] + '/' + \
        np_list['ne']['month'] + '/' + np_list['ne']['day']
    return np_date


def index(request):
    category_query = Category.objects.all().order_by('id')
    #current_category = Category.objects.all()

    breaking_query= BreakingNews.objects.all().order_by('id')
    # standard_news_query = StandardNews.objects.all()
    section_1 = StandardNews.objects.filter(
        category__section=1).order_by('-id')
    print(section_1, 'section_1')
    # first_section11 = section_1[0]

    #first_section12 = section_1[1]
    section1_section2 = section_1[2:5]
    print(section1_section2, 'section1_section2...............')
    section_2 = StandardNews.objects.filter(
        category__section=2).order_by('-id')
    print(section_2, 'section_2')
    # first_section21 = section_2[0]
    # print(first_section21, 'first_section21............')
    # first_section22 = section_2[1]
    # print(first_section22, 'first_section22')
    section2_section2 = section_2[2:5]
    section_3 = StandardNews.objects.filter(
        category__section=3).order_by('-id')
    print(section_3, 'section_3.........')
    section3_name = Category.objects.filter(section=3).last()
    # first_section31 = section_3[0]
    # first_section32 = section_3[1]
    # section3_section2 = section_3[2:5]

    today_date = datetime.now
    today_dates = date.today()
    current_time = datetime.now().time().strftime("%H:%M:%S")
    # print(current_time)

    nepali_date = nepali_datetime.datetime.today().strftime('%K-%n-%D (%G) , %i : %l')

    main_news_query = MainNews.objects.all().order_by('-id')[0:2]
    #main_news_query1 = MainNews.objects.all().order_by('-id')[2]
    main_news_query2 = MainNews.objects.all().order_by('-id')[3:7]
    news_query = StandardNews.objects.all().order_by('-id')[0:6]

    youtube_link_query = YoutubeLink.objects.all().order_by('-id')

    context = {'category_query': category_query, 'title': 'होमपेज', 'date': today_date,
               # 'first_section11': first_section11,
               'today_dates': today_dates, 'nepali_date': nepali_date,
               # 'first_section12': first_section12,
               'section1_section2': section1_section2,
               # 'first_section21': first_section21,
               'current_time': current_time,
               # 'first_section22': first_section22,
               'section2_section2': section2_section2,
               'section_3': section_3, 'section3_name': section3_name, 'main_news_query': main_news_query,
               # 'main_news_query1': main_news_query1,
               'main_news_query2': main_news_query2,
               'news_query': news_query,
               'youtube_link_query': youtube_link_query,
               'breaking_query': breaking_query }
    return render(request, 'index.html', context)


def per_page(request, ids):
    
    standard_news_query = StandardNews.objects.get(id=ids)
    
    print(standard_news_query, 'standard_news_query')
    # product = get_object_or_404(StandardNews, id=7)
    # print(product)
    category_query = Category.objects.all().order_by('id')
    today_date = datetime.now
    today_dates = datetime.date
    print(today_dates)
    nepali_date = nepali_datetime.datetime.today().strftime(
        '%K %N %D (%G), %h : %l : %s')
    np_date = latest_dates_np(standard_news_query.date_uploaded)

    news_query = StandardNews.objects.all().order_by('-id')[0:6]

    section_3 = StandardNews.objects.filter(
        category__section=3).order_by('-id')
    print(section_3, 'section_3')
    section3_name = Category.objects.filter(section=3).last()
    print(section3_name, ".......................")

    youtube_link_query = YoutubeLink.objects.all().order_by('-id')
    #to post the commetn in per page news
   
    

    context = {'standard_news_query': standard_news_query, 'title': 'होमपेज', 'category_query': category_query,
               'date': today_date, 'nepali_date': nepali_date, 'np_date': np_date,
               'news_query': news_query, 'section_3': section_3, 'section3_name': section3_name,
               'youtube_link_query': youtube_link_query}
    return render(request, 'per_page_news001.html', context)


#
# def hamro(request):
#     category_query = Category.objects.all().order_by('id')
#     standard_news_query = StandardNews.objects.all()
#     context = {'category_query': category_query, 'title': 'हाम्रो बारेमा', 'standard_news_query': standard_news_query}
#     return render(request, 'index.html', context)

def list_news(request, ids):
    category_query = Category.objects.all().order_by('id')
    current_category = Category.objects.get(id=ids)
    category_news_query = StandardNews.objects.filter(
        Q(category__id=ids) | Q(category__parent_id=ids))
    category_query1 = Category.objects.filter(id=ids).last()
    latest_news_query = LatestNews.objects.all().order_by('-id')[0:6]

    section_3 = StandardNews.objects.filter(
        category__section=3).order_by('-id')
    section3_name = Category.objects.filter(section=3).last()

    youtube_link_query = YoutubeLink.objects.all().order_by('-id')
    paginator_current_news = Paginator(category_news_query, 10)
    page_number_current_news = request.GET.get('page_news_object')
    try:
        page_obj_current_news = paginator_current_news.page(page_number_current_news)
    except PageNotAnInteger:
        page_obj_current_news = paginator_current_news.page(1)
    except EmptyPage:
        page_obj_current_news = paginator_current_news.page(paginator_current_news.num_pages)


    context = {'category_news_query': page_obj_current_news, 'category_query': category_query,'current_category': current_category,
               'category_query1': category_query1, 'latest_news_query': latest_news_query, 'section_3': section_3,
               'section3_name': section3_name, 'youtube_link_query': youtube_link_query}
    return render(request, 'list.html', context)



# function to post commetn in per page news
def post_comment(request,ids):
    if request.method == 'POST':
     form = NewsCommentform(request.POST)
    if form.is_valid():
        user_name = form.cleaned_data['user_name']
        comment = form.cleaned_data['comment']
        email=form.cleaned_data['email']
        #news_id = request.POST.get('news_id')
        #news_id=news_id
        
        news_comment = NewsComment(user_name=user_name, comment=comment, email=email, news_id=ids)
        news_comment.save()
        return redirect('per_page',ids)



    
