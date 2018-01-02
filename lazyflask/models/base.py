# Copyright 2017-2018 Be-Lazy Groups
# All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import six

from sqlalchemy import Column, DateTime, String, func, orm
from sqlalchemy.ext.declarative import declarative_base

from lazyflask import utils

BASE = declarative_base()


class BaseTable(BASE, six.Iterator):
    """
    base table
    """
    __abstract__ = True

    def __iter__(self):
        self._i = iter(orm.object_mapper(self).columns)
        return self

    def next(self):
        n = next(self._i).name
        return n, getattr(self, n)

    __next__ = next

    def __setitem__(self, key, value):
        setattr(self, key, value)

    def __getitem__(self, key):
        return getattr(self, key)

    def __contains__(self, key):
        try:
            getattr(self, key)
        except AttributeError:
            return False
        else:
            return True

    def get(self, key, default=None):
        """get item
        """
        return getattr(self, key, default)

    def save(self, session):
        """Save this object."""
        with session.begin(subtransactions=True):
            session.add(self)
            session.flush()

    def update(self, values):
        """make the model object act like a dict
        """
        for k, v in six.iteritems(values):
            setattr(self, k, v)

    def to_dict(self, **args):
        """Make the model object behave like a dict.
        Includes attributes from joins.
        """
        local = dict((key, value) for key, value in self)
        joined = dict([(k, v) for k, v in six.iteritems(self.__dict__)
                      if not k[0] == '_'])
        local.update(joined)
        return local

    def iteritems(self):
        """Make the model object behave like a dict."""
        return six.iteritems(self.to_dict())

    def items(self):
        """Make the model object behave like a dict."""
        return self._as_dict().items()

    def keys(self):
        """Make the model object behave like a dict."""
        return [key for key, _ in self.iteritems()]


class HasId(object):
    """add if subclass have an id
    """

    id = Column(String(36), primary_key=True, default=utils.uuid_generator)


class HasNameDescription(object):
    """add if subclass have name and description
    """
    name = Column(String(45), nullable=True)
    description = Column(String(100), nullable=True)


class HasTime(object):
    """has create and update time stamp columns.
    """
    created_on = Column(DateTime, default=func.now())
