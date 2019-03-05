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

class lsnsession(base_resource) :
    """Configuration for lsn session resource."""
    def __init__(self) :
        self._nattype = ""
        self._clientname = ""
        self._network = ""
        self._netmask = ""
        self._network6 = ""
        self._td = 0
        self._natip = ""
        self._natport2 = 0
        self._natprefix = ""
        self._subscrip = ""
        self._subscrport = 0
        self._destip = ""
        self._destport = 0
        self._natport = 0
        self._transportprotocol = ""
        self._sessionestdir = ""
        self._dsttd = 0
        self._srctd = 0
        self.___count = 0

    @property
    def nattype(self) :
        """Type of sessions to be displayed.<br/>Default value: NAT44<br/>Possible values = NAT44, DS-Lite."""
        try :
            return self._nattype
        except Exception as e:
            raise e

    @nattype.setter
    def nattype(self, nattype) :
        """Type of sessions to be displayed.<br/>Default value: NAT44<br/>Possible values = NAT44, DS-Lite

        :param nattype: 

        """
        try :
            self._nattype = nattype
        except Exception as e:
            raise e

    @property
    def clientname(self) :
        """Name of the LSN Client entity."""
        try :
            return self._clientname
        except Exception as e:
            raise e

    @clientname.setter
    def clientname(self, clientname) :
        """Name of the LSN Client entity.

        :param clientname: 

        """
        try :
            self._clientname = clientname
        except Exception as e:
            raise e

    @property
    def network(self) :
        """IP address or network address of subscriber(s)."""
        try :
            return self._network
        except Exception as e:
            raise e

    @network.setter
    def network(self, network) :
        """IP address or network address of subscriber(s).

        :param network: 

        """
        try :
            self._network = network
        except Exception as e:
            raise e

    @property
    def netmask(self) :
        """Subnet mask for the IP address specified by the network parameter."""
        try :
            return self._netmask
        except Exception as e:
            raise e

    @netmask.setter
    def netmask(self, netmask) :
        """Subnet mask for the IP address specified by the network parameter.

        :param netmask: 

        """
        try :
            self._netmask = netmask
        except Exception as e:
            raise e

    @property
    def network6(self) :
        """IPv6 address of the LSN subscriber or B4 device."""
        try :
            return self._network6
        except Exception as e:
            raise e

    @network6.setter
    def network6(self, network6) :
        """IPv6 address of the LSN subscriber or B4 device.

        :param network6: 

        """
        try :
            self._network6 = network6
        except Exception as e:
            raise e

    @property
    def td(self) :
        """Traffic domain ID of the LSN client entity.<br/>Default value: 0<br/>Maximum length =  4094."""
        try :
            return self._td
        except Exception as e:
            raise e

    @td.setter
    def td(self, td) :
        """Traffic domain ID of the LSN client entity.<br/>Default value: 0<br/>Maximum length =  4094

        :param td: 

        """
        try :
            self._td = td
        except Exception as e:
            raise e

    @property
    def natip(self) :
        """Mapped NAT IP address used in LSN sessions."""
        try :
            return self._natip
        except Exception as e:
            raise e

    @natip.setter
    def natip(self, natip) :
        """Mapped NAT IP address used in LSN sessions.

        :param natip: 

        """
        try :
            self._natip = natip
        except Exception as e:
            raise e

    @property
    def natport2(self) :
        """Mapped NAT port used in the LSN sessions."""
        try :
            return self._natport2
        except Exception as e:
            raise e

    @natport2.setter
    def natport2(self, natport2) :
        """Mapped NAT port used in the LSN sessions.

        :param natport2: 

        """
        try :
            self._natport2 = natport2
        except Exception as e:
            raise e

    @property
    def natprefix(self) :
        """IPv6 address of the LSN subscriber(s) or subscriber network(B4-Device) on whose traffic the NetScaler ADC perform Large Scale NAT."""
        try :
            return self._natprefix
        except Exception as e:
            raise e

    @property
    def subscrip(self) :
        """The Source IP address."""
        try :
            return self._subscrip
        except Exception as e:
            raise e

    @property
    def subscrport(self) :
        """The Source Port."""
        try :
            return self._subscrport
        except Exception as e:
            raise e

    @property
    def destip(self) :
        """The Destination IP address."""
        try :
            return self._destip
        except Exception as e:
            raise e

    @property
    def destport(self) :
        """The Destination Port."""
        try :
            return self._destport
        except Exception as e:
            raise e

    @property
    def natport(self) :
        """The NAT Port."""
        try :
            return self._natport
        except Exception as e:
            raise e

    @property
    def transportprotocol(self) :
        """The Transport Protocol for the session.<br/>Possible values = TCP, UDP, ICMP."""
        try :
            return self._transportprotocol
        except Exception as e:
            raise e

    @property
    def sessionestdir(self) :
        """The Session establishment direction, session was established for outbound or inbound packet.<br/>Possible values = OUT, IN."""
        try :
            return self._sessionestdir
        except Exception as e:
            raise e

    @property
    def dsttd(self) :
        """ """
        try :
            return self._dsttd
        except Exception as e:
            raise e

    @property
    def srctd(self) :
        """ """
        try :
            return self._srctd
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(lsnsession_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.lsnsession
        except Exception as e :
            raise e

    def _get_object_name(self) :
        """Returns the value of object identifier argument"""
        try :
            return 0
        except Exception as e :
            raise e



    @classmethod
    def flush(cls, client, resource) :
        """Use this API to flush lsnsession.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                flushresource = lsnsession()
                flushresource.nattype = resource.nattype
                flushresource.clientname = resource.clientname
                flushresource.network = resource.network
                flushresource.netmask = resource.netmask
                flushresource.network6 = resource.network6
                flushresource.td = resource.td
                flushresource.natip = resource.natip
                flushresource.natport2 = resource.natport2
                return flushresource.perform_operation(client,"flush")
            else :
                if (resource and len(resource) > 0) :
                    flushresources = [ lsnsession() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        flushresources[i].nattype = resource[i].nattype
                        flushresources[i].clientname = resource[i].clientname
                        flushresources[i].network = resource[i].network
                        flushresources[i].netmask = resource[i].netmask
                        flushresources[i].network6 = resource[i].network6
                        flushresources[i].td = resource[i].td
                        flushresources[i].natip = resource[i].natip
                        flushresources[i].natport2 = resource[i].natport2
                result = cls.perform_operation_bulk_request(client, flushresources,"flush")
            return result
        except Exception as e :
            raise e

    @classmethod
    def get(cls, client, name="", option_="") :
        """Use this API to fetch all the lsnsession resources that are configured on netscaler.

        :param client: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            if not name :
                obj = lsnsession()
                response = obj.get_resources(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def get_args(cls, client, args) :
        """Use this API to fetch all the lsnsession resources that are configured on netscaler.
            # This uses lsnsession_args which is a way to provide additional arguments while fetching the resources.

        :param client: 
        :param args: 

        """
        try :
            obj = lsnsession()
            option_ = options()
            option_.args = nitro_util.object_to_string_withoutquotes(args)
            response = obj.get_resources(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def get_filtered(cls, client, filter_) :
        """Use this API to fetch filtered set of lsnsession resources.
        filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = lsnsession()
            option_ = options()
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def count(cls, client) :
        """Use this API to count the lsnsession resources configured on NetScaler.

        :param client: 

        """
        try :
            obj = lsnsession()
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
        """Use this API to count filtered the set of lsnsession resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = lsnsession()
            option_ = options()
            option_.count = True
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            if response :
                return response[0].__dict__['___count']
            return 0
        except Exception as e :
            raise e


    class Transportprotocol:
        """ """
        TCP = "TCP"
        UDP = "UDP"
        ICMP = "ICMP"

    class Sessionestdir:
        """ """
        OUT = "OUT"
        IN = "IN"

    class Nattype:
        """ """
        NAT44 = "NAT44"
        DS_Lite = "DS-Lite"

class lsnsession_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.lsnsession = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.lsnsession = [lsnsession() for _ in range(length)]

