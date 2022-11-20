from rest_framework.routers import DefaultRouter
from django.urls import include, path

from cats.views import CatViewSet

# from cats.views import CatList, CatDetail

# создаем экземпляр класса SimpleRouter
router = DefaultRouter()
# зарегистрируем эндпоинты с помощью метода register()
# парамметры метода register: URL-префикс и название вьюсета,
#  для которого создается набор эндпоинтов
router.register('cats', CatViewSet)
# после регистрации  эндпоинтов надо включить новые эндпоинты
# в список urlpatterns
# перечень эндпоинтов доступен в router.urls
# включим их в головной urls.py
urlpatterns = [
   path('', include(router.urls))
]
# только что созданный роутер сгенерирует два эндпоинта
# теперь через эти эндпоинты доступны любые операции с моделью



# urlpatterns = [
#    path('cats/', CatList.as_view()),
#    path('cats/<int:pk>/', CatDetail.as_view()),
# ]
