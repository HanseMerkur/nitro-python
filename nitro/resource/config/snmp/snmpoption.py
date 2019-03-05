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

class snmpoption(base_resource) :
    """Configuration for SNMP option resource."""
    def __init__(self) :
        self._snmpset = ""
        self._snmptraplogging = ""
        self._partitionnameintrap = ""

    @property
    def snmpset(self) :
        """Accept SNMP SET requests sent to the NetScaler appliance, and allow SNMP managers to write values to MIB objects that are configured for write access.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._snmpset
        except Exception as e:
            raise e

    @snmpset.setter
    def snmpset(self, snmpset) :
        """Accept SNMP SET requests sent to the NetScaler appliance, and allow SNMP managers to write values to MIB objects that are configured for write access.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED

        :param snmpset: 

        """
        try :
            self._snmpset = snmpset
        except Exception as e:
            raise e

    @property
    def snmptraplogging(self) :
        """Log any SNMP trap events (for SNMP alarms in which logging is enabled) even if no trap listeners are configured. With the default setting, SNMP trap events are logged if at least one trap listener is configured on the appliance.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._snmptraplogging
        except Exception as e:
            raise e

    @snmptraplogging.setter
    def snmptraplogging(self, snmptraplogging) :
        """Log any SNMP trap events (for SNMP alarms in which logging is enabled) even if no trap listeners are configured. With the default setting, SNMP trap events are logged if at least one trap listener is configured on the appliance.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED

        :param snmptraplogging: 

        """
        try :
            self._snmptraplogging = snmptraplogging
        except Exception as e:
            raise e

    @property
    def partitionnameintrap(self) :
        """Send partition name as a varbind in traps. By default the partition names are not sent as a varbind.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._partitionnameintrap
        except Exception as e:
            raise e

    @partitionnameintrap.setter
    def partitionnameintrap(self, partitionnameintrap) :
        """Send partition name as a varbind in traps. By default the partition names are not sent as a varbind.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED

        :param partitionnameintrap: 

        """
        try :
            self._partitionnameintrap = partitionnameintrap
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(snmpoption_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.snmpoption
        except Exception as e :
            raise e

    def _get_object_name(self) :
        """Returns the value of object identifier argument"""
        try :
            return 0
        except Exception as e :
            raise e



    @classmethod
    def update(cls, client, resource) :
        """Use this API to update snmpoption.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                updateresource = snmpoption()
                updateresource.snmpset = resource.snmpset
                updateresource.snmptraplogging = resource.snmptraplogging
                updateresource.partitionnameintrap = resource.partitionnameintrap
                return updateresource.update_resource(client)
        except Exception as e :
            raise e

    @classmethod
    def unset(cls, client, resource, args) :
        """Use this API to unset the properties of snmpoption resource.
        Properties that need to be unset are specified in args array.

        :param client: 
        :param resource: 
        :param args: 

        """
        try :
            if type(resource) is not list :
                unsetresource = snmpoption()
                return unsetresource.unset_resource(client, args)
        except Exception as e :
            raise e

    @classmethod
    def get(cls, client, name="", option_="") :
        """Use this API to fetch all the snmpoption resources that are configured on netscaler.

        :param client: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            if not name :
                obj = snmpoption()
                response = obj.get_resources(client, option_)
            return response
        except Exception as e :
            raise e


    class Snmptraplogging:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Snmpset:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Partitionnameintrap:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

class snmpoption_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.snmpoption = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.snmpoption = [snmpoption() for _ in range(length)]

