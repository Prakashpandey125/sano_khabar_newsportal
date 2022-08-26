from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='ap_index'),
    path('dashboard/', views.ap_dashboard, name='ap_dashboard'),
    path('admin_signup_post/', views.admin_signup_post, name='admin_signup_post'),
    path('landing_page/', views.ap_landing_page, name='ap_landing_page'),
    #main page of title name
    path('layout_page/', views.ap_layout_page, name='ap_layout_page'),
    path('sanghiya/', views.ap_sanghiya_page, name='ap_sanghiya_page'),
    path('add_news/', views.ap_add_news, name='ap_add_news'),
    #path('view_breaking_news/', views.ap_view_breaking_news, name='admin_view_breaking_news'),
    

    path('youtube/', views.ap_youtube, name='ap_youtube'),
    path('edit-youtube/<int:ids>', views.edit_youtube_page, name='admin_edit_youtube_page'),
    path('edit_youtube_page_post/<int:ids>', views.edit_youtube_page_post, name='edit_youtube_page_post'),

    path('main_news/', views.ap_main_news_page, name='ap_main_news_page'),
    path('latest_news/', views.ap_latest_news_page, name='ap_latest_news_page'),
#breaking_news
    path('breaking_news/', views.ap_breaking_news_listpage, name='ap_breaking_news_listpage'),
    path('add_breaking_news/', views.ap_add_breaking_news, name='ap_add_breaking_news'),
    path('ap_add_breaking_news_post/', views.ap_add_breaking_news_post, name='ap_add_breaking_news_post'), 
    path('breaking-news/<int:ids>', views.ap_edit_breaking_news_page, name='admin_edit_breaking_news_page'),
    
    path('edit_breaking_news_page_post/<int:ids>', views.edit_breaking_news_page_post,
         name='edit_breaking_news_page_post'),
    path('delete_breaking_news/<int:ids>', views.delete_breaking_news_page, name='admin_delete_breaking_news'),

    path('edit-news/<int:ids>', views.ap_edit_news_page, name='admin_edit_news_page'),

    #done by me
    path('delete_news/<int:ids>', views.delete_youtube_page, name='admin_delete_youtube_page'),
    path('delete_main_news/<int:ids>', views.delete_main_news_page, name='admin_delete_main_news_page'),
    path('delete_latest_news/<int:ids>', views.delete_latest_news_page, name='admin_delete_latest_news'),
    

    path('add_more/', views.ap_add_more_tittle, name='ap_add_more_tittle'),
    path('add_more_post/', views.add_more_post, name='ap_add_more_post'),
    path('add_main_news_btn/', views.add_main_news_btn, name='add_main_news_btn'),
    path('add_youtube_news/', views.ap_add_youtube_news, name='ap_add_youtube_news'),
    path('add_youtube/', views.ap_add_youtube, name='ap_add_youtube'),

    #url to rename category tittle
    path('titles_name/', views.ap_titles_name, name='ap_titles_name'),
    path('ap_rename_tittle_name/', views.ap_rename_category, name='ap_rename_category'),

    # url to ads page 
    path('ap_adding_ads/', views.add_adds, name='add_adds'),
    path('ads_list/', views.ads_list_page, name='ads_list_page'),
    path('adding_ads', views.add_ads_post, name='add_ads_post'),
    path('edit_ads/<int:ids>', views.edit_ads, name='edit_ads'),
    path('edit_ads_post/<int:ids>', views.edit_ads_post, name='edit_ads_post'),
    path('delete_ads/<int:ids>', views.delete_ads_page, name='delete_ads_page'),

# adding_sub_title
    path('into_samachar/', views.ap_into_samachar, name='ap_into_samachar'),

#adding new Details
    path('ap_add_news/', views.ap_add_news, name='ap_add_news'),
    path('ap_add_news_post/', views.ap_add_news_post, name='ap_add_news_post'),
    path('edit_news/<int:ids>', views.ap_edit_news, name='ap_edit_news'),
    path('admin_edit_news_post/<int:ids>', views.ap_edit_news_post, name='ap_edit_news_post'),
    path('delete_news_page/<int:ids>', views.delete_news_page, name='delete_news_page'),

    path('ap_add_sub_title/<int:ids>', views.ap_add_sub_title, name='ap_add_sub_title'),
    path('ap_add_sub_title_post/<int:ids>', views.ap_add_sub_title_post, name='ap_add_sub_title_post'),
    
    



]
