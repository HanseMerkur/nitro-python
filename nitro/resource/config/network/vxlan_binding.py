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

class vxlan_binding(base_resource):
    """Binding class showing the resources that can be bound to vxlan_binding."""
    def __init__(self) :
        self._id = 0
        self.vxlan_iptunnel_binding = []
        self.vxlan_nsip_binding = []
        self.vxlan_nsip6_binding = []

    @property
    def id(self) :
        """A positive integer, which is also called VXLAN Network Identifier (VNI), that uniquely identifies a VXLAN.<br/>Minimum value =  1<br/>Maximum value =  16777215."""
        try :
            return self._id
        except Exception as e:
            raise e

    @id.setter
    def id(self, id) :
        """A positive integer, which is also called VXLAN Network Identifier (VNI), that uniquely identifies a VXLAN.<br/>Minimum value =  1<br/>Maximum value =  16777215

        :param id: 

        """
        try :
            self._id = id
        except Exception as e:
            raise e

    @property
    def vxlan_nsip6_bindings(self) :
        """nsip6 that can be bound to vxlan."""
        try :
            return self._vxlan_nsip6_binding
        except Exception as e:
            raise e

    @property
    def vxlan_nsip_bindings(self) :
        """nsip that can be bound to vxlan."""
        try :
            return self._vxlan_nsip_binding
        except Exception as e:
            raise e

    @property
    def vxlan_iptunnel_bindings(self) :
        """iptunnel that can be bound to vxlan."""
        try :
            return self._vxlan_iptunnel_binding
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(vxlan_binding_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.vxlan_binding
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
        """Use this API to fetch vxlan_binding resource.

        :param service: 
        :param id: 

        """
        try :
            if type(id) is not list :
                obj = vxlan_binding()
                obj.id = id
                response = obj.get_resource(service)
            else :
                if id and len(id) > 0 :
                    obj = [vxlan_binding() for _ in range(len(id))]
                    for i in range(len(id)) :
                        obj[i].id = id[i];
                        response[i] = obj[i].get_resource(service)
            return response
        except Exception as e:
            raise e

class vxlan_binding_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.vxlan_binding = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.vxlan_binding = [vxlan_binding() for _ in range(length)]

