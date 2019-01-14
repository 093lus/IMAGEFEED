from rest_framework.exceptions import APIException


class InvalidAPIQuery(APIException):
    status_code = 400
    default_detail = 'invalid query parameters were provided'