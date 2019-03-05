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

class riseapbrsvc(base_resource) :
    """Configuration for RISE Apbr services resource."""

        #------- Read only Parameter ---------

    def __init__(self) :
        self._name = ""
        self._risesvctype = ""
        self._serverip = ""
        self._nexthopip = ""
        self._vlan = 0
        self._protocol = ""
        self._serverport = 0
        self.___count = 0

    @property
    def name(self) :
        """Name for the APBR service."""
        try :
            return self._name
        except Exception as e:
            raise e

    @property
    def risesvctype(self) :
        """Service or Service Group.<br/>Possible values = Service, ServiceGroup."""
        try :
            return self._risesvctype
        except Exception as e:
            raise e

    @property
    def serverip(self) :
        """Server IP for APBR service."""
        try :
            return self._serverip
        except Exception as e:
            raise e

    @property
    def nexthopip(self) :
        """Nexthop IP for APBR service."""
        try :
            return self._nexthopip
        except Exception as e:
            raise e

    @property
    def vlan(self) :
        """Vlan id for APBR service."""
        try :
            return self._vlan
        except Exception as e:
            raise e

    @property
    def protocol(self) :
        """Protocol type for APBR service.<br/>Possible values = HTTP, FTP, TCP, UDP, SSL, SSL_BRIDGE, SSL_TCP, DTLS, NNTP, RPCSVR, DNS, ADNS, SNMP, RTSP, DHCPRA, ANY, SIP_UDP, SIP_TCP, SIP_SSL, DNS_TCP, ADNS_TCP, MYSQL, MSSQL, ORACLE, RADIUS, RADIUSListener, RDP, DIAMETER, SSL_DIAMETER, TFTP, SMPP, PPTP, GRE, SYSLOGTCP, SYSLOGUDP, FIX."""
        try :
            return self._protocol
        except Exception as e:
            raise e

    @property
    def serverport(self) :
        """Server port for APBR service.<br/>Range 1 - 65535."""
        try :
            return self._serverport
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(riseapbrsvc_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.riseapbrsvc
        except Exception as e :
            raise e

    def _get_object_name(self) :
        """Returns the value of object identifier argument"""
        try :
            return 0
        except Exception as e :
            raise e



    @classmethod
    def get(cls, client, name="", option_="") :
        """Use this API to fetch all the riseapbrsvc resources that are configured on netscaler.

        :param client: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            if not name :
                obj = riseapbrsvc()
                response = obj.get_resources(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def get_filtered(cls, client, filter_) :
        """Use this API to fetch filtered set of riseapbrsvc resources.
        filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = riseapbrsvc()
            option_ = options()
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def count(cls, client) :
        """Use this API to count the riseapbrsvc resources configured on NetScaler.

        :param client: 

        """
        try :
            obj = riseapbrsvc()
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
        """Use this API to count filtered the set of riseapbrsvc resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = riseapbrsvc()
            option_ = options()
            option_.count = True
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            if response :
                return response[0].__dict__['___count']
            return 0
        except Exception as e :
            raise e


    class Protocol:
        """ """
        HTTP = "HTTP"
        FTP = "FTP"
        TCP = "TCP"
        UDP = "UDP"
        SSL = "SSL"
        SSL_BRIDGE = "SSL_BRIDGE"
        SSL_TCP = "SSL_TCP"
        DTLS = "DTLS"
        NNTP = "NNTP"
        RPCSVR = "RPCSVR"
        DNS = "DNS"
        ADNS = "ADNS"
        SNMP = "SNMP"
        RTSP = "RTSP"
        DHCPRA = "DHCPRA"
        ANY = "ANY"
        SIP_UDP = "SIP_UDP"
        SIP_TCP = "SIP_TCP"
        SIP_SSL = "SIP_SSL"
        DNS_TCP = "DNS_TCP"
        ADNS_TCP = "ADNS_TCP"
        MYSQL = "MYSQL"
        MSSQL = "MSSQL"
        ORACLE = "ORACLE"
        RADIUS = "RADIUS"
        RADIUSListener = "RADIUSListener"
        RDP = "RDP"
        DIAMETER = "DIAMETER"
        SSL_DIAMETER = "SSL_DIAMETER"
        TFTP = "TFTP"
        SMPP = "SMPP"
        PPTP = "PPTP"
        GRE = "GRE"
        SYSLOGTCP = "SYSLOGTCP"
        SYSLOGUDP = "SYSLOGUDP"
        FIX = "FIX"

    class Risesvctype:
        """ """
        Service = "Service"
        ServiceGroup = "ServiceGroup"

class riseapbrsvc_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.riseapbrsvc = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.riseapbrsvc = [riseapbrsvc() for _ in range(length)]

