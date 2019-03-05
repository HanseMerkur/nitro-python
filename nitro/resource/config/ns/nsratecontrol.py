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

class nsratecontrol(base_resource) :
    """Configuration for rate control resource."""
    def __init__(self) :
        self._tcpthreshold = 0
        self._udpthreshold = 0
        self._icmpthreshold = 0
        self._tcprstthreshold = 0

    @property
    def tcpthreshold(self) :
        """Number of SYNs permitted per 10 milliseconds."""
        try :
            return self._tcpthreshold
        except Exception as e:
            raise e

    @tcpthreshold.setter
    def tcpthreshold(self, tcpthreshold) :
        """Number of SYNs permitted per 10 milliseconds.

        :param tcpthreshold: 

        """
        try :
            self._tcpthreshold = tcpthreshold
        except Exception as e:
            raise e

    @property
    def udpthreshold(self) :
        """Number of UDP packets permitted per 10 milliseconds."""
        try :
            return self._udpthreshold
        except Exception as e:
            raise e

    @udpthreshold.setter
    def udpthreshold(self, udpthreshold) :
        """Number of UDP packets permitted per 10 milliseconds.

        :param udpthreshold: 

        """
        try :
            self._udpthreshold = udpthreshold
        except Exception as e:
            raise e

    @property
    def icmpthreshold(self) :
        """Number of ICMP packets permitted per 10 milliseconds.<br/>Default value: 100."""
        try :
            return self._icmpthreshold
        except Exception as e:
            raise e

    @icmpthreshold.setter
    def icmpthreshold(self, icmpthreshold) :
        """Number of ICMP packets permitted per 10 milliseconds.<br/>Default value: 100

        :param icmpthreshold: 

        """
        try :
            self._icmpthreshold = icmpthreshold
        except Exception as e:
            raise e

    @property
    def tcprstthreshold(self) :
        """The number of TCP RST packets permitted per 10 milli second. zero means rate control is disabled and 0xffffffff means every thing is rate controlled.<br/>Default value: 100."""
        try :
            return self._tcprstthreshold
        except Exception as e:
            raise e

    @tcprstthreshold.setter
    def tcprstthreshold(self, tcprstthreshold) :
        """The number of TCP RST packets permitted per 10 milli second. zero means rate control is disabled and 0xffffffff means every thing is rate controlled.<br/>Default value: 100

        :param tcprstthreshold: 

        """
        try :
            self._tcprstthreshold = tcprstthreshold
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(nsratecontrol_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.nsratecontrol
        except Exception as e :
            raise e

    def _get_object_name(self) :
        """Returns the value of object identifier argument"""
        try :
            return 0
        except Exception as e :
            raise e



    @classmethod
    def update(cls, client, resource) :
        """Use this API to update nsratecontrol.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                updateresource = nsratecontrol()
                updateresource.tcpthreshold = resource.tcpthreshold
                updateresource.udpthreshold = resource.udpthreshold
                updateresource.icmpthreshold = resource.icmpthreshold
                updateresource.tcprstthreshold = resource.tcprstthreshold
                return updateresource.update_resource(client)
        except Exception as e :
            raise e

    @classmethod
    def unset(cls, client, resource, args) :
        """Use this API to unset the properties of nsratecontrol resource.
        Properties that need to be unset are specified in args array.

        :param client: 
        :param resource: 
        :param args: 

        """
        try :
            if type(resource) is not list :
                unsetresource = nsratecontrol()
                return unsetresource.unset_resource(client, args)
        except Exception as e :
            raise e

    @classmethod
    def get(cls, client, name="", option_="") :
        """Use this API to fetch all the nsratecontrol resources that are configured on netscaler.

        :param client: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            if not name :
                obj = nsratecontrol()
                response = obj.get_resources(client, option_)
            return response
        except Exception as e :
            raise e


class nsratecontrol_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.nsratecontrol = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.nsratecontrol = [nsratecontrol() for _ in range(length)]

