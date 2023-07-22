import io
from rest_framework import serializers
from .models import Women


# class WomenModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


class WomenSerializer(serializers.ModelSerializer):
    # це поле дає можливість при додаванні нового запису у бд автоматично підвязувати юзера під котрим було здійснено запит
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    class Meta:
        model = Women
        fields = "__all__"

