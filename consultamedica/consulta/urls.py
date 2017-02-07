from django.conf.urls import include,url
from consulta import views
from django.contrib import admin

urlpatterns = [

   url(r'^$', views.home),
   url(r'^consultas$', views.consultas),
   url(r'^paciente_forms$', views.paciente_forms, name='paciente_forms'),
   url(r'^medico_forms$', views.medico_forms, name='medico_forms'),
   url(r'^medicos$', views.medicos),
   url(r'^pacientes$', views.pacientes),
   url(r'^admin/', include(admin.site.urls)),
]