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

class vxlan(base_resource) :
    """Configuration for "VXLAN" resource."""
    def __init__(self) :
        self._id = 0
        self._vlan = 0
        self._port = 0
        self._dynamicrouting = ""
        self._ipv6dynamicrouting = ""
        self._td = 0
        self.___count = 0

    @property
    def id(self) :
        """A positive integer, which is also called VXLAN Network Identifier (VNI), that uniquely identifies a VXLAN.<br/>Minimum length =  1<br/>Maximum length =  16777215."""
        try :
            return self._id
        except Exception as e:
            raise e

    @id.setter
    def id(self, id) :
        """A positive integer, which is also called VXLAN Network Identifier (VNI), that uniquely identifies a VXLAN.<br/>Minimum length =  1<br/>Maximum length =  16777215

        :param id: 

        """
        try :
            self._id = id
        except Exception as e:
            raise e

    @property
    def vlan(self) :
        """ID of VLANs whose traffic is allowed over this VXLAN. If you do not specify any VLAN IDs, the NetScaler allows traffic of all VLANs that are not part of any other VXLANs.<br/>Minimum length =  1<br/>Maximum length =  4094."""
        try :
            return self._vlan
        except Exception as e:
            raise e

    @vlan.setter
    def vlan(self, vlan) :
        """ID of VLANs whose traffic is allowed over this VXLAN. If you do not specify any VLAN IDs, the NetScaler allows traffic of all VLANs that are not part of any other VXLANs.<br/>Minimum length =  1<br/>Maximum length =  4094

        :param vlan: 

        """
        try :
            self._vlan = vlan
        except Exception as e:
            raise e

    @property
    def port(self) :
        """Specifies UDP destination port for VXLAN packets.<br/>Default value: 4789<br/>Minimum length =  1<br/>Maximum length =  65534."""
        try :
            return self._port
        except Exception as e:
            raise e

    @port.setter
    def port(self, port) :
        """Specifies UDP destination port for VXLAN packets.<br/>Default value: 4789<br/>Minimum length =  1<br/>Maximum length =  65534

        :param port: 

        """
        try :
            self._port = port
        except Exception as e:
            raise e

    @property
    def dynamicrouting(self) :
        """Enable dynamic routing on this VXLAN.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._dynamicrouting
        except Exception as e:
            raise e

    @dynamicrouting.setter
    def dynamicrouting(self, dynamicrouting) :
        """Enable dynamic routing on this VXLAN.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED

        :param dynamicrouting: 

        """
        try :
            self._dynamicrouting = dynamicrouting
        except Exception as e:
            raise e

    @property
    def ipv6dynamicrouting(self) :
        """Enable all IPv6 dynamic routing protocols on this VXLAN. Note: For the ENABLED setting to work, you must configure IPv6 dynamic routing protocols from the VTYSH command line.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._ipv6dynamicrouting
        except Exception as e:
            raise e

    @ipv6dynamicrouting.setter
    def ipv6dynamicrouting(self, ipv6dynamicrouting) :
        """Enable all IPv6 dynamic routing protocols on this VXLAN. Note: For the ENABLED setting to work, you must configure IPv6 dynamic routing protocols from the VTYSH command line.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED

        :param ipv6dynamicrouting: 

        """
        try :
            self._ipv6dynamicrouting = ipv6dynamicrouting
        except Exception as e:
            raise e

    @property
    def td(self) :
        """Integer value that uniquely identifies the traffic domain in which you want to configure the entity. If you do not specify an ID, the entity becomes part of the default traffic domain, which has an ID of 0."""
        try :
            return self._td
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(vxlan_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.vxlan
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
        """Use this API to add vxlan.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                addresource = vxlan()
                addresource.id = resource.id
                addresource.vlan = resource.vlan
                addresource.port = resource.port
                addresource.dynamicrouting = resource.dynamicrouting
                addresource.ipv6dynamicrouting = resource.ipv6dynamicrouting
                return addresource.add_resource(client)
            else :
                if (resource and len(resource) > 0) :
                    addresources = [ vxlan() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        addresources[i].id = resource[i].id
                        addresources[i].vlan = resource[i].vlan
                        addresources[i].port = resource[i].port
                        addresources[i].dynamicrouting = resource[i].dynamicrouting
                        addresources[i].ipv6dynamicrouting = resource[i].ipv6dynamicrouting
                result = cls.add_bulk_request(client, addresources)
            return result
        except Exception as e :
            raise e

    @classmethod
    def delete(cls, client, resource) :
        """Use this API to delete vxlan.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                deleteresource = vxlan()
                if type(resource) !=  type(deleteresource):
                    deleteresource.id = resource
                else :
                    deleteresource.id = resource.id
                return deleteresource.delete_resource(client)
            else :
                if type(resource[0]) != cls :
                    if (resource and len(resource) > 0) :
                        deleteresources = [ vxlan() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            deleteresources[i].id = resource[i]
                else :
                    if (resource and len(resource) > 0) :
                        deleteresources = [ vxlan() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            deleteresources[i].id = resource[i].id
                result = cls.delete_bulk_request(client, deleteresources)
            return result
        except Exception as e :
            raise e

    @classmethod
    def update(cls, client, resource) :
        """Use this API to update vxlan.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                updateresource = vxlan()
                updateresource.id = resource.id
                updateresource.vlan = resource.vlan
                updateresource.port = resource.port
                updateresource.dynamicrouting = resource.dynamicrouting
                updateresource.ipv6dynamicrouting = resource.ipv6dynamicrouting
                return updateresource.update_resource(client)
            else :
                if (resource and len(resource) > 0) :
                    updateresources = [ vxlan() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        updateresources[i].id = resource[i].id
                        updateresources[i].vlan = resource[i].vlan
                        updateresources[i].port = resource[i].port
                        updateresources[i].dynamicrouting = resource[i].dynamicrouting
                        updateresources[i].ipv6dynamicrouting = resource[i].ipv6dynamicrouting
                result = cls.update_bulk_request(client, updateresources)
            return result
        except Exception as e :
            raise e

    @classmethod
    def unset(cls, client, resource, args) :
        """Use this API to unset the properties of vxlan resource.
        Properties that need to be unset are specified in args array.

        :param client: 
        :param resource: 
        :param args: 

        """
        try :
            if type(resource) is not list :
                unsetresource = vxlan()
                if type(resource) !=  type(unsetresource):
                    unsetresource.id = resource
                else :
                    unsetresource.id = resource.id
                return unsetresource.unset_resource(client, args)
            else :
                if type(resource[0]) != cls :
                    if (resource and len(resource) > 0) :
                        unsetresources = [ vxlan() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            unsetresources[i].id = resource[i]
                else :
                    if (resource and len(resource) > 0) :
                        unsetresources = [ vxlan() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            unsetresources[i].id = resource[i].id
                result = cls.unset_bulk_request(client, unsetresources, args)
            return result
        except Exception as e :
            raise e

    @classmethod
    def get(cls, client, name="", option_="") :
        """Use this API to fetch all the vxlan resources that are configured on netscaler.

        :param client: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            if not name :
                obj = vxlan()
                response = obj.get_resources(client, option_)
            else :
                if type(name) != cls :
                    if type(name) is not list :
                        obj = vxlan()
                        obj.id = name
                        response = obj.get_resource(client, option_)
                    else :
                        if name and len(name) > 0 :
                            response = [vxlan() for _ in range(len(name))]
                            obj = [vxlan() for _ in range(len(name))]
                            for i in range(len(name)) :
                                obj[i] = vxlan()
                                obj[i].id = name[i]
                                response[i] = obj[i].get_resource(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def get_filtered(cls, client, filter_) :
        """Use this API to fetch filtered set of vxlan resources.
        filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = vxlan()
            option_ = options()
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def count(cls, client) :
        """Use this API to count the vxlan resources configured on NetScaler.

        :param client: 

        """
        try :
            obj = vxlan()
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
        """Use this API to count filtered the set of vxlan resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = vxlan()
            option_ = options()
            option_.count = True
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            if response :
                return response[0].__dict__['___count']
            return 0
        except Exception as e :
            raise e


    class Ipv6dynamicrouting:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Dynamicrouting:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

class vxlan_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.vxlan = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.vxlan = [vxlan() for _ in range(length)]

