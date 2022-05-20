from rest_framework import serializers

from .models import User, Report


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name"]


class ReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = Report
        fields = [
            "report_text",
            "negative_attitude_opt",
            "trolling_opt",
            "verbal_abuse_opt",
            "unskilled_player_opt",
            "is_andy_tong_opt",
        ]
