from django.db import models

# Create your models here.

language_choices = [
    ('en', 'English'),
    ('es', 'Español'),
    ('fr', 'Français'),
    ('de', 'Deutsch'),
    ('it', 'Italiano'),
    ('pt', 'Português')
]


class Word(models.Model):
    word_text = models.CharField('text', max_length=200)
    word_lang = models.CharField(
        'language', max_length=2,
        choices=language_choices, default='en'
        )
    word_freq = models.FloatField('frequency', default=1.0)
    word_date = models.DateTimeField('posted date', auto_now_add=True)

    def __str__(self):
        return self.word_text

    def get_dict(self):
        return {
            'word_text': self.word_text,
            'word_lang': self.word_lang,
            'word_freq': self.word_freq,
            'word_date': self.word_date
        }

    def get_lang(self):
        return self.word_lang

    def get_freq(self):
        return self.word_freq

    def get_date(self):
        return self.word_date
