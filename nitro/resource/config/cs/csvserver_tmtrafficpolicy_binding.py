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

class csvserver_tmtrafficpolicy_binding(base_resource) :
    """Binding class showing the tmtrafficpolicy that can be bound to csvserver."""
    def __init__(self) :
        self._policyname = ""
        self._priority = 0
        self._name = ""
        self._targetlbvserver = ""
        self._gotopriorityexpression = ""
        self._bindpoint = ""
        self._invoke = False
        self._labeltype = ""
        self._labelname = ""
        self.___count = 0

    @property
    def priority(self) :
        """Priority for the policy."""
        try :
            return self._priority
        except Exception as e:
            raise e

    @priority.setter
    def priority(self, priority) :
        """Priority for the policy.

        :param priority: 

        """
        try :
            self._priority = priority
        except Exception as e:
            raise e

    @property
    def bindpoint(self) :
        """For a rewrite policy, the bind point to which to bind the policy. Note: This parameter applies only to rewrite policies, because content switching policies are evaluated only at request time."""
        try :
            return self._bindpoint
        except Exception as e:
            raise e

    @bindpoint.setter
    def bindpoint(self, bindpoint) :
        """For a rewrite policy, the bind point to which to bind the policy. Note: This parameter applies only to rewrite policies, because content switching policies are evaluated only at request time.

        :param bindpoint: 

        """
        try :
            self._bindpoint = bindpoint
        except Exception as e:
            raise e

    @property
    def policyname(self) :
        """Policies bound to this vserver."""
        try :
            return self._policyname
        except Exception as e:
            raise e

    @policyname.setter
    def policyname(self, policyname) :
        """Policies bound to this vserver.

        :param policyname: 

        """
        try :
            self._policyname = policyname
        except Exception as e:
            raise e

    @property
    def labelname(self) :
        """Name of the label to be invoked."""
        try :
            return self._labelname
        except Exception as e:
            raise e

    @labelname.setter
    def labelname(self, labelname) :
        """Name of the label to be invoked.

        :param labelname: 

        """
        try :
            self._labelname = labelname
        except Exception as e:
            raise e

    @property
    def name(self) :
        """Name of the content switching virtual server to which the content switching policy applies.<br/>Minimum length =  1."""
        try :
            return self._name
        except Exception as e:
            raise e

    @name.setter
    def name(self, name) :
        """Name of the content switching virtual server to which the content switching policy applies.<br/>Minimum length =  1

        :param name: 

        """
        try :
            self._name = name
        except Exception as e:
            raise e

    @property
    def gotopriorityexpression(self) :
        """Expression or other value specifying the next policy to be evaluated if the current policy evaluates to TRUE.  Specify one of the following values:
        * NEXT - Evaluate the policy with the next higher priority number.
        * END - End policy evaluation.
        * USE_INVOCATION_RESULT - Applicable if this policy invokes another policy label. If the final goto in the invoked policy label has a value of END, the evaluation stops. If the final goto is anything other than END, the current policy label performs a NEXT.
        * A default syntax expression that evaluates to a number.
        If you specify an expression, the number to which it evaluates determines the next policy to evaluate, as follows:
        * If the expression evaluates to a higher numbered priority, the policy with that priority is evaluated next.
        * If the expression evaluates to the priority of the current policy, the policy with the next higher numbered priority is evaluated next.
        * If the expression evaluates to a priority number that is numerically higher than the highest numbered priority, policy evaluation ends.
        An UNDEF event is triggered if:
        * The expression is invalid.
        * The expression evaluates to a priority number that is numerically lower than the current policy's priority.
        * The expression evaluates to a priority number that is between the current policy's priority number (say, 30) and the highest priority number (say, 100), but does not match any configured priority number (for example, the expression evaluates to the number 85). This example assumes that the priority number increments by 10 for every successive policy, and therefore a priority number of 85 does not exist in the policy label.


        """
        try :
            return self._gotopriorityexpression
        except Exception as e:
            raise e

    @gotopriorityexpression.setter
    def gotopriorityexpression(self, gotopriorityexpression) :
        """Expression or other value specifying the next policy to be evaluated if the current policy evaluates to TRUE.  Specify one of the following values:
        * NEXT - Evaluate the policy with the next higher priority number.
        * END - End policy evaluation.
        * USE_INVOCATION_RESULT - Applicable if this policy invokes another policy label. If the final goto in the invoked policy label has a value of END, the evaluation stops. If the final goto is anything other than END, the current policy label performs a NEXT.
        * A default syntax expression that evaluates to a number.
        If you specify an expression, the number to which it evaluates determines the next policy to evaluate, as follows:
        * If the expression evaluates to a higher numbered priority, the policy with that priority is evaluated next.
        * If the expression evaluates to the priority of the current policy, the policy with the next higher numbered priority is evaluated next.
        * If the expression evaluates to a priority number that is numerically higher than the highest numbered priority, policy evaluation ends.
        An UNDEF event is triggered if:
        * The expression is invalid.
        * The expression evaluates to a priority number that is numerically lower than the current policy's priority.
        * The expression evaluates to a priority number that is between the current policy's priority number (say, 30) and the highest priority number (say, 100), but does not match any configured priority number (for example, the expression evaluates to the number 85). This example assumes that the priority number increments by 10 for every successive policy, and therefore a priority number of 85 does not exist in the policy label.

        :param gotopriorityexpression: 

        """
        try :
            self._gotopriorityexpression = gotopriorityexpression
        except Exception as e:
            raise e

    @property
    def targetlbvserver(self) :
        """Name of the Load Balancing virtual server to which the content is switched, if policy rule is evaluated to be TRUE.
        Example: bind cs vs cs1 -policyname pol1 -priority 101 -targetLBVserver lb1
        Note: Use this parameter only in case of Content Switching policy bind operations to a CS vserver.


        """
        try :
            return self._targetlbvserver
        except Exception as e:
            raise e

    @targetlbvserver.setter
    def targetlbvserver(self, targetlbvserver) :
        """Name of the Load Balancing virtual server to which the content is switched, if policy rule is evaluated to be TRUE.
        Example: bind cs vs cs1 -policyname pol1 -priority 101 -targetLBVserver lb1
        Note: Use this parameter only in case of Content Switching policy bind operations to a CS vserver

        :param targetlbvserver: 

        """
        try :
            self._targetlbvserver = targetlbvserver
        except Exception as e:
            raise e

    @property
    def invoke(self) :
        """Invoke a policy label if this policy's rule evaluates to TRUE (valid only for default-syntax policies such as application firewall, transform, integrated cache, rewrite, responder, and content switching)."""
        try :
            return self._invoke
        except Exception as e:
            raise e

    @invoke.setter
    def invoke(self, invoke) :
        """Invoke a policy label if this policy's rule evaluates to TRUE (valid only for default-syntax policies such as application firewall, transform, integrated cache, rewrite, responder, and content switching).

        :param invoke: 

        """
        try :
            self._invoke = invoke
        except Exception as e:
            raise e

    @property
    def labeltype(self) :
        """Type of label to be invoked."""
        try :
            return self._labeltype
        except Exception as e:
            raise e

    @labeltype.setter
    def labeltype(self, labeltype) :
        """Type of label to be invoked.

        :param labeltype: 

        """
        try :
            self._labeltype = labeltype
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(csvserver_tmtrafficpolicy_binding_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.csvserver_tmtrafficpolicy_binding
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
    def add(cls, client, resource) :
        """

        :param client: 
        :param resource: 

        """
        try :
            if resource and type(resource) is not list :
                updateresource = csvserver_tmtrafficpolicy_binding()
                updateresource.name = resource.name
                updateresource.policyname = resource.policyname
                updateresource.targetlbvserver = resource.targetlbvserver
                updateresource.priority = resource.priority
                updateresource.gotopriorityexpression = resource.gotopriorityexpression
                updateresource.bindpoint = resource.bindpoint
                updateresource.invoke = resource.invoke
                updateresource.labeltype = resource.labeltype
                updateresource.labelname = resource.labelname
                return updateresource.update_resource(client)
            else :
                if resource and len(resource) > 0 :
                    updateresources = [csvserver_tmtrafficpolicy_binding() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        updateresources[i].name = resource[i].name
                        updateresources[i].policyname = resource[i].policyname
                        updateresources[i].targetlbvserver = resource[i].targetlbvserver
                        updateresources[i].priority = resource[i].priority
                        updateresources[i].gotopriorityexpression = resource[i].gotopriorityexpression
                        updateresources[i].bindpoint = resource[i].bindpoint
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
                deleteresource = csvserver_tmtrafficpolicy_binding()
                deleteresource.name = resource.name
                deleteresource.policyname = resource.policyname
                deleteresource.bindpoint = resource.bindpoint
                deleteresource.priority = resource.priority
                return deleteresource.delete_resource(client)
            else :
                if resource and len(resource) > 0 :
                    deleteresources = [csvserver_tmtrafficpolicy_binding() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        deleteresources[i].name = resource[i].name
                        deleteresources[i].policyname = resource[i].policyname
                        deleteresources[i].bindpoint = resource[i].bindpoint
                        deleteresources[i].priority = resource[i].priority
                return cls.delete_bulk_request(client, deleteresources)
        except Exception as e :
            raise e

    @classmethod
    def get(cls, service, name) :
        """Use this API to fetch csvserver_tmtrafficpolicy_binding resources.

        :param service: 
        :param name: 

        """
        try :
            obj = csvserver_tmtrafficpolicy_binding()
            obj.name = name
            response = obj.get_resources(service)
            return response
        except Exception as e:
            raise e

    @classmethod
    def get_filtered(cls, service, name, filter_) :
        """Use this API to fetch filtered set of csvserver_tmtrafficpolicy_binding resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param service: 
        :param name: 
        :param filter_: 

        """
        try :
            obj = csvserver_tmtrafficpolicy_binding()
            obj.name = name
            option_ = options()
            option_.filter = filter_
            response = obj.getfiltered(service, option_)
            return response
        except Exception as e:
            raise e

    @classmethod
    def count(cls, service, name) :
        """Use this API to count csvserver_tmtrafficpolicy_binding resources configued on NetScaler.

        :param service: 
        :param name: 

        """
        try :
            obj = csvserver_tmtrafficpolicy_binding()
            obj.name = name
            option_ = options()
            option_.count = True
            response = obj.get_resources(service, option_)
            if response :
                return response[0].__dict__['___count']
            return 0
        except Exception as e:
            raise e

    @classmethod
    def count_filtered(cls, service, name, filter_) :
        """Use this API to count the filtered set of csvserver_tmtrafficpolicy_binding resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param service: 
        :param name: 
        :param filter_: 

        """
        try :
            obj = csvserver_tmtrafficpolicy_binding()
            obj.name = name
            option_ = options()
            option_.count = True
            option_.filter = filter_
            response = obj.getfiltered(service, option_)
            if response :
                return response[0].__dict__['___count']
            return 0
        except Exception as e:
            raise e

    class Bindpoint:
        """ """
        REQUEST = "REQUEST"
        RESPONSE = "RESPONSE"

    class Labeltype:
        """ """
        reqvserver = "reqvserver"
        resvserver = "resvserver"
        policylabel = "policylabel"

class csvserver_tmtrafficpolicy_binding_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.csvserver_tmtrafficpolicy_binding = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.csvserver_tmtrafficpolicy_binding = [csvserver_tmtrafficpolicy_binding() for _ in range(length)]

