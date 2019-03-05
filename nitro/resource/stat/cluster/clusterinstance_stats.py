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

class clusterinstance_stats(base_resource) :
    """Statistics for cluster instance resource."""
    def __init__(self) :
        self._clid = 0
        self._clearstats = ""
        self._clnumnodes = 0
        self._clcurstatus = ""
        self._clviewleader = ""
        self._totsteeredpkts = 0
        self._clbkplanerx = 0
        self._clbkplanerxrate = 0
        self._clbkplanetx = 0
        self._clbkplanetxrate = 0
        self._numdfddroppkts = 0
        self._totpropagationtimeout = 0

    @property
    def clid(self) :
        """ID of the cluster instance for which to display statistics.<br/>Minimum value =  1<br/>Maximum value =  16."""
        try :
            return self._clid
        except Exception as e:
            raise e

    @clid.setter
    def clid(self, clid) :
        """ID of the cluster instance for which to display statistics.

        :param clid: 

        """
        try :
            self._clid = clid
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
    def totpropagationtimeout(self) :
        """Number of times the update to the client timed-out."""
        try :
            return self._totpropagationtimeout
        except Exception as e:
            raise e

    @property
    def clbkplanetx(self) :
        """Traffic transmitted from backplane (in mbits)."""
        try :
            return self._clbkplanetx
        except Exception as e:
            raise e

    @property
    def clbkplanetxrate(self) :
        """Rate (/s) counter for clbkplanetx."""
        try :
            return self._clbkplanetxrate
        except Exception as e:
            raise e

    @property
    def totsteeredpkts(self) :
        """Total number of packets steered on the cluster backplane."""
        try :
            return self._totsteeredpkts
        except Exception as e:
            raise e

    @property
    def numdfddroppkts(self) :
        """Number of steered packets that are dropped."""
        try :
            return self._numdfddroppkts
        except Exception as e:
            raise e

    @property
    def clviewleader(self) :
        """NSIP address of the Configuration Coordinator of the cluster."""
        try :
            return self._clviewleader
        except Exception as e:
            raise e

    @property
    def clbkplanerx(self) :
        """Traffic received on backplane (in mbits)."""
        try :
            return self._clbkplanerx
        except Exception as e:
            raise e

    @property
    def clcurstatus(self) :
        """State of the cluster."""
        try :
            return self._clcurstatus
        except Exception as e:
            raise e

    @property
    def clnumnodes(self) :
        """Number of nodes in the cluster."""
        try :
            return self._clnumnodes
        except Exception as e:
            raise e

    @property
    def clbkplanerxrate(self) :
        """Rate (/s) counter for clbkplanerx."""
        try :
            return self._clbkplanerxrate
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(clusterinstance_response, response, self.__class__.__name__.replace('_stats',''))
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.clusterinstance
        except Exception as e :
            raise e

    def _get_object_name(self) :
        """Returns the value of object identifier argument"""
        try :
            if self.clid is not None :
                return str(self.clid)
            return None
        except Exception as e :
            raise e



    @classmethod
    def  get(cls, service, name="", option_="") :
        """Use this API to fetch the statistics of all clusterinstance_stats resources that are configured on netscaler.

        :param service: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            obj = clusterinstance_stats()
            if not name :
                response = obj.stat_resources(service, option_)
            else :
                obj.clid = name
                response = obj.stat_resource(service, option_)
            return response
        except Exception as e:
            raise e

    class Clearstats:
        """ """
        basic = "basic"
        full = "full"

class clusterinstance_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.clusterinstance = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.clusterinstance = [clusterinstance_stats() for _ in range(length)]

