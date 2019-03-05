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

class nsrpcnode(base_resource) :
    """Configuration for rpc node resource."""
    def __init__(self) :
        self._ipaddress = ""
        self._password = ""
        self._srcip = ""
        self._secure = ""
        self.___count = 0

    @property
    def ipaddress(self) :
        """IP address of the node. This has to be in the same subnet as the NSIP address.<br/>Minimum length =  1."""
        try :
            return self._ipaddress
        except Exception as e:
            raise e

    @ipaddress.setter
    def ipaddress(self, ipaddress) :
        """IP address of the node. This has to be in the same subnet as the NSIP address.<br/>Minimum length =  1

        :param ipaddress: 

        """
        try :
            self._ipaddress = ipaddress
        except Exception as e:
            raise e

    @property
    def password(self) :
        """Password to be used in authentication with the peer system node.<br/>Minimum length =  1."""
        try :
            return self._password
        except Exception as e:
            raise e

    @password.setter
    def password(self, password) :
        """Password to be used in authentication with the peer system node.<br/>Minimum length =  1

        :param password: 

        """
        try :
            self._password = password
        except Exception as e:
            raise e

    @property
    def srcip(self) :
        """Source IP address to be used to communicate with the peer system node. The default value is 0, which means that the appliance uses the NSIP address as the source IP address."""
        try :
            return self._srcip
        except Exception as e:
            raise e

    @srcip.setter
    def srcip(self, srcip) :
        """Source IP address to be used to communicate with the peer system node. The default value is 0, which means that the appliance uses the NSIP address as the source IP address.

        :param srcip: 

        """
        try :
            self._srcip = srcip
        except Exception as e:
            raise e

    @property
    def secure(self) :
        """State of the channel when talking to the node.<br/>Possible values = YES, NO."""
        try :
            return self._secure
        except Exception as e:
            raise e

    @secure.setter
    def secure(self, secure) :
        """State of the channel when talking to the node.<br/>Possible values = YES, NO

        :param secure: 

        """
        try :
            self._secure = secure
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(nsrpcnode_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.nsrpcnode
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
    def update(cls, client, resource) :
        """Use this API to update nsrpcnode.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                updateresource = nsrpcnode()
                updateresource.ipaddress = resource.ipaddress
                updateresource.password = resource.password
                updateresource.srcip = resource.srcip
                updateresource.secure = resource.secure
                return updateresource.update_resource(client)
            else :
                if (resource and len(resource) > 0) :
                    updateresources = [ nsrpcnode() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        updateresources[i].ipaddress = resource[i].ipaddress
                        updateresources[i].password = resource[i].password
                        updateresources[i].srcip = resource[i].srcip
                        updateresources[i].secure = resource[i].secure
                result = cls.update_bulk_request(client, updateresources)
            return result
        except Exception as e :
            raise e

    @classmethod
    def unset(cls, client, resource, args) :
        """Use this API to unset the properties of nsrpcnode resource.
        Properties that need to be unset are specified in args array.

        :param client: 
        :param resource: 
        :param args: 

        """
        try :
            if type(resource) is not list :
                unsetresource = nsrpcnode()
                if type(resource) !=  type(unsetresource):
                    unsetresource.ipaddress = resource
                else :
                    unsetresource.ipaddress = resource.ipaddress
                return unsetresource.unset_resource(client, args)
            else :
                if type(resource[0]) != cls :
                    if (resource and len(resource) > 0) :
                        unsetresources = [ nsrpcnode() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            unsetresources[i].ipaddress = resource[i]
                else :
                    if (resource and len(resource) > 0) :
                        unsetresources = [ nsrpcnode() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            unsetresources[i].ipaddress = resource[i].ipaddress
                result = cls.unset_bulk_request(client, unsetresources, args)
            return result
        except Exception as e :
            raise e

    @classmethod
    def get(cls, client, name="", option_="") :
        """Use this API to fetch all the nsrpcnode resources that are configured on netscaler.

        :param client: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            if not name :
                obj = nsrpcnode()
                response = obj.get_resources(client, option_)
            else :
                if type(name) != cls :
                    if type(name) is not list :
                        obj = nsrpcnode()
                        obj.ipaddress = name
                        response = obj.get_resource(client, option_)
                    else :
                        if name and len(name) > 0 :
                            response = [nsrpcnode() for _ in range(len(name))]
                            obj = [nsrpcnode() for _ in range(len(name))]
                            for i in range(len(name)) :
                                obj[i] = nsrpcnode()
                                obj[i].ipaddress = name[i]
                                response[i] = obj[i].get_resource(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def get_filtered(cls, client, filter_) :
        """Use this API to fetch filtered set of nsrpcnode resources.
        filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = nsrpcnode()
            option_ = options()
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def count(cls, client) :
        """Use this API to count the nsrpcnode resources configured on NetScaler.

        :param client: 

        """
        try :
            obj = nsrpcnode()
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
        """Use this API to count filtered the set of nsrpcnode resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = nsrpcnode()
            option_ = options()
            option_.count = True
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            if response :
                return response[0].__dict__['___count']
            return 0
        except Exception as e :
            raise e


    class Secure:
        """ """
        YES = "YES"
        NO = "NO"

class nsrpcnode_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.nsrpcnode = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.nsrpcnode = [nsrpcnode() for _ in range(length)]

