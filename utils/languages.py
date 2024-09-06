from django.utils import translation


def language(lang):
    if lang:
        translation.activate('uz')
    else:
        translation.activate('ru')
