# mbti_app/management/commands/populate_mbti.py
from django.core.management.base import BaseCommand
from mbti_app.models import MBTIType, Question
from django.conf import settings

class Command(BaseCommand):
    help = 'Populate MBTI types and questions into the database'

    def handle(self, *args, **kwargs):  # Include **kwargs
        # Clear existing data to avoid duplicates
        try:
            MBTIType.objects.all().delete()
            Question.objects.all().delete()
        except Exception as e:
            self.stdout.write(self.style.ERROR(f"❌ Error clearing existing data: {str(e)}"))
            return

        # Create MBTI types
        MBTIType.objects.create(
            type_code="INTJ",
            name="The Architect",
            description="Analytical problem-solvers who enjoy abstract thinking."


        )

        # Create questions
        Question.objects.create(
            text="I prefer plans over spontaneity.",
            dichotomy="JP",
            direction=-1  # -1 = "No" maps to Judging (J), 1 = "Yes" to Perceiving (P)
        )

        self.stdout.write(self.style.SUCCESS("✅ MBTI data populated!"))