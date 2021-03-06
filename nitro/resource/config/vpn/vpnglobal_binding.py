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

class vpnglobal_binding(base_resource):
    """Binding class showing the resources that can be bound to vpnglobal_binding."""
    def __init__(self) :
        self.vpnglobal_intranetip6_binding = []
        self.vpnglobal_auditnslogpolicy_binding = []
        self.vpnglobal_authenticationpolicy_binding = []
        self.vpnglobal_authenticationradiuspolicy_binding = []
        self.vpnglobal_vpnsessionpolicy_binding = []
        self.vpnglobal_domain_binding = []
        self.vpnglobal_vpneula_binding = []
        self.vpnglobal_vpnclientlessaccesspolicy_binding = []
        self.vpnglobal_intranetip_binding = []
        self.vpnglobal_vpnnexthopserver_binding = []
        self.vpnglobal_authenticationldappolicy_binding = []
        self.vpnglobal_sharefileserver_binding = []
        self.vpnglobal_vpntrafficpolicy_binding = []
        self.vpnglobal_authenticationlocalpolicy_binding = []
        self.vpnglobal_vpnintranetapplication_binding = []
        self.vpnglobal_appcontroller_binding = []
        self.vpnglobal_authenticationnegotiatepolicy_binding = []
        self.vpnglobal_authenticationtacacspolicy_binding = []
        self.vpnglobal_vpnportaltheme_binding = []
        self.vpnglobal_authenticationsamlpolicy_binding = []
        self.vpnglobal_staserver_binding = []
        self.vpnglobal_auditsyslogpolicy_binding = []
        self.vpnglobal_authenticationcertpolicy_binding = []
        self.vpnglobal_vpnurl_binding = []

    @property
    def vpnglobal_vpnintranetapplication_bindings(self) :
        """vpnintranetapplication that can be bound to vpnglobal."""
        try :
            return self._vpnglobal_vpnintranetapplication_binding
        except Exception as e:
            raise e

    @property
    def vpnglobal_authenticationsamlpolicy_bindings(self) :
        """authenticationsamlpolicy that can be bound to vpnglobal."""
        try :
            return self._vpnglobal_authenticationsamlpolicy_binding
        except Exception as e:
            raise e

    @property
    def vpnglobal_intranetip_bindings(self) :
        """intranetip that can be bound to vpnglobal."""
        try :
            return self._vpnglobal_intranetip_binding
        except Exception as e:
            raise e

    @property
    def vpnglobal_authenticationradiuspolicy_bindings(self) :
        """authenticationradiuspolicy that can be bound to vpnglobal."""
        try :
            return self._vpnglobal_authenticationradiuspolicy_binding
        except Exception as e:
            raise e

    @property
    def vpnglobal_staserver_bindings(self) :
        """staserver that can be bound to vpnglobal."""
        try :
            return self._vpnglobal_staserver_binding
        except Exception as e:
            raise e

    @property
    def vpnglobal_sharefileserver_bindings(self) :
        """sharefileserver that can be bound to vpnglobal."""
        try :
            return self._vpnglobal_sharefileserver_binding
        except Exception as e:
            raise e

    @property
    def vpnglobal_intranetip6_bindings(self) :
        """intranetip6 that can be bound to vpnglobal."""
        try :
            return self._vpnglobal_intranetip6_binding
        except Exception as e:
            raise e

    @property
    def vpnglobal_appcontroller_bindings(self) :
        """appcontroller that can be bound to vpnglobal."""
        try :
            return self._vpnglobal_appcontroller_binding
        except Exception as e:
            raise e

    @property
    def vpnglobal_authenticationtacacspolicy_bindings(self) :
        """authenticationtacacspolicy that can be bound to vpnglobal."""
        try :
            return self._vpnglobal_authenticationtacacspolicy_binding
        except Exception as e:
            raise e

    @property
    def vpnglobal_authenticationpolicy_bindings(self) :
        """authenticationpolicy that can be bound to vpnglobal."""
        try :
            return self._vpnglobal_authenticationpolicy_binding
        except Exception as e:
            raise e

    @property
    def vpnglobal_vpntrafficpolicy_bindings(self) :
        """vpntrafficpolicy that can be bound to vpnglobal."""
        try :
            return self._vpnglobal_vpntrafficpolicy_binding
        except Exception as e:
            raise e

    @property
    def vpnglobal_domain_bindings(self) :
        """domain that can be bound to vpnglobal."""
        try :
            return self._vpnglobal_domain_binding
        except Exception as e:
            raise e

    @property
    def vpnglobal_vpnnexthopserver_bindings(self) :
        """vpnnexthopserver that can be bound to vpnglobal."""
        try :
            return self._vpnglobal_vpnnexthopserver_binding
        except Exception as e:
            raise e

    @property
    def vpnglobal_authenticationldappolicy_bindings(self) :
        """authenticationldappolicy that can be bound to vpnglobal."""
        try :
            return self._vpnglobal_authenticationldappolicy_binding
        except Exception as e:
            raise e

    @property
    def vpnglobal_vpnsessionpolicy_bindings(self) :
        """vpnsessionpolicy that can be bound to vpnglobal."""
        try :
            return self._vpnglobal_vpnsessionpolicy_binding
        except Exception as e:
            raise e

    @property
    def vpnglobal_authenticationcertpolicy_bindings(self) :
        """authenticationcertpolicy that can be bound to vpnglobal."""
        try :
            return self._vpnglobal_authenticationcertpolicy_binding
        except Exception as e:
            raise e

    @property
    def vpnglobal_authenticationnegotiatepolicy_bindings(self) :
        """authenticationnegotiatepolicy that can be bound to vpnglobal."""
        try :
            return self._vpnglobal_authenticationnegotiatepolicy_binding
        except Exception as e:
            raise e

    @property
    def vpnglobal_auditsyslogpolicy_bindings(self) :
        """auditsyslogpolicy that can be bound to vpnglobal."""
        try :
            return self._vpnglobal_auditsyslogpolicy_binding
        except Exception as e:
            raise e

    @property
    def vpnglobal_vpneula_bindings(self) :
        """vpneula that can be bound to vpnglobal."""
        try :
            return self._vpnglobal_vpneula_binding
        except Exception as e:
            raise e

    @property
    def vpnglobal_vpnurl_bindings(self) :
        """vpnurl that can be bound to vpnglobal."""
        try :
            return self._vpnglobal_vpnurl_binding
        except Exception as e:
            raise e

    @property
    def vpnglobal_vpnportaltheme_bindings(self) :
        """vpnportaltheme that can be bound to vpnglobal."""
        try :
            return self._vpnglobal_vpnportaltheme_binding
        except Exception as e:
            raise e

    @property
    def vpnglobal_vpnclientlessaccesspolicy_bindings(self) :
        """vpnclientlessaccesspolicy that can be bound to vpnglobal."""
        try :
            return self._vpnglobal_vpnclientlessaccesspolicy_binding
        except Exception as e:
            raise e

    @property
    def vpnglobal_authenticationlocalpolicy_bindings(self) :
        """authenticationlocalpolicy that can be bound to vpnglobal."""
        try :
            return self._vpnglobal_authenticationlocalpolicy_binding
        except Exception as e:
            raise e

    @property
    def vpnglobal_auditnslogpolicy_bindings(self) :
        """auditnslogpolicy that can be bound to vpnglobal."""
        try :
            return self._vpnglobal_auditnslogpolicy_binding
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(vpnglobal_binding_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.vpnglobal_binding
        except Exception as e :
            raise e

    def _get_object_name(self) :
        """Returns the value of object identifier argument"""
        try :
            return 0
        except Exception as e :
            raise e



    @classmethod
    def get(self, service) :
        """Use this API to fetch a vpnglobal_binding resource .

        :param service: 

        """
        try :
            obj = vpnglobal_binding()
            response = obj.get_resource(service)
            return response

        except Exception as e:
            raise e

class vpnglobal_binding_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.vpnglobal_binding = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.vpnglobal_binding = [vpnglobal_binding() for _ in range(length)]

