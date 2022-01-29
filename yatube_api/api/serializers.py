from rest_framework import serializers

from posts.models import Post, Group, Comment


class PostSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(required=False)

    class Meta:
        model = Post
        fields = ('id', 'text', 'pub_date', 'author', 'image', 'group',)


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description',)


class CommentsSerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField(required=False, read_only=True)
    post = serializers.PrimaryKeyRelatedField(queryset=Post.objects.all(),
                                              required=False
                                              )

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created',)
