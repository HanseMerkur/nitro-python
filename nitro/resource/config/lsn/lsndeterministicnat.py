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

class lsndeterministicnat(base_resource) :
    """Configuration for deterministic NAT resource."""
    def __init__(self) :
        self._clientname = ""
        self._network6 = ""
        self._subscrip = ""
        self._td = 0
        self._natip = ""
        self._natprefix = ""
        self._subscrip2 = ""
        self._natip2 = ""
        self._firstport = 0
        self._lastport = 0
        self._srctd = 0
        self._nattype = ""
        self.___count = 0

    @property
    def clientname(self) :
        """The name of the LSN Client."""
        try :
            return self._clientname
        except Exception as e:
            raise e

    @clientname.setter
    def clientname(self, clientname) :
        """The name of the LSN Client.

        :param clientname: 

        """
        try :
            self._clientname = clientname
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
    def subscrip(self) :
        """The Client IP address."""
        try :
            return self._subscrip
        except Exception as e:
            raise e

    @subscrip.setter
    def subscrip(self, subscrip) :
        """The Client IP address.

        :param subscrip: 

        """
        try :
            self._subscrip = subscrip
        except Exception as e:
            raise e

    @property
    def td(self) :
        """The LSN client TD.<br/>Default value: 0<br/>Maximum length =  4094."""
        try :
            return self._td
        except Exception as e:
            raise e

    @td.setter
    def td(self, td) :
        """The LSN client TD.<br/>Default value: 0<br/>Maximum length =  4094

        :param td: 

        """
        try :
            self._td = td
        except Exception as e:
            raise e

    @property
    def natip(self) :
        """The NAT IP address.<br/>Minimum length =  1."""
        try :
            return self._natip
        except Exception as e:
            raise e

    @natip.setter
    def natip(self, natip) :
        """The NAT IP address.<br/>Minimum length =  1

        :param natip: 

        """
        try :
            self._natip = natip
        except Exception as e:
            raise e

    @property
    def natprefix(self) :
        """IPv6 address of the LSN  subscriber network(B4-Device) on whose traffic the NetScaler ADC perform Large Scale NAT."""
        try :
            return self._natprefix
        except Exception as e:
            raise e

    @property
    def subscrip2(self) :
        """The Subscriber IP address."""
        try :
            return self._subscrip2
        except Exception as e:
            raise e

    @property
    def natip2(self) :
        """The NAT IP address."""
        try :
            return self._natip2
        except Exception as e:
            raise e

    @property
    def firstport(self) :
        """The Application Protocol Port of the Profile.<br/>Minimum value =  1<br/>Maximum value =  65535."""
        try :
            return self._firstport
        except Exception as e:
            raise e

    @property
    def lastport(self) :
        """The Application Protocol Ending Port of the Profile.<br/>Minimum value =  1<br/>Maximum value =  65535."""
        try :
            return self._lastport
        except Exception as e:
            raise e

    @property
    def srctd(self) :
        """The LSN client TD.<br/>Minimum value =  0<br/>Maximum value =  4094."""
        try :
            return self._srctd
        except Exception as e:
            raise e

    @property
    def nattype(self) :
        """Type of subscriber info(ex: nat44 or ds-lite).<br/>Default value: NAT44<br/>Possible values = NAT44, DS-Lite."""
        try :
            return self._nattype
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(lsndeterministicnat_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.lsndeterministicnat
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
        """Use this API to fetch all the lsndeterministicnat resources that are configured on netscaler.

        :param client: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            if not name :
                obj = lsndeterministicnat()
                response = obj.get_resources(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def get_args(cls, client, args) :
        """Use this API to fetch all the lsndeterministicnat resources that are configured on netscaler.
            # This uses lsndeterministicnat_args which is a way to provide additional arguments while fetching the resources.

        :param client: 
        :param args: 

        """
        try :
            obj = lsndeterministicnat()
            option_ = options()
            option_.args = nitro_util.object_to_string_withoutquotes(args)
            response = obj.get_resources(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def get_filtered(cls, client, filter_) :
        """Use this API to fetch filtered set of lsndeterministicnat resources.
        filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = lsndeterministicnat()
            option_ = options()
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def count(cls, client) :
        """Use this API to count the lsndeterministicnat resources configured on NetScaler.

        :param client: 

        """
        try :
            obj = lsndeterministicnat()
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
        """Use this API to count filtered the set of lsndeterministicnat resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = lsndeterministicnat()
            option_ = options()
            option_.count = True
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            if response :
                return response[0].__dict__['___count']
            return 0
        except Exception as e :
            raise e


    class Nattype:
        """ """
        NAT44 = "NAT44"
        DS_Lite = "DS-Lite"

class lsndeterministicnat_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.lsndeterministicnat = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.lsndeterministicnat = [lsndeterministicnat() for _ in range(length)]

