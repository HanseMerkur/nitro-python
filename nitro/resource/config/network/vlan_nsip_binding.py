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

class vlan_nsip_binding(base_resource) :
    """Binding class showing the nsip that can be bound to vlan."""
    def __init__(self) :
        self._ipaddress = ""
        self._netmask = ""
        self._td = 0
        self._ownergroup = ""
        self._id = 0
        self.___count = 0

    @property
    def ownergroup(self) :
        """The owner node group in a Cluster for this vlan.<br/>Default value: DEFAULT_NG<br/>Minimum length =  1."""
        try :
            return self._ownergroup
        except Exception as e:
            raise e

    @ownergroup.setter
    def ownergroup(self, ownergroup) :
        """The owner node group in a Cluster for this vlan.<br/>Default value: DEFAULT_NG<br/>Minimum length =  1

        :param ownergroup: 

        """
        try :
            self._ownergroup = ownergroup
        except Exception as e:
            raise e

    @property
    def id(self) :
        """Specifies the virtual LAN ID.<br/>Minimum value =  1<br/>Maximum value =  4094."""
        try :
            return self._id
        except Exception as e:
            raise e

    @id.setter
    def id(self, id) :
        """Specifies the virtual LAN ID.<br/>Minimum value =  1<br/>Maximum value =  4094

        :param id: 

        """
        try :
            self._id = id
        except Exception as e:
            raise e

    @property
    def td(self) :
        """Integer value that uniquely identifies the traffic domain in which you want to configure the entity. If you do not specify an ID, the entity becomes part of the default traffic domain, which has an ID of 0.<br/>Minimum value =  0<br/>Maximum value =  4094."""
        try :
            return self._td
        except Exception as e:
            raise e

    @td.setter
    def td(self, td) :
        """Integer value that uniquely identifies the traffic domain in which you want to configure the entity. If you do not specify an ID, the entity becomes part of the default traffic domain, which has an ID of 0.<br/>Minimum value =  0<br/>Maximum value =  4094

        :param td: 

        """
        try :
            self._td = td
        except Exception as e:
            raise e

    @property
    def netmask(self) :
        """Subnet mask for the network address defined for this VLAN."""
        try :
            return self._netmask
        except Exception as e:
            raise e

    @netmask.setter
    def netmask(self, netmask) :
        """Subnet mask for the network address defined for this VLAN.

        :param netmask: 

        """
        try :
            self._netmask = netmask
        except Exception as e:
            raise e

    @property
    def ipaddress(self) :
        """The IP address assigned to the VLAN."""
        try :
            return self._ipaddress
        except Exception as e:
            raise e

    @ipaddress.setter
    def ipaddress(self, ipaddress) :
        """The IP address assigned to the VLAN.

        :param ipaddress: 

        """
        try :
            self._ipaddress = ipaddress
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(vlan_nsip_binding_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.vlan_nsip_binding
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
        """

        :param client: 
        :param resource: 

        """
        try :
            if resource and type(resource) is not list :
                updateresource = vlan_nsip_binding()
                updateresource.id = resource.id
                updateresource.ipaddress = resource.ipaddress
                updateresource.netmask = resource.netmask
                updateresource.td = resource.td
                updateresource.ownergroup = resource.ownergroup
                return updateresource.update_resource(client)
            else :
                if resource and len(resource) > 0 :
                    updateresources = [vlan_nsip_binding() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        updateresources[i].id = resource[i].id
                        updateresources[i].ipaddress = resource[i].ipaddress
                        updateresources[i].netmask = resource[i].netmask
                        updateresources[i].td = resource[i].td
                        updateresources[i].ownergroup = resource[i].ownergroup
                return cls.update_bulk_request(client, updateresources)
        except Exception as e :
            raise e

    @classmethod
    def delete(cls, client, resource) :
        """

        :param client: 
        :param resource: 

        """
        try :
            if resource and type(resource) is not list :
                deleteresource = vlan_nsip_binding()
                deleteresource.id = resource.id
                deleteresource.ipaddress = resource.ipaddress
                deleteresource.netmask = resource.netmask
                deleteresource.td = resource.td
                deleteresource.ownergroup = resource.ownergroup
                return deleteresource.delete_resource(client)
            else :
                if resource and len(resource) > 0 :
                    deleteresources = [vlan_nsip_binding() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        deleteresources[i].id = resource[i].id
                        deleteresources[i].ipaddress = resource[i].ipaddress
                        deleteresources[i].netmask = resource[i].netmask
                        deleteresources[i].td = resource[i].td
                        deleteresources[i].ownergroup = resource[i].ownergroup
                return cls.delete_bulk_request(client, deleteresources)
        except Exception as e :
            raise e

    @classmethod
    def get(cls, service, id) :
        """Use this API to fetch vlan_nsip_binding resources.

        :param service: 
        :param id: 

        """
        try :
            obj = vlan_nsip_binding()
            obj.id = id
            response = obj.get_resources(service)
            return response
        except Exception as e:
            raise e

    @classmethod
    def get_filtered(cls, service, id, filter_) :
        """Use this API to fetch filtered set of vlan_nsip_binding resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param service: 
        :param id: 
        :param filter_: 

        """
        try :
            obj = vlan_nsip_binding()
            obj.id = id
            option_ = options()
            option_.filter = filter_
            response = obj.getfiltered(service, option_)
            return response
        except Exception as e:
            raise e

    @classmethod
    def count(cls, service, id) :
        """Use this API to count vlan_nsip_binding resources configued on NetScaler.

        :param service: 
        :param id: 

        """
        try :
            obj = vlan_nsip_binding()
            obj.id = id
            option_ = options()
            option_.count = True
            response = obj.get_resources(service, option_)
            if response :
                return response[0].__dict__['___count']
            return 0
        except Exception as e:
            raise e

    @classmethod
    def count_filtered(cls, service, id, filter_) :
        """Use this API to count the filtered set of vlan_nsip_binding resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param service: 
        :param id: 
        :param filter_: 

        """
        try :
            obj = vlan_nsip_binding()
            obj.id = id
            option_ = options()
            option_.count = True
            option_.filter = filter_
            response = obj.getfiltered(service, option_)
            if response :
                return response[0].__dict__['___count']
            return 0
        except Exception as e:
            raise e

class vlan_nsip_binding_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.vlan_nsip_binding = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.vlan_nsip_binding = [vlan_nsip_binding() for _ in range(length)]

