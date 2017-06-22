from django.conf.urls import url
from .views import laptop, index, pc, ProductDetail

urlpatterns = [
	url(r"^$", index, name="index"),
	url(r"^pc/$", pc, name="pc" ),
	url(r"^pc/laptops/$", laptop.all_laptop, name="laptop"),
	url(r"^pc/laptops/simple/$", laptop.simple, name="simple"),
	url(r"^pc/laptops/universal/$", laptop.universal, name="universal"),
	url(r"^pc/laptops/lungs/$", laptop.lungs, name="lungs"),
	url(r"^pc/laptops/gaming/$", laptop.gaming, name="gaming"),
	url(r"^pc/laptops/detail/(?P<product_id>\d+)/$", ProductDetail, name="detail"),
]