from django.shortcuts import render
from django.views import generic
from cafe.models import Dish, Position, DishType, Ingredient, Employee, Order
from django.urls import reverse_lazy


def index(request):
    context = {
        "num_sushi": Dish.objects.filter(dish_type__name="sushi").count(),
        "num_salad": Dish.objects.filter(dish_type__name="salad").count(),
        "num_pizza": Dish.objects.filter(dish_type__name="pizza").count(),
        "num_soup": Dish.objects.filter(dish_type__name="soup").count()
    }
    return render(request, "cafe/index.html", context=context)


class PositionCreateView(generic.CreateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("cafe:position-list")


class PositionListView(generic.ListView):
    model = Position


class PositionUpdateView(generic.UpdateView):
    model = Position
    fields = "__all__"
    success_url = reverse_lazy("cafe:position-list")


class PositionDeleteView(generic.DeleteView):
    model = Position
    success_url = reverse_lazy("cafe:position-list")


class DishTypeListView(generic.ListView):
    model = DishType
    template_name = "cafe/dish_type_list.html"
    context_object_name = "dish_type_list"


class IngredientListView(generic.ListView):
    model = Ingredient


class EmployeeListView(generic.ListView):
    model = Employee


class DishListView(generic.ListView):
    model = Dish


class OrderListView(generic.ListView):
    model = Order
