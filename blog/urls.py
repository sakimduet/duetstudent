from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),                          # post list
    url(r'^post/(?P<pk>\d+)/$', views.post_detail, name='post_detail'),     # post details
    url(r'^post/new/$', views.post_new, name='post_new'),                   # for new post
    url(r'^post/(?P<pk>\d+)/edit/$', views.post_edit, name='post_edit'),    # post edit
    url(r'^drafts/$', views.post_draft_list, name='post_draft_list'),       # post save as draft
    url(r'^post/(?P<pk>\d+)/publish/$', views.post_publish, name='post_publish'), # add publish button
    url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),    # delete post button
    url(r'^post/(?P<pk>\d+)/comment/$', views.add_comment_to_post, name='add_comment_to_post'), #comment url
    url(r'^comment/(?P<pk>\d+)/approve/$', views.comment_approve, name='comment_approve'),  # comment approve
    url(r'^comment/(?P<pk>\d+)/remove/$', views.comment_remove, name='comment_remove'),     #comment remove url
    url(r'^contact/$', views.contact, name='contact'),
    url(r'^about/$',views.about, name='about'),
    url(r'^mailshow/$',views.mailshow, name='mailshow'),
]
