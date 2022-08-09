from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
	path('', views.index, name = "index"),
	path('login', views.signin, name="signin"),
	path('logout', views.signout, name="signout"),
	path('registration', views.registration, name="registration"),
	path('cake/<int:id>', views.get_cake, name="cake"),
	path('cakes', views.get_cakes, name="cakes"),
	path('category/<int:id>', views.get_cake_category, name="category"),
	path('writer/<int:id>', views.get_writer, name = "writer"),
	path("about/",views.AboutView,name="about"),
	path("desigin/",views.Desigin,name="desigin")
]
