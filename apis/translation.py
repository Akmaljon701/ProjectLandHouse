from modeltranslation.translator import register, TranslationOptions
from apis import models


@register(models.Object)
class ObjectsTranslationOptions(TranslationOptions):
    fields = ('title', 'name', 'description')
