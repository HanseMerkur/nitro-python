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

class nspbr6_stats(base_resource) :
    """Statistics for PBR6 entry resource."""
    def __init__(self) :
        self._name = ""
        self._clearstats = ""
        self._pbr6totpktsallowed = 0
        self._pbr6pktsallowedrate = 0
        self._pbr6totpktsdenied = 0
        self._pbr6pktsdeniedrate = 0
        self._pbr6tothits = 0
        self._pbr6hitsrate = 0
        self._pbr6totmisses = 0
        self._pbr6missesrate = 0
        self._pbr6perhits = 0
        self._pbr6perhitsrate = 0

    @property
    def name(self) :
        """Name of the PBR6 whose statistics you want the NetScaler appliance to display.<br/>Minimum length =  1."""
        try :
            return self._name
        except Exception as e:
            raise e

    @name.setter
    def name(self, name) :
        """Name of the PBR6 whose statistics you want the NetScaler appliance to display.

        :param name: 

        """
        try :
            self._name = name
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
    def pbr6pktsallowedrate(self) :
        """Rate (/s) counter for pbr6totpktsallowed."""
        try :
            return self._pbr6pktsallowedrate
        except Exception as e:
            raise e

    @property
    def pbr6pktsdeniedrate(self) :
        """Rate (/s) counter for pbr6totpktsdenied."""
        try :
            return self._pbr6pktsdeniedrate
        except Exception as e:
            raise e

    @property
    def pbr6perhits(self) :
        """Number of times the pbr6 was hit."""
        try :
            return self._pbr6perhits
        except Exception as e:
            raise e

    @property
    def pbr6totpktsallowed(self) :
        """Total packets that matched the PBR6 with action ALLOW ."""
        try :
            return self._pbr6totpktsallowed
        except Exception as e:
            raise e

    @property
    def pbr6missesrate(self) :
        """Rate (/s) counter for pbr6totmisses."""
        try :
            return self._pbr6missesrate
        except Exception as e:
            raise e

    @property
    def pbr6tothits(self) :
        """Total packets that matched one of the configured PBR6."""
        try :
            return self._pbr6tothits
        except Exception as e:
            raise e

    @property
    def pbr6perhitsrate(self) :
        """Rate (/s) counter for pbr6perhits."""
        try :
            return self._pbr6perhitsrate
        except Exception as e:
            raise e

    @property
    def pbr6totpktsdenied(self) :
        """Total packets that matched PBR6 with action DENY ."""
        try :
            return self._pbr6totpktsdenied
        except Exception as e:
            raise e

    @property
    def pbr6hitsrate(self) :
        """Rate (/s) counter for pbr6tothits."""
        try :
            return self._pbr6hitsrate
        except Exception as e:
            raise e

    @property
    def pbr6totmisses(self) :
        """Total packets that did not match any PBR6."""
        try :
            return self._pbr6totmisses
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(nspbr6_response, response, self.__class__.__name__.replace('_stats',''))
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.nspbr6
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
        """Use this API to fetch the statistics of all nspbr6_stats resources that are configured on netscaler.

        :param service: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            obj = nspbr6_stats()
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

class nspbr6_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.nspbr6 = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.nspbr6 = [nspbr6_stats() for _ in range(length)]

