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

class appfwglobal_appfwpolicy_binding(base_resource) :
    """Binding class showing the appfwpolicy that can be bound to appfwglobal."""
    def __init__(self) :
        self._policyname = ""
        self._priority = 0
        self._gotopriorityexpression = ""
        self._invoke = False
        self._state = ""
        self._labeltype = ""
        self._labelname = ""
        self._numpol = 0
        self._flowtype = 0
        self._type = ""
        self._policytype = ""
        self._globalbindtype = ""
        self.___count = 0

    @property
    def priority(self) :
        """The priority of the policy."""
        try :
            return self._priority
        except Exception as e:
            raise e

    @priority.setter
    def priority(self, priority) :
        """The priority of the policy.

        :param priority: 

        """
        try :
            self._priority = priority
        except Exception as e:
            raise e

    @property
    def globalbindtype(self) :
        """.<br/>Default value: SYSTEM_GLOBAL<br/>Possible values = SYSTEM_GLOBAL, VPN_GLOBAL, RNAT_GLOBAL."""
        try :
            return self._globalbindtype
        except Exception as e:
            raise e

    @globalbindtype.setter
    def globalbindtype(self, globalbindtype) :
        """.<br/>Default value: SYSTEM_GLOBAL<br/>Possible values = SYSTEM_GLOBAL, VPN_GLOBAL, RNAT_GLOBAL

        :param globalbindtype: 

        """
        try :
            self._globalbindtype = globalbindtype
        except Exception as e:
            raise e

    @property
    def policyname(self) :
        """Name of the policy."""
        try :
            return self._policyname
        except Exception as e:
            raise e

    @policyname.setter
    def policyname(self, policyname) :
        """Name of the policy.

        :param policyname: 

        """
        try :
            self._policyname = policyname
        except Exception as e:
            raise e

    @property
    def labelname(self) :
        """Name of the policy label to invoke if the current policy evaluates to TRUE, the invoke parameter is set, and Label Type is set to Policy Label."""
        try :
            return self._labelname
        except Exception as e:
            raise e

    @labelname.setter
    def labelname(self, labelname) :
        """Name of the policy label to invoke if the current policy evaluates to TRUE, the invoke parameter is set, and Label Type is set to Policy Label.

        :param labelname: 

        """
        try :
            self._labelname = labelname
        except Exception as e:
            raise e

    @property
    def state(self) :
        """Enable or disable the binding to activate or deactivate the policy. This is applicable to classic policies only.<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._state
        except Exception as e:
            raise e

    @state.setter
    def state(self, state) :
        """Enable or disable the binding to activate or deactivate the policy. This is applicable to classic policies only.<br/>Possible values = ENABLED, DISABLED

        :param state: 

        """
        try :
            self._state = state
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
    def type(self) :
        """Bind point to which to policy is bound.<br/>Possible values = REQ_OVERRIDE, REQ_DEFAULT, NONE."""
        try :
            return self._type
        except Exception as e:
            raise e

    @type.setter
    def type(self, type) :
        """Bind point to which to policy is bound.<br/>Possible values = REQ_OVERRIDE, REQ_DEFAULT, NONE

        :param type: 

        """
        try :
            self._type = type
        except Exception as e:
            raise e

    @property
    def invoke(self) :
        """If the current policy evaluates to TRUE, terminate evaluation of policies bound to the current policy label, and then forward the request to the specified virtual server or evaluate the specified policy label."""
        try :
            return self._invoke
        except Exception as e:
            raise e

    @invoke.setter
    def invoke(self, invoke) :
        """If the current policy evaluates to TRUE, terminate evaluation of policies bound to the current policy label, and then forward the request to the specified virtual server or evaluate the specified policy label.

        :param invoke: 

        """
        try :
            self._invoke = invoke
        except Exception as e:
            raise e

    @property
    def labeltype(self) :
        """Type of policy label invocation.<br/>Possible values = reqvserver, policylabel."""
        try :
            return self._labeltype
        except Exception as e:
            raise e

    @labeltype.setter
    def labeltype(self, labeltype) :
        """Type of policy label invocation.<br/>Possible values = reqvserver, policylabel

        :param labeltype: 

        """
        try :
            self._labeltype = labeltype
        except Exception as e:
            raise e

    @property
    def flowtype(self) :
        """flowtype of the bound application firewall policy."""
        try :
            return self._flowtype
        except Exception as e:
            raise e

    @property
    def numpol(self) :
        """The number of policies bound to the bindpoint."""
        try :
            return self._numpol
        except Exception as e:
            raise e

    @property
    def policytype(self) :
        """.<br/>Possible values = Classic Policy, Advanced Policy."""
        try :
            return self._policytype
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(appfwglobal_appfwpolicy_binding_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.appfwglobal_appfwpolicy_binding
        except Exception as e :
            raise e

    def _get_object_name(self) :
        """Returns the value of object identifier argument"""
        try :
            return 0
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
                updateresource = appfwglobal_appfwpolicy_binding()
                updateresource.policyname = resource.policyname
                updateresource.priority = resource.priority
                updateresource.state = resource.state
                updateresource.gotopriorityexpression = resource.gotopriorityexpression
                updateresource.type = resource.type
                updateresource.invoke = resource.invoke
                updateresource.labeltype = resource.labeltype
                updateresource.labelname = resource.labelname
                return updateresource.update_resource(client)
            else :
                if resource and len(resource) > 0 :
                    updateresources = [appfwglobal_appfwpolicy_binding() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        updateresources[i].policyname = resource[i].policyname
                        updateresources[i].priority = resource[i].priority
                        updateresources[i].state = resource[i].state
                        updateresources[i].gotopriorityexpression = resource[i].gotopriorityexpression
                        updateresources[i].type = resource[i].type
                        updateresources[i].invoke = resource[i].invoke
                        updateresources[i].labeltype = resource[i].labeltype
                        updateresources[i].labelname = resource[i].labelname
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
                deleteresource = appfwglobal_appfwpolicy_binding()
                deleteresource.policyname = resource.policyname
                deleteresource.type = resource.type
                deleteresource.priority = resource.priority
                return deleteresource.delete_resource(client)
            else :
                if resource and len(resource) > 0 :
                    deleteresources = [appfwglobal_appfwpolicy_binding() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        deleteresources[i].policyname = resource[i].policyname
                        deleteresources[i].type = resource[i].type
                        deleteresources[i].priority = resource[i].priority
                return cls.delete_bulk_request(client, deleteresources)
        except Exception as e :
            raise e

    @classmethod
    def get(cls, service) :
        """Use this API to fetch a appfwglobal_appfwpolicy_binding resources.

        :param service: 

        """
        try :
            obj = appfwglobal_appfwpolicy_binding()
            response = obj.get_resources(service)
            return response
        except Exception as e:
            raise e

    @classmethod
    def get_filtered(cls, service, filter_) :
        """Use this API to fetch filtered set of appfwglobal_appfwpolicy_binding resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param service: 
        :param filter_: 

        """
        try :
            obj = appfwglobal_appfwpolicy_binding()
            option_ = options()
            option_.filter = filter_
            response = obj.getfiltered(service, option_)
            return response
        except Exception as e:
            raise e

    @classmethod
    def count(cls, service) :
        """Use this API to count appfwglobal_appfwpolicy_binding resources configued on NetScaler.

        :param service: 

        """
        try :
            obj = appfwglobal_appfwpolicy_binding()
            option_ = options()
            option_.count = True
            response = obj.get_resources(service, option_)
            if response :
                return response[0].__dict__['___count']
            return 0
        except Exception as e:
            raise e

    @classmethod
    def count_filtered(cls, service, filter_) :
        """Use this API to count the filtered set of appfwglobal_appfwpolicy_binding resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param service: 
        :param filter_: 

        """
        try :
            obj = appfwglobal_appfwpolicy_binding()
            option_ = options()
            option_.count = True
            option_.filter = filter_
            response = obj.getfiltered(service, option_)
            if response :
                return response[0].__dict__['___count']
            return 0
        except Exception as e:
            raise e

    class Globalbindtype:
        """ """
        SYSTEM_GLOBAL = "SYSTEM_GLOBAL"
        VPN_GLOBAL = "VPN_GLOBAL"
        RNAT_GLOBAL = "RNAT_GLOBAL"

    class Type:
        """ """
        REQ_OVERRIDE = "REQ_OVERRIDE"
        REQ_DEFAULT = "REQ_DEFAULT"
        NONE = "NONE"

    class Labeltype:
        """ """
        reqvserver = "reqvserver"
        policylabel = "policylabel"

    class Policytype:
        """ """
        Classic_Policy = "Classic Policy"
        Advanced_Policy = "Advanced Policy"

    class State:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

class appfwglobal_appfwpolicy_binding_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.appfwglobal_appfwpolicy_binding = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.appfwglobal_appfwpolicy_binding = [appfwglobal_appfwpolicy_binding() for _ in range(length)]

