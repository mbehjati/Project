from django import forms

from restaurant.models import FoodCook, Cook, FoodType, Material, Warehouse, OrderDeliveryMan, OrderWaiter


def foods_for_cook(cook):
    ans = ()
    all_tasks = FoodCook.objects.all()
    for task in all_tasks:
        if task.cook == cook and task.done is False:
            ans = ans + ((task, task),)
    return ans


class OrderAuthenticationForm(forms.Form):
    order_id = forms.IntegerField()


class CookDuty(forms.Form):
    # cook = None
    def __init__(self, *args, **kwargs):
        cook = kwargs.pop('cook')
        super(CookDuty, self).__init__(*args, **kwargs)
        self.fields['duty'].choices = foods_for_cook(cook)

    duty = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, label="وظایف")


def duty_for_delivery(deliveryman):
    ans = ()
    all_tasks = OrderDeliveryMan.objects.all()
    for task in all_tasks:
        if task.deliveryman == deliveryman and task.done is False:
            ans = ans + ((task, task),)
    return ans


class DeliveryDutyForm(forms.Form):
    # cook = None
    def __init__(self, *args, **kwargs):
        deliveryman = kwargs.pop('deliveryman')
        super(DeliveryDutyForm, self).__init__(*args, **kwargs)
        self.fields['duty'].choices = duty_for_delivery(deliveryman)

    duty = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, label="وظایف")


def duty_for_waiter(waiter):
    ans = ()
    all_tasks = OrderWaiter.objects.all()
    for task in all_tasks:
        if task.waiter == waiter and task.done is False:
            ans = ans + ((task, task),)
    return ans


class WaiterDutyForm(forms.Form):
    # cook = None
    def __init__(self, *args, **kwargs):
        waiter = kwargs.pop('waiter')
        super(WaiterDutyForm, self).__init__(*args, **kwargs)
        self.fields['duty'].choices = duty_for_waiter(waiter)

    duty = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, label="وظایف")


def get_all_food_types():
    all_food = FoodType.objects.all()
    ans = ()
    for f in all_food:
        print(f)
        ans += ((f.name, f),)
    return ans


def get_all_materials():
    all_materials = Material.objects.all()
    ans = ()
    for m in all_materials:
        ans += ((m.name, m),)
    return ans


class RecipeForm(forms.Form):
    all_foods = get_all_food_types()
    # food = forms.ChoiceField(widget=forms.Select, choices=all_foods, label="غذا")
    recipe = forms.CharField(label="دستور پخت")
    # material = forms.ChoiceField(widget=forms.Select , choices=get_all_materials())


class AbilityForm(forms.Form):
    all_foods = get_all_food_types()
    foods = forms.ChoiceField(widget=forms.Select, choices=all_foods, label="توانایی پخت ")
    number = forms.IntegerField(label=" تعداد")


class FoodOfferForm(forms.Form):
    all_foods = get_all_food_types()
    food = forms.ChoiceField(widget=forms.Select, choices=all_foods, label="غذا")
    suggest = forms.ChoiceField(widget=forms.Select, choices=all_foods, label="پیشنهاد")


def get_all_warehouse():
    all_warehouses = Warehouse.objects.all()
    ans = ()
    for w in all_warehouses:
        ans += ((w, w),)
    return ans


class MaterialForm(forms.Form):
    material = forms.ChoiceField(widget=forms.Select, choices=get_all_materials() , label='ماده اولیه')
    wareHouse = forms.ChoiceField(widget=forms.Select, choices=get_all_warehouse() , label='انبار')
    value = forms.IntegerField(label='مقدار')
    expire_date = forms.DateField(label='تاریخ انقضا')


class ReportForm(forms.Form):
    warehouse = forms.ChoiceField(widget=forms.Select, choices=get_all_warehouse(), label="انبار")


class OrderingForm(forms.Form):
    pass
