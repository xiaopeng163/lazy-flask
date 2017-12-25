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

from .i18n import _


class LazyException(Exception):
    """Base Lazy Exception.

    To correctly use this class, inherit from it and define
    a 'message' property. That message will get printf'd
    with the keyword arguments provided to the constructor.
    """
    message = _("An unknown exception occurred.")

    def __init__(self, **kwargs):
        try:
            super(LazyException, self).__init__(self.message % kwargs)
            self.msg = self.message % kwargs
        except Exception:
            # at least get the core message out if something happened
            super(LazyException, self).__init__(self.message)

    def __unicode__(self):
        return unicode(self.msg)
