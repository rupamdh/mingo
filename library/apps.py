from django.apps import AppConfig


class LibraryConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'library'
    verbose_name = 'Library'  # Customize the app name in admin interface
    verbose_name_plural = 'Libraries'  # Customize the app name in admin interface in plural form
    icon = 'ki-add-folder'
