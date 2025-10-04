from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from hworks.views import ActividadesList, ActividadesCreate,ActividadesUpdate,ActividadesDetail,ActividadDelete

app_name = 'hworks'

urlpatterns = [
    path('hworks/activity_list/', ActividadesList.as_view(), name='activity_list'),
    path('hworks/create_activity/', ActividadesCreate.as_view(), name='create_activity'),
    path('hworks/update/<int:pk>/', ActividadesUpdate.as_view(), name='update_activity'),
    path('hworks/delete/<int:pk>/', ActividadDelete.as_view(), name='delete_activity'),
    path('hworks/detail/<int:pk>/', ActividadesDetail.as_view(), name='activity_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
