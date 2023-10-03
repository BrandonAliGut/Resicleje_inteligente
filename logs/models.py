from django.db import models

# Create your models here.
class Log_categorias(models.Model):
    """
    img             = models.CharField(max_length=50, blank=False)
    information     = models.CharField(max_length=50, blank=False)
    description     = models.CharField(max_length=50, blank=False)
    created_at      = models.CharField(max_length=50, blank=False)
    update_at       = models.CharField(max_length=50, blank=False)
    name            = models.CharField(max_length=50, blank=False)
    request_method  = models.CharField(max_length=50, blank=False)
    """
    pass
    def save_categories(self):
        pass
    
class Historial_Log_Actions_grupos():
    """
    name_group      = models.CharField(max_length=50, blank=False)
    user            = models.CharField(max_length=50, blank=False)
    address_ip      = models.CharField(max_length=50, blank=False)
    request_method  = models.CharField(max_length=50, blank=False)
    permisssos      = models.CharField(max_length=50, blank=False)
    is_admin        = models.CharField(max_length=50, blank=False)
    is_staf         = models.CharField(max_length=50, blank=False)
    created_at      = models.CharField(max_length=50, blank=False)
    update_at       = models.CharField(max_length=50, blank=False)
    """   
    pass
    
class Historial_Log_Actions_user():
    """
    user            = models.CharField(max_length=50, blank=False)
    address_ip      = models.CharField(max_length=50, blank=False)
    request_method  = models.CharField(max_length=50, blank=False)
    is_admin        = models.CharField(max_length=50, blank=False)
    is_staf         = models.CharField(max_length=50, blank=False)
    created_at      = models.CharField(max_length=50, blank=False)
    update_at       = models.CharField(max_length=50, blank=False)
    grupo           = models.CharField(max_length=50, blank=False)
    """
    pass

class Historial_Log_Actions_user():
    """user         = models.CharField(max_length=50, blank=False)
    user_validated  = models.CharField(max_length=50, blank=False)
    address_ip      = models.CharField(max_length=50, blank=False)
    password_old    = models.CharField(max_length=50, blank=False)
    password_nuew   = models.CharField(max_length=50, blank=False)
    request_method  = models.CharField(max_length=50, blank=False)
    created_at      = models.CharField(max_length=50, blank=False)
    update_at       = models.CharField(max_length=50, blank=False)
    """
    pass

class Historial_Log_Actions(models.Model):
    """
    user                = models.CharField(max_length=50, blank=False)
    address_ip          = models.CharField(max_length=50, blank=False)
    Affected_tables     = models.CharField(max_length=50, blank=False)
    Table_changes       = models.CharField(max_length=50, blank=False)
    request_method      = models.CharField(max_length=50, blank=False)
    date                = models.CharField(max_length=50, blank=False)
    time                = models.CharField(max_length=50, blank=False)
    roles               = models.CharField(max_length=50, blank=False)
    is_authentication   = models.CharField(max_length=50, blank=False)
    is_admin            = models.CharField(max_length=50, blank=False)
    is_staf             = models.CharField(max_length=50, blank=False)
    
    """
    pass
    def capturer():
        pass
    
class Session_log(models.Model):
    """
    user            = models.CharField(max_length=50, blank=False)
    address_ip      = models.CharField(max_length=50, blank=False)
    time_token      = models.CharField(max_length=50, blank=False)
    refres_token    = models.CharField(max_length=50, blank=False)
    date            = models.CharField(max_length=50, blank=False)
    time            = models.CharField(max_length=50, blank=False)
    status          = models.CharField(max_length=50, blank=False)
    error_sms       = models.CharField(max_length=50, blank=False)
    
    """
    pass

class access_violation(models.Model):
    """
    user            = models.CharField(max_length=50, blank=False)
    address_ip      = models.CharField(max_length=50, blank=False)
    created_at      = models.CharField(max_length=50, blank=False)
    affected_table  = models.CharField(max_length=50, blank=False)
    
    """
    pass