from .ml_model import MentorshipModel
from alumni_app.models import Alumni, Mentorship

class MentorshipMatcher:
    def __init__(self):
        self.model = MentorshipModel()

    def get_recommendations(self, alumni_email):
        alumni = Alumni.objects.get(email=alumni_email)
        # Example feature extraction
        skills = alumni.skills
        area_of_interest = alumni.area_of_interest
        # Predicting recommendations
        recommendations = self.model.predict(skills, area_of_interest)
        # Fetch matching alumni or create matching logic
        matched_alumni = Alumni.objects.filter(skills__in=skills, area_of_interest=area_of_interest)
        return matched_alumni
