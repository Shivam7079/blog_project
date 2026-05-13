from rest_framework import serializers

from .models import (
    Post,
    Comment,
    Profile
)


class CommentSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField()

    class Meta:

        model = Comment

        fields = [
            'id',
            'user',
            'text',
            'created_at'
        ]


class PostSerializer(serializers.ModelSerializer):

    total_likes = serializers.ReadOnlyField()

    comments = CommentSerializer(
        many=True,
        read_only=True
    )

    class Meta:

        model = Post

        fields = [
            'id',
            'title',
            'content',
            'image',
            'created_at',
            'total_likes',
            'comments'
        ]


class ProfileSerializer(serializers.ModelSerializer):

    user = serializers.StringRelatedField()

    class Meta:

        model = Profile

        fields = [
            'id',
            'user',
            'bio',
            'profile_image'
        ]