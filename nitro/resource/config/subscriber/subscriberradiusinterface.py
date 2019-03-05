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

class subscriberradiusinterface(base_resource) :
    """Configuration for RADIUS interface Parameters resource."""
    def __init__(self) :
        self._listeningservice = ""
        self._svrstate = ""

    @property
    def listeningservice(self) :
        """Name of RADIUS LISTENING service that will process RADIUS accounting requests.<br/>Minimum length =  1."""
        try :
            return self._listeningservice
        except Exception as e:
            raise e

    @listeningservice.setter
    def listeningservice(self, listeningservice) :
        """Name of RADIUS LISTENING service that will process RADIUS accounting requests.<br/>Minimum length =  1

        :param listeningservice: 

        """
        try :
            self._listeningservice = listeningservice
        except Exception as e:
            raise e

    @property
    def svrstate(self) :
        """The state of the radius service.<br/>Possible values = UP, DOWN, UNKNOWN, BUSY, OUT OF SERVICE, GOING OUT OF SERVICE, DOWN WHEN GOING OUT OF SERVICE, NS_EMPTY_STR, Unknown, DISABLED."""
        try :
            return self._svrstate
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(subscriberradiusinterface_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.subscriberradiusinterface
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
        """Use this API to update subscriberradiusinterface.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                updateresource = subscriberradiusinterface()
                updateresource.listeningservice = resource.listeningservice
                return updateresource.update_resource(client)
        except Exception as e :
            raise e

    @classmethod
    def get(cls, client, name="", option_="") :
        """Use this API to fetch all the subscriberradiusinterface resources that are configured on netscaler.

        :param client: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            if not name :
                obj = subscriberradiusinterface()
                response = obj.get_resources(client, option_)
            return response
        except Exception as e :
            raise e


    class Svrstate:
        """ """
        UP = "UP"
        DOWN = "DOWN"
        UNKNOWN = "UNKNOWN"
        BUSY = "BUSY"
        OUT_OF_SERVICE = "OUT OF SERVICE"
        GOING_OUT_OF_SERVICE = "GOING OUT OF SERVICE"
        DOWN_WHEN_GOING_OUT_OF_SERVICE = "DOWN WHEN GOING OUT OF SERVICE"
        NS_EMPTY_STR = "NS_EMPTY_STR"
        Unknown = "Unknown"
        DISABLED = "DISABLED"

class subscriberradiusinterface_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.subscriberradiusinterface = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.subscriberradiusinterface = [subscriberradiusinterface() for _ in range(length)]

