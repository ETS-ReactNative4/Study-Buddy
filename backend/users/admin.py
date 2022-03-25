from django.contrib import admin
from django.utils.translation import gettext_lazy as _

from .models import User


@admin.register(User)
class AppointmentModelAdmin(admin.ModelAdmin):
    fields = [
        "username",
        "email",
    ]
    list_display = [
        "username",
        "email",
        "get_appointments",
    ]

    @admin.display(description=_("Appointments"))
    def get_appointments(self, user) -> str:
        text = ", ".join(
            [f"{m.topic}" for m in user.appointments.all()])
        return text
