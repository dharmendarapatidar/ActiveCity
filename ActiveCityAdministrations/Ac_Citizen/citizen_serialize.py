from rest_framework.serializers import ModelSerializer
from .models import Citizen_Table,Complaint_Table,Feedback_Table


class CitizenSerialize(ModelSerializer):
    class Meta:
        model = Citizen_Table
        fields = '__all__'


class ComplaintSerialize(ModelSerializer):
    class Meta:
        model = Complaint_Table
        fields = '__all__'


class FeedbackSerialize(ModelSerializer):
    class Meta:
        model = Feedback_Table
        fields = '__all__'
