from mycrm import models
enabled_admins ={}

class BaseAdmin(object):
    list_display = []
    list_filters = []
    search_fields = []
    list_per_page = 20
    ordering = None

class CustomerAdmin(BaseAdmin):
    list_display = ["id",'qq','name','source','consultant','consult_course','date','status']
    list_filters = ['source','consultant','consult_course','status','date']
    search_fields = ['qq','name',"consultant__name"]

    #model = models.Customer
    list_per_page = 5
    ordering = "qq"

class CustomerFollowUpAdmin(BaseAdmin):
    list_display = ('customer','consultant','date')

def register(models_class,admin_class=None):
    if models_class._meta.app_label not in enabled_admins:
        enabled_admins[models_class._meta.app_label] ={}
    admin_class.model = models_class
    enabled_admins[models_class._meta.app_label][models_class._meta.model_name] = admin_class

register(models.Customer,CustomerAdmin)
register(models.CustomerFollowUp,CustomerFollowUpAdmin)