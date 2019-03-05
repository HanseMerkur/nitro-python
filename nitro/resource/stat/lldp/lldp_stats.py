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

class lldp_stats(base_resource) :
    """ """
    def __init__(self) :
        self._ifnum = ""
        self._clearstats = ""
        self._rxportframestotal = 0
        self._rxportframesrate = 0
        self._rxportbytestotal = 0
        self._rxportbytesrate = 0
        self._txportframestotal = 0
        self._txportframesrate = 0
        self._txportbytestotal = 0
        self._txportbytesrate = 0
        self._rxportframeserrors = 0
        self._rxportframeserrorsrate = 0
        self._rxporttlvsdiscardedtotal = 0
        self._rxporttlvsdiscardedrate = 0
        self._rxporttlvsunrecognizedtotal = 0
        self._rxporttlvsunrecognizedrate = 0

    @property
    def ifnum(self) :
        """LLDP Statistics per interfaces."""
        try :
            return self._ifnum
        except Exception as e:
            raise e

    @ifnum.setter
    def ifnum(self, ifnum) :
        """LLDP Statistics per interfaces

        :param ifnum: 

        """
        try :
            self._ifnum = ifnum
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
    def rxporttlvsdiscardedtotal(self) :
        """Total discarded LLDP packets."""
        try :
            return self._rxporttlvsdiscardedtotal
        except Exception as e:
            raise e

    @property
    def rxportframeserrors(self) :
        """Total errors in LLDP packets."""
        try :
            return self._rxportframeserrors
        except Exception as e:
            raise e

    @property
    def rxportframeserrorsrate(self) :
        """Rate (/s) counter for rxportframeserrors."""
        try :
            return self._rxportframeserrorsrate
        except Exception as e:
            raise e

    @property
    def rxportframestotal(self) :
        """Total LLDP Packets received."""
        try :
            return self._rxportframestotal
        except Exception as e:
            raise e

    @property
    def txportbytestotal(self) :
        """Total LLDP bytes transmitted."""
        try :
            return self._txportbytestotal
        except Exception as e:
            raise e

    @property
    def txportframestotal(self) :
        """Total LLDP Packets transmitted."""
        try :
            return self._txportframestotal
        except Exception as e:
            raise e

    @property
    def rxporttlvsunrecognizedtotal(self) :
        """Total TLVs not Recognised."""
        try :
            return self._rxporttlvsunrecognizedtotal
        except Exception as e:
            raise e

    @property
    def rxportbytesrate(self) :
        """Rate (/s) counter for rxportbytestotal."""
        try :
            return self._rxportbytesrate
        except Exception as e:
            raise e

    @property
    def rxportbytestotal(self) :
        """Total LLDP bytes received."""
        try :
            return self._rxportbytestotal
        except Exception as e:
            raise e

    @property
    def rxporttlvsdiscardedrate(self) :
        """Rate (/s) counter for rxporttlvsdiscardedtotal."""
        try :
            return self._rxporttlvsdiscardedrate
        except Exception as e:
            raise e

    @property
    def txportbytesrate(self) :
        """Rate (/s) counter for txportbytestotal."""
        try :
            return self._txportbytesrate
        except Exception as e:
            raise e

    @property
    def rxporttlvsunrecognizedrate(self) :
        """Rate (/s) counter for rxporttlvsunrecognizedtotal."""
        try :
            return self._rxporttlvsunrecognizedrate
        except Exception as e:
            raise e

    @property
    def rxportframesrate(self) :
        """Rate (/s) counter for rxportframestotal."""
        try :
            return self._rxportframesrate
        except Exception as e:
            raise e

    @property
    def txportframesrate(self) :
        """Rate (/s) counter for txportframestotal."""
        try :
            return self._txportframesrate
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(lldp_response, response, self.__class__.__name__.replace('_stats',''))
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.lldp
        except Exception as e :
            raise e

    def _get_object_name(self) :
        """Returns the value of object identifier argument"""
        try :
            if self.ifnum is not None :
                return str(self.ifnum)
            return None
        except Exception as e :
            raise e



    @classmethod
    def  get(cls, service, name="", option_="") :
        """Use this API to fetch the statistics of all lldp_stats resources that are configured on netscaler.

        :param service: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            obj = lldp_stats()
            if not name :
                response = obj.stat_resources(service, option_)
            else :
                obj.ifnum = name
                response = obj.stat_resource(service, option_)
            return response
        except Exception as e:
            raise e

    class Clearstats:
        """ """
        basic = "basic"
        full = "full"

class lldp_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.lldp = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.lldp = [lldp_stats() for _ in range(length)]

