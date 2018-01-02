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

from __future__ import print_function
from datetime import datetime
import uuid

import six
import prettytable


def timestamp():
    """return current time
    """
    return datetime.now().__str__()


def uuid_generator():
    """generate uuid string
    """
    return uuid.uuid4().hex


def print_list(objs, fields, exclude_unavailable=False):
    """Prints a list of objects.
    @param objs: Objects to print
    @param fields: Fields on each object to be printed
    @param exclude_unavailable: Boolean to decide if unavailable fields are
                                removed
    """
    rows = []
    removed_fields = []
    for o in objs:
        row = []
        for field in fields:
            if field in removed_fields:
                continue
            if isinstance(o, dict) and field in o:
                data = o[field]
            else:
                if not hasattr(o, field) and exclude_unavailable:
                    removed_fields.append(field)
                    continue
                else:
                    data = getattr(o, field, '')
            if data is None:
                data = '-'
            if isinstance(data, six.string_types) and "\r" in data:
                data = data.replace("\r", " ")
            row.append(data)
        rows.append(row)

    for f in removed_fields:
        fields.remove(f)

    pt = prettytable.PrettyTable((f for f in fields), caching=False)
    pt.align = 'l'
    for row in rows:
        pt.add_row(row)
    print(pt)
