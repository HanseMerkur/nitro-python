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


class systemeventhistory_args :
    """Provides additional arguments required for fetching the systemeventhistory resource."""
    def __init__(self) :
        self._starttime = ""
        self._endtime = ""
        self._last = 0
        self._unit = ""
        self._datasource = ""

    @property
    def starttime(self) :
        """Specify start time in mmddyyyyhhmm to start collecting values from that timestamp."""
        try :
            return self._starttime
        except Exception as e:
            raise e

    @starttime.setter
    def starttime(self, starttime) :
        """Specify start time in mmddyyyyhhmm to start collecting values from that timestamp.

        :param starttime: 

        """
        try :
            self._starttime = starttime
        except Exception as e:
            raise e

    @property
    def endtime(self) :
        """Specify end time in mmddyyyyhhmm upto which values have to be collected."""
        try :
            return self._endtime
        except Exception as e:
            raise e

    @endtime.setter
    def endtime(self, endtime) :
        """Specify end time in mmddyyyyhhmm upto which values have to be collected.

        :param endtime: 

        """
        try :
            self._endtime = endtime
        except Exception as e:
            raise e

    @property
    def last(self) :
        """Last is literal way of saying a certain time period from the current moment. Example: -last 1 hour, -last 1 day, et cetera.<br/>Default value: 1."""
        try :
            return self._last
        except Exception as e:
            raise e

    @last.setter
    def last(self, last) :
        """Last is literal way of saying a certain time period from the current moment. Example: -last 1 hour, -last 1 day, et cetera.<br/>Default value: 1

        :param last: 

        """
        try :
            self._last = last
        except Exception as e:
            raise e

    @property
    def unit(self) :
        """Specify the time period from current moment. Example 1 x where x = hours/ days/ years.<br/>Possible values = HOURS, DAYS, MONTHS."""
        try :
            return self._unit
        except Exception as e:
            raise e

    @unit.setter
    def unit(self, unit) :
        """Specify the time period from current moment. Example 1 x where x = hours/ days/ years.<br/>Possible values = HOURS, DAYS, MONTHS

        :param unit: 

        """
        try :
            self._unit = unit
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

    class Unit:
        """ """
        HOURS = "HOURS"
        DAYS = "DAYS"
        MONTHS = "MONTHS"

