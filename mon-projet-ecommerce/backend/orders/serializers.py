from rest_framework import serializers
from .models import Order, OrderItem

class OrderItemSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    
    class Meta:
        model = OrderItem
        fields = ['id', 'product', 'product_name', 'product_price', 'quantity', 'variant']

class OrderSerializer(serializers.ModelSerializer):
    items = OrderItemSerializer(many=True, read_only=True)
    user = serializers.StringRelatedField(read_only=True)
    
    class Meta:
        model = Order
        fields = [
            'id', 'user', 'status', 'total', 'shipping_address',
            'shipping_city', 'shipping_postal_code', 'shipping_country',
            'payment_method', 'payment_id', 'tracking_number', 'note',
            'items', 'created_at', 'updated_at'
        ]
        read_only_fields = ['user', 'created_at', 'updated_at']