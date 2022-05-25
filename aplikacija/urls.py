from django.urls import path
from . import views

urlpatterns = [
    path("",views.start, name="start"),
    path("about_us/",views.about_us, name="about_us"),
    path("interijer/",views.interijer, name="interijer"),
    path("eksterijer/",views.eksterijer, name="eksterijer"),
    path("save_posts/",views.save_posts, name="save_posts"),
    path("post/<slug:slug>", views.SinglePostView.as_view(), name="post-detail-page"),
    path("read-later",views.ReadLaterView.as_view(),name="read-later")
]
