from django.urls import path, include

from . import views
from .api import EmployeeCreateApi,EmployeeApi,EmployeeUpdateApi,EmployeeDeleteApi


urlpatterns = [
    path('employee_list',views.employee_list,name='employee_list'),
    path('employee_insert/', views.employee_insert, name='employee_insert'),
    path('<int:id>/', views.employee_insert, name='employee_update'),
    path('delete/<int:id>/', views.employee_delete, name='employee_delete'),


    path('api',EmployeeApi.as_view()),
    path('api/create',EmployeeCreateApi.as_view()),
    path('api/update/<int:pk>',EmployeeUpdateApi.as_view()),
    path('api/delete/<int:pk>',EmployeeDeleteApi.as_view()),
    path('login_user/', include('login_user.urls')),
    path('api/password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]