from django.contrib import admin

# Register your models here.
from django.core.mail import send_mail

from restaurant.models import User, Employee, Cook, ParkingMan, WarehouseMan, Waiter, DeliveryMan, Clerk, Branch, \
    Comment, Menu, CommentEmp, FoodType, FoodInMenu, FoodInBranch, Email, DiscountCode, Setting, TestModel, TasteType, \
    FoodTypeTaste, Order, Parking, Chair, ChairInOrder, ParkingInOrder, Food, FoodCook, CookAbility, FoodOffer, \
    Warehouse, Material, MaterialInWarehouse, MaterialInFood, OrderDeliveryMan, OrderWaiter, MyUser


def send_mail_to_users(modeladmin, request, queryset):
    mail_list = []
    for user in queryset:
        mail_list.append(user.user.email)
    all_emails = Email.objects.all()
    for email in all_emails:
        if email.to_be_send:
            send_mail(str(email.title), str(email.body), 'rafiei.mina73@gmail.com', mail_list, fail_silently=False)


send_mail_to_users.short_description = "send mail"


def send_discount_code_to_users(modeladmin, request, queryset):
    mail_list = []
    for user in queryset:
        mail_list.append(user.user.email)
    all_discount_code = DiscountCode.objects.all()
    for discount_code in all_discount_code:
        if discount_code.to_be_send:
            send_mail(str("discount code"), email_body_for_discount(discount_code), 'rafiei.mina73@gmail.com',
                      mail_list, fail_silently=False)


send_discount_code_to_users.short_description = "send discount code"


def email_body_for_discount(discount):
    ans = 'Hi , \nThis discount code is for you :' + str(
        discount.code) + ', it is a ' + str(
        discount.percent) + '% discount for you' + '\nyou can use it until ' + discount.deadline.strftime(
        '%m/%d/%Y')
    return ans


def uncheck(modeladmin, request, queryset):
    queryset.update(to_be_send=False)


uncheck.short_description = "uncheck emails"


def check(modeladmin, request, queryset):
    queryset.update(to_be_send=True)


check.short_description = "check emails"


@admin.register(MyUser)
class AdminUser(admin.ModelAdmin):
    actions = [send_mail_to_users, send_discount_code_to_users]
    pass


@admin.register(Employee)
class AdminEmployee(admin.ModelAdmin):
    pass


@admin.register(Cook)
class AdminUser(admin.ModelAdmin):
    pass


@admin.register(ParkingMan)
class AdminParkingMan(admin.ModelAdmin):
    pass


@admin.register(WarehouseMan)
class AdminWareHouseman(admin.ModelAdmin):
    pass


@admin.register(Waiter)
class AdminWaiter(admin.ModelAdmin):
    pass


@admin.register(DeliveryMan)
class AdminDeliveryMan(admin.ModelAdmin):
    pass


@admin.register(Clerk)
class AdminClerk(admin.ModelAdmin):
    pass


@admin.register(Branch)
class AdminBranch(admin.ModelAdmin):
    pass


@admin.register(Comment)
class AdminComment(admin.ModelAdmin):
    pass


@admin.register(Menu)
class AdminMenu(admin.ModelAdmin):
    pass


@admin.register(CommentEmp)
class AdminCommentEmp(admin.ModelAdmin):
    pass


@admin.register(FoodType)
class AdminFoodType(admin.ModelAdmin):
    # exclude = ('rate',)
    pass


@admin.register(FoodInMenu)
class AdminFoodInMenu(admin.ModelAdmin):
    pass


@admin.register(FoodInBranch)
class AdminFoodInBranch(admin.ModelAdmin):
    pass


@admin.register(Email)
class AdminEmail(admin.ModelAdmin):
    actions = [check, uncheck]
    pass


@admin.register(DiscountCode)
class AdminDiscountCode(admin.ModelAdmin):
    actions = [check, uncheck]
    pass


@admin.register(Setting)
class AdminMySettings(admin.ModelAdmin):
    actions = [check, uncheck]
    pass


@admin.register(TestModel)
class AdminTestModel(admin.ModelAdmin):
    actions = [check, uncheck]
    pass


@admin.register(TasteType)
class AdminTasteType(admin.ModelAdmin):
    pass


@admin.register(FoodTypeTaste)
class AdminFoodTypeTaste(admin.ModelAdmin):
    exclude = ('recipe', 'rate',)
    pass


# admin.site.register(SingletonModel)

@admin.register(Order)
class AdminOrder(admin.ModelAdmin):
    pass


@admin.register(Parking)
class AdminParking(admin.ModelAdmin):
    pass


@admin.register(Chair)
class AdminChair(admin.ModelAdmin):
    pass


@admin.register(ChairInOrder)
class AdminChairInOrder(admin.ModelAdmin):
    pass


@admin.register(ParkingInOrder)
class AdminParkingInOrder(admin.ModelAdmin):
    pass


@admin.register(Food)
class AdminFood(admin.ModelAdmin):
    pass


@admin.register(FoodCook)
class AdminFoodCook(admin.ModelAdmin):
    pass


@admin.register(CookAbility)
class AdminCookAbility(admin.ModelAdmin):
    pass


@admin.register(FoodOffer)
class AdminFoodOffer(admin.ModelAdmin):
    pass


@admin.register(Warehouse)
class AdminWareHouse(admin.ModelAdmin):
    pass


@admin.register(Material)
class AdminMaterial(admin.ModelAdmin):
    pass


@admin.register(MaterialInWarehouse)
class AdminMaterialInWarehouse(admin.ModelAdmin):
    pass


@admin.register(MaterialInFood)
class AdminMaterialInFood(admin.ModelAdmin):
    pass


@admin.register(OrderDeliveryMan)
class AdminOrderDelivery(admin.ModelAdmin):
    pass


@admin.register(OrderWaiter)
class AdminOrderWaiter(admin.ModelAdmin):
    pass