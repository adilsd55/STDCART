from . import views
from django.urls import path

app_name = 'users'
urlpatterns = [
    # customer rating-feedback view
    path('crf/<int:pc>/', views.CusRatFeed, name='CusRatFeed'),

    # orders
    
]