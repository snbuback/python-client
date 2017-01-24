# coding: utf-8

"""
Copyright 2016 SmartBear Software

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

        http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.

    Ref: https://github.com/swagger-api/swagger-codegen
"""

from pprint import pformat
from six import iteritems


class PagedAlert(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self):
        """
        PagedAlert - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'items': 'list[Alert]',
            'offset': 'int',
            'limit': 'int',
            'cursor': 'str',
            'total_items': 'int',
            'more_items': 'bool',
            'sort': 'Sorting'
        }

        self.attribute_map = {
            'items': 'items',
            'offset': 'offset',
            'limit': 'limit',
            'cursor': 'cursor',
            'total_items': 'totalItems',
            'more_items': 'moreItems',
            'sort': 'sort'
        }

        self._items = None
        self._offset = None
        self._limit = None
        self._cursor = None
        self._total_items = None
        self._more_items = None
        self._sort = None

    @property
    def items(self):
        """
        Gets the items of this PagedAlert.
        List of requested items

        :return: The items of this PagedAlert.
        :rtype: list[Alert]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this PagedAlert.
        List of requested items

        :param items: The items of this PagedAlert.
        :type: list[Alert]
        """
        self._items = items

    @property
    def offset(self):
        """
        Gets the offset of this PagedAlert.


        :return: The offset of this PagedAlert.
        :rtype: int
        """
        return self._offset

    @offset.setter
    def offset(self, offset):
        """
        Sets the offset of this PagedAlert.


        :param offset: The offset of this PagedAlert.
        :type: int
        """
        self._offset = offset

    @property
    def limit(self):
        """
        Gets the limit of this PagedAlert.


        :return: The limit of this PagedAlert.
        :rtype: int
        """
        return self._limit

    @limit.setter
    def limit(self, limit):
        """
        Sets the limit of this PagedAlert.


        :param limit: The limit of this PagedAlert.
        :type: int
        """
        self._limit = limit

    @property
    def cursor(self):
        """
        Gets the cursor of this PagedAlert.
        The id at which the current (limited) search can be continued to obtain more matching items

        :return: The cursor of this PagedAlert.
        :rtype: str
        """
        return self._cursor

    @cursor.setter
    def cursor(self, cursor):
        """
        Sets the cursor of this PagedAlert.
        The id at which the current (limited) search can be continued to obtain more matching items

        :param cursor: The cursor of this PagedAlert.
        :type: str
        """
        self._cursor = cursor

    @property
    def total_items(self):
        """
        Gets the total_items of this PagedAlert.
        An estimate (lower-bound) of the total number of items available for return.  May not be a tight estimate for facet queries

        :return: The total_items of this PagedAlert.
        :rtype: int
        """
        return self._total_items

    @total_items.setter
    def total_items(self, total_items):
        """
        Sets the total_items of this PagedAlert.
        An estimate (lower-bound) of the total number of items available for return.  May not be a tight estimate for facet queries

        :param total_items: The total_items of this PagedAlert.
        :type: int
        """
        self._total_items = total_items

    @property
    def more_items(self):
        """
        Gets the more_items of this PagedAlert.
        Whether more items are available for return by increment offset or cursor

        :return: The more_items of this PagedAlert.
        :rtype: bool
        """
        return self._more_items

    @more_items.setter
    def more_items(self, more_items):
        """
        Sets the more_items of this PagedAlert.
        Whether more items are available for return by increment offset or cursor

        :param more_items: The more_items of this PagedAlert.
        :type: bool
        """
        self._more_items = more_items

    @property
    def sort(self):
        """
        Gets the sort of this PagedAlert.
        How returned items have been sorted

        :return: The sort of this PagedAlert.
        :rtype: Sorting
        """
        return self._sort

    @sort.setter
    def sort(self, sort):
        """
        Sets the sort of this PagedAlert.
        How returned items have been sorted

        :param sort: The sort of this PagedAlert.
        :type: Sorting
        """
        self._sort = sort

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
        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other

