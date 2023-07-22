# castome permissions
# has_permission - дозводяє налаштовувати права доступу на рівні всього запиту від клієнту від клієнтів
# has_object_permission - права доступу на рівні окремого обєкту
from rest_framework import permissions


# продивлятися може коден а видаляти може тільки адмін
class IsAdminOrReadOnly(permissions.BasePermission):
    # переопределчєм метод
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            # дажмо доступ усім
            return True
        # перевіряю що користквач зайшов як адміністратор
        return bool(request.user and request.user.is_staff)


# Змінювати зможк тільки власник
class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        print(f'{obj.user=}')
        print(f'{request.user=}')
        if request.method in permissions.SAFE_METHODS:
            return True
        # user - назва поля в бд
        return obj.user == request.user
    