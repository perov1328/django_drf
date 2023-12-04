"""
URL configuration for config project.

The `urlpatterns` list routes URLs to apiviews. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function apiviews
    1. Add an import:  from my_app import apiviews
    2. Add a URL to urlpatterns:  path('', apiviews.home, name='home')
Class-based apiviews
    1. Add an import:  from other_app.apiviews import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('studies.urls', namespace='studies')),
    path('users/', include('users.urls', namespace='users')),
    path('payment/', include('payment.urls', namespace='payment')),
]
