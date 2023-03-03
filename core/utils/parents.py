# from rest_framework import viewsets, status
# from rest_framework.response import Response

#
# class OrdinaryViewSet(viewsets.ModelViewSet):
#
#     def update(self, request, key=None, *args, **kwargs):
#         obj = self.get_object()
#         result = self.serializer_class(data=request.data)
#         if result.is_valid():
#             result.update(instance=obj, validated_data=request.data)
#             return Response(result.data, status=status.HTTP_200_OK)
#         return Response(data=result.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def destroy(self, request, *args, **kwargs):
#         obj = self.get_object()
#         if request.GET['type'] == 'soft':
#             result = self.serializer_class(obj, data=request.data)
#             if result.is_valid():
#                 result.__delete__(obj)
#                 return Response(status=status.HTTP_204_NO_CONTENT)
#             return Response(data=result.errors, status=status.HTTP_400_BAD_REQUEST)
#         if request.GET['type'] == 'hard':
#             obj.delete()
#
#         return Response(status=status.HTTP_403_FORBIDDEN)
#
#     pass
