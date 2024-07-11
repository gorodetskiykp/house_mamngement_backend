from django.contrib import admin

from .models import BuildingChief, EntranceChief, FloorChief, Vote, VoteResults

admin.site.register(BuildingChief)
admin.site.register(EntranceChief)
admin.site.register(FloorChief)
admin.site.register(Vote)
admin.site.register(VoteResults)
