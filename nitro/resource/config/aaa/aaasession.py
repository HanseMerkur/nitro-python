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

class aaasession(base_resource) :
    """Configuration for active connection resource."""
    def __init__(self) :
        self._username = ""
        self._groupname = ""
        self._iip = ""
        self._netmask = ""
        self._all = False
        self._publicip = ""
        self._publicport = 0
        self._ipaddress = ""
        self._port = 0
        self._privateip = ""
        self._privateport = 0
        self._destip = ""
        self._destport = 0
        self._intranetip = ""
        self._intranetip6 = ""
        self._peid = 0
        self.___count = 0

    @property
    def username(self) :
        """Name of the AAA user.<br/>Minimum length =  1."""
        try :
            return self._username
        except Exception as e:
            raise e

    @username.setter
    def username(self, username) :
        """Name of the AAA user.<br/>Minimum length =  1

        :param username: 

        """
        try :
            self._username = username
        except Exception as e:
            raise e

    @property
    def groupname(self) :
        """Name of the AAA group.<br/>Minimum length =  1."""
        try :
            return self._groupname
        except Exception as e:
            raise e

    @groupname.setter
    def groupname(self, groupname) :
        """Name of the AAA group.<br/>Minimum length =  1

        :param groupname: 

        """
        try :
            self._groupname = groupname
        except Exception as e:
            raise e

    @property
    def iip(self) :
        """IP address or the first address in the intranet IP range.<br/>Minimum length =  1."""
        try :
            return self._iip
        except Exception as e:
            raise e

    @iip.setter
    def iip(self, iip) :
        """IP address or the first address in the intranet IP range.<br/>Minimum length =  1

        :param iip: 

        """
        try :
            self._iip = iip
        except Exception as e:
            raise e

    @property
    def netmask(self) :
        """Subnet mask for the intranet IP range.<br/>Minimum length =  1."""
        try :
            return self._netmask
        except Exception as e:
            raise e

    @netmask.setter
    def netmask(self, netmask) :
        """Subnet mask for the intranet IP range.<br/>Minimum length =  1

        :param netmask: 

        """
        try :
            self._netmask = netmask
        except Exception as e:
            raise e

    @property
    def all(self) :
        """Terminate all active AAA-TM/VPN sessions."""
        try :
            return self._all
        except Exception as e:
            raise e

    @all.setter
    def all(self, all) :
        """Terminate all active AAA-TM/VPN sessions.

        :param all: 

        """
        try :
            self._all = all
        except Exception as e:
            raise e

    @property
    def publicip(self) :
        """Client's public IP address."""
        try :
            return self._publicip
        except Exception as e:
            raise e

    @property
    def publicport(self) :
        """Client's public port.<br/>Range 1 - 65535."""
        try :
            return self._publicport
        except Exception as e:
            raise e

    @property
    def ipaddress(self) :
        """NetScaler's IP address."""
        try :
            return self._ipaddress
        except Exception as e:
            raise e

    @property
    def port(self) :
        """NetScaler's port.<br/>Range 1 - 65535."""
        try :
            return self._port
        except Exception as e:
            raise e

    @property
    def privateip(self) :
        """Client's private/mapped IP address."""
        try :
            return self._privateip
        except Exception as e:
            raise e

    @property
    def privateport(self) :
        """Client's private/mapped port.<br/>Range 1 - 65535."""
        try :
            return self._privateport
        except Exception as e:
            raise e

    @property
    def destip(self) :
        """Destination IP address."""
        try :
            return self._destip
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
    def intranetip(self) :
        """Specifies the Intranet IP."""
        try :
            return self._intranetip
        except Exception as e:
            raise e

    @property
    def intranetip6(self) :
        """Specifies the Intranet IP6."""
        try :
            return self._intranetip6
        except Exception as e:
            raise e

    @property
    def peid(self) :
        """Core id of the session owner."""
        try :
            return self._peid
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(aaasession_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.aaasession
        except Exception as e :
            raise e

    def _get_object_name(self) :
        """Returns the value of object identifier argument"""
        try :
            return 0
        except Exception as e :
            raise e



    @classmethod
    def kill(cls, client, resource) :
        """Use this API to kill aaasession.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                killresource = aaasession()
                killresource.username = resource.username
                killresource.groupname = resource.groupname
                killresource.iip = resource.iip
                killresource.netmask = resource.netmask
                killresource.all = resource.all
                return killresource.perform_operation(client,"kill")
            else :
                if (resource and len(resource) > 0) :
                    killresources = [ aaasession() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        killresources[i].username = resource[i].username
                        killresources[i].groupname = resource[i].groupname
                        killresources[i].iip = resource[i].iip
                        killresources[i].netmask = resource[i].netmask
                        killresources[i].all = resource[i].all
                result = cls.perform_operation_bulk_request(client, killresources,"kill")
            return result
        except Exception as e :
            raise e

    @classmethod
    def get(cls, client, name="", option_="") :
        """Use this API to fetch all the aaasession resources that are configured on netscaler.

        :param client: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            if not name :
                obj = aaasession()
                response = obj.get_resources(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def get_args(cls, client, args) :
        """Use this API to fetch all the aaasession resources that are configured on netscaler.
            # This uses aaasession_args which is a way to provide additional arguments while fetching the resources.

        :param client: 
        :param args: 

        """
        try :
            obj = aaasession()
            option_ = options()
            option_.args = nitro_util.object_to_string_withoutquotes(args)
            response = obj.get_resources(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def get_filtered(cls, client, filter_) :
        """Use this API to fetch filtered set of aaasession resources.
        filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = aaasession()
            option_ = options()
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def count(cls, client) :
        """Use this API to count the aaasession resources configured on NetScaler.

        :param client: 

        """
        try :
            obj = aaasession()
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
        """Use this API to count filtered the set of aaasession resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = aaasession()
            option_ = options()
            option_.count = True
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            if response :
                return response[0].__dict__['___count']
            return 0
        except Exception as e :
            raise e


class aaasession_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.aaasession = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.aaasession = [aaasession() for _ in range(length)]

