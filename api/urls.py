from django.urls import path

from . import views

urlpatterns = [
    path('v1/data', views.DataList.as_view()),
    path('v1/data/<str:iso_code>', views.DataDetail.as_view()),
    path('v1/country', views.CountryList.as_view()),

    path('fn/data', views.getData),
    path('fn/data/<str:iso_code>', views.getDataByIsoCode)
]