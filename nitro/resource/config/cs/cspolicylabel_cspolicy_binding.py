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

class cspolicylabel_cspolicy_binding(base_resource) :
    """Binding class showing the cspolicy that can be bound to cspolicylabel."""
    def __init__(self) :
        self._policyname = ""
        self._priority = 0
        self._targetvserver = ""
        self._gotopriorityexpression = ""
        self._invoke = False
        self._labeltype = ""
        self._invoke_labelname = ""
        self._labelname = ""
        self.___count = 0

    @property
    def priority(self) :
        """Specifies the priority of the policy."""
        try :
            return self._priority
        except Exception as e:
            raise e

    @priority.setter
    def priority(self, priority) :
        """Specifies the priority of the policy.

        :param priority: 

        """
        try :
            self._priority = priority
        except Exception as e:
            raise e

    @property
    def gotopriorityexpression(self) :
        """Expression specifying the priority of the next policy which will get evaluated if the current policy rule evaluates to TRUE."""
        try :
            return self._gotopriorityexpression
        except Exception as e:
            raise e

    @gotopriorityexpression.setter
    def gotopriorityexpression(self, gotopriorityexpression) :
        """Expression specifying the priority of the next policy which will get evaluated if the current policy rule evaluates to TRUE.

        :param gotopriorityexpression: 

        """
        try :
            self._gotopriorityexpression = gotopriorityexpression
        except Exception as e:
            raise e

    @property
    def policyname(self) :
        """Name of the content switching policy."""
        try :
            return self._policyname
        except Exception as e:
            raise e

    @policyname.setter
    def policyname(self, policyname) :
        """Name of the content switching policy.

        :param policyname: 

        """
        try :
            self._policyname = policyname
        except Exception as e:
            raise e

    @property
    def targetvserver(self) :
        """Name of the virtual server to which to forward requests that match the policy."""
        try :
            return self._targetvserver
        except Exception as e:
            raise e

    @targetvserver.setter
    def targetvserver(self, targetvserver) :
        """Name of the virtual server to which to forward requests that match the policy.

        :param targetvserver: 

        """
        try :
            self._targetvserver = targetvserver
        except Exception as e:
            raise e

    @property
    def labeltype(self) :
        """Type of policy label invocation.<br/>Possible values = policylabel."""
        try :
            return self._labeltype
        except Exception as e:
            raise e

    @labeltype.setter
    def labeltype(self, labeltype) :
        """Type of policy label invocation.<br/>Possible values = policylabel

        :param labeltype: 

        """
        try :
            self._labeltype = labeltype
        except Exception as e:
            raise e

    @property
    def labelname(self) :
        """Name of the policy label to which to bind a content switching policy."""
        try :
            return self._labelname
        except Exception as e:
            raise e

    @labelname.setter
    def labelname(self, labelname) :
        """Name of the policy label to which to bind a content switching policy.

        :param labelname: 

        """
        try :
            self._labelname = labelname
        except Exception as e:
            raise e

    @property
    def invoke_labelname(self) :
        """Name of the label to invoke if the current policy rule evaluates to TRUE."""
        try :
            return self._invoke_labelname
        except Exception as e:
            raise e

    @invoke_labelname.setter
    def invoke_labelname(self, invoke_labelname) :
        """Name of the label to invoke if the current policy rule evaluates to TRUE.

        :param invoke_labelname: 

        """
        try :
            self._invoke_labelname = invoke_labelname
        except Exception as e:
            raise e

    @property
    def invoke(self) :
        """ """
        try :
            return self._invoke
        except Exception as e:
            raise e

    @invoke.setter
    def invoke(self, invoke) :
        """

        :param invoke: 

        """
        try :
            self._invoke = invoke
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(cspolicylabel_cspolicy_binding_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.cspolicylabel_cspolicy_binding
        except Exception as e :
            raise e

    def _get_object_name(self) :
        """Returns the value of object identifier argument"""
        try :
            if self.labelname is not None :
                return str(self.labelname)
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
                updateresource = cspolicylabel_cspolicy_binding()
                updateresource.labelname = resource.labelname
                updateresource.policyname = resource.policyname
                updateresource.priority = resource.priority
                updateresource.targetvserver = resource.targetvserver
                updateresource.gotopriorityexpression = resource.gotopriorityexpression
                updateresource.invoke = resource.invoke
                updateresource.labeltype = resource.labeltype
                updateresource.invoke_labelname = resource.invoke_labelname
                return updateresource.update_resource(client)
            else :
                if resource and len(resource) > 0 :
                    updateresources = [cspolicylabel_cspolicy_binding() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        updateresources[i].labelname = resource[i].labelname
                        updateresources[i].policyname = resource[i].policyname
                        updateresources[i].priority = resource[i].priority
                        updateresources[i].targetvserver = resource[i].targetvserver
                        updateresources[i].gotopriorityexpression = resource[i].gotopriorityexpression
                        updateresources[i].invoke = resource[i].invoke
                        updateresources[i].labeltype = resource[i].labeltype
                        updateresources[i].invoke_labelname = resource[i].invoke_labelname
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
                deleteresource = cspolicylabel_cspolicy_binding()
                deleteresource.labelname = resource.labelname
                deleteresource.policyname = resource.policyname
                return deleteresource.delete_resource(client)
            else :
                if resource and len(resource) > 0 :
                    deleteresources = [cspolicylabel_cspolicy_binding() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        deleteresources[i].labelname = resource[i].labelname
                        deleteresources[i].policyname = resource[i].policyname
                return cls.delete_bulk_request(client, deleteresources)
        except Exception as e :
            raise e

    @classmethod
    def get(cls, service, labelname) :
        """Use this API to fetch cspolicylabel_cspolicy_binding resources.

        :param service: 
        :param labelname: 

        """
        try :
            obj = cspolicylabel_cspolicy_binding()
            obj.labelname = labelname
            response = obj.get_resources(service)
            return response
        except Exception as e:
            raise e

    @classmethod
    def get_filtered(cls, service, labelname, filter_) :
        """Use this API to fetch filtered set of cspolicylabel_cspolicy_binding resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param service: 
        :param labelname: 
        :param filter_: 

        """
        try :
            obj = cspolicylabel_cspolicy_binding()
            obj.labelname = labelname
            option_ = options()
            option_.filter = filter_
            response = obj.getfiltered(service, option_)
            return response
        except Exception as e:
            raise e

    @classmethod
    def count(cls, service, labelname) :
        """Use this API to count cspolicylabel_cspolicy_binding resources configued on NetScaler.

        :param service: 
        :param labelname: 

        """
        try :
            obj = cspolicylabel_cspolicy_binding()
            obj.labelname = labelname
            option_ = options()
            option_.count = True
            response = obj.get_resources(service, option_)
            if response :
                return response[0].__dict__['___count']
            return 0
        except Exception as e:
            raise e

    @classmethod
    def count_filtered(cls, service, labelname, filter_) :
        """Use this API to count the filtered set of cspolicylabel_cspolicy_binding resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param service: 
        :param labelname: 
        :param filter_: 

        """
        try :
            obj = cspolicylabel_cspolicy_binding()
            obj.labelname = labelname
            option_ = options()
            option_.count = True
            option_.filter = filter_
            response = obj.getfiltered(service, option_)
            if response :
                return response[0].__dict__['___count']
            return 0
        except Exception as e:
            raise e

    class Labeltype:
        """ """
        policylabel = "policylabel"

class cspolicylabel_cspolicy_binding_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.cspolicylabel_cspolicy_binding = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.cspolicylabel_cspolicy_binding = [cspolicylabel_cspolicy_binding() for _ in range(length)]

