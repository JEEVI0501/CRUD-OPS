from django.urls import re_path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns=[
    re_path(r'^department$',views.deptApi),
    re_path(r'^department/([0-9]+)$',views.deptApi),

    re_path(r'^employee$',views.employeesApi),
    re_path(r'^employee/([0-9]+)$',views.employeesApi),

    re_path(r'^Employee/SaveFile$',views.SaveFile)

] + static(settings.ASSET_URL, document_root = settings.ASSET_ROOT)