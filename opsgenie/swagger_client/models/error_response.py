# coding: utf-8

"""
    OpsGenie REST API

    OpsGenie API Description

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from pprint import pformat

from six import iteritems


class ErrorResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """

    def __init__(self, request_id=None, took=0.0, message=None, code=None, response_headers=None):
        """
        ErrorResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'request_id': 'str',
            'took': 'float',
            'message': 'str',
            'code': 'int',
            'response_headers': 'dict(str, list[str])'
        }

        self.attribute_map = {
            'request_id': 'requestId',
            'took': 'took',
            'message': 'message',
            'code': 'code',
            'response_headers': 'responseHeaders'
        }

        self._request_id = request_id
        self._took = took
        self._message = message
        self._code = code
        self._response_headers = response_headers

    @property
    def request_id(self):
        """
        Gets the request_id of this ErrorResponse.

        :return: The request_id of this ErrorResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """
        Sets the request_id of this ErrorResponse.

        :param request_id: The request_id of this ErrorResponse.
        :type: str
        """
        if request_id is None:
            raise ValueError("Invalid value for `request_id`, must not be `None`")

        self._request_id = request_id

    @property
    def took(self):
        """
        Gets the took of this ErrorResponse.

        :return: The took of this ErrorResponse.
        :rtype: float
        """
        return self._took

    @took.setter
    def took(self, took):
        """
        Sets the took of this ErrorResponse.

        :param took: The took of this ErrorResponse.
        :type: float
        """
        if took is None:
            raise ValueError("Invalid value for `took`, must not be `None`")

        self._took = took

    @property
    def message(self):
        """
        Gets the message of this ErrorResponse.

        :return: The message of this ErrorResponse.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """
        Sets the message of this ErrorResponse.

        :param message: The message of this ErrorResponse.
        :type: str
        """

        self._message = message

    @property
    def code(self):
        """
        Gets the code of this ErrorResponse.

        :return: The code of this ErrorResponse.
        :rtype: int
        """
        return self._code

    @code.setter
    def code(self, code):
        """
        Sets the code of this ErrorResponse.

        :param code: The code of this ErrorResponse.
        :type: int
        """

        self._code = code

    @property
    def response_headers(self):
        """
        Gets the response_headers of this ErrorResponse.

        :return: The response_headers of this ErrorResponse.
        :rtype: dict(str, list[str])
        """
        return self._response_headers

    @response_headers.setter
    def response_headers(self, response_headers):
        """
        Sets the response_headers of this ErrorResponse.

        :param response_headers: The response_headers of this ErrorResponse.
        :type: dict(str, list[str])
        """

        self._response_headers = response_headers

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, ErrorResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
