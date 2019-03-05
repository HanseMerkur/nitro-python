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

class nd6ravariables(base_resource) :
    """Configuration for nd6 Router Advertisment configuration variables resource."""
    def __init__(self) :
        self._vlan = 0
        self._ceaserouteradv = ""
        self._sendrouteradv = ""
        self._srclinklayeraddroption = ""
        self._onlyunicastrtadvresponse = ""
        self._managedaddrconfig = ""
        self._otheraddrconfig = ""
        self._currhoplimit = 0
        self._maxrtadvinterval = 0
        self._minrtadvinterval = 0
        self._linkmtu = 0
        self._reachabletime = 0
        self._retranstime = 0
        self._defaultlifetime = 0
        self._lastrtadvtime = 0
        self._nextrtadvdelay = 0
        self.___count = 0

    @property
    def vlan(self) :
        """The VLAN number.<br/>Maximum length =  4094."""
        try :
            return self._vlan
        except Exception as e:
            raise e

    @vlan.setter
    def vlan(self, vlan) :
        """The VLAN number.<br/>Maximum length =  4094

        :param vlan: 

        """
        try :
            self._vlan = vlan
        except Exception as e:
            raise e

    @property
    def ceaserouteradv(self) :
        """Cease router advertisements on this vlan.<br/>Default value: NO<br/>Possible values = YES, NO."""
        try :
            return self._ceaserouteradv
        except Exception as e:
            raise e

    @ceaserouteradv.setter
    def ceaserouteradv(self, ceaserouteradv) :
        """Cease router advertisements on this vlan.<br/>Default value: NO<br/>Possible values = YES, NO

        :param ceaserouteradv: 

        """
        try :
            self._ceaserouteradv = ceaserouteradv
        except Exception as e:
            raise e

    @property
    def sendrouteradv(self) :
        """whether the router sends periodic RAs and responds to Router Solicitations.<br/>Default value: NO<br/>Possible values = YES, NO."""
        try :
            return self._sendrouteradv
        except Exception as e:
            raise e

    @sendrouteradv.setter
    def sendrouteradv(self, sendrouteradv) :
        """whether the router sends periodic RAs and responds to Router Solicitations.<br/>Default value: NO<br/>Possible values = YES, NO

        :param sendrouteradv: 

        """
        try :
            self._sendrouteradv = sendrouteradv
        except Exception as e:
            raise e

    @property
    def srclinklayeraddroption(self) :
        """Include source link layer address option in RA messages.<br/>Default value: YES<br/>Possible values = YES, NO."""
        try :
            return self._srclinklayeraddroption
        except Exception as e:
            raise e

    @srclinklayeraddroption.setter
    def srclinklayeraddroption(self, srclinklayeraddroption) :
        """Include source link layer address option in RA messages.<br/>Default value: YES<br/>Possible values = YES, NO

        :param srclinklayeraddroption: 

        """
        try :
            self._srclinklayeraddroption = srclinklayeraddroption
        except Exception as e:
            raise e

    @property
    def onlyunicastrtadvresponse(self) :
        """Send only Unicast Router Advertisements in respond to Router Solicitations.<br/>Default value: NO<br/>Possible values = YES, NO."""
        try :
            return self._onlyunicastrtadvresponse
        except Exception as e:
            raise e

    @onlyunicastrtadvresponse.setter
    def onlyunicastrtadvresponse(self, onlyunicastrtadvresponse) :
        """Send only Unicast Router Advertisements in respond to Router Solicitations.<br/>Default value: NO<br/>Possible values = YES, NO

        :param onlyunicastrtadvresponse: 

        """
        try :
            self._onlyunicastrtadvresponse = onlyunicastrtadvresponse
        except Exception as e:
            raise e

    @property
    def managedaddrconfig(self) :
        """Value to be placed in the Managed address configuration flag field.<br/>Default value: NO<br/>Possible values = YES, NO."""
        try :
            return self._managedaddrconfig
        except Exception as e:
            raise e

    @managedaddrconfig.setter
    def managedaddrconfig(self, managedaddrconfig) :
        """Value to be placed in the Managed address configuration flag field.<br/>Default value: NO<br/>Possible values = YES, NO

        :param managedaddrconfig: 

        """
        try :
            self._managedaddrconfig = managedaddrconfig
        except Exception as e:
            raise e

    @property
    def otheraddrconfig(self) :
        """Value to be placed in the Other configuration flag field.<br/>Default value: NO<br/>Possible values = YES, NO."""
        try :
            return self._otheraddrconfig
        except Exception as e:
            raise e

    @otheraddrconfig.setter
    def otheraddrconfig(self, otheraddrconfig) :
        """Value to be placed in the Other configuration flag field.<br/>Default value: NO<br/>Possible values = YES, NO

        :param otheraddrconfig: 

        """
        try :
            self._otheraddrconfig = otheraddrconfig
        except Exception as e:
            raise e

    @property
    def currhoplimit(self) :
        """Current Hop limit.<br/>Default value: 64<br/>Maximum length =  255."""
        try :
            return self._currhoplimit
        except Exception as e:
            raise e

    @currhoplimit.setter
    def currhoplimit(self, currhoplimit) :
        """Current Hop limit.<br/>Default value: 64<br/>Maximum length =  255

        :param currhoplimit: 

        """
        try :
            self._currhoplimit = currhoplimit
        except Exception as e:
            raise e

    @property
    def maxrtadvinterval(self) :
        """Maximum time allowed between unsolicited multicast RAs, in seconds.<br/>Default value: 600<br/>Minimum length =  4<br/>Maximum length =  1800."""
        try :
            return self._maxrtadvinterval
        except Exception as e:
            raise e

    @maxrtadvinterval.setter
    def maxrtadvinterval(self, maxrtadvinterval) :
        """Maximum time allowed between unsolicited multicast RAs, in seconds.<br/>Default value: 600<br/>Minimum length =  4<br/>Maximum length =  1800

        :param maxrtadvinterval: 

        """
        try :
            self._maxrtadvinterval = maxrtadvinterval
        except Exception as e:
            raise e

    @property
    def minrtadvinterval(self) :
        """Minimum time interval between RA messages, in seconds.<br/>Default value: 198<br/>Minimum length =  3<br/>Maximum length =  1350."""
        try :
            return self._minrtadvinterval
        except Exception as e:
            raise e

    @minrtadvinterval.setter
    def minrtadvinterval(self, minrtadvinterval) :
        """Minimum time interval between RA messages, in seconds.<br/>Default value: 198<br/>Minimum length =  3<br/>Maximum length =  1350

        :param minrtadvinterval: 

        """
        try :
            self._minrtadvinterval = minrtadvinterval
        except Exception as e:
            raise e

    @property
    def linkmtu(self) :
        """The Link MTU.<br/>Default value: 0<br/>Maximum length =  1500."""
        try :
            return self._linkmtu
        except Exception as e:
            raise e

    @linkmtu.setter
    def linkmtu(self, linkmtu) :
        """The Link MTU.<br/>Default value: 0<br/>Maximum length =  1500

        :param linkmtu: 

        """
        try :
            self._linkmtu = linkmtu
        except Exception as e:
            raise e

    @property
    def reachabletime(self) :
        """Reachable time, in milliseconds.<br/>Default value: 0<br/>Maximum length =  3600000."""
        try :
            return self._reachabletime
        except Exception as e:
            raise e

    @reachabletime.setter
    def reachabletime(self, reachabletime) :
        """Reachable time, in milliseconds.<br/>Default value: 0<br/>Maximum length =  3600000

        :param reachabletime: 

        """
        try :
            self._reachabletime = reachabletime
        except Exception as e:
            raise e

    @property
    def retranstime(self) :
        """Retransmission time, in milliseconds.<br/>Default value: 0."""
        try :
            return self._retranstime
        except Exception as e:
            raise e

    @retranstime.setter
    def retranstime(self, retranstime) :
        """Retransmission time, in milliseconds.<br/>Default value: 0

        :param retranstime: 

        """
        try :
            self._retranstime = retranstime
        except Exception as e:
            raise e

    @property
    def defaultlifetime(self) :
        """Default life time, in seconds.<br/>Default value: 1800<br/>Maximum length =  9000."""
        try :
            return self._defaultlifetime
        except Exception as e:
            raise e

    @defaultlifetime.setter
    def defaultlifetime(self, defaultlifetime) :
        """Default life time, in seconds.<br/>Default value: 1800<br/>Maximum length =  9000

        :param defaultlifetime: 

        """
        try :
            self._defaultlifetime = defaultlifetime
        except Exception as e:
            raise e

    @property
    def lastrtadvtime(self) :
        """Last RA sent timestamp."""
        try :
            return self._lastrtadvtime
        except Exception as e:
            raise e

    @property
    def nextrtadvdelay(self) :
        """Next RA delay."""
        try :
            return self._nextrtadvdelay
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(nd6ravariables_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.nd6ravariables
        except Exception as e :
            raise e

    def _get_object_name(self) :
        """Returns the value of object identifier argument"""
        try :
            if self.vlan is not None :
                return str(self.vlan)
            return None
        except Exception as e :
            raise e



    @classmethod
    def update(cls, client, resource) :
        """Use this API to update nd6ravariables.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                updateresource = nd6ravariables()
                updateresource.vlan = resource.vlan
                updateresource.ceaserouteradv = resource.ceaserouteradv
                updateresource.sendrouteradv = resource.sendrouteradv
                updateresource.srclinklayeraddroption = resource.srclinklayeraddroption
                updateresource.onlyunicastrtadvresponse = resource.onlyunicastrtadvresponse
                updateresource.managedaddrconfig = resource.managedaddrconfig
                updateresource.otheraddrconfig = resource.otheraddrconfig
                updateresource.currhoplimit = resource.currhoplimit
                updateresource.maxrtadvinterval = resource.maxrtadvinterval
                updateresource.minrtadvinterval = resource.minrtadvinterval
                updateresource.linkmtu = resource.linkmtu
                updateresource.reachabletime = resource.reachabletime
                updateresource.retranstime = resource.retranstime
                updateresource.defaultlifetime = resource.defaultlifetime
                return updateresource.update_resource(client)
            else :
                if (resource and len(resource) > 0) :
                    updateresources = [ nd6ravariables() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        updateresources[i].vlan = resource[i].vlan
                        updateresources[i].ceaserouteradv = resource[i].ceaserouteradv
                        updateresources[i].sendrouteradv = resource[i].sendrouteradv
                        updateresources[i].srclinklayeraddroption = resource[i].srclinklayeraddroption
                        updateresources[i].onlyunicastrtadvresponse = resource[i].onlyunicastrtadvresponse
                        updateresources[i].managedaddrconfig = resource[i].managedaddrconfig
                        updateresources[i].otheraddrconfig = resource[i].otheraddrconfig
                        updateresources[i].currhoplimit = resource[i].currhoplimit
                        updateresources[i].maxrtadvinterval = resource[i].maxrtadvinterval
                        updateresources[i].minrtadvinterval = resource[i].minrtadvinterval
                        updateresources[i].linkmtu = resource[i].linkmtu
                        updateresources[i].reachabletime = resource[i].reachabletime
                        updateresources[i].retranstime = resource[i].retranstime
                        updateresources[i].defaultlifetime = resource[i].defaultlifetime
                result = cls.update_bulk_request(client, updateresources)
            return result
        except Exception as e :
            raise e

    @classmethod
    def unset(cls, client, resource, args) :
        """Use this API to unset the properties of nd6ravariables resource.
        Properties that need to be unset are specified in args array.

        :param client: 
        :param resource: 
        :param args: 

        """
        try :
            if type(resource) is not list :
                unsetresource = nd6ravariables()
                if type(resource) !=  type(unsetresource):
                    unsetresource.vlan = resource
                else :
                    unsetresource.vlan = resource.vlan
                return unsetresource.unset_resource(client, args)
            else :
                if type(resource[0]) != cls :
                    if (resource and len(resource) > 0) :
                        unsetresources = [ nd6ravariables() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            unsetresources[i].vlan = resource[i]
                else :
                    if (resource and len(resource) > 0) :
                        unsetresources = [ nd6ravariables() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            unsetresources[i].vlan = resource[i].vlan
                result = cls.unset_bulk_request(client, unsetresources, args)
            return result
        except Exception as e :
            raise e

    @classmethod
    def get(cls, client, name="", option_="") :
        """Use this API to fetch all the nd6ravariables resources that are configured on netscaler.

        :param client: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            if not name :
                obj = nd6ravariables()
                response = obj.get_resources(client, option_)
            else :
                if type(name) != cls :
                    if type(name) is not list :
                        obj = nd6ravariables()
                        obj.vlan = name
                        response = obj.get_resource(client, option_)
                    else :
                        if name and len(name) > 0 :
                            response = [nd6ravariables() for _ in range(len(name))]
                            obj = [nd6ravariables() for _ in range(len(name))]
                            for i in range(len(name)) :
                                obj[i] = nd6ravariables()
                                obj[i].vlan = name[i]
                                response[i] = obj[i].get_resource(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def get_filtered(cls, client, filter_) :
        """Use this API to fetch filtered set of nd6ravariables resources.
        filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = nd6ravariables()
            option_ = options()
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def count(cls, client) :
        """Use this API to count the nd6ravariables resources configured on NetScaler.

        :param client: 

        """
        try :
            obj = nd6ravariables()
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
        """Use this API to count filtered the set of nd6ravariables resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = nd6ravariables()
            option_ = options()
            option_.count = True
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            if response :
                return response[0].__dict__['___count']
            return 0
        except Exception as e :
            raise e


    class Managedaddrconfig:
        """ """
        YES = "YES"
        NO = "NO"

    class Onlyunicastrtadvresponse:
        """ """
        YES = "YES"
        NO = "NO"

    class Sendrouteradv:
        """ """
        YES = "YES"
        NO = "NO"

    class Otheraddrconfig:
        """ """
        YES = "YES"
        NO = "NO"

    class Srclinklayeraddroption:
        """ """
        YES = "YES"
        NO = "NO"

    class Ceaserouteradv:
        """ """
        YES = "YES"
        NO = "NO"

class nd6ravariables_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.nd6ravariables = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.nd6ravariables = [nd6ravariables() for _ in range(length)]

