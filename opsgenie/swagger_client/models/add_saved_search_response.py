# coding: utf-8

"""
    OpsGenie REST API

    OpsGenie API Description

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from pprint import pformat

from six import iteritems


class AddSavedSearchResponse(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """

    def __init__(self, request_id=None, took=0.0, data=None):
        """
        AddSavedSearchResponse - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'request_id': 'str',
            'took': 'float',
            'data': 'SavedSearchMeta'
        }

        self.attribute_map = {
            'request_id': 'requestId',
            'took': 'took',
            'data': 'data'
        }

        self._request_id = request_id
        self._took = took
        self._data = data

    @property
    def request_id(self):
        """
        Gets the request_id of this AddSavedSearchResponse.

        :return: The request_id of this AddSavedSearchResponse.
        :rtype: str
        """
        return self._request_id

    @request_id.setter
    def request_id(self, request_id):
        """
        Sets the request_id of this AddSavedSearchResponse.

        :param request_id: The request_id of this AddSavedSearchResponse.
        :type: str
        """
        if request_id is None:
            raise ValueError("Invalid value for `request_id`, must not be `None`")

        self._request_id = request_id

    @property
    def took(self):
        """
        Gets the took of this AddSavedSearchResponse.

        :return: The took of this AddSavedSearchResponse.
        :rtype: float
        """
        return self._took

    @took.setter
    def took(self, took):
        """
        Sets the took of this AddSavedSearchResponse.

        :param took: The took of this AddSavedSearchResponse.
        :type: float
        """
        if took is None:
            raise ValueError("Invalid value for `took`, must not be `None`")

        self._took = took

    @property
    def data(self):
        """
        Gets the data of this AddSavedSearchResponse.

        :return: The data of this AddSavedSearchResponse.
        :rtype: SavedSearchMeta
        """
        return self._data

    @data.setter
    def data(self, data):
        """
        Sets the data of this AddSavedSearchResponse.

        :param data: The data of this AddSavedSearchResponse.
        :type: SavedSearchMeta
        """

        self._data = data

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
        if not isinstance(other, AddSavedSearchResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
