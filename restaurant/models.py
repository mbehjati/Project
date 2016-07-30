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
        return self.warehouse_id


class Material(models.Model):
    name = models.CharField(max_length=50)
    expire_date = models.DateTimeField(null=True)


class MaterialInWarehouse(models.Model):
    warehouse = models.ForeignKey(Warehouse)
    material = models.ForeignKey(Material)
    value = models.IntegerField()


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


class Ability(models.Model):
    ability_id = models.IntegerField(primary_key=True)
    definition = models.TextField()


class CookAbility(models.Model):
    cook = models.ForeignKey(Cook)
    ability = models.ForeignKey(Ability)


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
    trackID = models.IntegerField()
    branch = models.ForeignKey(Branch)
    user = models.ForeignKey(User)


class Menu(models.Model):
    # image = models.ImageField()
    name = models.CharField(max_length=50)
    description = models.TextField(null=True)
    branch = models.ForeignKey(Branch)


class PeriodicOrder(models.Model):
    weeks_num = models.IntegerField()
    # TODO: DayList
    trackID = models.IntegerField()
    branch = models.ForeignKey(Branch)


class FoodType(models.Model):
    name = models.CharField(max_length=50)
    recipe = models.TextField()
    rate = models.FloatField(null=True)
    price = models.IntegerField()

    # image = models.ImageField()


class TasteType(models.Model):
    name = models.TextField(max_length=50)




class Food(models.Model):
    food_type = models.ForeignKey(FoodType)
    status = models.BooleanField()
    order = models.ForeignKey(Order)
    # TODO: what to do ?!


class FoodInMenu(models.Model):
    food_type = models.ForeignKey(FoodType)
    menu = models.ForeignKey(Menu)


class FoodInBranch(models.Model):
    food_type = models.ForeignKey(FoodType)
    branch = models.ForeignKey(Branch)


class Chair(models.Model):
    id = models.IntegerField(primary_key=True)
    state = models.IntegerField()
    branch = models.ForeignKey(Branch)


class Parking(models.Model):
    id = models.IntegerField(primary_key=True)
    state = models.IntegerField()
    branch = models.ForeignKey(Branch)


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
