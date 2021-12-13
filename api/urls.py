from django.urls import path,include
from . import views
urlpatterns = [
    path('get_lab_details',views.LabDetails.as_view()),
    path('get_insuarance_details',views.InsuaranceDetails.as_view()),
    path('get_transport_details',views.TransportDetails.as_view()),
    path('crop_analysis',views.CropAnalysis.as_view())
]