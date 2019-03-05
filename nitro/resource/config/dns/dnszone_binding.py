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

class dnszone_binding(base_resource):
    """Binding class showing the resources that can be bound to dnszone_binding."""
    def __init__(self) :
        self._zonename = ""
        self.dnszone_domain_binding = []
        self.dnszone_dnskey_binding = []

    @property
    def zonename(self) :
        """Name of the zone. Mutually exclusive with the type parameter.<br/>Minimum length =  1."""
        try :
            return self._zonename
        except Exception as e:
            raise e

    @zonename.setter
    def zonename(self, zonename) :
        """Name of the zone. Mutually exclusive with the type parameter.<br/>Minimum length =  1

        :param zonename: 

        """
        try :
            self._zonename = zonename
        except Exception as e:
            raise e

    @property
    def dnszone_dnskey_bindings(self) :
        """dnskey that can be bound to dnszone."""
        try :
            return self._dnszone_dnskey_binding
        except Exception as e:
            raise e

    @property
    def dnszone_domain_bindings(self) :
        """domain that can be bound to dnszone."""
        try :
            return self._dnszone_domain_binding
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(dnszone_binding_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.dnszone_binding
        except Exception as e :
            raise e

    def _get_object_name(self) :
        """Returns the value of object identifier argument"""
        try :
            if self.zonename is not None :
                return str(self.zonename)
            return None
        except Exception as e :
            raise e



    @classmethod
    def get(self, service, zonename) :
        """Use this API to fetch dnszone_binding resource.

        :param service: 
        :param zonename: 

        """
        try :
            if type(zonename) is not list :
                obj = dnszone_binding()
                obj.zonename = zonename
                response = obj.get_resource(service)
            else :
                if zonename and len(zonename) > 0 :
                    obj = [dnszone_binding() for _ in range(len(zonename))]
                    for i in range(len(zonename)) :
                        obj[i].zonename = zonename[i];
                        response[i] = obj[i].get_resource(service)
            return response
        except Exception as e:
            raise e

class dnszone_binding_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.dnszone_binding = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.dnszone_binding = [dnszone_binding() for _ in range(length)]

