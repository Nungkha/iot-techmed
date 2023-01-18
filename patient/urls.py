from django.urls import path, include
from . import views
from django.views.i18n import JavaScriptCatalog
# from .views import PatientViewSet
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register(r'Patient', PatientViewSet)


urlpatterns = [
    path('', views.PatientListView.as_view(), name='patient_list'),
    path('patient/<int:pk>', views.PatientDetailView.as_view(), name='patient_detail'),
    path('patient/<int:pk>/edit', views.PatientUpdateView.as_view(), name='patient_update'),
    path('patient/<int:pk>/delete', views.PatientDeleteView.as_view(), name='patient_delete'),
    path('patient/new', views.PatientCreateView.as_view(), name='patient_new'),
    path('patient/<int:pk>/edit/medTaken', views.medTakenView.as_view(), name='med_taken'),


    path('jsi18n', JavaScriptCatalog.as_view(), name='js-catlog'),
    # path("api/", views.routineAPI()),
    # path('', include(router.urls)),
    # path('api-auth/', include('rest_framework.urls'))
    # path('authorized/', views.authorized, name='authorized'),
    path('routine/', views.routine_list)



]