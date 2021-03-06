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

class lsnclient_network_binding(base_resource) :
    """Binding class showing the network that can be bound to lsnclient."""
    def __init__(self) :
        self._network = ""
        self._netmask = ""
        self._clientname = ""
        self._td = 0
        self.___count = 0

    @property
    def network(self) :
        """IPv4 address(es) of the LSN subscriber(s) or subscriber network(s) on whose traffic you want the NetScaler ADC to perform Large Scale NAT.<br/>Minimum length =  1."""
        try :
            return self._network
        except Exception as e:
            raise e

    @network.setter
    def network(self, network) :
        """IPv4 address(es) of the LSN subscriber(s) or subscriber network(s) on whose traffic you want the NetScaler ADC to perform Large Scale NAT.<br/>Minimum length =  1

        :param network: 

        """
        try :
            self._network = network
        except Exception as e:
            raise e

    @property
    def clientname(self) :
        """Name for the LSN client entity. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the LSN client is created. The following requirement applies only to the NetScaler CLI: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "lsn client1" or 'lsn client1'). .<br/>Minimum length =  1<br/>Maximum length =  127."""
        try :
            return self._clientname
        except Exception as e:
            raise e

    @clientname.setter
    def clientname(self, clientname) :
        """Name for the LSN client entity. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the LSN client is created. The following requirement applies only to the NetScaler CLI: If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "lsn client1" or 'lsn client1'). .<br/>Minimum length =  1<br/>Maximum length =  127

        :param clientname: 

        """
        try :
            self._clientname = clientname
        except Exception as e:
            raise e

    @property
    def td(self) :
        """ID of the traffic domain on which this subscriber or the subscriber network (as specified by the network parameter) belongs.
        If you do not specify an ID, the subscriber or the subscriber network becomes part of the default traffic domain.<br/>Default value: 0<br/>Minimum value =  0<br/>Maximum value =  4094.


        """
        try :
            return self._td
        except Exception as e:
            raise e

    @td.setter
    def td(self, td) :
        """ID of the traffic domain on which this subscriber or the subscriber network (as specified by the network parameter) belongs.
        If you do not specify an ID, the subscriber or the subscriber network becomes part of the default traffic domain.<br/>Default value: 0<br/>Minimum value =  0<br/>Maximum value =  4094

        :param td: 

        """
        try :
            self._td = td
        except Exception as e:
            raise e

    @property
    def netmask(self) :
        """Subnet mask for the IPv4 address specified in the Network parameter."""
        try :
            return self._netmask
        except Exception as e:
            raise e

    @netmask.setter
    def netmask(self, netmask) :
        """Subnet mask for the IPv4 address specified in the Network parameter.

        :param netmask: 

        """
        try :
            self._netmask = netmask
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(lsnclient_network_binding_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.lsnclient_network_binding
        except Exception as e :
            raise e

    def _get_object_name(self) :
        """Returns the value of object identifier argument"""
        try :
            if self.clientname is not None :
                return str(self.clientname)
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
                updateresource = lsnclient_network_binding()
                updateresource.clientname = resource.clientname
                updateresource.network = resource.network
                updateresource.netmask = resource.netmask
                updateresource.td = resource.td
                return updateresource.update_resource(client)
            else :
                if resource and len(resource) > 0 :
                    updateresources = [lsnclient_network_binding() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        updateresources[i].clientname = resource[i].clientname
                        updateresources[i].network = resource[i].network
                        updateresources[i].netmask = resource[i].netmask
                        updateresources[i].td = resource[i].td
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
                deleteresource = lsnclient_network_binding()
                deleteresource.clientname = resource.clientname
                deleteresource.network = resource.network
                deleteresource.netmask = resource.netmask
                deleteresource.td = resource.td
                return deleteresource.delete_resource(client)
            else :
                if resource and len(resource) > 0 :
                    deleteresources = [lsnclient_network_binding() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        deleteresources[i].clientname = resource[i].clientname
                        deleteresources[i].network = resource[i].network
                        deleteresources[i].netmask = resource[i].netmask
                        deleteresources[i].td = resource[i].td
                return cls.delete_bulk_request(client, deleteresources)
        except Exception as e :
            raise e

    @classmethod
    def get(cls, service, clientname) :
        """Use this API to fetch lsnclient_network_binding resources.

        :param service: 
        :param clientname: 

        """
        try :
            obj = lsnclient_network_binding()
            obj.clientname = clientname
            response = obj.get_resources(service)
            return response
        except Exception as e:
            raise e

    @classmethod
    def get_filtered(cls, service, clientname, filter_) :
        """Use this API to fetch filtered set of lsnclient_network_binding resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param service: 
        :param clientname: 
        :param filter_: 

        """
        try :
            obj = lsnclient_network_binding()
            obj.clientname = clientname
            option_ = options()
            option_.filter = filter_
            response = obj.getfiltered(service, option_)
            return response
        except Exception as e:
            raise e

    @classmethod
    def count(cls, service, clientname) :
        """Use this API to count lsnclient_network_binding resources configued on NetScaler.

        :param service: 
        :param clientname: 

        """
        try :
            obj = lsnclient_network_binding()
            obj.clientname = clientname
            option_ = options()
            option_.count = True
            response = obj.get_resources(service, option_)
            if response :
                return response[0].__dict__['___count']
            return 0
        except Exception as e:
            raise e

    @classmethod
    def count_filtered(cls, service, clientname, filter_) :
        """Use this API to count the filtered set of lsnclient_network_binding resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param service: 
        :param clientname: 
        :param filter_: 

        """
        try :
            obj = lsnclient_network_binding()
            obj.clientname = clientname
            option_ = options()
            option_.count = True
            option_.filter = filter_
            response = obj.getfiltered(service, option_)
            if response :
                return response[0].__dict__['___count']
            return 0
        except Exception as e:
            raise e

class lsnclient_network_binding_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.lsnclient_network_binding = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.lsnclient_network_binding = [lsnclient_network_binding() for _ in range(length)]

