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

class responderpolicy_binding(base_resource):
    """Binding class showing the resources that can be bound to responderpolicy_binding."""
    def __init__(self) :
        self._name = ""
        self.responderpolicy_responderpolicylabel_binding = []
        self.responderpolicy_csvserver_binding = []
        self.responderpolicy_lbvserver_binding = []
        self.responderpolicy_responderglobal_binding = []
        self.responderpolicy_crvserver_binding = []

    @property
    def name(self) :
        """Name of the responder policy for which to display settings."""
        try :
            return self._name
        except Exception as e:
            raise e

    @name.setter
    def name(self, name) :
        """Name of the responder policy for which to display settings.

        :param name: 

        """
        try :
            self._name = name
        except Exception as e:
            raise e

    @property
    def responderpolicy_crvserver_bindings(self) :
        """crvserver that can be bound to responderpolicy."""
        try :
            return self._responderpolicy_crvserver_binding
        except Exception as e:
            raise e

    @property
    def responderpolicy_lbvserver_bindings(self) :
        """lbvserver that can be bound to responderpolicy."""
        try :
            return self._responderpolicy_lbvserver_binding
        except Exception as e:
            raise e

    @property
    def responderpolicy_responderpolicylabel_bindings(self) :
        """responderpolicylabel that can be bound to responderpolicy."""
        try :
            return self._responderpolicy_responderpolicylabel_binding
        except Exception as e:
            raise e

    @property
    def responderpolicy_responderglobal_bindings(self) :
        """responderglobal that can be bound to responderpolicy."""
        try :
            return self._responderpolicy_responderglobal_binding
        except Exception as e:
            raise e

    @property
    def responderpolicy_csvserver_bindings(self) :
        """csvserver that can be bound to responderpolicy."""
        try :
            return self._responderpolicy_csvserver_binding
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(responderpolicy_binding_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.responderpolicy_binding
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
        """Use this API to fetch responderpolicy_binding resource.

        :param service: 
        :param name: 

        """
        try :
            if type(name) is not list :
                obj = responderpolicy_binding()
                obj.name = name
                response = obj.get_resource(service)
            else :
                if name and len(name) > 0 :
                    obj = [responderpolicy_binding() for _ in range(len(name))]
                    for i in range(len(name)) :
                        obj[i].name = name[i];
                        response[i] = obj[i].get_resource(service)
            return response
        except Exception as e:
            raise e

class responderpolicy_binding_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.responderpolicy_binding = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.responderpolicy_binding = [responderpolicy_binding() for _ in range(length)]

