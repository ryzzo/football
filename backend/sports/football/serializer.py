from rest_framework import serializers
from .models import Team, MatchGame, Stat

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['name', 'coach', 'logo']

class MatchGameSerializer(serializers.ModelSerializer):
    home_team = TeamSerializer(read_only=True)
    away_team = TeamSerializer(read_only=True)
    class Meta:
        model = MatchGame
        fields = ['home_team', 'home_team_scores',
                  'away_team', 'away_team_scores',
                  'date', 'time', 'played']

class StatSerializer(serializers.ModelSerializer):
    #team_name = serializers.ReadOnlyField(source='team.name')
    team = TeamSerializer(read_only=True)
    class Meta:
        model = Stat
        fields = ['team',
                  'matches_played', 'matches_won',
                  'matches_lost', 'matches_drawn',
                  'goals_for', 'goals_against',
                  'goal_difference', 'points']
        