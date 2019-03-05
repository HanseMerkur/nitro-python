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

class nslicense(base_resource) :
    """Configuration for license resource."""

        #------- Read only Parameter ---------

    def __init__(self) :
        self._wl = False
        self._sp = False
        self._lb = False
        self._cs = False
        self._cr = False
        self._sc = False
        self._cmp = False
        self._delta = False
        self._pq = False
        self._ssl = False
        self._gslb = False
        self._gslbp = False
        self._hdosp = False
        self._routing = False
        self._cf = False
        self._contentaccelerator = False
        self._ic = False
        self._sslvpn = False
        self._f_sslvpn_users = 0
        self._f_ica_users = 0
        self._aaa = False
        self._ospf = False
        self._rip = False
        self._bgp = False
        self._rewrite = False
        self._ipv6pt = False
        self._appfw = False
        self._responder = False
        self._agee = False
        self._nsxn = False
        self._htmlinjection = False
        self._modelid = 0
        self._push = False
        self._wionns = False
        self._appflow = False
        self._cloudbridge = False
        self._cloudbridgeappliance = False
        self._cloudextenderappliance = False
        self._isis = False
        self._cluster = False
        self._ch = False
        self._appqoe = False
        self._appflowica = False
        self._isstandardlic = False
        self._isenterpriselic = False
        self._isplatinumlic = False
        self._rise = False
        self._vpath = False
        self._feo = False
        self._lsn = False
        self._rdpproxy = False
        self._rep = False

    @property
    def wl(self) :
        """Web Logging."""
        try :
            return self._wl
        except Exception as e:
            raise e

    @property
    def sp(self) :
        """Surge Protection."""
        try :
            return self._sp
        except Exception as e:
            raise e

    @property
    def lb(self) :
        """Load Balancing."""
        try :
            return self._lb
        except Exception as e:
            raise e

    @property
    def cs(self) :
        """Content Switching."""
        try :
            return self._cs
        except Exception as e:
            raise e

    @property
    def cr(self) :
        """Cache Redirect."""
        try :
            return self._cr
        except Exception as e:
            raise e

    @property
    def sc(self) :
        """Sure Connect."""
        try :
            return self._sc
        except Exception as e:
            raise e

    @property
    def cmp(self) :
        """Compression."""
        try :
            return self._cmp
        except Exception as e:
            raise e

    @property
    def delta(self) :
        """Delta Compression."""
        try :
            return self._delta
        except Exception as e:
            raise e

    @property
    def pq(self) :
        """Priority Queuing."""
        try :
            return self._pq
        except Exception as e:
            raise e

    @property
    def ssl(self) :
        """Secure Sockets Layer."""
        try :
            return self._ssl
        except Exception as e:
            raise e

    @property
    def gslb(self) :
        """Global Server Load Balancing."""
        try :
            return self._gslb
        except Exception as e:
            raise e

    @property
    def gslbp(self) :
        """GSLB Proximity."""
        try :
            return self._gslbp
        except Exception as e:
            raise e

    @property
    def hdosp(self) :
        """DOS Protection."""
        try :
            return self._hdosp
        except Exception as e:
            raise e

    @property
    def routing(self) :
        """Routing."""
        try :
            return self._routing
        except Exception as e:
            raise e

    @property
    def cf(self) :
        """Content Filter."""
        try :
            return self._cf
        except Exception as e:
            raise e

    @property
    def contentaccelerator(self) :
        """transparent Integrated Caching."""
        try :
            return self._contentaccelerator
        except Exception as e:
            raise e

    @property
    def ic(self) :
        """Integrated Caching."""
        try :
            return self._ic
        except Exception as e:
            raise e

    @property
    def sslvpn(self) :
        """SSL VPN."""
        try :
            return self._sslvpn
        except Exception as e:
            raise e

    @property
    def f_sslvpn_users(self) :
        """Number of licensed users allowed by this license."""
        try :
            return self._f_sslvpn_users
        except Exception as e:
            raise e

    @property
    def f_ica_users(self) :
        """Number of licensed users allowed by ICAONLY license. As long as the AG Feature is licensed,
        unlimited number of ICA connections are accepted.
        (In API, 0 value for this parameter means unlimited when AG license in ON).


        """
        try :
            return self._f_ica_users
        except Exception as e:
            raise e

    @property
    def aaa(self) :
        """AAA."""
        try :
            return self._aaa
        except Exception as e:
            raise e

    @property
    def ospf(self) :
        """OSPF Routing."""
        try :
            return self._ospf
        except Exception as e:
            raise e

    @property
    def rip(self) :
        """RIP Routing."""
        try :
            return self._rip
        except Exception as e:
            raise e

    @property
    def bgp(self) :
        """BGP Routing."""
        try :
            return self._bgp
        except Exception as e:
            raise e

    @property
    def rewrite(self) :
        """Rewrite."""
        try :
            return self._rewrite
        except Exception as e:
            raise e

    @property
    def ipv6pt(self) :
        """IPv6 protocol translation."""
        try :
            return self._ipv6pt
        except Exception as e:
            raise e

    @property
    def appfw(self) :
        """Application Firewall."""
        try :
            return self._appfw
        except Exception as e:
            raise e

    @property
    def responder(self) :
        """Responder."""
        try :
            return self._responder
        except Exception as e:
            raise e

    @property
    def agee(self) :
        """ """
        try :
            return self._agee
        except Exception as e:
            raise e

    @property
    def nsxn(self) :
        """ """
        try :
            return self._nsxn
        except Exception as e:
            raise e

    @property
    def htmlinjection(self) :
        """HTML Injection."""
        try :
            return self._htmlinjection
        except Exception as e:
            raise e

    @property
    def modelid(self) :
        """Model Number ID."""
        try :
            return self._modelid
        except Exception as e:
            raise e

    @property
    def push(self) :
        """NetScaler Push."""
        try :
            return self._push
        except Exception as e:
            raise e

    @property
    def wionns(self) :
        """WI on NS."""
        try :
            return self._wionns
        except Exception as e:
            raise e

    @property
    def appflow(self) :
        """AppFlow."""
        try :
            return self._appflow
        except Exception as e:
            raise e

    @property
    def cloudbridge(self) :
        """CloudBridge."""
        try :
            return self._cloudbridge
        except Exception as e:
            raise e

    @property
    def cloudbridgeappliance(self) :
        """ """
        try :
            return self._cloudbridgeappliance
        except Exception as e:
            raise e

    @property
    def cloudextenderappliance(self) :
        """ """
        try :
            return self._cloudextenderappliance
        except Exception as e:
            raise e

    @property
    def isis(self) :
        """ISIS Routing."""
        try :
            return self._isis
        except Exception as e:
            raise e

    @property
    def cluster(self) :
        """Clustering."""
        try :
            return self._cluster
        except Exception as e:
            raise e

    @property
    def ch(self) :
        """Call Home."""
        try :
            return self._ch
        except Exception as e:
            raise e

    @property
    def appqoe(self) :
        """AppQoS."""
        try :
            return self._appqoe
        except Exception as e:
            raise e

    @property
    def appflowica(self) :
        """Appflow for ICA."""
        try :
            return self._appflowica
        except Exception as e:
            raise e

    @property
    def isstandardlic(self) :
        """Standard License."""
        try :
            return self._isstandardlic
        except Exception as e:
            raise e

    @property
    def isenterpriselic(self) :
        """Enterprise License."""
        try :
            return self._isenterpriselic
        except Exception as e:
            raise e

    @property
    def isplatinumlic(self) :
        """Platinum License."""
        try :
            return self._isplatinumlic
        except Exception as e:
            raise e

    @property
    def rise(self) :
        """RISE."""
        try :
            return self._rise
        except Exception as e:
            raise e

    @property
    def vpath(self) :
        """Vpath."""
        try :
            return self._vpath
        except Exception as e:
            raise e

    @property
    def feo(self) :
        """Front End Optimization."""
        try :
            return self._feo
        except Exception as e:
            raise e

    @property
    def lsn(self) :
        """Large Scale NAT."""
        try :
            return self._lsn
        except Exception as e:
            raise e

    @property
    def rdpproxy(self) :
        """RDPPROXY."""
        try :
            return self._rdpproxy
        except Exception as e:
            raise e

    @property
    def rep(self) :
        """IP Reputation."""
        try :
            return self._rep
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(nslicense_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.nslicense
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
        """Use this API to fetch all the nslicense resources that are configured on netscaler.

        :param client: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            if not name :
                obj = nslicense()
                response = obj.get_resources(client, option_)
            return response
        except Exception as e :
            raise e


class nslicense_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.nslicense = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.nslicense = [nslicense() for _ in range(length)]

