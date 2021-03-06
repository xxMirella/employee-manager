from django.contrib import admin
from .models import Person, Country, State, City, Employee, Role, Address


def dismiss_employee(model_admin, requiest, queryset):
    queryset.update(still_employee=False)


def hire_again(model_admin, requiest, queryset):
    queryset.update(still_employee=True)


dismiss_employee.short_description = "Employee fired."
hire_again.short_description = "Employee hired again."


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'cpf', 'birthday', 'address']
    list_filter = ('name', 'cpf')
    search_fields = ('name', 'cpf')

    def get_actions(self, request):
        actions = super().get_actions(request)
        if request.user.username[0].upper() != 'J':
            if 'delete_selected' in actions:
                del actions['delete_selected']
        return actions


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['name']
    search_fields = ['name']

    def get_actions(self, request):
        actions = super().get_actions(request)
        if request.user.username[0].upper() != 'J':
            if 'delete_selected' in actions:
                del actions['delete_selected']
        return actions


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['name', 'state']
    list_filter = ('name', 'state')
    search_fields = ('name', 'state')

    def get_actions(self, request):
        actions = super().get_actions(request)
        if request.user.username[0].upper() != 'J':
            if 'delete_selected' in actions:
                del actions['delete_selected']
        return actions


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ['name', 'country']
    list_filter = ('name', 'country')
    search_fields = ('name', 'country')

    def get_actions(self, request):
        actions = super().get_actions(request)
        if request.user.username[0].upper() != 'J':
            if 'delete_selected' in actions:
                del actions['delete_selected']
        return actions


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['person', 'email', 'role', 'hiring_date', 'still_employee']
    list_filter = ('person__name', 'email', 'role__name', 'role__salary', 'still_employee')
    search_fields = ('person', 'role', 'email')
    actions = [dismiss_employee, hire_again]

    def get_actions(self, request):
        actions = super().get_actions(request)
        if request.user.username[0].upper() != 'J':
            if 'delete_selected' in actions:
                del actions['delete_selected']
        return actions


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ['name', 'salary', 'is_active']
    list_filter = ('name', 'salary', 'is_active')
    search_fields = ('name', 'salary')

    def get_actions(self, request):
        actions = super().get_actions(request)
        if request.user.username[0].upper() != 'J':
            if 'delete_selected' in actions:
                del actions['delete_selected']
        return actions


@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['street', 'number', 'neighborhood', 'zip_code', 'city']
    list_filter = ('street', 'neighborhood', 'zip_code', 'city')
    search_fields = ('street', 'neighborhood', 'zip_code', 'city')

    def get_actions(self, request):
        actions = super().get_actions(request)
        if request.user.username[0].upper() != 'J':
            if 'delete_selected' in actions:
                del actions['delete_selected']
        return actions


admin.site.index_title = ""
admin.site.site_header = "Employees Manager"
admin.site.site_title = "Employees Manager"
