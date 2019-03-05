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

class snmptrap(base_resource) :
    """Configuration for snmp trap resource."""
    def __init__(self) :
        self._trapclass = ""
        self._trapdestination = ""
        self._version = ""
        self._td = 0
        self._destport = 0
        self._communityname = ""
        self._srcip = ""
        self._severity = ""
        self._allpartitions = ""
        self.___count = 0

    @property
    def trapclass(self) :
        """Type of trap messages that the NetScaler appliance sends to the trap listener: Generic or the enterprise-specific messages defined in the MIB file.<br/>Possible values = generic, specific."""
        try :
            return self._trapclass
        except Exception as e:
            raise e

    @trapclass.setter
    def trapclass(self, trapclass) :
        """Type of trap messages that the NetScaler appliance sends to the trap listener: Generic or the enterprise-specific messages defined in the MIB file.<br/>Possible values = generic, specific

        :param trapclass: 

        """
        try :
            self._trapclass = trapclass
        except Exception as e:
            raise e

    @property
    def trapdestination(self) :
        """IPv4 or the IPv6 address of the trap listener to which the NetScaler appliance is to send SNMP trap messages.<br/>Minimum length =  1."""
        try :
            return self._trapdestination
        except Exception as e:
            raise e

    @trapdestination.setter
    def trapdestination(self, trapdestination) :
        """IPv4 or the IPv6 address of the trap listener to which the NetScaler appliance is to send SNMP trap messages.<br/>Minimum length =  1

        :param trapdestination: 

        """
        try :
            self._trapdestination = trapdestination
        except Exception as e:
            raise e

    @property
    def version(self) :
        """SNMP version, which determines the format of trap messages sent to the trap listener.
        This setting must match the setting on the trap listener. Otherwise, the listener drops the trap messages.<br/>Default value: V2<br/>Possible values = V1, V2, V3.


        """
        try :
            return self._version
        except Exception as e:
            raise e

    @version.setter
    def version(self, version) :
        """SNMP version, which determines the format of trap messages sent to the trap listener.
        This setting must match the setting on the trap listener. Otherwise, the listener drops the trap messages.<br/>Default value: V2<br/>Possible values = V1, V2, V3

        :param version: 

        """
        try :
            self._version = version
        except Exception as e:
            raise e

    @property
    def td(self) :
        """Integer value that uniquely identifies the traffic domain in which you want to configure the entity. If you do not specify an ID, the entity becomes part of the default traffic domain, which has an ID of 0.<br/>Maximum length =  4094."""
        try :
            return self._td
        except Exception as e:
            raise e

    @td.setter
    def td(self, td) :
        """Integer value that uniquely identifies the traffic domain in which you want to configure the entity. If you do not specify an ID, the entity becomes part of the default traffic domain, which has an ID of 0.<br/>Maximum length =  4094

        :param td: 

        """
        try :
            self._td = td
        except Exception as e:
            raise e

    @property
    def destport(self) :
        """UDP port at which the trap listener listens for trap messages. This setting must match the setting on the trap listener. Otherwise, the listener drops the trap messages.<br/>Default value: 162<br/>Minimum length =  1<br/>Maximum length =  65534."""
        try :
            return self._destport
        except Exception as e:
            raise e

    @destport.setter
    def destport(self, destport) :
        """UDP port at which the trap listener listens for trap messages. This setting must match the setting on the trap listener. Otherwise, the listener drops the trap messages.<br/>Default value: 162<br/>Minimum length =  1<br/>Maximum length =  65534

        :param destport: 

        """
        try :
            self._destport = destport
        except Exception as e:
            raise e

    @property
    def communityname(self) :
        """Password (string) sent with the trap messages, so that the trap listener can authenticate them. Can include 1 to 31 uppercase or lowercase letters, numbers, and hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon (:), and underscore (_) characters.
        You must specify the same community string on the trap listener device. Otherwise, the trap listener drops the trap messages.
        The following requirement applies only to the NetScaler CLI:
        If the string includes one or more spaces, enclose the name in double or single quotation marks (for example, "my string" or 'my string').


        """
        try :
            return self._communityname
        except Exception as e:
            raise e

    @communityname.setter
    def communityname(self, communityname) :
        """Password (string) sent with the trap messages, so that the trap listener can authenticate them. Can include 1 to 31 uppercase or lowercase letters, numbers, and hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon (:), and underscore (_) characters.
        You must specify the same community string on the trap listener device. Otherwise, the trap listener drops the trap messages.
        The following requirement applies only to the NetScaler CLI:
        If the string includes one or more spaces, enclose the name in double or single quotation marks (for example, "my string" or 'my string').

        :param communityname: 

        """
        try :
            self._communityname = communityname
        except Exception as e:
            raise e

    @property
    def srcip(self) :
        """IPv4 or IPv6 address that the NetScaler appliance inserts as the source IP address in all SNMP trap messages that it sends to this trap listener. By default this is the appliance's NSIP or NSIP6 address, but you can specify an IPv4 MIP or SNIP address or a SNIP6 address.<br/>Minimum length =  1."""
        try :
            return self._srcip
        except Exception as e:
            raise e

    @srcip.setter
    def srcip(self, srcip) :
        """IPv4 or IPv6 address that the NetScaler appliance inserts as the source IP address in all SNMP trap messages that it sends to this trap listener. By default this is the appliance's NSIP or NSIP6 address, but you can specify an IPv4 MIP or SNIP address or a SNIP6 address.<br/>Minimum length =  1

        :param srcip: 

        """
        try :
            self._srcip = srcip
        except Exception as e:
            raise e

    @property
    def severity(self) :
        """Severity level at or above which the NetScaler appliance sends trap messages to this trap listener. The severity levels, in increasing order of severity, are Informational, Warning, Minor, Major, Critical. This parameter can be set for trap listeners of type SPECIFIC only. The default is to send all levels of trap messages.
        Important: Trap messages are not assigned severity levels unless you specify severity levels when configuring SNMP alarms.<br/>Default value: Unknown<br/>Possible values = Critical, Major, Minor, Warning, Informational.


        """
        try :
            return self._severity
        except Exception as e:
            raise e

    @severity.setter
    def severity(self, severity) :
        """Severity level at or above which the NetScaler appliance sends trap messages to this trap listener. The severity levels, in increasing order of severity, are Informational, Warning, Minor, Major, Critical. This parameter can be set for trap listeners of type SPECIFIC only. The default is to send all levels of trap messages.
        Important: Trap messages are not assigned severity levels unless you specify severity levels when configuring SNMP alarms.<br/>Default value: Unknown<br/>Possible values = Critical, Major, Minor, Warning, Informational

        :param severity: 

        """
        try :
            self._severity = severity
        except Exception as e:
            raise e

    @property
    def allpartitions(self) :
        """Send traps of all partitions to this destination.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._allpartitions
        except Exception as e:
            raise e

    @allpartitions.setter
    def allpartitions(self, allpartitions) :
        """Send traps of all partitions to this destination.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED

        :param allpartitions: 

        """
        try :
            self._allpartitions = allpartitions
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(snmptrap_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.snmptrap
        except Exception as e :
            raise e

    def _get_object_name(self) :
        """Returns the value of object identifier argument"""
        try :
            if self.trapclass is not None :
                return str(self.trapclass)
            return None
        except Exception as e :
            raise e



    @classmethod
    def add(cls, client, resource) :
        """Use this API to add snmptrap.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                addresource = snmptrap()
                addresource.trapclass = resource.trapclass
                addresource.trapdestination = resource.trapdestination
                addresource.version = resource.version
                addresource.td = resource.td
                addresource.destport = resource.destport
                addresource.communityname = resource.communityname
                addresource.srcip = resource.srcip
                addresource.severity = resource.severity
                addresource.allpartitions = resource.allpartitions
                return addresource.add_resource(client)
            else :
                if (resource and len(resource) > 0) :
                    addresources = [ snmptrap() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        addresources[i].trapclass = resource[i].trapclass
                        addresources[i].trapdestination = resource[i].trapdestination
                        addresources[i].version = resource[i].version
                        addresources[i].td = resource[i].td
                        addresources[i].destport = resource[i].destport
                        addresources[i].communityname = resource[i].communityname
                        addresources[i].srcip = resource[i].srcip
                        addresources[i].severity = resource[i].severity
                        addresources[i].allpartitions = resource[i].allpartitions
                result = cls.add_bulk_request(client, addresources)
            return result
        except Exception as e :
            raise e

    @classmethod
    def delete(cls, client, resource) :
        """Use this API to delete snmptrap.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                deleteresource = snmptrap()
                if type(resource) !=  type(deleteresource):
                    deleteresource.trapclass = resource
                else :
                    deleteresource.trapclass = resource.trapclass
                    deleteresource.trapdestination = resource.trapdestination
                    deleteresource.version = resource.version
                    deleteresource.td = resource.td
                return deleteresource.delete_resource(client)
            else :
                if type(resource[0]) != cls :
                    if (resource and len(resource) > 0) :
                        deleteresources = [ snmptrap() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            deleteresources[i].trapclass = resource[i]
                else :
                    if (resource and len(resource) > 0) :
                        deleteresources = [ snmptrap() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            deleteresources[i].trapclass = resource[i].trapclass
                            deleteresources[i].trapdestination = resource[i].trapdestination
                            deleteresources[i].version = resource[i].version
                            deleteresources[i].td = resource[i].td
                result = cls.delete_bulk_request(client, deleteresources)
            return result
        except Exception as e :
            raise e

    @classmethod
    def update(cls, client, resource) :
        """Use this API to update snmptrap.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                updateresource = snmptrap()
                updateresource.trapclass = resource.trapclass
                updateresource.trapdestination = resource.trapdestination
                updateresource.version = resource.version
                updateresource.td = resource.td
                updateresource.destport = resource.destport
                updateresource.communityname = resource.communityname
                updateresource.srcip = resource.srcip
                updateresource.severity = resource.severity
                updateresource.allpartitions = resource.allpartitions
                return updateresource.update_resource(client)
            else :
                if (resource and len(resource) > 0) :
                    updateresources = [ snmptrap() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        updateresources[i].trapclass = resource[i].trapclass
                        updateresources[i].trapdestination = resource[i].trapdestination
                        updateresources[i].version = resource[i].version
                        updateresources[i].td = resource[i].td
                        updateresources[i].destport = resource[i].destport
                        updateresources[i].communityname = resource[i].communityname
                        updateresources[i].srcip = resource[i].srcip
                        updateresources[i].severity = resource[i].severity
                        updateresources[i].allpartitions = resource[i].allpartitions
                result = cls.update_bulk_request(client, updateresources)
            return result
        except Exception as e :
            raise e

    @classmethod
    def unset(cls, client, resource, args) :
        """Use this API to unset the properties of snmptrap resource.
        Properties that need to be unset are specified in args array.

        :param client: 
        :param resource: 
        :param args: 

        """
        try :
            if type(resource) is not list :
                unsetresource = snmptrap()
                unsetresource.trapclass = resource.trapclass
                unsetresource.trapdestination = resource.trapdestination
                unsetresource.version = resource.version
                unsetresource.td = resource.td
                return unsetresource.unset_resource(client, args)
            else :
                if type(resource[0]) == cls :
                    if (resource and len(resource) > 0) :
                        unsetresources = [ snmptrap() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            unsetresources[i].trapclass = resource[i].trapclass
                            unsetresources[i].trapdestination = resource[i].trapdestination
                            unsetresources[i].version = resource[i].version
                            unsetresources[i].td = resource[i].td
                result = cls.unset_bulk_request(client, unsetresources, args)
            return result
        except Exception as e :
            raise e

    @classmethod
    def get(cls, client, name="", option_="") :
        """Use this API to fetch all the snmptrap resources that are configured on netscaler.

        :param client: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            if not name :
                obj = snmptrap()
                response = obj.get_resources(client, option_)
            else :
                if type(name) == cls :
                    if type(name) is not list :
                        option_ = options()
                        option_.args = nitro_util.object_to_string_withoutquotes(name)
                        response = name.get_resource(client, option_)
                    else :
                        if name and len(name) > 0 :
                            response = [snmptrap() for _ in range(len(name))]
                            for i in range(len(name)) :
                                option_ = options()
                                option_.args = nitro_util.object_to_string_withoutquotes(name[i])
                                response[i] = name[i].get_resource(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def get_filtered(cls, client, filter_) :
        """Use this API to fetch filtered set of snmptrap resources.
        filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = snmptrap()
            option_ = options()
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def count(cls, client) :
        """Use this API to count the snmptrap resources configured on NetScaler.

        :param client: 

        """
        try :
            obj = snmptrap()
            option_ = options()
            option_.count = True
            response = obj.get_resources(client, option_)
            if response :
                return response[0].__dict__['___count']
            return 0
        except Exception as e :
            raise e

    @classmethod
    def count_filtered(cls, client, filter_) :
        """Use this API to count filtered the set of snmptrap resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = snmptrap()
            option_ = options()
            option_.count = True
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            if response :
                return response[0].__dict__['___count']
            return 0
        except Exception as e :
            raise e


    class Allpartitions:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Trapclass:
        """ """
        generic = "generic"
        specific = "specific"

    class Severity:
        """ """
        Critical = "Critical"
        Major = "Major"
        Minor = "Minor"
        Warning = "Warning"
        Informational = "Informational"

    class Version:
        """ """
        V1 = "V1"
        V2 = "V2"
        V3 = "V3"

class snmptrap_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.snmptrap = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.snmptrap = [snmptrap() for _ in range(length)]

