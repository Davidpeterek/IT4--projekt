"""Konfigurace adresy URL mysite

Seznam 'urlpatterns' směruje adresy URL do zobrazení. Další informace naleznete zde:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Příklady:
Zobrazení funkcí
    1. Přidejte import: z my_app importujte pohledy
    2. Přidejte adresu URL do urlpatterns: path('', views.home, name='home')
Zobrazení založená na třídách
    1. Přidejte import: z importu other_app.views
    2. Přidejte adresu URL do urlpatterns: path('', Home.as_view(), name='home')
Včetně dalšího URLconfu
    1. Importujte funkci include(): z django.urls import include, path
    2. Přidejte adresu URL do urlpatterns: path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('', include('main.urls')),
    path('admin/', admin.site.urls),
]
