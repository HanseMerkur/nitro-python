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

class systemgroup_systemcmdpolicy_binding(base_resource) :
    """Binding class showing the systemcmdpolicy that can be bound to systemgroup."""
    def __init__(self) :
        self._policyname = ""
        self._priority = 0
        self._groupname = ""
        self.___count = 0

    @property
    def priority(self) :
        """The priority of the command policy."""
        try :
            return self._priority
        except Exception as e:
            raise e

    @priority.setter
    def priority(self, priority) :
        """The priority of the command policy.

        :param priority: 

        """
        try :
            self._priority = priority
        except Exception as e:
            raise e

    @property
    def policyname(self) :
        """The name of command policy."""
        try :
            return self._policyname
        except Exception as e:
            raise e

    @policyname.setter
    def policyname(self, policyname) :
        """The name of command policy.

        :param policyname: 

        """
        try :
            self._policyname = policyname
        except Exception as e:
            raise e

    @property
    def groupname(self) :
        """Name of the system group.<br/>Minimum length =  1."""
        try :
            return self._groupname
        except Exception as e:
            raise e

    @groupname.setter
    def groupname(self, groupname) :
        """Name of the system group.<br/>Minimum length =  1

        :param groupname: 

        """
        try :
            self._groupname = groupname
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(systemgroup_systemcmdpolicy_binding_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.systemgroup_systemcmdpolicy_binding
        except Exception as e :
            raise e

    def _get_object_name(self) :
        """Returns the value of object identifier argument"""
        try :
            if self.groupname is not None :
                return str(self.groupname)
            return None
        except Exception as e :
            raise e



    @classmethod
    def add(cls, client, resource) :
        """

        :param client: 
        :param resource: 

        """
        try :
            if resource and type(resource) is not list :
                updateresource = systemgroup_systemcmdpolicy_binding()
                updateresource.groupname = resource.groupname
                updateresource.policyname = resource.policyname
                updateresource.priority = resource.priority
                return updateresource.update_resource(client)
            else :
                if resource and len(resource) > 0 :
                    updateresources = [systemgroup_systemcmdpolicy_binding() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        updateresources[i].groupname = resource[i].groupname
                        updateresources[i].policyname = resource[i].policyname
                        updateresources[i].priority = resource[i].priority
                return cls.update_bulk_request(client, updateresources)
        except Exception as e :
            raise e

    @classmethod
    def delete(cls, client, resource) :
        """

        :param client: 
        :param resource: 

        """
        try :
            if resource and type(resource) is not list :
                deleteresource = systemgroup_systemcmdpolicy_binding()
                deleteresource.groupname = resource.groupname
                deleteresource.policyname = resource.policyname
                return deleteresource.delete_resource(client)
            else :
                if resource and len(resource) > 0 :
                    deleteresources = [systemgroup_systemcmdpolicy_binding() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        deleteresources[i].groupname = resource[i].groupname
                        deleteresources[i].policyname = resource[i].policyname
                return cls.delete_bulk_request(client, deleteresources)
        except Exception as e :
            raise e

    @classmethod
    def get(cls, service, groupname) :
        """Use this API to fetch systemgroup_systemcmdpolicy_binding resources.

        :param service: 
        :param groupname: 

        """
        try :
            obj = systemgroup_systemcmdpolicy_binding()
            obj.groupname = groupname
            response = obj.get_resources(service)
            return response
        except Exception as e:
            raise e

    @classmethod
    def get_filtered(cls, service, groupname, filter_) :
        """Use this API to fetch filtered set of systemgroup_systemcmdpolicy_binding resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param service: 
        :param groupname: 
        :param filter_: 

        """
        try :
            obj = systemgroup_systemcmdpolicy_binding()
            obj.groupname = groupname
            option_ = options()
            option_.filter = filter_
            response = obj.getfiltered(service, option_)
            return response
        except Exception as e:
            raise e

    @classmethod
    def count(cls, service, groupname) :
        """Use this API to count systemgroup_systemcmdpolicy_binding resources configued on NetScaler.

        :param service: 
        :param groupname: 

        """
        try :
            obj = systemgroup_systemcmdpolicy_binding()
            obj.groupname = groupname
            option_ = options()
            option_.count = True
            response = obj.get_resources(service, option_)
            if response :
                return response[0].__dict__['___count']
            return 0
        except Exception as e:
            raise e

    @classmethod
    def count_filtered(cls, service, groupname, filter_) :
        """Use this API to count the filtered set of systemgroup_systemcmdpolicy_binding resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param service: 
        :param groupname: 
        :param filter_: 

        """
        try :
            obj = systemgroup_systemcmdpolicy_binding()
            obj.groupname = groupname
            option_ = options()
            option_.count = True
            option_.filter = filter_
            response = obj.getfiltered(service, option_)
            if response :
                return response[0].__dict__['___count']
            return 0
        except Exception as e:
            raise e

class systemgroup_systemcmdpolicy_binding_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.systemgroup_systemcmdpolicy_binding = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.systemgroup_systemcmdpolicy_binding = [systemgroup_systemcmdpolicy_binding() for _ in range(length)]

