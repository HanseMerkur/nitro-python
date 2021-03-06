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

class aaauser_vpnintranetapplication_binding(base_resource) :
    """Binding class showing the vpnintranetapplication that can be bound to aaauser."""
    def __init__(self) :
        self._intranetapplication = ""
        self._acttype = 0
        self._username = ""
        self._gotopriorityexpression = ""
        self.___count = 0

    @property
    def gotopriorityexpression(self) :
        """Expression or other value specifying the next policy to evaluate if the current policy evaluates to TRUE.  Specify one of the following values:
        * NEXT - Evaluate the policy with the next higher priority number.
        * END - End policy evaluation.
        * USE_INVOCATION_RESULT - Applicable if this policy invokes another policy label. If the final goto in the invoked policy label has a value of END, the evaluation stops. If the final goto is anything other than END, the current policy label performs a NEXT.
        * A default syntax or classic expression that evaluates to a number.
        If you specify an expression, the number to which it evaluates determines the next policy to evaluate, as follows:
        *  If the expression evaluates to a higher numbered priority, the policy with that priority is evaluated next.
        * If the expression evaluates to the priority of the current policy, the policy with the next higher numbered priority is evaluated next.
        * If the expression evaluates to a number that is larger than the largest numbered priority, policy evaluation ends.
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
        """Expression or other value specifying the next policy to evaluate if the current policy evaluates to TRUE.  Specify one of the following values:
        * NEXT - Evaluate the policy with the next higher priority number.
        * END - End policy evaluation.
        * USE_INVOCATION_RESULT - Applicable if this policy invokes another policy label. If the final goto in the invoked policy label has a value of END, the evaluation stops. If the final goto is anything other than END, the current policy label performs a NEXT.
        * A default syntax or classic expression that evaluates to a number.
        If you specify an expression, the number to which it evaluates determines the next policy to evaluate, as follows:
        *  If the expression evaluates to a higher numbered priority, the policy with that priority is evaluated next.
        * If the expression evaluates to the priority of the current policy, the policy with the next higher numbered priority is evaluated next.
        * If the expression evaluates to a number that is larger than the largest numbered priority, policy evaluation ends.
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
    def username(self) :
        """User account to which to bind the policy.<br/>Minimum length =  1."""
        try :
            return self._username
        except Exception as e:
            raise e

    @username.setter
    def username(self, username) :
        """User account to which to bind the policy.<br/>Minimum length =  1

        :param username: 

        """
        try :
            self._username = username
        except Exception as e:
            raise e

    @property
    def intranetapplication(self) :
        """Name of the intranet VPN application to which the policy applies."""
        try :
            return self._intranetapplication
        except Exception as e:
            raise e

    @intranetapplication.setter
    def intranetapplication(self, intranetapplication) :
        """Name of the intranet VPN application to which the policy applies.

        :param intranetapplication: 

        """
        try :
            self._intranetapplication = intranetapplication
        except Exception as e:
            raise e

    @property
    def acttype(self) :
        """ """
        try :
            return self._acttype
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(aaauser_vpnintranetapplication_binding_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.aaauser_vpnintranetapplication_binding
        except Exception as e :
            raise e

    def _get_object_name(self) :
        """Returns the value of object identifier argument"""
        try :
            if self.username is not None :
                return str(self.username)
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
                updateresource = aaauser_vpnintranetapplication_binding()
                updateresource.username = resource.username
                updateresource.intranetapplication = resource.intranetapplication
                updateresource.gotopriorityexpression = resource.gotopriorityexpression
                return updateresource.update_resource(client)
            else :
                if resource and len(resource) > 0 :
                    updateresources = [aaauser_vpnintranetapplication_binding() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        updateresources[i].username = resource[i].username
                        updateresources[i].intranetapplication = resource[i].intranetapplication
                        updateresources[i].gotopriorityexpression = resource[i].gotopriorityexpression
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
                deleteresource = aaauser_vpnintranetapplication_binding()
                deleteresource.username = resource.username
                deleteresource.intranetapplication = resource.intranetapplication
                return deleteresource.delete_resource(client)
            else :
                if resource and len(resource) > 0 :
                    deleteresources = [aaauser_vpnintranetapplication_binding() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        deleteresources[i].username = resource[i].username
                        deleteresources[i].intranetapplication = resource[i].intranetapplication
                return cls.delete_bulk_request(client, deleteresources)
        except Exception as e :
            raise e

    @classmethod
    def get(cls, service, username) :
        """Use this API to fetch aaauser_vpnintranetapplication_binding resources.

        :param service: 
        :param username: 

        """
        try :
            obj = aaauser_vpnintranetapplication_binding()
            obj.username = username
            response = obj.get_resources(service)
            return response
        except Exception as e:
            raise e

    @classmethod
    def get_filtered(cls, service, username, filter_) :
        """Use this API to fetch filtered set of aaauser_vpnintranetapplication_binding resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param service: 
        :param username: 
        :param filter_: 

        """
        try :
            obj = aaauser_vpnintranetapplication_binding()
            obj.username = username
            option_ = options()
            option_.filter = filter_
            response = obj.getfiltered(service, option_)
            return response
        except Exception as e:
            raise e

    @classmethod
    def count(cls, service, username) :
        """Use this API to count aaauser_vpnintranetapplication_binding resources configued on NetScaler.

        :param service: 
        :param username: 

        """
        try :
            obj = aaauser_vpnintranetapplication_binding()
            obj.username = username
            option_ = options()
            option_.count = True
            response = obj.get_resources(service, option_)
            if response :
                return response[0].__dict__['___count']
            return 0
        except Exception as e:
            raise e

    @classmethod
    def count_filtered(cls, service, username, filter_) :
        """Use this API to count the filtered set of aaauser_vpnintranetapplication_binding resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param service: 
        :param username: 
        :param filter_: 

        """
        try :
            obj = aaauser_vpnintranetapplication_binding()
            obj.username = username
            option_ = options()
            option_.count = True
            option_.filter = filter_
            response = obj.getfiltered(service, option_)
            if response :
                return response[0].__dict__['___count']
            return 0
        except Exception as e:
            raise e

class aaauser_vpnintranetapplication_binding_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.aaauser_vpnintranetapplication_binding = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.aaauser_vpnintranetapplication_binding = [aaauser_vpnintranetapplication_binding() for _ in range(length)]

