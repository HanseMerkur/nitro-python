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

from nitro.resource.base.base_resource import base_resource
from nitro.resource.base.base_resource import base_response
from nitro.service.options import options
from nitro.exception.nitro_exception import nitro_exception

from nitro.util.nitro_util import nitro_util

class streamidentifier_stats(base_resource) :
    """Statistics for identifier resource."""
    def __init__(self) :
        self._name = ""
        self._pattern = []
        self._clearstats = ""
        self._sortby = ""
        self._sortorder = ""
        self._streamobjreq = 0
        self._streamobjbandw = 0
        self._streamobjresptime = 0
        self._streamobjconn = 0
        self._streamobjbreachcnt = 0

    @property
    def name(self) :
        """Name of the stream identifier.<br/>Minimum length =  1."""
        try :
            return self._name
        except Exception as e:
            raise e

    @name.setter
    def name(self, name) :
        """Name of the stream identifier.

        :param name: 

        """
        try :
            self._name = name
        except Exception as e:
            raise e

    @property
    def pattern(self) :
        """Values on which grouping is performed are displayed in the output as row titles. If grouping is performed on two or more fields, their values are separated by a question mark in the row title.
        For example, consider a selector that contains the expressions HTTP.REQ.URL and CLIENT.IP.SRC (in that order), on an appliance that has accumulated records of a number of requests for two URLs, example.com/page1.html and example.com/page2.html, from two client IP addresses, 192.0.2.10 and 192.0.2.11.
        With a pattern of ? ?, the appliance performs grouping on both fields and displays statistics for the following:
        * Requests for example.com/abc.html from 192.0.2.10, with a row title of example.com/abc.html?192.0.2.10.
        * Requests for example.com/abc.html from 192.0.2.11, with a row title of example.com/abc.html?192.0.2.11.
        * Requests for example.com/def.html from 192.0.2.10, with a row title of example.com/def.html?192.0.2.10.
        * Requests for example.com/def.html from 192.0.2.11, with a row title of example.com/def.html?192.0.2.11.
        With a pattern of * ?, the appliance performs grouping on only the client IP address values and displays statistics for the following requests:
        * All requests from 192.0.2.10, with the IP address as the row title.
        * All requests from 192.0.2.11, with the IP address as the row title.
        With a pattern of ? *, the appliance performs grouping on only the URL values and displays statistics for the following requests:
        * All requests for example.com/abc.html, with the URL as the row title.
        * All requests for example.com/def.html, with the URL as the row title.
        With a pattern of * *, the appliance displays one set of collective statistics for all the requests received, with no row title.
        With a pattern of example.com/abc.html ?, the appliance displays statistics for requests for example.com/abc.html from each unique client IP address.
        With a pattern of * 192.0.2.11, the appliance displays statistics for all requests from 192.0.2.11.


        """
        try :
            return self._pattern
        except Exception as e:
            raise e

    @pattern.setter
    def pattern(self, pattern) :
        """Values on which grouping is performed are displayed in the output as row titles. If grouping is performed on two or more fields, their values are separated by a question mark in the row title.
        For example, consider a selector that contains the expressions HTTP.REQ.URL and CLIENT.IP.SRC (in that order), on an appliance that has accumulated records of a number of requests for two URLs, example.com/page1.html and example.com/page2.html, from two client IP addresses, 192.0.2.10 and 192.0.2.11.
        With a pattern of ? ?, the appliance performs grouping on both fields and displays statistics for the following:
        * Requests for example.com/abc.html from 192.0.2.10, with a row title of example.com/abc.html?192.0.2.10.
        * Requests for example.com/abc.html from 192.0.2.11, with a row title of example.com/abc.html?192.0.2.11.
        * Requests for example.com/def.html from 192.0.2.10, with a row title of example.com/def.html?192.0.2.10.
        * Requests for example.com/def.html from 192.0.2.11, with a row title of example.com/def.html?192.0.2.11.
        With a pattern of * ?, the appliance performs grouping on only the client IP address values and displays statistics for the following requests:
        * All requests from 192.0.2.10, with the IP address as the row title.
        * All requests from 192.0.2.11, with the IP address as the row title.
        With a pattern of ? *, the appliance performs grouping on only the URL values and displays statistics for the following requests:
        * All requests for example.com/abc.html, with the URL as the row title.
        * All requests for example.com/def.html, with the URL as the row title.
        With a pattern of * *, the appliance displays one set of collective statistics for all the requests received, with no row title.
        With a pattern of example.com/abc.html ?, the appliance displays statistics for requests for example.com/abc.html from each unique client IP address.
        With a pattern of * 192.0.2.11, the appliance displays statistics for all requests from 192.0.2.11.

        :param pattern: 

        """
        try :
            self._pattern = pattern
        except Exception as e:
            raise e

    @property
    def clearstats(self) :
        """Clear the statsistics / counters.<br/>Possible values = basic, full."""
        try :
            return self._clearstats
        except Exception as e:
            raise e

    @clearstats.setter
    def clearstats(self, clearstats) :
        """Clear the statsistics / counters

        :param clearstats: 

        """
        try :
            self._clearstats = clearstats
        except Exception as e:
            raise e

    @property
    def sortby(self) :
        """use this argument to sort by specific key.<br/>Possible values = ."""
        try :
            return self._sortby
        except Exception as e:
            raise e

    @sortby.setter
    def sortby(self, sortby) :
        """use this argument to sort by specific key

        :param sortby: 

        """
        try :
            self._sortby = sortby
        except Exception as e:
            raise e

    @property
    def sortorder(self) :
        """use this argument to specify sort order.<br/>Default value: SORT_DESCENDING<br/>Possible values = ascending, descending."""
        try :
            return self._sortorder
        except Exception as e:
            raise e

    @sortorder.setter
    def sortorder(self, sortorder) :
        """use this argument to specify sort order

        :param sortorder: 

        """
        try :
            self._sortorder = sortorder
        except Exception as e:
            raise e

    @property
    def streamobjconn(self) :
        """Current connections on the stream session."""
        try :
            return self._streamobjconn
        except Exception as e:
            raise e

    @property
    def streamobjbreachcnt(self) :
        """Total Breaching Transactions in configured interval."""
        try :
            return self._streamobjbreachcnt
        except Exception as e:
            raise e

    @property
    def streamobjbandw(self) :
        """Total Bandwidth consumed."""
        try :
            return self._streamobjbandw
        except Exception as e:
            raise e

    @property
    def streamobjresptime(self) :
        """Average response time of the stream session."""
        try :
            return self._streamobjresptime
        except Exception as e:
            raise e

    @property
    def streamobjreq(self) :
        """Total number of Stream Requests recieved."""
        try :
            return self._streamobjreq
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(streamidentifier_response, response, self.__class__.__name__.replace('_stats',''))
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.streamidentifier
        except Exception as e :
            raise e

    def _get_object_name(self) :
        """Returns the value of object identifier argument"""
        try :
            if self.name is not None :
                return str(self.name)
            return None
        except Exception as e :
            raise e



    @classmethod
    def  get(cls, service, name="", option_="") :
        """Use this API to fetch the statistics of all streamidentifier_stats resources that are configured on netscaler.

        :param service: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            obj = streamidentifier_stats()
            if name :
                obj.name = name
                response = obj.stat_resource(service, option_)
            option_ = options()
            option_.args = nitro_util.object_to_string_withoutquotes(name)
            response = obj.stat_resource(service, option_)
            return response
        except Exception as e:
            raise e

    class Clearstats:
        """ """
        basic = "basic"
        full = "full"

    class Sortorder:
        """ """
        ascending = "ascending"
        descending = "descending"

class streamidentifier_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.streamidentifier = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.streamidentifier = [streamidentifier_stats() for _ in range(length)]

