from quiz.models import Quiz, QuizTaker, Question, Answer, UsersAnswer
from rest_framework import serializers

class QuizListSerializer(serializers.ModelSerializer):
	questions_count = serializers.SerializerMethodField()
	class Meta:
		model = Quiz
		fields = ["id", "name", "description", "image", "slug", "questions_count"]
		read_only_fields = ["questions_count"]