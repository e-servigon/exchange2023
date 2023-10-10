from django.db import models

# Create your models here.

class TranslateTexts(models.Model):
    language_code_origin = models.CharField(max_length=2)
    language_code_destiny = models.CharField(max_length=2)
    text_to_translate = models.CharField(max_length=255)
    text_translated = models.CharField(max_length=255)

    def __str__ (self):
        return 'el texto traducido es %s %s' % (self.language_code_destiny, self.text_translated)
