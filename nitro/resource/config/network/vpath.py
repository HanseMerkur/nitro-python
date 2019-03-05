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

class vpath(base_resource) :
    """Configuration for Vpath resource."""
    def __init__(self) :
        self._name = ""
        self._destip = ""
        self._netmask = ""
        self._gateway = ""
        self.___count = 0

    @property
    def name(self) :
        """Name for the vPath. Must begin with a letter, number, or the underscore character (_), and can consist of letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at sign (@), equals (=), colon (:), and underscore characters. Cannot be changed after the profile is created. Choose a name that helps identify the net profile.<br/>Minimum length =  1."""
        try :
            return self._name
        except Exception as e:
            raise e

    @name.setter
    def name(self, name) :
        """Name for the vPath. Must begin with a letter, number, or the underscore character (_), and can consist of letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at sign (@), equals (=), colon (:), and underscore characters. Cannot be changed after the profile is created. Choose a name that helps identify the net profile.<br/>Minimum length =  1

        :param name: 

        """
        try :
            self._name = name
        except Exception as e:
            raise e

    @property
    def destip(self) :
        """This is the destination ip, where vPath encapsulated packets needs to be sent.<br/>Minimum length =  1."""
        try :
            return self._destip
        except Exception as e:
            raise e

    @destip.setter
    def destip(self, destip) :
        """This is the destination ip, where vPath encapsulated packets needs to be sent.<br/>Minimum length =  1

        :param destip: 

        """
        try :
            self._destip = destip
        except Exception as e:
            raise e

    @property
    def netmask(self) :
        """Subnet mask associated with the destination network."""
        try :
            return self._netmask
        except Exception as e:
            raise e

    @netmask.setter
    def netmask(self, netmask) :
        """Subnet mask associated with the destination network.

        :param netmask: 

        """
        try :
            self._netmask = netmask
        except Exception as e:
            raise e

    @property
    def gateway(self) :
        """Next hop gateway to reach the destination address."""
        try :
            return self._gateway
        except Exception as e:
            raise e

    @gateway.setter
    def gateway(self, gateway) :
        """Next hop gateway to reach the destination address.

        :param gateway: 

        """
        try :
            self._gateway = gateway
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(vpath_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.vpath
        except Exception as e :
            raise e

    def _get_object_name(self) :
        """Returns the value of object identifier argument"""
        try :
            if self.name is not None :
                return str(self.name)
            return None
        except Exception as e :
            raise e



    @classmethod
    def add(cls, client, resource) :
        """Use this API to add vpath.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                addresource = vpath()
                addresource.name = resource.name
                addresource.destip = resource.destip
                addresource.netmask = resource.netmask
                addresource.gateway = resource.gateway
                return addresource.add_resource(client)
            else :
                if (resource and len(resource) > 0) :
                    addresources = [ vpath() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        addresources[i].name = resource[i].name
                        addresources[i].destip = resource[i].destip
                        addresources[i].netmask = resource[i].netmask
                        addresources[i].gateway = resource[i].gateway
                result = cls.add_bulk_request(client, addresources)
            return result
        except Exception as e :
            raise e

    @classmethod
    def delete(cls, client, resource) :
        """Use this API to delete vpath.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                deleteresource = vpath()
                if type(resource) !=  type(deleteresource):
                    deleteresource.name = resource
                else :
                    deleteresource.name = resource.name
                return deleteresource.delete_resource(client)
            else :
                if type(resource[0]) != cls :
                    if (resource and len(resource) > 0) :
                        deleteresources = [ vpath() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            deleteresources[i].name = resource[i]
                else :
                    if (resource and len(resource) > 0) :
                        deleteresources = [ vpath() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            deleteresources[i].name = resource[i].name
                result = cls.delete_bulk_request(client, deleteresources)
            return result
        except Exception as e :
            raise e

    @classmethod
    def get(cls, client, name="", option_="") :
        """Use this API to fetch all the vpath resources that are configured on netscaler.

        :param client: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            if not name :
                obj = vpath()
                response = obj.get_resources(client, option_)
            else :
                if type(name) != cls :
                    if type(name) is not list :
                        obj = vpath()
                        obj.name = name
                        response = obj.get_resource(client, option_)
                    else :
                        if name and len(name) > 0 :
                            response = [vpath() for _ in range(len(name))]
                            obj = [vpath() for _ in range(len(name))]
                            for i in range(len(name)) :
                                obj[i] = vpath()
                                obj[i].name = name[i]
                                response[i] = obj[i].get_resource(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def get_filtered(cls, client, filter_) :
        """Use this API to fetch filtered set of vpath resources.
        filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = vpath()
            option_ = options()
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def count(cls, client) :
        """Use this API to count the vpath resources configured on NetScaler.

        :param client: 

        """
        try :
            obj = vpath()
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
        """Use this API to count filtered the set of vpath resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = vpath()
            option_ = options()
            option_.count = True
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            if response :
                return response[0].__dict__['___count']
            return 0
        except Exception as e :
            raise e


class vpath_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.vpath = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.vpath = [vpath() for _ in range(length)]

