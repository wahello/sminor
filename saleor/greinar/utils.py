from .models import greinar


def greinars_visible_to_user(user):
    if user.is_authenticated and user.is_active and user.is_staff:
        return greinar.objects.all()
    return greinar.objects.public()
