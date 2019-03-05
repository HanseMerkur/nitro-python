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

class sslprofile_binding(base_resource):
    """Binding class showing the resources that can be bound to sslprofile_binding."""
    def __init__(self) :
        self._name = ""
        self.sslprofile_sslcipher_binding = []
        self.sslprofile_ecccurve_binding = []
        self.sslprofile_sslvserver_binding = []
        self.sslprofile_sslciphersuite_binding = []

    @property
    def name(self) :
        """Name of the SSL profile for which to show detailed information.<br/>Minimum length =  1<br/>Maximum length =  127."""
        try :
            return self._name
        except Exception as e:
            raise e

    @name.setter
    def name(self, name) :
        """Name of the SSL profile for which to show detailed information.<br/>Minimum length =  1<br/>Maximum length =  127

        :param name: 

        """
        try :
            self._name = name
        except Exception as e:
            raise e

    @property
    def sslprofile_ecccurve_bindings(self) :
        """ecccurve that can be bound to sslprofile."""
        try :
            return self._sslprofile_ecccurve_binding
        except Exception as e:
            raise e

    @property
    def sslprofile_sslciphersuite_bindings(self) :
        """sslciphersuite that can be bound to sslprofile."""
        try :
            return self._sslprofile_sslciphersuite_binding
        except Exception as e:
            raise e

    @property
    def sslprofile_sslvserver_bindings(self) :
        """sslvserver that can be bound to sslprofile."""
        try :
            return self._sslprofile_sslvserver_binding
        except Exception as e:
            raise e

    @property
    def sslprofile_sslcipher_bindings(self) :
        """sslcipher that can be bound to sslprofile."""
        try :
            return self._sslprofile_sslcipher_binding
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(sslprofile_binding_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.sslprofile_binding
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
        """Use this API to fetch sslprofile_binding resource.

        :param service: 
        :param name: 

        """
        try :
            if type(name) is not list :
                obj = sslprofile_binding()
                obj.name = name
                response = obj.get_resource(service)
            else :
                if name and len(name) > 0 :
                    obj = [sslprofile_binding() for _ in range(len(name))]
                    for i in range(len(name)) :
                        obj[i].name = name[i];
                        response[i] = obj[i].get_resource(service)
            return response
        except Exception as e:
            raise e

class sslprofile_binding_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.sslprofile_binding = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.sslprofile_binding = [sslprofile_binding() for _ in range(length)]

