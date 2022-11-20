from rest_framework import generics
# from rest_framework.response import Response
# from rest_framework import status

from .models import Cat
from .serializers import CatSerializer


# создаем первый класс на основе дженерика,
# который будет создавать новый объект
# или возвращать всю коллекцию объектов
class CatList(generics.ListCreateAPIView):
    # в этом класса создаем только два поля
    # набор записей, queryset
    queryset = Cat.objects.all()
    # сериализатор
    serializer_class = CatSerializer


# создаем второй класс на основе другого дженерика,
# который возвращает, обновляет, удаляет
# объекты модели по одному
class CatDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cat.objects.all()
    serializer = CatSerializer


# # все операции CRUD при использовании view-классов принято разделять
#  на две группы
# # первая группа(первый класс class APICat) описывает создание нового объекта
# # и запрос всех существующих объектов
# class APICat(APIView):
#     # запрос всех существующих объектов
#     def get(self, request):
#         cats = Cat.objects.all()
#         serializer = CatSerializer(cats, many=True)
#         return Response(serializer.data)
#     # создание нового объекта

#     def post(self, request):
#         serializer = CatSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)


# функция, которая добавляет в БД новую запись
# def cat_list(request):
#     # если метод POST, то
#     # создаем объект сериализатора и передаем в него данные из POST-запроса
#     if request.method == 'POST':
#         serializer = CatSerializer(data=request.data, many=True)
#         # если полученные данные валидны
#         if serializer.is_valid():
#             # то сохраняем данные в базу через метод save()
#             serializer.save()
#             # и возвращаем JSON со всеми данными нового объекта
#             # и статус-код 201
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         # если же данные не валидны, возвращаем инфо об ошибке и
#         # соответствующие данные об ошибке
#         return Response(
# serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     # если же метод GET, то вью-функция должна получить из БД queryset,
#     # в котором будут храниться запрошенные объекты модели
#     cats = Cat.objects.all()
#     # затем queryset нужно сериализовать. Для этого передаем
#     # в сериализатор первым аргументом queryset
#     serializer = CatSerializer(cats, many=True)
#     return Response(serializer.data)
