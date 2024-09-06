from django.db.models import TextChoices


class ObjectStatuses(TextChoices):
    IN_PROCESS = 'IN_PROCESS'
    FINISHED = 'FINISHED'


class ObjectRoomStatuses(TextChoices):
    SOLD = 'SOLD'
    NOT_SOLD = 'NOT_SOLD'


class ApplicationStatuses(TextChoices):
    NEW = 'NEW'
    OLD = 'OLD'
