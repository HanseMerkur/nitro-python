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

class l2param(base_resource) :
    """Configuration for Layer 2 related parameter resource."""
    def __init__(self) :
        self._mbfpeermacupdate = 0
        self._maxbridgecollision = 0
        self._bdggrpproxyarp = ""
        self._bdgsetting = ""
        self._garponvridintf = ""
        self._macmodefwdmypkt = ""
        self._usemymac = ""
        self._proxyarp = ""
        self._garpreply = ""
        self._mbfinstlearning = ""
        self._rstintfonhafo = ""
        self._skipproxyingbsdtraffic = ""
        self._returntoethernetsender = ""
        self._stopmacmoveupdate = ""

    @property
    def mbfpeermacupdate(self) :
        """When mbf_instant_learning is enabled, learn any changes in peer's MAC after this time interval, which is in 10ms ticks.<br/>Default value: 10."""
        try :
            return self._mbfpeermacupdate
        except Exception as e:
            raise e

    @mbfpeermacupdate.setter
    def mbfpeermacupdate(self, mbfpeermacupdate) :
        """When mbf_instant_learning is enabled, learn any changes in peer's MAC after this time interval, which is in 10ms ticks.<br/>Default value: 10

        :param mbfpeermacupdate: 

        """
        try :
            self._mbfpeermacupdate = mbfpeermacupdate
        except Exception as e:
            raise e

    @property
    def maxbridgecollision(self) :
        """Maximum bridge collision for loop detection .<br/>Default value: 20."""
        try :
            return self._maxbridgecollision
        except Exception as e:
            raise e

    @maxbridgecollision.setter
    def maxbridgecollision(self, maxbridgecollision) :
        """Maximum bridge collision for loop detection .<br/>Default value: 20

        :param maxbridgecollision: 

        """
        try :
            self._maxbridgecollision = maxbridgecollision
        except Exception as e:
            raise e

    @property
    def bdggrpproxyarp(self) :
        """Set/reset proxy ARP in bridge group deployment.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._bdggrpproxyarp
        except Exception as e:
            raise e

    @bdggrpproxyarp.setter
    def bdggrpproxyarp(self, bdggrpproxyarp) :
        """Set/reset proxy ARP in bridge group deployment.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED

        :param bdggrpproxyarp: 

        """
        try :
            self._bdggrpproxyarp = bdggrpproxyarp
        except Exception as e:
            raise e

    @property
    def bdgsetting(self) :
        """Bridging settings for C2C behavior.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._bdgsetting
        except Exception as e:
            raise e

    @bdgsetting.setter
    def bdgsetting(self, bdgsetting) :
        """Bridging settings for C2C behavior.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED

        :param bdgsetting: 

        """
        try :
            self._bdgsetting = bdgsetting
        except Exception as e:
            raise e

    @property
    def garponvridintf(self) :
        """Send GARP messagess on VRID-configured interfaces upon failover .<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._garponvridintf
        except Exception as e:
            raise e

    @garponvridintf.setter
    def garponvridintf(self, garponvridintf) :
        """Send GARP messagess on VRID-configured interfaces upon failover .<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED

        :param garponvridintf: 

        """
        try :
            self._garponvridintf = garponvridintf
        except Exception as e:
            raise e

    @property
    def macmodefwdmypkt(self) :
        """MAC mode vserver forward packets destined to VIPs.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._macmodefwdmypkt
        except Exception as e:
            raise e

    @macmodefwdmypkt.setter
    def macmodefwdmypkt(self, macmodefwdmypkt) :
        """MAC mode vserver forward packets destined to VIPs.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED

        :param macmodefwdmypkt: 

        """
        try :
            self._macmodefwdmypkt = macmodefwdmypkt
        except Exception as e:
            raise e

    @property
    def usemymac(self) :
        """Set/reset cfg_use_my_mac .<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._usemymac
        except Exception as e:
            raise e

    @usemymac.setter
    def usemymac(self, usemymac) :
        """Set/reset cfg_use_my_mac .<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED

        :param usemymac: 

        """
        try :
            self._usemymac = usemymac
        except Exception as e:
            raise e

    @property
    def proxyarp(self) :
        """Set/reset cfg_proxy_arp_dr .<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._proxyarp
        except Exception as e:
            raise e

    @proxyarp.setter
    def proxyarp(self, proxyarp) :
        """Set/reset cfg_proxy_arp_dr .<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED

        :param proxyarp: 

        """
        try :
            self._proxyarp = proxyarp
        except Exception as e:
            raise e

    @property
    def garpreply(self) :
        """Set/reset REPLY form of GARP .<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._garpreply
        except Exception as e:
            raise e

    @garpreply.setter
    def garpreply(self, garpreply) :
        """Set/reset REPLY form of GARP .<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED

        :param garpreply: 

        """
        try :
            self._garpreply = garpreply
        except Exception as e:
            raise e

    @property
    def mbfinstlearning(self) :
        """Enable instant learning of MAC changes in MBF mode.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._mbfinstlearning
        except Exception as e:
            raise e

    @mbfinstlearning.setter
    def mbfinstlearning(self, mbfinstlearning) :
        """Enable instant learning of MAC changes in MBF mode.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED

        :param mbfinstlearning: 

        """
        try :
            self._mbfinstlearning = mbfinstlearning
        except Exception as e:
            raise e

    @property
    def rstintfonhafo(self) :
        """Enable the reset interface upon HA failover.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._rstintfonhafo
        except Exception as e:
            raise e

    @rstintfonhafo.setter
    def rstintfonhafo(self, rstintfonhafo) :
        """Enable the reset interface upon HA failover.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED

        :param rstintfonhafo: 

        """
        try :
            self._rstintfonhafo = rstintfonhafo
        except Exception as e:
            raise e

    @property
    def skipproxyingbsdtraffic(self) :
        """Enable the proxying of FreeBSD traffic.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._skipproxyingbsdtraffic
        except Exception as e:
            raise e

    @skipproxyingbsdtraffic.setter
    def skipproxyingbsdtraffic(self, skipproxyingbsdtraffic) :
        """Enable the proxying of FreeBSD traffic.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED

        :param skipproxyingbsdtraffic: 

        """
        try :
            self._skipproxyingbsdtraffic = skipproxyingbsdtraffic
        except Exception as e:
            raise e

    @property
    def returntoethernetsender(self) :
        """ """
        try :
            return self._returntoethernetsender
        except Exception as e:
            raise e

    @returntoethernetsender.setter
    def returntoethernetsender(self, returntoethernetsender) :
        """

        :param returntoethernetsender: 

        """
        try :
            self._returntoethernetsender = returntoethernetsender
        except Exception as e:
            raise e

    @property
    def stopmacmoveupdate(self) :
        """Stop propagation of server mac change to natpcbs.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._stopmacmoveupdate
        except Exception as e:
            raise e

    @stopmacmoveupdate.setter
    def stopmacmoveupdate(self, stopmacmoveupdate) :
        """Stop propagation of server mac change to natpcbs.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED

        :param stopmacmoveupdate: 

        """
        try :
            self._stopmacmoveupdate = stopmacmoveupdate
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(l2param_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.l2param
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
        """Use this API to update l2param.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                updateresource = l2param()
                updateresource.mbfpeermacupdate = resource.mbfpeermacupdate
                updateresource.maxbridgecollision = resource.maxbridgecollision
                updateresource.bdggrpproxyarp = resource.bdggrpproxyarp
                updateresource.bdgsetting = resource.bdgsetting
                updateresource.garponvridintf = resource.garponvridintf
                updateresource.macmodefwdmypkt = resource.macmodefwdmypkt
                updateresource.usemymac = resource.usemymac
                updateresource.proxyarp = resource.proxyarp
                updateresource.garpreply = resource.garpreply
                updateresource.mbfinstlearning = resource.mbfinstlearning
                updateresource.rstintfonhafo = resource.rstintfonhafo
                updateresource.skipproxyingbsdtraffic = resource.skipproxyingbsdtraffic
                updateresource.returntoethernetsender = resource.returntoethernetsender
                updateresource.stopmacmoveupdate = resource.stopmacmoveupdate
                return updateresource.update_resource(client)
        except Exception as e :
            raise e

    @classmethod
    def unset(cls, client, resource, args) :
        """Use this API to unset the properties of l2param resource.
        Properties that need to be unset are specified in args array.

        :param client: 
        :param resource: 
        :param args: 

        """
        try :
            if type(resource) is not list :
                unsetresource = l2param()
                return unsetresource.unset_resource(client, args)
        except Exception as e :
            raise e

    @classmethod
    def get(cls, client, name="", option_="") :
        """Use this API to fetch all the l2param resources that are configured on netscaler.

        :param client: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            if not name :
                obj = l2param()
                response = obj.get_resources(client, option_)
            return response
        except Exception as e :
            raise e


    class Proxyarp:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Usemymac:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Bdgsetting:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Returntoethernetsender:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Rstintfonhafo:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Mbfinstlearning:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Macmodefwdmypkt:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Bdggrpproxyarp:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Garponvridintf:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Garpreply:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Skipproxyingbsdtraffic:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Stopmacmoveupdate:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

class l2param_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.l2param = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.l2param = [l2param() for _ in range(length)]

