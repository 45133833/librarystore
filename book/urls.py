from django.urls import path
from .views import *
from django.conf.urls.static import static
from librarystore.settings import DEBUG,STATIC_ROOT,STATIC_URL,MEDIA_ROOT,MEDIA_URL

urlpatterns=[
    path('',index , name='index'),
    path('upload/',upload , name='upload-book'),
    path('update/<int:id>/',update_book ),
    path('delete/<int:id>/',delete_book),
    
]

urlpatterns += static(STATIC_URL , document_root=STATIC_ROOT)
urlpatterns += static(MEDIA_URL , document_root=MEDIA_ROOT)

