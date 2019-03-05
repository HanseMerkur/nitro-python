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

class cachepolicylabel_policybinding_binding(base_resource) :
    """Binding class showing the policybinding that can be bound to cachepolicylabel."""
    def __init__(self) :
        self._policyname = ""
        self._priority = 0
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
        """Name of the cache policy to bind to the policy label."""
        try :
            return self._policyname
        except Exception as e:
            raise e

    @policyname.setter
    def policyname(self, policyname) :
        """Name of the cache policy to bind to the policy label.

        :param policyname: 

        """
        try :
            self._policyname = policyname
        except Exception as e:
            raise e

    @property
    def labeltype(self) :
        """Type of policy label to invoke: an unnamed label associated with a virtual server, or user-defined policy label.<br/>Possible values = reqvserver, resvserver, policylabel."""
        try :
            return self._labeltype
        except Exception as e:
            raise e

    @labeltype.setter
    def labeltype(self, labeltype) :
        """Type of policy label to invoke: an unnamed label associated with a virtual server, or user-defined policy label.<br/>Possible values = reqvserver, resvserver, policylabel

        :param labeltype: 

        """
        try :
            self._labeltype = labeltype
        except Exception as e:
            raise e

    @property
    def labelname(self) :
        """Name of the cache policy label to which to bind the policy."""
        try :
            return self._labelname
        except Exception as e:
            raise e

    @labelname.setter
    def labelname(self, labelname) :
        """Name of the cache policy label to which to bind the policy.

        :param labelname: 

        """
        try :
            self._labelname = labelname
        except Exception as e:
            raise e

    @property
    def invoke_labelname(self) :
        """Name of the policy label to invoke if the current policy rule evaluates to TRUE."""
        try :
            return self._invoke_labelname
        except Exception as e:
            raise e

    @invoke_labelname.setter
    def invoke_labelname(self, invoke_labelname) :
        """Name of the policy label to invoke if the current policy rule evaluates to TRUE.

        :param invoke_labelname: 

        """
        try :
            self._invoke_labelname = invoke_labelname
        except Exception as e:
            raise e

    @property
    def invoke(self) :
        """Invoke policies bound to a virtual server or a user-defined policy label. After the invoked policies are evaluated, the flow returns to the policy with the next-lower priority."""
        try :
            return self._invoke
        except Exception as e:
            raise e

    @invoke.setter
    def invoke(self, invoke) :
        """Invoke policies bound to a virtual server or a user-defined policy label. After the invoked policies are evaluated, the flow returns to the policy with the next-lower priority.

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
            result = service.payload_formatter.string_to_resource(cachepolicylabel_policybinding_binding_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.cachepolicylabel_policybinding_binding
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
    def get(cls, service, labelname) :
        """Use this API to fetch cachepolicylabel_policybinding_binding resources.

        :param service: 
        :param labelname: 

        """
        try :
            obj = cachepolicylabel_policybinding_binding()
            obj.labelname = labelname
            response = obj.get_resources(service)
            return response
        except Exception as e:
            raise e

    @classmethod
    def get_filtered(cls, service, labelname, filter_) :
        """Use this API to fetch filtered set of cachepolicylabel_policybinding_binding resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param service: 
        :param labelname: 
        :param filter_: 

        """
        try :
            obj = cachepolicylabel_policybinding_binding()
            obj.labelname = labelname
            option_ = options()
            option_.filter = filter_
            response = obj.getfiltered(service, option_)
            return response
        except Exception as e:
            raise e

    @classmethod
    def count(cls, service, labelname) :
        """Use this API to count cachepolicylabel_policybinding_binding resources configued on NetScaler.

        :param service: 
        :param labelname: 

        """
        try :
            obj = cachepolicylabel_policybinding_binding()
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
        """Use this API to count the filtered set of cachepolicylabel_policybinding_binding resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param service: 
        :param labelname: 
        :param filter_: 

        """
        try :
            obj = cachepolicylabel_policybinding_binding()
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
        reqvserver = "reqvserver"
        resvserver = "resvserver"
        policylabel = "policylabel"

class cachepolicylabel_policybinding_binding_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.cachepolicylabel_policybinding_binding = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.cachepolicylabel_policybinding_binding = [cachepolicylabel_policybinding_binding() for _ in range(length)]

