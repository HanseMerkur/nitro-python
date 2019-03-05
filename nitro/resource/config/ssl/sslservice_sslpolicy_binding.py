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

class sslservice_sslpolicy_binding(base_resource) :
    """Binding class showing the sslpolicy that can be bound to sslservice."""
    def __init__(self) :
        self._policyname = ""
        self._priority = 0
        self._polinherit = 0
        self._gotopriorityexpression = ""
        self._invoke = False
        self._labeltype = ""
        self._labelname = ""
        self._servicename = ""
        self.___count = 0

    @property
    def priority(self) :
        """The priority of the policies bound to this SSL service."""
        try :
            return self._priority
        except Exception as e:
            raise e

    @priority.setter
    def priority(self, priority) :
        """The priority of the policies bound to this SSL service.

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
        """The SSL policy binding."""
        try :
            return self._policyname
        except Exception as e:
            raise e

    @policyname.setter
    def policyname(self, policyname) :
        """The SSL policy binding.

        :param policyname: 

        """
        try :
            self._policyname = policyname
        except Exception as e:
            raise e

    @property
    def servicename(self) :
        """Name of the SSL service for which to set advanced configuration.<br/>Minimum length =  1."""
        try :
            return self._servicename
        except Exception as e:
            raise e

    @servicename.setter
    def servicename(self, servicename) :
        """Name of the SSL service for which to set advanced configuration.<br/>Minimum length =  1

        :param servicename: 

        """
        try :
            self._servicename = servicename
        except Exception as e:
            raise e

    @property
    def labeltype(self) :
        """Type of policy label invocation.<br/>Possible values = vserver, service, policylabel."""
        try :
            return self._labeltype
        except Exception as e:
            raise e

    @labeltype.setter
    def labeltype(self, labeltype) :
        """Type of policy label invocation.<br/>Possible values = vserver, service, policylabel

        :param labeltype: 

        """
        try :
            self._labeltype = labeltype
        except Exception as e:
            raise e

    @property
    def labelname(self) :
        """Name of the label to invoke if the current policy rule evaluates to TRUE."""
        try :
            return self._labelname
        except Exception as e:
            raise e

    @labelname.setter
    def labelname(self, labelname) :
        """Name of the label to invoke if the current policy rule evaluates to TRUE.

        :param labelname: 

        """
        try :
            self._labelname = labelname
        except Exception as e:
            raise e

    @property
    def invoke(self) :
        """Invoke flag. This attribute is relevant only for ADVANCED policies."""
        try :
            return self._invoke
        except Exception as e:
            raise e

    @invoke.setter
    def invoke(self, invoke) :
        """Invoke flag. This attribute is relevant only for ADVANCED policies.

        :param invoke: 

        """
        try :
            self._invoke = invoke
        except Exception as e:
            raise e

    @property
    def polinherit(self) :
        """Whether the bound policy is a inherited policy or not."""
        try :
            return self._polinherit
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(sslservice_sslpolicy_binding_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.sslservice_sslpolicy_binding
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
    def add(cls, client, resource) :
        """

        :param client: 
        :param resource: 

        """
        try :
            if resource and type(resource) is not list :
                updateresource = sslservice_sslpolicy_binding()
                updateresource.servicename = resource.servicename
                updateresource.policyname = resource.policyname
                updateresource.priority = resource.priority
                updateresource.gotopriorityexpression = resource.gotopriorityexpression
                updateresource.invoke = resource.invoke
                updateresource.labeltype = resource.labeltype
                updateresource.labelname = resource.labelname
                return updateresource.update_resource(client)
            else :
                if resource and len(resource) > 0 :
                    updateresources = [sslservice_sslpolicy_binding() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        updateresources[i].servicename = resource[i].servicename
                        updateresources[i].policyname = resource[i].policyname
                        updateresources[i].priority = resource[i].priority
                        updateresources[i].gotopriorityexpression = resource[i].gotopriorityexpression
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
                deleteresource = sslservice_sslpolicy_binding()
                deleteresource.servicename = resource.servicename
                deleteresource.policyname = resource.policyname
                deleteresource.priority = resource.priority
                return deleteresource.delete_resource(client)
            else :
                if resource and len(resource) > 0 :
                    deleteresources = [sslservice_sslpolicy_binding() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        deleteresources[i].servicename = resource[i].servicename
                        deleteresources[i].policyname = resource[i].policyname
                        deleteresources[i].priority = resource[i].priority
                return cls.delete_bulk_request(client, deleteresources)
        except Exception as e :
            raise e

    @classmethod
    def get(cls, service, servicename) :
        """Use this API to fetch sslservice_sslpolicy_binding resources.

        :param service: 
        :param servicename: 

        """
        try :
            obj = sslservice_sslpolicy_binding()
            obj.servicename = servicename
            response = obj.get_resources(service)
            return response
        except Exception as e:
            raise e

    @classmethod
    def get_filtered(cls, service, servicename, filter_) :
        """Use this API to fetch filtered set of sslservice_sslpolicy_binding resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param service: 
        :param servicename: 
        :param filter_: 

        """
        try :
            obj = sslservice_sslpolicy_binding()
            obj.servicename = servicename
            option_ = options()
            option_.filter = filter_
            response = obj.getfiltered(service, option_)
            return response
        except Exception as e:
            raise e

    @classmethod
    def count(cls, service, servicename) :
        """Use this API to count sslservice_sslpolicy_binding resources configued on NetScaler.

        :param service: 
        :param servicename: 

        """
        try :
            obj = sslservice_sslpolicy_binding()
            obj.servicename = servicename
            option_ = options()
            option_.count = True
            response = obj.get_resources(service, option_)
            if response :
                return response[0].__dict__['___count']
            return 0
        except Exception as e:
            raise e

    @classmethod
    def count_filtered(cls, service, servicename, filter_) :
        """Use this API to count the filtered set of sslservice_sslpolicy_binding resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param service: 
        :param servicename: 
        :param filter_: 

        """
        try :
            obj = sslservice_sslpolicy_binding()
            obj.servicename = servicename
            option_ = options()
            option_.count = True
            option_.filter = filter_
            response = obj.getfiltered(service, option_)
            if response :
                return response[0].__dict__['___count']
            return 0
        except Exception as e:
            raise e

    class Ecccurvename:
        """ """
        ALL = "ALL"
        P_224 = "P_224"
        P_256 = "P_256"
        P_384 = "P_384"
        P_521 = "P_521"

    class Labeltype:
        """ """
        vserver = "vserver"
        service = "service"
        policylabel = "policylabel"

    class Crlcheck:
        """ """
        Mandatory = "Mandatory"
        Optional = "Optional"

    class Ocspcheck:
        """ """
        Mandatory = "Mandatory"
        Optional = "Optional"

class sslservice_sslpolicy_binding_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.sslservice_sslpolicy_binding = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.sslservice_sslpolicy_binding = [sslservice_sslpolicy_binding() for _ in range(length)]

