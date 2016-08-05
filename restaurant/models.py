from enum import unique

from django.core.mail import send_mail
from django.core.validators import RegexValidator
from django.db import models


# Create your models here.
class GeneralUser(models.Model):
    id = models.IntegerField
    # TODO: not a model!


class User(models.Model):
    name = models.CharField(max_length=50)
    username = models.CharField(max_length=20, primary_key=True)
    password = models.CharField(max_length=8)
    address = models.TextField()
    # phone_regex = RegexValidator()//TODO:validate regex
    phone_number = models.CharField(max_length=11)
    email = models.EmailField()

    def __str__(self):
        return self.username


class Warehouse(models.Model):
    warehouse_id = models.IntegerField(primary_key=True)
    address = models.TextField()

    def __str__(self):
        return "انبار شماره "+str(self.warehouse_id)


class Material(models.Model):
    name = models.CharField(max_length=50 , primary_key=True)

    def __str__(self):
        return str(self.name)



class MaterialInWarehouse(models.Model):
    warehouse = models.ForeignKey(Warehouse)
    material = models.ForeignKey(Material)
    value = models.IntegerField()
    expire_date = models.DateTimeField(null=True)




class Branch(models.Model):
    branch_id = models.IntegerField(primary_key=True)
    address = models.TextField()
    phone_number = models.CharField(max_length=11)
    domain = models.TextField(null=True)

    # TODO: mahdude ghabele ersal

    def __str__(self):
        return "branch " + str(self.branch_id)


class Employee(models.Model):
    name = models.CharField(max_length=50)
    employee_id = models.IntegerField(primary_key=True)
    branch = models.ForeignKey(Branch)

    def __str__(self):
        return str(self.employee_id) + " : " + self.name


class Cook(models.Model):
    cook_id = models.OneToOneField(Employee, primary_key=True)

    def __str__(self):
        return str(self.cook_id.name)


class Ability(models.Model):
    ability_id = models.IntegerField(primary_key=True)
    definition = models.TextField()


class FoodType(models.Model):
    name = models.CharField(max_length=50, primary_key=True)
    recipe = models.TextField(null=True)
    rate = models.FloatField(default=5)
    price = models.IntegerField()
    image = models.ImageField(upload_to='food', null=True)

    def __str__(self):
        return str(self.name)
        # image = models.ImageField()

class CookAbility(models.Model):
    cook = models.ForeignKey(Cook)
    ability = models.ForeignKey(FoodType)
    number = models.IntegerField()


class Task(models.Model):
    task_id = models.IntegerField(primary_key=True)
    description = models.TextField()
    # TODO: task for each employee


class TaskEmployee(models.Model):
    task = models.ForeignKey(Task)
    employee = models.ForeignKey(Employee)


class ParkingMan(models.Model):
    parking_man_id = models.OneToOneField(Employee, primary_key=True)




class Waiter(models.Model):
    waiter_id = models.OneToOneField(Employee, primary_key=True)


class WarehouseMan(models.Model):
    warehouse_man_id = models.OneToOneField(Employee, primary_key=True)


class DeliveryMan(models.Model):
    delivery_man_id = models.OneToOneField(Employee, primary_key=True)


class Clerk(models.Model):
    clerk_id = models.OneToOneField(Employee, primary_key=True)


class CommentEmp(models.Model):
    # comment for employee
    text = models.TextField()
    state = models.BooleanField()
    date = models.DateTimeField()
    user = models.ForeignKey(User)
    employee = models.ForeignKey(Employee)


class Order(models.Model):
    is_permanent = models.BooleanField()
    is_changable = models.BooleanField()
    has_child = models.NullBooleanField()
    place = models.BooleanField(default='True', choices=((1, 'منزل'),
                                                         (2, 'حضوری'),))
    trackID = models.IntegerField()
    branch = models.ForeignKey(Branch)
    user = models.ForeignKey(User)
    date = models.DateField()
    time = models.TimeField()


class Menu(models.Model):
    # image = models.ImageField()
    name = models.CharField(max_length=50)
    description = models.TextField(null=True)
    branch = models.OneToOneField(Branch, on_delete=models.CASCADE,
                                  primary_key=True)

    def __str__(self):
        return str(self.name)


