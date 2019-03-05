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

class sslservice_binding(base_resource):
    """Binding class showing the resources that can be bound to sslservice_binding."""
    def __init__(self) :
        self._servicename = ""
        self.sslservice_sslcipher_binding = []
        self.sslservice_ecccurve_binding = []
        self.sslservice_sslpolicy_binding = []
        self.sslservice_sslcertkey_binding = []
        self.sslservice_sslciphersuite_binding = []

    @property
    def servicename(self) :
        """Name of the SSL service for which to show detailed information.<br/>Minimum length =  1."""
        try :
            return self._servicename
        except Exception as e:
            raise e

    @servicename.setter
    def servicename(self, servicename) :
        """Name of the SSL service for which to show detailed information.<br/>Minimum length =  1

        :param servicename: 

        """
        try :
            self._servicename = servicename
        except Exception as e:
            raise e

    @property
    def sslservice_sslciphersuite_bindings(self) :
        """sslciphersuite that can be bound to sslservice."""
        try :
            return self._sslservice_sslciphersuite_binding
        except Exception as e:
            raise e

    @property
    def sslservice_sslcertkey_bindings(self) :
        """sslcertkey that can be bound to sslservice."""
        try :
            return self._sslservice_sslcertkey_binding
        except Exception as e:
            raise e

    @property
    def sslservice_sslcipher_bindings(self) :
        """sslcipher that can be bound to sslservice."""
        try :
            return self._sslservice_sslcipher_binding
        except Exception as e:
            raise e

    @property
    def sslservice_ecccurve_bindings(self) :
        """ecccurve that can be bound to sslservice."""
        try :
            return self._sslservice_ecccurve_binding
        except Exception as e:
            raise e

    @property
    def sslservice_sslpolicy_bindings(self) :
        """sslpolicy that can be bound to sslservice."""
        try :
            return self._sslservice_sslpolicy_binding
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(sslservice_binding_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.sslservice_binding
        except Exception as e :
            raise e

    def _get_object_name(self) :
        """Returns the value of object identifier argument"""
        try :
            if self.servicename is not None :
                return str(self.servicename)
            return None
        except Exception as e :
            raise e



    @classmethod
    def get(self, service, servicename) :
        """Use this API to fetch sslservice_binding resource.

        :param service: 
        :param servicename: 

        """
        try :
            if type(servicename) is not list :
                obj = sslservice_binding()
                obj.servicename = servicename
                response = obj.get_resource(service)
            else :
                if servicename and len(servicename) > 0 :
                    obj = [sslservice_binding() for _ in range(len(servicename))]
                    for i in range(len(servicename)) :
                        obj[i].servicename = servicename[i];
                        response[i] = obj[i].get_resource(service)
            return response
        except Exception as e:
            raise e

class sslservice_binding_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.sslservice_binding = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.sslservice_binding = [sslservice_binding() for _ in range(length)]

