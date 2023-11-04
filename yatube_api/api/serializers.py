from rest_framework import serializers
from rest_framework.relations import SlugRelatedField
from django.core.exceptions import ValidationError

from posts.models import Comment, Post, Group, Follow, User


class PostSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Post


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = '__all__'
        model = Comment
        read_only_fields = ('post',)


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Group


class FollowSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    following = serializers.SlugRelatedField(
        slug_field='username', queryset=User.objects.all(), required=True,)

    class Meta:
        fields = ('user', 'following')
        model = Follow

    def validate_following(self, value):
        user = self.context['request'].user

        if user == value:
            raise ValidationError("Вы не можете подписаться на сами себя.")

        if Follow.objects.filter(user=user, following=value).exists():
            raise ValidationError("Вы уже подписаны на этого пользователя.")

        return value
