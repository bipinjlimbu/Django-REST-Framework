from rest_framework.decorators import api_view
from rest_framework.response import Response
from ..serializers import ProductSerializer
from rest_framework import status
from ..models import Product

@api_view(['GET','POST'])
def product_view(request):
    if request.method == 'GET':
        product = Product.objects.all()
        print(product)
        serializer = ProductSerializer(product,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':"Data posted successfully",'data':serializer.data},status=status.HTTP_201_CREATED)
        else:
            return Response({'error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET','PUT','DELETE'])
def product_detail_view(request,id):
    try:
        product = Product.objects.get(id=id)
    except Product.DoesNotExist:
        return Response({'error':'Product not found'},status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data,status=status.HTTP_200_OK)
    
    if request.method == 'PUT':
        serializer = ProductSerializer(product,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data updated successfully','data':serializer.data},status=status.HTTP_200_OK)
        else:
            return Response({'error':serializer.errors},status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        product.delete()
        return Response({'msg':'Product deleted successfully'},status=status.HTTP_204_NO_CONTENT)