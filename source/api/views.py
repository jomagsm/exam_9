from django.shortcuts import render, get_object_or_404
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import ensure_csrf_cookie
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from webapp.models import Photo, Favorites


class AddFavoriteView(APIView):
    permission_classes = [IsAuthenticated]

    @method_decorator(ensure_csrf_cookie)
    def post(self, request, pk=None):
        print('dsflsdlgklgsklsgdlkdgsjkldsglkjdsgjkldsgkjldgjksl')
        photo = get_object_or_404(Photo, pk=pk)
        created = Favorites.objects.get_or_create(photo=photo, user=request.user)
        if created:
            photo.save()
            return Response({'pk': pk})
        else:
            return Response(status=403)


class RemoveFavoritesView(APIView):
    permission_classes = [IsAuthenticated]

    @method_decorator(ensure_csrf_cookie)
    def delete(self, request, pk=None):
        favorites = get_object_or_404(Favorites, photo_id=pk)
        favorites.delete()
        return Response({'pk': pk})
#
#
#
#
#
#
# from django.shortcuts import render, get_object_or_404
# from rest_framework.permissions import AllowAny, IsAuthenticated
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from webapp.models import Photo, Favorites
#
#
# class AddFavoriteView(APIView):
#     permission_classes = [IsAuthenticated]
#
#     def get(self, request, pk=None):
#         photo = get_object_or_404(Photo, pk=pk)
#         created = Favorites.objects.get_or_create(photo=photo, user=request.user)
#         if created:
#             return Response({'pk': pk})
#         else:
#             return Response(status=403)
#
#
# class RemoveFavoritesView(APIView):
#     permission_classes = [IsAuthenticated]
#
#     def get(self, request, pk=None):
#         favorites = get_object_or_404(Favorites, photo_id=pk)
#         favorites.delete()
#         return Response({'pk': pk})
#
# class PhotoViewSet(ViewSet):
#     queryset = Photo.objects.all()
    # permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    # def get_permissions(self):
    #     print(self.action)
    #     print(self.request.method)
    #     if self.action in ['list', 'retrieve']:  # self.request.method == "GET"
    #         return [GETModelPermissions()]
    #     else:
    #         return [AllowAny()]

    # def list(self, request):
    #     objects = Article.objects.all()
    #     slr = ArticleSerializer(objects, many=True, context={'request': request})
    #     return Response(slr.data)

    # def create(self, request):
    #     slr = ArticleSerializer(data=request.data, context={'request': request})
    #     if slr.is_valid():
    #         article = slr.save()
    #         return Response(slr.data)
    #     else:
    #         return Response(slr.errors, status=400)
    #
    # def retrieve(self, request, pk=None):
    #     article = get_object_or_404(Article, pk=pk)
    #     slr = ArticleSerializer(article, context={'request': request})
    #     return Response(slr.data)
    #
    # def update(self, request, pk=None):
    #     article = get_object_or_404(Article, pk=pk)
    #     slr = ArticleSerializer(data=request.data, instance=article, context={'request': request})
    #     if slr.is_valid():
    #         article = slr.save()
    #         return Response(slr.data)
    #     else:
    #         return Response(slr.errors, status=400)
    #
    # def destroy(self, request, pk=None):
    #     article = get_object_or_404(Article, pk=pk)
    #     article.delete()
    #     return Response({'pk': pk})
    #
    # @action(methods=['post'], detail=True)
    # def like(self, request, pk=None):
    #     article = get_object_or_404(Article, pk=pk)
    #     like, created = ArticleLike.objects.get_or_create(article=article, user=request.user)
    #     if created:
    #         article.like_count += 1
    #         article.save()
    #         return Response({'pk': pk, 'likes': article.like_count})
    #     else:
    #         return Response(status=403)

    # @action(methods=['delete'], detail=True)
    # def unlike(self, request, pk=None):
    #     article = get_object_or_404(Article, pk=pk)
    #     like = get_object_or_404(article.likes, user=request.user)
    #     like.delete()
    #     article.like_count -= 1
    #     article.save()
    #     return Response({'pk': pk, 'likes': article.like_count})
