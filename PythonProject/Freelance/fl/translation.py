from .models import Project, Offer
from modeltranslation.translator import TranslationOptions,register

@register(Project)
class ProjectTranslationOptions(TranslationOptions):
    fields = ('title', 'description')

@register(Offer)
class OfferTranslationOptions(TranslationOptions):
    fields = ('message',)