import api_views
import views
from django.urls import path
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'api/person', api_views.PersonModelViewSet)
urlpatterns = [
                  path('', views.HomePage.as_view(), name="home"),
                  path('add/', views.AddPhoneFormView.as_view(), name="add_phone"),
                  path('all/', views.AllContacts.as_view(), name="all_contacts"),
                  path('delete/<int:pk>', views.DeletePhoneView.as_view(), name="delete_contact"),
                  path('login/', views.user_login, name="login"),
                  path('logout/', views.user_logout, name="logout"),
                  path('register/', views.register, name="register"),
                  path('feedback/', views.contact, name="feedback"),
                  # path('api/person/', api_views.person_list, name="list-person"),
                  # path('api/person-list/', api_views.PersonListView.as_view(), name="list-person"),
                  # path('api/person-detail/<int:pk>/', api_views.PersonDetailView.as_view(), name="detail-person"),
                  # path('api/person-update/<int:pk>/', api_views.PersonUpdateView.as_view(), name="update-person"),
              ] + router.urls
