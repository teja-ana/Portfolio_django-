from django.contrib import admin
from django.urls import path, include
from home import views

#Django admin headeer customisation
admin.site.site_header="Login to Develpoer Krishna_Teja"
admin.site.site_title="Welcome to dashboard"
admin.site.index_title="Welcome to potral"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls'))

]
