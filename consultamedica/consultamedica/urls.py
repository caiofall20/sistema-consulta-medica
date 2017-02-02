"""consultamedica URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from consulta.views import model_forms

urlpatterns = [
	url(r'^',include('consulta.urls')),
	url(r'^admin/', admin.site.urls),
    url(r'medico_forms$', model_forms, name='medico_forms'),
	url(r'^django-model-forms/$', model_forms, name='consulta_model_forms_django'),
    url(r'^paciente_forms$', model_forms, name='paciente_forms'),
   
   ]
