from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Product
from django.db.models import Q


class Index(ListView):

    model = Product
    template_name = 'warehouse_m/index.html'

    # fetch all products
    queryset = Product.objects.all()
    context_object_name = 'products'
    paginate_by = 8



def search_index(request):
    if request.method == 'POST':
        query = request.POST['search']
        # Search by manufacturer, category or the code of the product
        result = Product.objects.filter(Q(manufacturer__icontains=query) | Q(category__icontains=query) |
                                        Q(code__icontains=query))
        return render(request, 'warehouse_m/search.html', {'result': result})
    return HttpResponseRedirect(reverse('warehouse_m:index'))


class UpdateProduct(UpdateView):
    model = Product
    fields = '__all__'


class CreateProduct(CreateView):
    model = Product
    fields = '__all__'


class DeleteProduct(DeleteView):
    model = Product
    success_url = reverse_lazy('warehouse_m:index')





