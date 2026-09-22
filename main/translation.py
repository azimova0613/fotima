from modeltranslation.translator import TranslationOptions,register
from .models import *


@register(story)
class storyTranslationOptions(TranslationOptions):
    fields=('nomi','title','text')

@register(story2)
class storyTranslationOptions(TranslationOptions):
    fields=('nomi','narx','title','nomi2')

@register(story3)
class storyTranslationOptions(TranslationOptions):
    fields=('nomi','title')

@register(story4)
class storyTranslationOptions(TranslationOptions):
    fields=('nomi','text')

@register(story5)
class storyTranslationOptions(TranslationOptions):
    fields=('nomi','text')

@register(story6)
class storyTranslationOptions(TranslationOptions):
    fields=('nomi','text')

@register(story7)
class storyTranslationOptions(TranslationOptions):
    fields=('nomi','text')

@register(story8)
class storyTranslationOptions(TranslationOptions):
    fields=('nomi','text')

@register(story9)
class storyTranslationOptions(TranslationOptions):
    fields=('nomi',)

@register(story14)
class storyTranslationOptions(TranslationOptions):
    fields=('nomi','narx','image','xarid')

@register(story15)
class storyTranslationOptions(TranslationOptions):
    fields=('nomi','nomi2','title')

@register(story16)
class storyTranslationOptions(TranslationOptions):
    fields=('nomi','image','nomi2','title')

@register(story17)
class storyTranslationOptions(TranslationOptions):
    fields=('nomi','nomi2','title')

@register(story18)
class storyTranslationOptions(TranslationOptions):
    fields=('nomi','nomi2','title')

@register(story19)
class storyTranslationOptions(TranslationOptions):
    fields=('nomi','text')


@register(story20)
class storyTranslationOptions(TranslationOptions):
    fields=('nomi','adres','adres2','tel2','tel','email')

@register(story21)
class storyTranslationOptions(TranslationOptions):
    fields=('nomi','image')

@register(story22)
class storyTranslationOptions(TranslationOptions):
    fields=('nomi','nomi2','emailid','nomi3')

@register(shop1)
class shop1TranslationOptions(TranslationOptions):
    fields=('nomi','nomi2','title')

@register(kantak)
class storyTranslationOptions(TranslationOptions):
    fields=('nomi','text')

@register(kantakt2)
class kantakt2TranslationOptions(TranslationOptions):
    fields=('Username','Phone','Email','massage')

@register(march)
class marchTranslationOptions(TranslationOptions):
    fields=('nomi','nomi2','nomi3','text')

@register(camment)
class cammentTranslationOptions(TranslationOptions):
    fields=('nomi','nomi2','sana','text','image')

@register(izoh)
class izohTranslationOptions(TranslationOptions):
    fields=('ism','text','email','mavzu')

@register(post)
class postTranslationOptions(TranslationOptions):
    fields=('sana','text','image')

@register(post2)
class post2TranslationOptions(TranslationOptions):
    fields=('nomi','nomi2','nomi3','narx','title')

@register(xarid)
class xaridTranslationOptions(TranslationOptions):
    fields=('nomi','nomi2','nomi3','narx','title','nomi4')

@register(xarid2)
class xarid2TranslationOptions(TranslationOptions):
    fields=('nomi','nomi2','text')

@register(xarid3)
class xarid3TranslationOptions(TranslationOptions):
    fields=('title',)

@register(loyiha)
class loyihaTranslationOptions(TranslationOptions):
    fields=('nomi','title')

@register(page)
class pageTranslationOptions(TranslationOptions):
    fields=('nomi','nomi2','nomi3',)

@register(jamoa)
class jamoa2TranslationOptions(TranslationOptions):
    fields=('nomi','nomi2','nomi3',)

@register(jamoa2)
class jamoa2TranslationOptions(TranslationOptions):
    fields=('nomi','nomi2','nomi3',)

@register(dehqon)
class dehqonTranslationOptions(TranslationOptions):
    fields=('nomi','text2','text')









