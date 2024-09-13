from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users.views import custom_logout
import food.views as foodview
from users import views as user_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', foodview.index, name="index"),
    path('food/', include('food.urls')),
    path('register/', user_views.register, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name="login"),
    # path('logout/', auth_views.LogoutView.as_view(template_name='logout.html'), name="logout"),
    path('logout/', custom_logout, name='logout'),
    path('profile/', user_views.profilepage, name="profile")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
