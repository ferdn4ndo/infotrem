from rest_framework import viewsets
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response

from infotrem.services.policy import IsLoggedIn, IsModeratorOrReadOnly

