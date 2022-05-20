from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    path('reports', views.report_list),
    path('reports/<int:user_id>', views.report_list),
    path('reports/report/<int:pk>', views.report_detail),
    path('users', views.user_list),
    path('users/<int:pk>', views.user_detail),
]


urlpatterns = format_suffix_patterns(urlpatterns)
