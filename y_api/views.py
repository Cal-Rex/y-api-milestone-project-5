from rest_framework.decorators import api_view
from rest_framework.response import Response
from .settings import (
        JWT_AUTH_COOKIE,
        JWT_AUTH_REFRESH_COOKIE,
        JWT_AUTH_SAMESITE,
        JWT_AUTH_SECURE,
    )


@api_view()
def root_route(request):
    """
    object returned when visiting root route
    of API, gives prompts on how to navigate via browser
    """
    return Response({
        "message": "welcome to the Y API",
        "instructions 1": "suffix the url with /admin to log in",
        "instructions 2": "Or, view the different tables with:",
        "instructions 3": [
            "/profiles",
            "/posts",
            "/comments",
            "/follows",
            "/likes",
            "/votes",
        ]
    })



@api_view(['POST'])
def logout_route(request):
    """
    dj-rest-auth logout view fix
    """
    response = Response()
    response.set_cookie(
        key=JWT_AUTH_COOKIE,
        value='',
        httponly=True,
        expires='Thu, 01 Jan 1970 00:00:00 GMT',
        max_age=0,
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )
    response.set_cookie(
        key=JWT_AUTH_REFRESH_COOKIE,
        value='',
        httponly=True,
        expires='Thu, 01 Jan 1970 00:00:00 GMT',
        max_age=0,
        samesite=JWT_AUTH_SAMESITE,
        secure=JWT_AUTH_SECURE,
    )
    return response


# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .settings import (
#     JWT_AUTH_COOKIE,
#     JWT_AUTH_REFRESH_COOKIE,
#     JWT_AUTH_SAMESITE,
#     JWT_AUTH_SECURE,
# )

# @api_view(['POST'])
# def logout_route(request):
#     response = Response()
#     response.set_cookie(
#         key=JWT_AUTH_COOKIE,
#         value='',
#         httponly=True,
#         expires='Thu, 01 Jan 1970 00:00:00 GMT',
#         max_age=0,
#         samesite=JWT_AUTH_SAMESITE,
#         secure=JWT_AUTH_SECURE,
#     )
#     response.set_cookie(
#         key=JWT_AUTH_REFRESH_COOKIE,
#         value='',
#         httponly=True,
#         expires='Thu, 01 Jan 1970 00:00:00 GMT',
#         max_age=0,
#         samesite=JWT_AUTH_SAMESITE,
#         secure=JWT_AUTH_SECURE,
#     )
#     return response

