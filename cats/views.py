from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Cat, Owner, Achievement
from .serializers import OwnerSerializer, AchievementSerializer
from .serializers import CatSerializer, CatListSerializer


class UpdateDeleteViewSet(mixins.UpdateModelMixin, mixins.DestroyModelMixin, viewsets.GenericViewSet):
    pass


class CreateRetrieveViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin,
                            viewsets.GenericViewSet):
    pass


class LightCatViewSet(CreateRetrieveViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer

    @action(detail=False, url_path='recent-black-cats')
    def recent_black_cats(self, requests):
        cats = Cat.objects.filter(color='Black')[:5]
        serializer = self.get_serializer(cats, many=True)
        return Response(serializer.data)


    def get_serializer_class(self):
        # Если запрошенное действие (action) — получение списка объектов ('list')
        if self.action == 'list':
            # ...то применяем CatListSerializer
            return CatListSerializer
        # А если запрошенное действие — не 'list', применяем CatSerializer
        return CatSerializer


class OwnerViewSet(viewsets.ModelViewSet):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer


class AchievementViewSet(viewsets.ModelViewSet):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer