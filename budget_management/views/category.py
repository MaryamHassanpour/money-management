from rest_framework.viewsets import ModelViewSet
from ..serializers.category import CategorySerializer
from ..models.category import Category

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    def initial(self, request, *args, **kwargs):
        request.data.update({'user': request.user})
        return super().initial(request, *args, **kwargs)
    
    def get_queryset(self):
        queryset = super().get_queryset()
        search = self.request.query_params.get('search')
        if search:
            queryset = queryset.filter(name__contains=search)
        return queryset
