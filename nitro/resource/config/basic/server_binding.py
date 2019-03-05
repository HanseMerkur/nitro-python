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

class server_binding(base_resource):
    """Binding class showing the resources that can be bound to server_binding."""
    def __init__(self) :
        self._name = ""
        self.server_service_binding = []
        self.server_gslbservice_binding = []
        self.server_servicegroup_binding = []

    @property
    def name(self) :
        """Name of the server for which to display parameters.<br/>Minimum length =  1."""
        try :
            return self._name
        except Exception as e:
            raise e

    @name.setter
    def name(self, name) :
        """Name of the server for which to display parameters.<br/>Minimum length =  1

        :param name: 

        """
        try :
            self._name = name
        except Exception as e:
            raise e

    @property
    def server_servicegroup_bindings(self) :
        """servicegroup that can be bound to server."""
        try :
            return self._server_servicegroup_binding
        except Exception as e:
            raise e

    @property
    def server_service_bindings(self) :
        """service that can be bound to server."""
        try :
            return self._server_service_binding
        except Exception as e:
            raise e

    @property
    def server_gslbservice_bindings(self) :
        """gslbservice that can be bound to server."""
        try :
            return self._server_gslbservice_binding
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(server_binding_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.server_binding
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
    def get(self, service, name) :
        """Use this API to fetch server_binding resource.

        :param service: 
        :param name: 

        """
        try :
            if type(name) is not list :
                obj = server_binding()
                obj.name = name
                response = obj.get_resource(service)
            else :
                if name and len(name) > 0 :
                    obj = [server_binding() for _ in range(len(name))]
                    for i in range(len(name)) :
                        obj[i].name = name[i];
                        response[i] = obj[i].get_resource(service)
            return response
        except Exception as e:
            raise e

class server_binding_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.server_binding = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.server_binding = [server_binding() for _ in range(length)]

