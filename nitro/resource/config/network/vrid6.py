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

class vrid6(base_resource) :
    """Configuration for Virtual Router ID for IPv6 resource."""
    def __init__(self) :
        self._id = 0
        self._all = False
        self._ifaces = ""
        self._ifnum = ""
        self._type = ""
        self._priority = 0
        self._state = 0
        self._flags = 0
        self._ipaddress = ""
        self.___count = 0

    @property
    def id(self) :
        """Integer value that uniquely identifies a VMAC6 address.<br/>Minimum length =  1<br/>Maximum length =  255."""
        try :
            return self._id
        except Exception as e:
            raise e

    @id.setter
    def id(self, id) :
        """Integer value that uniquely identifies a VMAC6 address.<br/>Minimum length =  1<br/>Maximum length =  255

        :param id: 

        """
        try :
            self._id = id
        except Exception as e:
            raise e

    @property
    def all(self) :
        """Remove all configured VMAC6 addresses from the NetScaler appliance."""
        try :
            return self._all
        except Exception as e:
            raise e

    @all.setter
    def all(self, all) :
        """Remove all configured VMAC6 addresses from the NetScaler appliance.

        :param all: 

        """
        try :
            self._all = all
        except Exception as e:
            raise e

    @property
    def ifaces(self) :
        """Interfaces bound to this VRID."""
        try :
            return self._ifaces
        except Exception as e:
            raise e

    @property
    def ifnum(self) :
        """Interfaces bound to this VRID."""
        try :
            return self._ifnum
        except Exception as e:
            raise e

    @property
    def type(self) :
        """Type (static or dynamic) of this VRID.<br/>Possible values = STATIC, DYNAMIC."""
        try :
            return self._type
        except Exception as e:
            raise e

    @property
    def priority(self) :
        """The priority of this VRID."""
        try :
            return self._priority
        except Exception as e:
            raise e

    @property
    def state(self) :
        """State of this VRID."""
        try :
            return self._state
        except Exception as e:
            raise e

    @property
    def flags(self) :
        """Flags."""
        try :
            return self._flags
        except Exception as e:
            raise e

    @property
    def ipaddress(self) :
        """The IP address bound to the VRID6."""
        try :
            return self._ipaddress
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(vrid6_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.vrid6
        except Exception as e :
            raise e

    def _get_object_name(self) :
        """Returns the value of object identifier argument"""
        try :
            if self.id is not None :
                return str(self.id)
            return None
        except Exception as e :
            raise e



    @classmethod
    def add(cls, client, resource) :
        """Use this API to add vrid6.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                addresource = vrid6()
                addresource.id = resource.id
                return addresource.add_resource(client)
            else :
                if (resource and len(resource) > 0) :
                    addresources = [ vrid6() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        addresources[i].id = resource[i].id
                result = cls.add_bulk_request(client, addresources)
            return result
        except Exception as e :
            raise e

    @classmethod
    def delete(cls, client, resource) :
        """Use this API to delete vrid6.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                deleteresource = vrid6()
                if type(resource) !=  type(deleteresource):
                    deleteresource.id = resource
                else :
                    deleteresource.id = resource.id
                    deleteresource.all = resource.all
                return deleteresource.delete_resource(client)
            else :
                if type(resource[0]) != cls :
                    if (resource and len(resource) > 0) :
                        deleteresources = [ vrid6() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            deleteresources[i].id = resource[i]
                else :
                    if (resource and len(resource) > 0) :
                        deleteresources = [ vrid6() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            deleteresources[i].id = resource[i].id
                            deleteresources[i].all = resource[i].all
                result = cls.delete_bulk_request(client, deleteresources)
            return result
        except Exception as e :
            raise e

    @classmethod
    def get(cls, client, name="", option_="") :
        """Use this API to fetch all the vrid6 resources that are configured on netscaler.

        :param client: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            if not name :
                obj = vrid6()
                response = obj.get_resources(client, option_)
            else :
                if type(name) != cls :
                    if type(name) is not list :
                        obj = vrid6()
                        obj.id = name
                        response = obj.get_resource(client, option_)
                    else :
                        if name and len(name) > 0 :
                            response = [vrid6() for _ in range(len(name))]
                            obj = [vrid6() for _ in range(len(name))]
                            for i in range(len(name)) :
                                obj[i] = vrid6()
                                obj[i].id = name[i]
                                response[i] = obj[i].get_resource(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def get_filtered(cls, client, filter_) :
        """Use this API to fetch filtered set of vrid6 resources.
        filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = vrid6()
            option_ = options()
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def count(cls, client) :
        """Use this API to count the vrid6 resources configured on NetScaler.

        :param client: 

        """
        try :
            obj = vrid6()
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
        """Use this API to count filtered the set of vrid6 resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = vrid6()
            option_ = options()
            option_.count = True
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            if response :
                return response[0].__dict__['___count']
            return 0
        except Exception as e :
            raise e


    class Type:
        """ """
        STATIC = "STATIC"
        DYNAMIC = "DYNAMIC"

class vrid6_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.vrid6 = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.vrid6 = [vrid6() for _ in range(length)]

