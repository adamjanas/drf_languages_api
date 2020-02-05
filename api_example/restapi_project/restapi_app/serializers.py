from rest_framework import serializers
from .models import Language, Paradigm, Programmer

class LanguageSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Language
		fields = ('id','url', 'name', 'paradigm') 			#what i want to display#

class ParadigmSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Paradigm
		fields = ('id', 'url', 'name')

class ProgrammerSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Programmer
		fields = ('id', 'url', 'name', 'languages')
