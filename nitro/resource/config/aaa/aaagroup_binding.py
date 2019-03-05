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

class aaagroup_binding(base_resource):
    """Binding class showing the resources that can be bound to aaagroup_binding."""
    def __init__(self) :
        self._groupname = ""
        self.aaagroup_auditnslogpolicy_binding = []
        self.aaagroup_intranetip6_binding = []
        self.aaagroup_vpnsessionpolicy_binding = []
        self.aaagroup_intranetip_binding = []
        self.aaagroup_aaauser_binding = []
        self.aaagroup_vpntrafficpolicy_binding = []
        self.aaagroup_vpnintranetapplication_binding = []
        self.aaagroup_authorizationpolicy_binding = []
        self.aaagroup_auditsyslogpolicy_binding = []
        self.aaagroup_vpnurl_binding = []
        self.aaagroup_tmsessionpolicy_binding = []

    @property
    def groupname(self) :
        """Name of the group.<br/>Minimum length =  1."""
        try :
            return self._groupname
        except Exception as e:
            raise e

    @groupname.setter
    def groupname(self, groupname) :
        """Name of the group.<br/>Minimum length =  1

        :param groupname: 

        """
        try :
            self._groupname = groupname
        except Exception as e:
            raise e

    @property
    def aaagroup_vpntrafficpolicy_bindings(self) :
        """vpntrafficpolicy that can be bound to aaagroup."""
        try :
            return self._aaagroup_vpntrafficpolicy_binding
        except Exception as e:
            raise e

    @property
    def aaagroup_authorizationpolicy_bindings(self) :
        """authorizationpolicy that can be bound to aaagroup."""
        try :
            return self._aaagroup_authorizationpolicy_binding
        except Exception as e:
            raise e

    @property
    def aaagroup_intranetip_bindings(self) :
        """intranetip that can be bound to aaagroup."""
        try :
            return self._aaagroup_intranetip_binding
        except Exception as e:
            raise e

    @property
    def aaagroup_intranetip6_bindings(self) :
        """intranetip6 that can be bound to aaagroup."""
        try :
            return self._aaagroup_intranetip6_binding
        except Exception as e:
            raise e

    @property
    def aaagroup_auditnslogpolicy_bindings(self) :
        """auditnslogpolicy that can be bound to aaagroup."""
        try :
            return self._aaagroup_auditnslogpolicy_binding
        except Exception as e:
            raise e

    @property
    def aaagroup_vpnurl_bindings(self) :
        """vpnurl that can be bound to aaagroup."""
        try :
            return self._aaagroup_vpnurl_binding
        except Exception as e:
            raise e

    @property
    def aaagroup_auditsyslogpolicy_bindings(self) :
        """auditsyslogpolicy that can be bound to aaagroup."""
        try :
            return self._aaagroup_auditsyslogpolicy_binding
        except Exception as e:
            raise e

    @property
    def aaagroup_aaauser_bindings(self) :
        """aaauser that can be bound to aaagroup."""
        try :
            return self._aaagroup_aaauser_binding
        except Exception as e:
            raise e

    @property
    def aaagroup_tmsessionpolicy_bindings(self) :
        """tmsessionpolicy that can be bound to aaagroup."""
        try :
            return self._aaagroup_tmsessionpolicy_binding
        except Exception as e:
            raise e

    @property
    def aaagroup_vpnsessionpolicy_bindings(self) :
        """vpnsessionpolicy that can be bound to aaagroup."""
        try :
            return self._aaagroup_vpnsessionpolicy_binding
        except Exception as e:
            raise e

    @property
    def aaagroup_vpnintranetapplication_bindings(self) :
        """vpnintranetapplication that can be bound to aaagroup."""
        try :
            return self._aaagroup_vpnintranetapplication_binding
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(aaagroup_binding_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.aaagroup_binding
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
    def get(self, service, groupname) :
        """Use this API to fetch aaagroup_binding resource.

        :param service: 
        :param groupname: 

        """
        try :
            if type(groupname) is not list :
                obj = aaagroup_binding()
                obj.groupname = groupname
                response = obj.get_resource(service)
            else :
                if groupname and len(groupname) > 0 :
                    obj = [aaagroup_binding() for _ in range(len(groupname))]
                    for i in range(len(groupname)) :
                        obj[i].groupname = groupname[i];
                        response[i] = obj[i].get_resource(service)
            return response
        except Exception as e:
            raise e

class aaagroup_binding_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.aaagroup_binding = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.aaagroup_binding = [aaagroup_binding() for _ in range(length)]

