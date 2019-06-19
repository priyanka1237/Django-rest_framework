from django.urls import path,include

from django.contrib import admin
from frame1.views import snippet_list,snippet_detail
from rest_framework.urlpatterns import format_suffix_patterns
admin.autodiscover()

urlpatterns = [
    
    path('frame1/',include('frame1.urls')),
    path('admin/',admin.site.urls),
    path('snippets/', snippet_list),
    path('snippets/<int:pk>/',snippet_detail),
    path('api-auth/', include('rest_framework.urls')),
]
urlpatterns = format_suffix_patterns(urlpatterns)
