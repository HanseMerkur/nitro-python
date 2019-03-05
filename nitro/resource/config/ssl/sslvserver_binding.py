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

class sslvserver_binding(base_resource):
    """Binding class showing the resources that can be bound to sslvserver_binding."""
    def __init__(self) :
        self._vservername = ""
        self.sslvserver_sslpolicy_binding = []
        self.sslvserver_sslcipher_binding = []
        self.sslvserver_ecccurve_binding = []
        self.sslvserver_sslcertkey_binding = []
        self.sslvserver_sslciphersuite_binding = []

    @property
    def vservername(self) :
        """Name of the SSL virtual server for which to show detailed information.<br/>Minimum length =  1."""
        try :
            return self._vservername
        except Exception as e:
            raise e

    @vservername.setter
    def vservername(self, vservername) :
        """Name of the SSL virtual server for which to show detailed information.<br/>Minimum length =  1

        :param vservername: 

        """
        try :
            self._vservername = vservername
        except Exception as e:
            raise e

    @property
    def sslvserver_sslpolicy_bindings(self) :
        """sslpolicy that can be bound to sslvserver."""
        try :
            return self._sslvserver_sslpolicy_binding
        except Exception as e:
            raise e

    @property
    def sslvserver_sslcertkey_bindings(self) :
        """sslcertkey that can be bound to sslvserver."""
        try :
            return self._sslvserver_sslcertkey_binding
        except Exception as e:
            raise e

    @property
    def sslvserver_sslciphersuite_bindings(self) :
        """sslciphersuite that can be bound to sslvserver."""
        try :
            return self._sslvserver_sslciphersuite_binding
        except Exception as e:
            raise e

    @property
    def sslvserver_ecccurve_bindings(self) :
        """ecccurve that can be bound to sslvserver."""
        try :
            return self._sslvserver_ecccurve_binding
        except Exception as e:
            raise e

    @property
    def sslvserver_sslcipher_bindings(self) :
        """sslcipher that can be bound to sslvserver."""
        try :
            return self._sslvserver_sslcipher_binding
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(sslvserver_binding_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.sslvserver_binding
        except Exception as e :
            raise e

    def _get_object_name(self) :
        """Returns the value of object identifier argument"""
        try :
            if self.vservername is not None :
                return str(self.vservername)
            return None
        except Exception as e :
            raise e



    @classmethod
    def get(self, service, vservername) :
        """Use this API to fetch sslvserver_binding resource.

        :param service: 
        :param vservername: 

        """
        try :
            if type(vservername) is not list :
                obj = sslvserver_binding()
                obj.vservername = vservername
                response = obj.get_resource(service)
            else :
                if vservername and len(vservername) > 0 :
                    obj = [sslvserver_binding() for _ in range(len(vservername))]
                    for i in range(len(vservername)) :
                        obj[i].vservername = vservername[i];
                        response[i] = obj[i].get_resource(service)
            return response
        except Exception as e:
            raise e

class sslvserver_binding_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.sslvserver_binding = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.sslvserver_binding = [sslvserver_binding() for _ in range(length)]

