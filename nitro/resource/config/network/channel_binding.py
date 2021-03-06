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

class channel_binding(base_resource):
    """Binding class showing the resources that can be bound to channel_binding."""
    def __init__(self) :
        self._id = ""
        self.channel_interface_binding = []

    @property
    def id(self) :
        """ID of an LA channel or LA channel in cluster configuration whose details you want the NetScaler appliance to display.
        Specify an LA channel in LA/x notation, where x can range from 1 to 8 or a cluster LA channel in CLA/x notation or  Link redundant channel in LR/x notation , where x can range from 1 to 4.<br/>Minimum length =  1.


        """
        try :
            return self._id
        except Exception as e:
            raise e

    @id.setter
    def id(self, id) :
        """ID of an LA channel or LA channel in cluster configuration whose details you want the NetScaler appliance to display.
        Specify an LA channel in LA/x notation, where x can range from 1 to 8 or a cluster LA channel in CLA/x notation or  Link redundant channel in LR/x notation , where x can range from 1 to 4.<br/>Minimum length =  1

        :param id: 

        """
        try :
            self._id = id
        except Exception as e:
            raise e

    @property
    def channel_interface_bindings(self) :
        """interface that can be bound to channel."""
        try :
            return self._channel_interface_binding
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(channel_binding_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.channel_binding
        except Exception as e :
            raise e

    def _get_object_name(self) :
        """Returns the value of object identifier argument"""
        try :
            if self.id is not None :
                return str(self.id)
            return None
        except Exception as e :
            raise e



    @classmethod
    def get(self, service, id) :
        """Use this API to fetch channel_binding resource.

        :param service: 
        :param id: 

        """
        try :
            if type(id) is not list :
                obj = channel_binding()
                obj.id = id
                response = obj.get_resource(service)
            else :
                if id and len(id) > 0 :
                    obj = [channel_binding() for _ in range(len(id))]
                    for i in range(len(id)) :
                        obj[i].id = id[i];
                        response[i] = obj[i].get_resource(service)
            return response
        except Exception as e:
            raise e

class channel_binding_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.channel_binding = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.channel_binding = [channel_binding() for _ in range(length)]

