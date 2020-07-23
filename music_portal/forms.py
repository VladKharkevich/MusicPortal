from django import forms
from .models import *
from django.core.exceptions import ValidationError


class BandForm(forms.ModelForm):

	class Meta:
		model = Band
		fields = ['title', 'slug', 'biography', 'date_of_creation', 'date_of_breakup',
		          'photo', 'members', 'songs']
		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'slug': forms.TextInput(attrs={'class': 'form-control'}),
			'biography': forms.Textarea(attrs={'class': 'form-control'}),
			'date_of_creation': forms.NumberInput(attrs={'class': 'form-control'}),
			'date_of_breakup': forms.NumberInput(attrs={'class': 'form-control'}),
			'photo': forms.FileInput(attrs={'class': 'form-control'}),
			'members': forms.SelectMultiple(),
			'songs': forms.SelectMultiple(),
		}

	def clean_slug(self):
		new_slug = self.cleaned_data['slug'].lower()
		if new_slug == 'create':
			raise ValidationError("Slug may not be 'Create'")
		if News.objects.filter(slug__iexact=new_slug).count():
			raise ValidationError(f"Slug must be unique. We have '{new_slug}' slug already")
		return new_slug


class MusicianForm(forms.ModelForm):

	class Meta:
		model = Musician
		fields = ['first_name', 'last_name', 'slug', 'biography', 'date_of_birth',
		          'date_of_death', 'photo', 'songs']
		widgets = {
			'first_name': forms.TextInput(attrs={'class': 'form-control'}),
			'last_name': forms.TextInput(attrs={'class': 'form-control'}),
			'slug': forms.TextInput(attrs={'class': 'form-control'}),
			'biography': forms.Textarea(attrs={'class': 'form-control'}),
			'date_of_birth': forms.DateInput(attrs={'class': 'form-control'}),
			'date_of_death': forms.DateInput(attrs={'class': 'form-control'}),
			'photo': forms.FileInput(attrs={'class': 'form-control'}),
			'songs': forms.SelectMultiple()
		}

	def clean_slug(self):
		new_slug = self.cleaned_data['slug'].lower()
		if new_slug == 'create':
			raise ValidationError("Slug may not be 'Create'")
		if News.objects.filter(slug__iexact=new_slug).count():
			raise ValidationError(f"Slug must be unique. We have '{new_slug}' slug already")
		return new_slug


class MusicalInstrumentForm(forms.ModelForm):

	class Meta:
		model = MusicalInstrument
		fields = ['name', 'slug', 'description', 'photo', 'type_of_instrument']
		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'slug': forms.TextInput(attrs={'class': 'form-control'}),
			'description': forms.Textarea(attrs={'class': 'form-control'}),
			'type_of_instrument': forms.Select(attrs={'class': 'form-control'}),
			'photo': forms.FileInput(attrs={'class': 'form-control'}),
		}

	def clean_slug(self):
		new_slug = self.cleaned_data['slug'].lower()
		if new_slug == 'create':
			raise ValidationError("Slug may not be 'Create'")
		if News.objects.filter(slug__iexact=new_slug).count():
			raise ValidationError(f"Slug must be unique. We have '{new_slug}' slug already")
		return new_slug


class NewsForm(forms.ModelForm):

	class Meta:
		model = News
		fields = ['title', 'slug', 'content']
		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'slug': forms.TextInput(attrs={'class': 'form-control'}),
			'content': forms.Textarea(attrs={'class': 'form-control'}),
		}

	def clean_slug(self):
		new_slug = self.cleaned_data['slug'].lower()
		if new_slug == 'create':
			raise ValidationError("Slug may not be 'Create'")
		if News.objects.filter(slug__iexact=new_slug).count():
			raise ValidationError(f"Slug must be unique. We have '{new_slug}' slug already")
		return new_slug


class SongForm(forms.ModelForm):

	class Meta:
		model = Song
		fields = ['title', 'slug', 'album', 'songfile', 'year_of_creation']
		widgets = {
			'title': forms.TextInput(attrs={'class': 'form-control'}),
			'slug': forms.TextInput(attrs={'class': 'form-control'}),
			'album': forms.Select(attrs={'class': 'form-control'}),
			'year_of_creation': forms.NumberInput(attrs={'class': 'form-control'}),
			'songfile': forms.FileInput(attrs={'class': 'form-control'}),
		}

	def clean_slug(self):
		new_slug = self.cleaned_data['slug'].lower()
		if new_slug == 'create':
			raise ValidationError("Slug may not be 'Create'")
		if News.objects.filter(slug__iexact=new_slug).count():
			raise ValidationError(f"Slug must be unique. We have '{new_slug}' slug already")
		return new_slug
