#
# Copyright (c) 2008-2015 Citrix Systems, Inc.
#
#   Licensed under the Apache License, Version 2.0 (the "License")
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
#


class systemcounters_args :
    """Provides additional arguments required for fetching the systemcounters resource."""
    def __init__(self) :
        self._countergroup = ""
        self._datasource = ""

    @property
    def countergroup(self) :
        """Specify the (counter) group name which contains all the counters specific tot his particular group."""
        try :
            return self._countergroup
        except Exception as e:
            raise e

    @countergroup.setter
    def countergroup(self, countergroup) :
        """Specify the (counter) group name which contains all the counters specific tot his particular group.

        :param countergroup: 

        """
        try :
            self._countergroup = countergroup
        except Exception as e:
            raise e

    @property
    def datasource(self) :
        """Specifies the source which contains all the stored counter values."""
        try :
            return self._datasource
        except Exception as e:
            raise e

    @datasource.setter
    def datasource(self, datasource) :
        """Specifies the source which contains all the stored counter values.

        :param datasource: 

        """
        try :
            self._datasource = datasource
        except Exception as e:
            raise e

