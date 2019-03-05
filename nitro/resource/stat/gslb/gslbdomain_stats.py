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

class gslbdomain_stats(base_resource) :
    """Statistics for GSLB domain resource."""
    def __init__(self) :
        self._name = ""
        self._dnsrecordtype = ""
        self._clearstats = ""
        self._dnstotalqueries = 0
        self._dnsqueriesrate = 0
        self._gslbdnsrectype = ""

    @property
    def name(self) :
        """Name of the GSLB domain for which to display statistics. If you do not specify a name, statistics are shown for all configured GSLB
        domains.<br/>Minimum length =  1.


        """
        try :
            return self._name
        except Exception as e:
            raise e

    @name.setter
    def name(self, name) :
        """Name of the GSLB domain for which to display statistics. If you do not specify a name, statistics are shown for all configured GSLB
        domains.

        :param name: 

        """
        try :
            self._name = name
        except Exception as e:
            raise e

    @property
    def dnsrecordtype(self) :
        """.<br/>Possible values = A, AAAA, CNAME, NAPTR."""
        try :
            return self._dnsrecordtype
        except Exception as e:
            raise e

    @dnsrecordtype.setter
    def dnsrecordtype(self, dnsrecordtype) :
        """

        :param dnsrecordtype: 

        """
        try :
            self._dnsrecordtype = dnsrecordtype
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
    def dnsqueriesrate(self) :
        """Rate (/s) counter for dnstotalqueries."""
        try :
            return self._dnsqueriesrate
        except Exception as e:
            raise e

    @property
    def dnstotalqueries(self) :
        """Total number of DNS queries received."""
        try :
            return self._dnstotalqueries
        except Exception as e:
            raise e

    @property
    def gslbdnsrectype(self) :
        """Type of DNS record returned."""
        try :
            return self._gslbdnsrectype
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(gslbdomain_response, response, self.__class__.__name__.replace('_stats',''))
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.gslbdomain
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
        """Use this API to fetch the statistics of all gslbdomain_stats resources that are configured on netscaler.

        :param service: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            obj = gslbdomain_stats()
            if not name :
                response = obj.stat_resources(service, option_)
            else :
                obj.name = name
                response = obj.stat_resource(service, option_)
            return response
        except Exception as e:
            raise e

    class Clearstats:
        """ """
        basic = "basic"
        full = "full"

    class Dnsrecordtype:
        """ """
        A = "A"
        AAAA = "AAAA"
        CNAME = "CNAME"
        NAPTR = "NAPTR"

class gslbdomain_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.gslbdomain = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.gslbdomain = [gslbdomain_stats() for _ in range(length)]

