from modeltranslation.translator import translator, TranslationOptions
from .models import EmergenciesPostModel, DiseaseStateCategoryModel


class EmergenciesPostModelTranslationOptions(TranslationOptions):
    fields = ("category",)


translator.register(EmergenciesPostModel, EmergenciesPostModelTranslationOptions)


class DiseaseStateCategoryModelTranslationOptions(TranslationOptions):
    fields = ("name_disease",)


translator.register(DiseaseStateCategoryModel, DiseaseStateCategoryModelTranslationOptions)
