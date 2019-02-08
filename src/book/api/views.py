from django.shortcuts import render

from rest_framework.generics import CreateAPIView,ListAPIView
from rest_framework import mixins,generics

from .serializers import BookSerializers
from book.models import Book




class BookListAPIView(mixins.CreateModelMixin,generics.ListAPIView):
	permission_classes 				= []
	authentication_classes 			= []
	serializer_class 				= BookSerializers

	def get_queryset(self):
		return Book.objects.all()


	def post(self,request,*args,**kwargs):
		return self.create(request,*args,**kwargs)



class BookUpdateDeleteRetrieveAPIView(
			generics.RetrieveAPIView,
			mixins.UpdateModelMixin,
			mixins.DestroyModelMixin
	):
	permission_classes 				= []
	authentication_classes 			= []
	serializer_class 				= BookSerializers
	lookup_field 					= "id"
	queryset 						= Book.objects.all()


	def put(self,request,*args,**kwargs):
		return self.update(request,*args,**kwargs)

	def patch(self,request,*args,**kwargs):
		return self.update(request,*args,**kwargs)

	def delete(self,request,*args,**kwargs):
		return self.destroy(request,*args,**kwargs)	








# class BookList(generics.ListCreateAPIView):
# # class BookList(CreateAPIView,ListAPIView):
# # class BookList(mixins.CreateModelMixin,ListAPIView):
# 	permission_classes 				= []
# 	authentication_classes 			= []
# 	serializer_class 				= BookSerializers
# 	queryset 						= Book.objects.all()


# 	# def post(self,request,*args,**kwargs):
# 	# 	return self.create(request,*args,**kwargs)

# class BookRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
# # class BookRUDAPIView(generics.UpdateAPIView,generics.DestroyAPIView,generics.RetrieveAPIView):
# # class BookRUDAPIView(mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.RetrieveAPIView):
# 	permission_classes 				= []
# 	authentication_classes 			= []
# 	serializer_class 				= BookSerializers
# 	queryset 						= Book.objects.all()
# 	lookup_field 					= "id"


# 	# def put(self,request,*args,**kwargs):
# 	# 	return self.update(request,*args,**kwargs)

# 	# def delete(self,request,*args,**kwargs):
# 	# 	return self.destroy(request,*args,**kwargs)

# # Creating one endpoint for all.Not recommended.
# class CRUDLAPIView(generics.ListCreateAPIView,generics.RetrieveUpdateDestroyAPIView):
# 	permission_classes 				= []
# 	authentication_classes 			= []
# 	serializer_class 				= BookSerializers
# 	queryset 						= Book.objects.all()
# 	lookup_field 					= "id"