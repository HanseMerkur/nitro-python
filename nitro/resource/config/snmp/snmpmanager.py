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

class snmpmanager(base_resource) :
    """Configuration for manager resource."""
    def __init__(self) :
        self._ipaddress = ""
        self._netmask = ""
        self._domainresolveretry = 0
        self._ip = ""
        self._domain = ""
        self.___count = 0

    @property
    def ipaddress(self) :
        """IP address of the SNMP manager. Can be an IPv4 or IPv6 address. You can instead specify an IPv4 network address or IPv6 network prefix if you want the NetScaler appliance to respond to SNMP queries from any device on the specified network. Alternatively, instead of an IPv4 address, you can specify a host name that has been assigned to an SNMP manager. If you do so, you must add a DNS name server that resolves the host name of the SNMP manager to its IP address.
        Note: The NetScaler appliance does not support host names for SNMP managers that have IPv6 addresses.<br/>Minimum length =  1<br/>Maximum length =  255.


        """
        try :
            return self._ipaddress
        except Exception as e:
            raise e

    @ipaddress.setter
    def ipaddress(self, ipaddress) :
        """IP address of the SNMP manager. Can be an IPv4 or IPv6 address. You can instead specify an IPv4 network address or IPv6 network prefix if you want the NetScaler appliance to respond to SNMP queries from any device on the specified network. Alternatively, instead of an IPv4 address, you can specify a host name that has been assigned to an SNMP manager. If you do so, you must add a DNS name server that resolves the host name of the SNMP manager to its IP address.
        Note: The NetScaler appliance does not support host names for SNMP managers that have IPv6 addresses.<br/>Minimum length =  1<br/>Maximum length =  255

        :param ipaddress: 

        """
        try :
            self._ipaddress = ipaddress
        except Exception as e:
            raise e

    @property
    def netmask(self) :
        """Subnet mask associated with an IPv4 network address. If the IP address specifies the address or host name of a specific host, accept the default value of 255.255.255.255."""
        try :
            return self._netmask
        except Exception as e:
            raise e

    @netmask.setter
    def netmask(self, netmask) :
        """Subnet mask associated with an IPv4 network address. If the IP address specifies the address or host name of a specific host, accept the default value of 255.255.255.255.

        :param netmask: 

        """
        try :
            self._netmask = netmask
        except Exception as e:
            raise e

    @property
    def domainresolveretry(self) :
        """Amount of time, in seconds, for which the NetScaler appliance waits before sending another DNS query to resolve the host name of the SNMP manager if the last query failed. This parameter is valid for host-name based SNMP managers only. After a query succeeds, the TTL determines the wait time.<br/>Minimum length =  5<br/>Maximum length =  20939."""
        try :
            return self._domainresolveretry
        except Exception as e:
            raise e

    @domainresolveretry.setter
    def domainresolveretry(self, domainresolveretry) :
        """Amount of time, in seconds, for which the NetScaler appliance waits before sending another DNS query to resolve the host name of the SNMP manager if the last query failed. This parameter is valid for host-name based SNMP managers only. After a query succeeds, the TTL determines the wait time.<br/>Minimum length =  5<br/>Maximum length =  20939

        :param domainresolveretry: 

        """
        try :
            self._domainresolveretry = domainresolveretry
        except Exception as e:
            raise e

    @property
    def ip(self) :
        """The resolved IP address of the hostname manager."""
        try :
            return self._ip
        except Exception as e:
            raise e

    @property
    def domain(self) :
        """IP address of manager. It will be zero for hostname manager."""
        try :
            return self._domain
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(snmpmanager_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.snmpmanager
        except Exception as e :
            raise e

    def _get_object_name(self) :
        """Returns the value of object identifier argument"""
        try :
            if self.ipaddress is not None :
                return str(self.ipaddress)
            return None
        except Exception as e :
            raise e



    @classmethod
    def add(cls, client, resource) :
        """Use this API to add snmpmanager.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                addresource = snmpmanager()
                addresource.ipaddress = resource.ipaddress
                addresource.netmask = resource.netmask
                addresource.domainresolveretry = resource.domainresolveretry
                return addresource.add_resource(client)
            else :
                if (resource and len(resource) > 0) :
                    addresources = [ snmpmanager() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        addresources[i].ipaddress = resource[i].ipaddress
                        addresources[i].netmask = resource[i].netmask
                        addresources[i].domainresolveretry = resource[i].domainresolveretry
                result = cls.add_bulk_request(client, addresources)
            return result
        except Exception as e :
            raise e

    @classmethod
    def delete(cls, client, resource) :
        """Use this API to delete snmpmanager.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                deleteresource = snmpmanager()
                if type(resource) !=  type(deleteresource):
                    deleteresource.ipaddress = resource
                else :
                    deleteresource.ipaddress = resource.ipaddress
                    deleteresource.netmask = resource.netmask
                return deleteresource.delete_resource(client)
            else :
                if type(resource[0]) != cls :
                    if (resource and len(resource) > 0) :
                        deleteresources = [ snmpmanager() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            deleteresources[i].ipaddress = resource[i]
                else :
                    if (resource and len(resource) > 0) :
                        deleteresources = [ snmpmanager() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            deleteresources[i].ipaddress = resource[i].ipaddress
                            deleteresources[i].netmask = resource[i].netmask
                result = cls.delete_bulk_request(client, deleteresources)
            return result
        except Exception as e :
            raise e

    @classmethod
    def update(cls, client, resource) :
        """Use this API to update snmpmanager.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                updateresource = snmpmanager()
                updateresource.ipaddress = resource.ipaddress
                updateresource.netmask = resource.netmask
                updateresource.domainresolveretry = resource.domainresolveretry
                return updateresource.update_resource(client)
            else :
                if (resource and len(resource) > 0) :
                    updateresources = [ snmpmanager() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        updateresources[i].ipaddress = resource[i].ipaddress
                        updateresources[i].netmask = resource[i].netmask
                        updateresources[i].domainresolveretry = resource[i].domainresolveretry
                result = cls.update_bulk_request(client, updateresources)
            return result
        except Exception as e :
            raise e

    @classmethod
    def unset(cls, client, resource, args) :
        """Use this API to unset the properties of snmpmanager resource.
        Properties that need to be unset are specified in args array.

        :param client: 
        :param resource: 
        :param args: 

        """
        try :
            if type(resource) is not list :
                unsetresource = snmpmanager()
                unsetresource.ipaddress = resource.ipaddress
                unsetresource.netmask = resource.netmask
                return unsetresource.unset_resource(client, args)
            else :
                if type(resource[0]) == cls :
                    if (resource and len(resource) > 0) :
                        unsetresources = [ snmpmanager() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            unsetresources[i].ipaddress = resource[i].ipaddress
                            unsetresources[i].netmask = resource[i].netmask
                result = cls.unset_bulk_request(client, unsetresources, args)
            return result
        except Exception as e :
            raise e

    @classmethod
    def get(cls, client, name="", option_="") :
        """Use this API to fetch all the snmpmanager resources that are configured on netscaler.

        :param client: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            if not name :
                obj = snmpmanager()
                response = obj.get_resources(client, option_)
            else :
                if type(name) == cls :
                    if type(name) is not list :
                        option_ = options()
                        option_.args = nitro_util.object_to_string_withoutquotes(name)
                        response = name.get_resource(client, option_)
                    else :
                        if name and len(name) > 0 :
                            response = [snmpmanager() for _ in range(len(name))]
                            for i in range(len(name)) :
                                option_ = options()
                                option_.args = nitro_util.object_to_string_withoutquotes(name[i])
                                response[i] = name[i].get_resource(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def get_filtered(cls, client, filter_) :
        """Use this API to fetch filtered set of snmpmanager resources.
        filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = snmpmanager()
            option_ = options()
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def count(cls, client) :
        """Use this API to count the snmpmanager resources configured on NetScaler.

        :param client: 

        """
        try :
            obj = snmpmanager()
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
        """Use this API to count filtered the set of snmpmanager resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = snmpmanager()
            option_ = options()
            option_.count = True
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            if response :
                return response[0].__dict__['___count']
            return 0
        except Exception as e :
            raise e


class snmpmanager_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.snmpmanager = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.snmpmanager = [snmpmanager() for _ in range(length)]

