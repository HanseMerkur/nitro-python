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

class nspartition_binding(base_resource):
    """Binding class showing the resources that can be bound to nspartition_binding."""
    def __init__(self) :
        self._partitionname = ""
        self.nspartition_bridgegroup_binding = []
        self.nspartition_vlan_binding = []

    @property
    def partitionname(self) :
        """Name of partition for which to display parameters.<br/>Minimum length =  1."""
        try :
            return self._partitionname
        except Exception as e:
            raise e

    @partitionname.setter
    def partitionname(self, partitionname) :
        """Name of partition for which to display parameters.<br/>Minimum length =  1

        :param partitionname: 

        """
        try :
            self._partitionname = partitionname
        except Exception as e:
            raise e

    @property
    def nspartition_vlan_bindings(self) :
        """vlan that can be bound to nspartition."""
        try :
            return self._nspartition_vlan_binding
        except Exception as e:
            raise e

    @property
    def nspartition_bridgegroup_bindings(self) :
        """bridgegroup that can be bound to nspartition."""
        try :
            return self._nspartition_bridgegroup_binding
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(nspartition_binding_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.nspartition_binding
        except Exception as e :
            raise e

    def _get_object_name(self) :
        """Returns the value of object identifier argument"""
        try :
            if self.partitionname is not None :
                return str(self.partitionname)
            return None
        except Exception as e :
            raise e



    @classmethod
    def get(self, service, partitionname) :
        """Use this API to fetch nspartition_binding resource.

        :param service: 
        :param partitionname: 

        """
        try :
            if type(partitionname) is not list :
                obj = nspartition_binding()
                obj.partitionname = partitionname
                response = obj.get_resource(service)
            else :
                if partitionname and len(partitionname) > 0 :
                    obj = [nspartition_binding() for _ in range(len(partitionname))]
                    for i in range(len(partitionname)) :
                        obj[i].partitionname = partitionname[i];
                        response[i] = obj[i].get_resource(service)
            return response
        except Exception as e:
            raise e

class nspartition_binding_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.nspartition_binding = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.nspartition_binding = [nspartition_binding() for _ in range(length)]

