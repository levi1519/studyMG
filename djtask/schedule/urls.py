from django.urls import path
from .views import HorarioList, HorarioUpdate,HorarioCreate,HorarioDelete,HorarioDetail

app_name = 'schedule'

urlpatterns = [
    path('schedule_list/', HorarioList.as_view(), name='schedule_list'),
    path('create_schedule/',HorarioCreate.as_view(), name = 'create_schedule'),
    path('schedules/update/<int:pk>/',HorarioUpdate.as_view(),name = 'update_schedule'),
    path('schedules/delete/<int:pk>/', HorarioDelete.as_view(),name = 'delete_schedule' ),
    path('schedules/detail/<int:pk>/', HorarioDetail.as_view(), name='detail_schedule'),

]