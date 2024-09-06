from modeltranslation.translator import register, TranslationOptions
from apis import models


@register(models.Company)
class CompanyTranslationOptions(TranslationOptions):
    fields = (
        'name',
        'address',
        'description',
    )


@register(models.Object)
class ObjectsTranslationOptions(TranslationOptions):
    fields = (
        'title',
        'name',
        'description',
    )
