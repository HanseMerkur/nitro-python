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

class nsappflowcollector(base_resource) :
    """Configuration for appflowCollector resource."""
    def __init__(self) :
        self._name = ""
        self._ipaddress = ""
        self._port = 0
        self.___count = 0

    @property
    def name(self) :
        """Name of the AppFlow collector.<br/>Minimum length =  1<br/>Maximum length =  127."""
        try :
            return self._name
        except Exception as e:
            raise e

    @name.setter
    def name(self, name) :
        """Name of the AppFlow collector.<br/>Minimum length =  1<br/>Maximum length =  127

        :param name: 

        """
        try :
            self._name = name
        except Exception as e:
            raise e

    @property
    def ipaddress(self) :
        """The IPv4 address of the AppFlow collector."""
        try :
            return self._ipaddress
        except Exception as e:
            raise e

    @ipaddress.setter
    def ipaddress(self, ipaddress) :
        """The IPv4 address of the AppFlow collector.

        :param ipaddress: 

        """
        try :
            self._ipaddress = ipaddress
        except Exception as e:
            raise e

    @property
    def port(self) :
        """The UDP port on which the AppFlow collector is listening.<br/>Default value: 4739."""
        try :
            return self._port
        except Exception as e:
            raise e

    @port.setter
    def port(self, port) :
        """The UDP port on which the AppFlow collector is listening.<br/>Default value: 4739

        :param port: 

        """
        try :
            self._port = port
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(nsappflowcollector_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.nsappflowcollector
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
        """Use this API to add nsappflowcollector.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                addresource = nsappflowcollector()
                addresource.name = resource.name
                addresource.ipaddress = resource.ipaddress
                addresource.port = resource.port
                return addresource.add_resource(client)
            else :
                if (resource and len(resource) > 0) :
                    addresources = [ nsappflowcollector() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        addresources[i].name = resource[i].name
                        addresources[i].ipaddress = resource[i].ipaddress
                        addresources[i].port = resource[i].port
                result = cls.add_bulk_request(client, addresources)
            return result
        except Exception as e :
            raise e

    @classmethod
    def delete(cls, client, resource) :
        """Use this API to delete nsappflowcollector.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                deleteresource = nsappflowcollector()
                if type(resource) !=  type(deleteresource):
                    deleteresource.name = resource
                else :
                    deleteresource.name = resource.name
                return deleteresource.delete_resource(client)
            else :
                if type(resource[0]) != cls :
                    if (resource and len(resource) > 0) :
                        deleteresources = [ nsappflowcollector() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            deleteresources[i].name = resource[i]
                else :
                    if (resource and len(resource) > 0) :
                        deleteresources = [ nsappflowcollector() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            deleteresources[i].name = resource[i].name
                result = cls.delete_bulk_request(client, deleteresources)
            return result
        except Exception as e :
            raise e

    @classmethod
    def get(cls, client, name="", option_="") :
        """Use this API to fetch all the nsappflowcollector resources that are configured on netscaler.

        :param client: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            if not name :
                obj = nsappflowcollector()
                response = obj.get_resources(client, option_)
            else :
                if type(name) != cls :
                    if type(name) is not list :
                        obj = nsappflowcollector()
                        obj.name = name
                        response = obj.get_resource(client, option_)
                    else :
                        if name and len(name) > 0 :
                            response = [nsappflowcollector() for _ in range(len(name))]
                            obj = [nsappflowcollector() for _ in range(len(name))]
                            for i in range(len(name)) :
                                obj[i] = nsappflowcollector()
                                obj[i].name = name[i]
                                response[i] = obj[i].get_resource(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def get_filtered(cls, client, filter_) :
        """Use this API to fetch filtered set of nsappflowcollector resources.
        filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = nsappflowcollector()
            option_ = options()
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def count(cls, client) :
        """Use this API to count the nsappflowcollector resources configured on NetScaler.

        :param client: 

        """
        try :
            obj = nsappflowcollector()
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
        """Use this API to count filtered the set of nsappflowcollector resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = nsappflowcollector()
            option_ = options()
            option_.count = True
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            if response :
                return response[0].__dict__['___count']
            return 0
        except Exception as e :
            raise e


class nsappflowcollector_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.nsappflowcollector = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.nsappflowcollector = [nsappflowcollector() for _ in range(length)]

