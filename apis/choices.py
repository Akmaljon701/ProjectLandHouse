from django.db.models import TextChoices


class ObjectStatuses(TextChoices):
    IN_PROCESS = 'IN_PROCESS'
    FINISHED = 'FINISHED'
