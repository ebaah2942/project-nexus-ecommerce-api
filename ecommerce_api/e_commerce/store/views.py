from django.shortcuts import render
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import (
    Category, Product, Review, Favorite,
    Like, Cart, CartItem, Order, OrderItem
)
from .serializers import (
    CategorySerializer, ProductSerializer, ReviewSerializer,
    FavoriteSerializer, LikeSerializer, CartSerializer,
    CartItemSerializer, OrderSerializer, OrderItemSerializer
)
from .pagination import DefaultPagination

# Create your views here.


class BaseViewSet(viewsets.ModelViewSet):
    pagination_class = DefaultPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]


class CategoryViewSet(BaseViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    filterset_fields = ['name', 'slug']
    ordering_fields = ['name']


class ProductViewSet(BaseViewSet):
    queryset = Product.objects.filter(is_active=True)
    serializer_class = ProductSerializer
    filterset_fields = {
        'category__slug': ['exact'],
        'price': ['gte', 'lte'],
        'stock': ['gte', 'lte'],
    }
    ordering_fields = ['price', 'created_at']
    search_fields = ['name', 'description']


class ReviewViewSet(BaseViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    filterset_fields = ['product', 'user', 'rating']
    ordering_fields = ['created_at', 'rating']


class FavoriteViewSet(BaseViewSet):
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer
    filterset_fields = ['user', 'product']


class LikeViewSet(BaseViewSet):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    filterset_fields = ['user', 'product']


class CartViewSet(BaseViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
    filterset_fields = ['user']


class CartItemViewSet(BaseViewSet):
    queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    filterset_fields = ['cart', 'product']


class OrderViewSet(BaseViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    filterset_fields = ['user', 'status']
    ordering_fields = ['created_at']


class OrderItemViewSet(BaseViewSet):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer
    filterset_fields = ['order', 'product']
