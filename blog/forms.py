from django import forms
from django.utils.text import slugify

from .models import EntryImage


class AddEntryImage(forms.ModelForm):
    class Meta:
        model = EntryImage
        fields = (
            'title', 'image',
        )

    def save(self, *args, **kwargs):
        instance = super(AddEntryImage, self).save(commit=False)

        instance.slug = slugify(instance.title)
        instance.save()

        return instance
