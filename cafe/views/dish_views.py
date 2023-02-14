from django.views import generic
from cafe.models import Dish
from django.urls import reverse_lazy


class DishCreateView(generic.CreateView):
    model = Dish
    fields = ["image", "name", "dish_type", "price", "description"]

    def get_success_url(self):
        return reverse_lazy(
            "cafe:dish-recipe",
            kwargs={"pk": Dish.objects.get(name=self.request.POST["name"]).id}
        )


class DishListView(generic.ListView):
    queryset = Dish.objects.select_related("dish_type")
    paginate_by = 12


class DishDetailView(generic.DetailView):
    model = Dish


class DishUpdateView(generic.UpdateView):
    model = Dish
    fields = ["image", "name", "dish_type", "price", "description"]

    def get_success_url(self):
        return reverse_lazy(
            "cafe:dish-recipe",
            kwargs={"pk": Dish.objects.get(name=self.request.POST["name"]).id}
        )


class DishDeleteView(generic.DeleteView):
    model = Dish
    success_url = reverse_lazy("cafe:dish-list")
