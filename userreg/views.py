from djoser.views import UserViewSet
from userreg.pagination import LimitPageNumberPagination


class UserView(UserViewSet):
    pagination_class = LimitPageNumberPagination
