from rest_framework.serializers import ModelSerializer
from search_api_app.models import Data

class DataSerializer(ModelSerializer):
    class Meta:
        model = Data
        fields = ['title','content','creator','status','number','dispo','price']