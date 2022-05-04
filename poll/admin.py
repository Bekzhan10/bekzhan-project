from django.contrib import admin
from poll.models import Films
admin.site.register(Films)
from poll.models import Users
admin.site.register(Users)
from poll.models import Genres
admin.site.register(Genres)
from .models import Cartoons
admin.site.register(Cartoons)
from .models import Poll
admin.site.register(Poll)
from .models import Posts
admin.site.register(Posts)