class PeriodicOrder(models.Model):
    weeks_num = models.IntegerField()
    # TODO: DayList
    trackID = models.IntegerField()
    branch = models.ForeignKey(Branch)




class TasteType(models.Model):
    name = models.TextField(max_length=50)

    def __str__(self):
        return str(self.name)


class Food(models.Model):
    food_type = models.ForeignKey(FoodType)
    status = models.BooleanField()
    order = models.ForeignKey(Order)
    number = models.IntegerField()
    # TODO: what to do ?!

    def __str__(self):
        return str(self.food_type.name) +  ' برای سفارش ' +str(self.order.trackID) +' : تعداد ' + str(self.number)


class FoodInMenu(models.Model):
    food_type = models.ForeignKey(FoodType)
    menu = models.ForeignKey(Menu)

    def __str__(self):
        return str(self.food_type.name) + " - " + str(self.menu.name)


class FoodInBranch(models.Model):
    food_type = models.ForeignKey(FoodType)
    branch = models.ForeignKey(Branch)


class Chair(models.Model):
    id = models.IntegerField(primary_key=True)
    state = models.IntegerField()
    branch = models.ForeignKey(Branch)

    def __str__(self):
        return "chair " + str(self.id)


class Parking(models.Model):
    id = models.IntegerField(primary_key=True)
    state = models.IntegerField()
    branch = models.ForeignKey(Branch)

    def __str__(self):
        return "parking " + str(self.id)


class MaterialInFood(models.Model):
    material = models.ForeignKey(Material)
    food = models.ForeignKey(FoodType)
    value = models.IntegerField()


class Comment(models.Model):
    # comment for food
    text = models.TextField()
    state = models.BooleanField()
    date = models.DateTimeField()
    user = models.ForeignKey(User)
    food = models.ForeignKey(FoodType)


class Email(models.Model):
    title = models.CharField(max_length=50)
    body = models.TextField()
    to_be_send = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class DiscountCode(models.Model):
    code = models.IntegerField()
    description = models.CharField(max_length=50)
    to_be_send = models.BooleanField()
    percent = models.IntegerField()  # TODO: between 0 to 100 checking
    deadline = models.DateField()

    # TODO: foreach foodType ?

    def __str__(self):
        return str(self.code)


class Setting(models.Model):
    last_orders = models.BooleanField()
    most_liked = models.BooleanField()
    best_offer = models.BooleanField()

    def save(self, *args, **kwargs):
        self.pk = 1
        super(Setting, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class TestModel(models.Model):
    name = models.CharField(max_length=10)


class FoodTypeTaste(models.Model):
    food = models.ForeignKey(FoodType)
    taste = models.ForeignKey(TasteType)

    def __str__(self):
        return str(self.food.name) + " - " + str(self.taste.name)


class ChairInOrder(models.Model):
    chair = models.ForeignKey(Chair)
    order = models.ForeignKey(Order)

    def __str__(self):
        return "chair" + str(self.chair.id) + "for order " + str(self.order.id)


class ParkingInOrder(models.Model):
    parking = models.ForeignKey(Parking)
    order = models.ForeignKey(Order)

    def __str__(self):
        return "parking" + str(self.parking.id) + "for order " + str(self.order.id)


class FoodCook(models.Model):
    food = models.ForeignKey(Food)
    cook = models.ForeignKey(Cook)
    done = models.BooleanField(default=False)

    def __str__(self):
        return str(self.food.food_type.name) + ' برای سفارش ' + str(self.food.order.trackID) + ' : تعداد ' + str(self.food.number)


class FoodOffer(models.Model):
    food = models.ForeignKey(FoodType, related_name='food_for_offer')
    offer = models.ForeignKey(FoodType, related_name='offer')


class OrderDeliveryMan(models.Model):
    order = models.ForeignKey(Order)
    deliveryman = models.ForeignKey(DeliveryMan)
    done = models.BooleanField()

    def __str__(self):
        return 'سفارش شماره‌ي : ' + str(self.order.trackID)


class OrderWaiter(models.Model):
    order = models.ForeignKey(Order)
    waiter = models.ForeignKey(Waiter)
    done = models.BooleanField()

    def __str__(self):
        return 'سفارش شماره‌ی : '+ str(self.order.trackID)
