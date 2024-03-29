"""lr URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

import views
from views import *

urlpatterns = [
    path('', views.index),
    path('admin', views.admin),
    path('landfill', views.landfillAdd),
    path('landfill/<int:id>', views.landfill),
    path('landfillDel/<int:id>', views.landfillDel),
    path('landfill/landfillDel/<int:id>', views.landfillDel),
    path('form', views.formAdd),
    path('form/<int:id>', views.formEdit)
]
