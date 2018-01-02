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

from sqlalchemy import Column, String

from lazyflask.models import base


class User(base.BaseTable, base.HasId, base.HasTime):
    """user table
    """

    __tablename__ = 'users'

    name = Column(String(32), unique=True)
    password_hash = Column(String(256), nullable=False)
