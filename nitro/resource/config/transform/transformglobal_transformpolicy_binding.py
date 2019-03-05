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

class transformglobal_transformpolicy_binding(base_resource) :
    """Binding class showing the transformpolicy that can be bound to transformglobal."""
    def __init__(self) :
        self._policyname = ""
        self._type = ""
        self._priority = 0
        self._gotopriorityexpression = ""
        self._invoke = False
        self._labeltype = ""
        self._labelname = ""
        self._numpol = 0
        self._flowtype = 0
        self._globalbindtype = ""
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
        """Name of the transform policy."""
        try :
            return self._policyname
        except Exception as e:
            raise e

    @policyname.setter
    def policyname(self, policyname) :
        """Name of the transform policy.

        :param policyname: 

        """
        try :
            self._policyname = policyname
        except Exception as e:
            raise e

    @property
    def labelname(self) :
        """Name of the policy label to invoke if the current policy evaluates to TRUE, the invoke parameter is set, and the label type is Policy Label."""
        try :
            return self._labelname
        except Exception as e:
            raise e

    @labelname.setter
    def labelname(self, labelname) :
        """Name of the policy label to invoke if the current policy evaluates to TRUE, the invoke parameter is set, and the label type is Policy Label.

        :param labelname: 

        """
        try :
            self._labelname = labelname
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
    def invoke(self) :
        """If the current policy evaluates to TRUE, terminate evaluation of policies bound to the current policy label, and then forwards the request or response to the specified virtual server or evaluates the specified policy label."""
        try :
            return self._invoke
        except Exception as e:
            raise e

    @invoke.setter
    def invoke(self, invoke) :
        """If the current policy evaluates to TRUE, terminate evaluation of policies bound to the current policy label, and then forwards the request or response to the specified virtual server or evaluates the specified policy label.

        :param invoke: 

        """
        try :
            self._invoke = invoke
        except Exception as e:
            raise e

    @property
    def type(self) :
        """Specifies the bind point to which to bind the policy. Available settings function as follows:
        * REQ_OVERRIDE. Request override. Binds the policy to the priority request queue.
        * REQ_DEFAULT. Binds the policy to the default request queue.<br/>Possible values = REQ_OVERRIDE, REQ_DEFAULT.


        """
        try :
            return self._type
        except Exception as e:
            raise e

    @type.setter
    def type(self, type) :
        """Specifies the bind point to which to bind the policy. Available settings function as follows:
        * REQ_OVERRIDE. Request override. Binds the policy to the priority request queue.
        * REQ_DEFAULT. Binds the policy to the default request queue.<br/>Possible values = REQ_OVERRIDE, REQ_DEFAULT

        :param type: 

        """
        try :
            self._type = type
        except Exception as e:
            raise e

    @property
    def labeltype(self) :
        """Type of invocation. Available settings function as follows:
        * reqvserver - Send the request to the specified request virtual server.
        * resvserver - Send the response to the specified response virtual server.
        * policylabel - Invoke the specified policy label.<br/>Possible values = reqvserver, resvserver, policylabel.


        """
        try :
            return self._labeltype
        except Exception as e:
            raise e

    @labeltype.setter
    def labeltype(self, labeltype) :
        """Type of invocation. Available settings function as follows:
        * reqvserver - Send the request to the specified request virtual server.
        * resvserver - Send the response to the specified response virtual server.
        * policylabel - Invoke the specified policy label.<br/>Possible values = reqvserver, resvserver, policylabel

        :param labeltype: 

        """
        try :
            self._labeltype = labeltype
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
    def flowtype(self) :
        """flowtype of the bound transform policy."""
        try :
            return self._flowtype
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(transformglobal_transformpolicy_binding_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.transformglobal_transformpolicy_binding
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
                updateresource = transformglobal_transformpolicy_binding()
                updateresource.policyname = resource.policyname
                updateresource.priority = resource.priority
                updateresource.gotopriorityexpression = resource.gotopriorityexpression
                updateresource.type = resource.type
                updateresource.invoke = resource.invoke
                updateresource.labeltype = resource.labeltype
                updateresource.labelname = resource.labelname
                return updateresource.update_resource(client)
            else :
                if resource and len(resource) > 0 :
                    updateresources = [transformglobal_transformpolicy_binding() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        updateresources[i].policyname = resource[i].policyname
                        updateresources[i].priority = resource[i].priority
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
                deleteresource = transformglobal_transformpolicy_binding()
                deleteresource.policyname = resource.policyname
                deleteresource.type = resource.type
                deleteresource.priority = resource.priority
                return deleteresource.delete_resource(client)
            else :
                if resource and len(resource) > 0 :
                    deleteresources = [transformglobal_transformpolicy_binding() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        deleteresources[i].policyname = resource[i].policyname
                        deleteresources[i].type = resource[i].type
                        deleteresources[i].priority = resource[i].priority
                return cls.delete_bulk_request(client, deleteresources)
        except Exception as e :
            raise e

    @classmethod
    def get(cls, service) :
        """Use this API to fetch a transformglobal_transformpolicy_binding resources.

        :param service: 

        """
        try :
            obj = transformglobal_transformpolicy_binding()
            response = obj.get_resources(service)
            return response
        except Exception as e:
            raise e

    @classmethod
    def get_filtered(cls, service, filter_) :
        """Use this API to fetch filtered set of transformglobal_transformpolicy_binding resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param service: 
        :param filter_: 

        """
        try :
            obj = transformglobal_transformpolicy_binding()
            option_ = options()
            option_.filter = filter_
            response = obj.getfiltered(service, option_)
            return response
        except Exception as e:
            raise e

    @classmethod
    def count(cls, service) :
        """Use this API to count transformglobal_transformpolicy_binding resources configued on NetScaler.

        :param service: 

        """
        try :
            obj = transformglobal_transformpolicy_binding()
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
        """Use this API to count the filtered set of transformglobal_transformpolicy_binding resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param service: 
        :param filter_: 

        """
        try :
            obj = transformglobal_transformpolicy_binding()
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

    class Labeltype:
        """ """
        reqvserver = "reqvserver"
        resvserver = "resvserver"
        policylabel = "policylabel"

class transformglobal_transformpolicy_binding_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.transformglobal_transformpolicy_binding = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.transformglobal_transformpolicy_binding = [transformglobal_transformpolicy_binding() for _ in range(length)]

