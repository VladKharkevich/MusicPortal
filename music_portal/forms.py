from django import forms
from .models import News
from django.core.exceptions import ValidationError


class NewsCreateForm(forms.ModelForm):

	class Meta:
		model = News
		fields = ['title', 'slug', 'content']
		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-textinput'}),
			'slug': forms.TextInput(attrs={'class': 'form-textinput'}),
			'content': forms.Textarea(attrs={'class': 'form-textarea'}),
		}

	def clean_slug(self):
		new_slug = self.cleaned_data['slug'].lower()
		if new_slug == 'create':
			raise ValidationError("Slug may not be 'Create'")
		if News.objects.filter(slug__iexact=new_slug).count():
			raise ValidationError(f"Slug must be unique. We have '{new_slug}' slug already")
		return new_slug