from django.urls import path
from . import views

urlpatterns = [
    path('', views.MapView.as_view(), name='map'),
    path('connected-cpe/<int:pk>', views.ConnectedCpeAjaxView.as_view(), name='connected-cpe')
]
