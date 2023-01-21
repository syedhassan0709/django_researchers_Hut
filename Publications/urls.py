from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.homepage,name='home'),
    path('publication_level/',views.publications_level,name='publication_level'),
    path('publication_level/search',views.search,name='search'),
    path('publication_level/(<int:level_id>)/',views.publications_all,name='publication_article'),
    path('aboutus/',views.aboutus,name='aboutus')
    
]
