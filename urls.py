from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name = "index"),
    path('contact',views.contact,name ="contact"),
    path('testimonials',views.testimonials,name ="testimonials"),
    path('faq',views.faq,name="faq"),
    path('portfolio',views.portfolio,name ="portfolio"),
    path('register',views.register,name = "register"),
    path('login',views.login,name="login"),
    path('portfoliodetails',views.portfoliodetails,name="portfoliodetails"),
]