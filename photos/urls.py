from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    url(r'^$',views.index,name='index'),
    url(r'^profile/',views.profile,name='profile'),
    url(r'^new/post/', views.new_post, name='new-post'),
    url(r'^profile/edit',views.update_profile,name='edit-profile'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
