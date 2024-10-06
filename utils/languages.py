from django.utils import translation


def language(lang):
    if lang:
        translation.activate('ru')
    else:
        translation.activate('uz')
