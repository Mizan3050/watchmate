from rest_framework import serializers
from watchlist_app.models import WatchList,StreamPlatform


class WatchListSerializer(serializers.ModelSerializer):

    class Meta:
        model = WatchList
        fields = "__all__"

class StreamPlatformSerializer(serializers.ModelSerializer):

    class Meta:
        model = StreamPlatform
        fields = "__all__"


    # def get_len_name(self, object):
    #     print(object)
    #     return len(object.name)
    
    # def validate(self, data):
    #     if data['name'] == data['description']:
    #         raise serializers.ValidationError("Name and description cannot be same")
    #     else:
    #         return data
    
    # def validate_name(self, name):
    #     if(len(name) < 2):
    #         raise serializers.ValidationError("Name is too Short")
    #     else:
    #         return name



# def name_length(name):
#     if len(name) < 2:
#         raise serializers.ValidationError("Name is too Short")

# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()

#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
#     def validate(self, data):
#         if data['name'] == data['description']:
#             return serializers.ValidationError("Name and description cannot be same")
#         else:
#             return data
    
    # def validate_name(self, name):
    #     if(len(name) < 2):
    #         return serializers.ValidationError("Name is too Short")
    #     else:
    #         return name