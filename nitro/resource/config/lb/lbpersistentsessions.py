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

class lbpersistentsessions(base_resource) :
    """Configuration for persistence session resource."""
    def __init__(self) :
        self._vserver = ""
        self._persistenceparameter = ""
        self._type = 0
        self._typestring = ""
        self._srcip = ""
        self._srcipv6 = ""
        self._destip = ""
        self._destipv6 = ""
        self._flags = False
        self._destport = 0
        self._vservername = ""
        self._timeout = 0
        self._referencecount = 0
        self._persistenceparam = ""
        self._cnamepersparam = ""
        self.___count = 0

    @property
    def vserver(self) :
        """The name of the virtual server."""
        try :
            return self._vserver
        except Exception as e:
            raise e

    @vserver.setter
    def vserver(self, vserver) :
        """The name of the virtual server.

        :param vserver: 

        """
        try :
            self._vserver = vserver
        except Exception as e:
            raise e

    @property
    def persistenceparameter(self) :
        """The persistence parameter whose persistence sessions are to be flushed."""
        try :
            return self._persistenceparameter
        except Exception as e:
            raise e

    @persistenceparameter.setter
    def persistenceparameter(self, persistenceparameter) :
        """The persistence parameter whose persistence sessions are to be flushed.

        :param persistenceparameter: 

        """
        try :
            self._persistenceparameter = persistenceparameter
        except Exception as e:
            raise e

    @property
    def type(self) :
        """Type of Persistence."""
        try :
            return self._type
        except Exception as e:
            raise e

    @property
    def typestring(self) :
        """Type of Persistence as String."""
        try :
            return self._typestring
        except Exception as e:
            raise e

    @property
    def srcip(self) :
        """SOURCE IP."""
        try :
            return self._srcip
        except Exception as e:
            raise e

    @property
    def srcipv6(self) :
        """SOURCE IPv6 ADDRESS."""
        try :
            return self._srcipv6
        except Exception as e:
            raise e

    @property
    def destip(self) :
        """DESTINATION IP."""
        try :
            return self._destip
        except Exception as e:
            raise e

    @property
    def destipv6(self) :
        """DESTINATION IPv6 ADDRESS."""
        try :
            return self._destipv6
        except Exception as e:
            raise e

    @property
    def flags(self) :
        """IPv6 FLAGS."""
        try :
            return self._flags
        except Exception as e:
            raise e

    @property
    def destport(self) :
        """Destination port.<br/>Range 1 - 65535."""
        try :
            return self._destport
        except Exception as e:
            raise e

    @property
    def vservername(self) :
        """Virtual server name."""
        try :
            return self._vservername
        except Exception as e:
            raise e

    @property
    def timeout(self) :
        """Persistent Session timeout."""
        try :
            return self._timeout
        except Exception as e:
            raise e

    @property
    def referencecount(self) :
        """Reference Count."""
        try :
            return self._referencecount
        except Exception as e:
            raise e

    @property
    def persistenceparam(self) :
        """Specific persistence information . Callid in case of SIP_CALLID persistence entry , RTSP session id in case of RTSP_SESSIONID persistence entry."""
        try :
            return self._persistenceparam
        except Exception as e:
            raise e

    @property
    def cnamepersparam(self) :
        """The cname that is selected incase of gslb service."""
        try :
            return self._cnamepersparam
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(lbpersistentsessions_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.lbpersistentsessions
        except Exception as e :
            raise e

    def _get_object_name(self) :
        """Returns the value of object identifier argument"""
        try :
            return 0
        except Exception as e :
            raise e



    @classmethod
    def clear(cls, client, resource) :
        """Use this API to clear lbpersistentsessions.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                clearresource = lbpersistentsessions()
                clearresource.vserver = resource.vserver
                clearresource.persistenceparameter = resource.persistenceparameter
                return clearresource.perform_operation(client,"clear")
            else :
                if (resource and len(resource) > 0) :
                    clearresources = [ lbpersistentsessions() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        clearresources[i].vserver = resource[i].vserver
                        clearresources[i].persistenceparameter = resource[i].persistenceparameter
                result = cls.perform_operation_bulk_request(client, clearresources,"clear")
            return result
        except Exception as e :
            raise e

    @classmethod
    def get(cls, client, name="", option_="") :
        """Use this API to fetch all the lbpersistentsessions resources that are configured on netscaler.

        :param client: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            if not name :
                obj = lbpersistentsessions()
                response = obj.get_resources(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def get_args(cls, client, args) :
        """Use this API to fetch all the lbpersistentsessions resources that are configured on netscaler.
            # This uses lbpersistentsessions_args which is a way to provide additional arguments while fetching the resources.

        :param client: 
        :param args: 

        """
        try :
            obj = lbpersistentsessions()
            option_ = options()
            option_.args = nitro_util.object_to_string_withoutquotes(args)
            response = obj.get_resources(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def get_filtered(cls, client, filter_) :
        """Use this API to fetch filtered set of lbpersistentsessions resources.
        filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = lbpersistentsessions()
            option_ = options()
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def count(cls, client) :
        """Use this API to count the lbpersistentsessions resources configured on NetScaler.

        :param client: 

        """
        try :
            obj = lbpersistentsessions()
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
        """Use this API to count filtered the set of lbpersistentsessions resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = lbpersistentsessions()
            option_ = options()
            option_.count = True
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            if response :
                return response[0].__dict__['___count']
            return 0
        except Exception as e :
            raise e


class lbpersistentsessions_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.lbpersistentsessions = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.lbpersistentsessions = [lbpersistentsessions() for _ in range(length)]

