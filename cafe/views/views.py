from django.shortcuts import render
from cafe.models import Dish, Order

# def index(request):
#     context = {
#         "num_sushi": Dish.objects.filter(dish_type__name="sushi").count(),
#         "num_salad": Dish.objects.filter(dish_type__name="salad").count(),
#         "num_pizza": Dish.objects.filter(dish_type__name="pizza").count(),
#         "num_soup": Dish.objects.filter(dish_type__name="soup").count()
#     }
#     return render(request, "cafe/index.html", context=context)


def home(request):
    context = {
        "orders": Order.objects.filter(employee=request.user),
        "num_sushi": Dish.objects.filter(dish_type__name="sushi").count(),
        "num_salad": Dish.objects.filter(dish_type__name="salad").count(),
        "num_pizza": Dish.objects.filter(dish_type__name="pizza").count(),
        "num_soup": Dish.objects.filter(dish_type__name="soup").count()
    }
    return render(request, "cafe/home.html", context=context)
