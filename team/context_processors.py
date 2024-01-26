from .models import Team


def active_team(request):
    if request.user.is_authenticated:
        active_team = request.user.userprofile.get_active_team()
        
        if not active_team:
            active_team = Team.objects.filter(created_by=request.user).first()
    else:
        active_team = None

    return {'active_team': active_team}


# def active_team(request):
#     if request.user.is_authenticated:
#         active_team = request.user.userprofile.get_active_team()

#         if not active_team:
#             # Use .first() to get the first result or None if the queryset is empty
#             active_team = Team.objects.filter(Q(created_by=request.user)).first()

#     else:
#         active_team = None

#     return {'active_team': active_team}
