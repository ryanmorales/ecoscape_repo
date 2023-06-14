from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_401_UNAUTHORIZED, HTTP_400_BAD_REQUEST


class BaseViewSet(ViewSet):
    """ This class will handle the generic functionality of a viewset """

    @classmethod
    def error_response(self, message, extra_info={}):
        context = {
            "success": False,
            "error_message": message,
        }

        if extra_info:
            context["extra_info"] = extra_info

        return Response(context, status=HTTP_200_OK)

    @classmethod
    def success_response(self, message, extra_info={}):
        context = {
            "success": True,
            "message": message,
        }

        if extra_info:
            context["data"] = extra_info

        return Response(context, status=HTTP_200_OK)

    @classmethod
    def success_data_response(self, data):
        context = {
            "success": True,
            "data": data,
        }

        return Response(context, status=HTTP_200_OK)

    @classmethod
    def unauthorized_response(self):
        context = {
            "detail": "Invalid credentials"
        }

        return Response(context, status=HTTP_401_UNAUTHORIZED)

    @classmethod
    def bad_request_response(self, message, extra_info={}):
        context = {
            "success": False,
            "error_message": message,
        }

        if extra_info:
            context["extra_info"] = extra_info

        return Response(context, status=HTTP_400_BAD_REQUEST)
