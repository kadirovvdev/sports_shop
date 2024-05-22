from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from django.views import View
from .form import *




class CategoryView(View):
    def get(self, request):
        categories = Category.objects.all()
        context = {
            'categories': categories
        }
        return render(request, 'products_category.html', context=context)


class ProductView(View):
    def get(self, request):
        products = Product.objects.all()
        context = {
            'products': products
        }
        return render(request, 'football.html', context=context)




class OrderView(View):
    def get(self, request):
        form = OrderForm()
        return render(request, 'order.html', {'form': form})

    def post(self, request):
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products:order-success')
        return render(request, 'order.html', {'form': form})

class OrderSuccessView(View):
    def get(self, request):
        return render(request, 'order_success.html')



class BasketballView(View):
    def get(self, request):
        products = Product.objects.all()
        context = {
            'products': products
        }
        return render(request, 'basketball.html', context=context)



class MMAView(View):
    def get(self, request):
        products = Product.objects.all()
        context = {
            'products': products
        }
        return render(request, 'mma.html', context=context)


# class SearchResultsView(View):
#     def get(self, request):
#         search = request.GET.get('q')
#         results = Product.objects.filter(name__icontains=search) if search else []
#         context = {
#            'results': results,
#             'search': search
#         }
#         return render(request, 'football.html', context=context)