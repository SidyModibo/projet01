from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Order, OrderItem
from .serializers import OrderSerializer

class OrderViewSet(viewsets.ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        if self.request.user.is_staff:
            return Order.objects.all()
        return Order.objects.filter(user=self.request.user)
    
    def create(self, request, *args, **kwargs):
        # Création d'une commande à partir du panier
        cart = request.data.get('cart', [])
        shipping = request.data.get('shipping', {})
        payment_method = request.data.get('payment_method', 'CARD')
        
        total = sum(item['price'] * item['quantity'] for item in cart)
        
        order = Order.objects.create(
            user=request.user,
            total=total,
            shipping_address=shipping.get('address', ''),
            shipping_city=shipping.get('city', ''),
            shipping_postal_code=shipping.get('postal_code', ''),
            shipping_country=shipping.get('country', 'France'),
            payment_method=payment_method
        )
        
        for item in cart:
            OrderItem.objects.create(
                order=order,
                product_id=item['product_id'],
                product_name=item['name'],
                product_price=item['price'],
                quantity=item['quantity'],
                variant=item.get('variant', '')
            )
        
        # Ici, intégrer Stripe/PayPal
        
        serializer = self.get_serializer(order)
        return Response(serializer.data, status=status.HTTP_201_CREATED)