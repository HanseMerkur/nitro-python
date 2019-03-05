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

class vrid_interface_binding(base_resource) :
    """Binding class showing the interface that can be bound to vrid."""
    def __init__(self) :
        self._ifaces = ""
        self._trackifnum = ""
        self._vlan = 0
        self._flags = 0
        self._flags = 0
        self._id = 0
        self._ifnum = ""
        self.___count = 0

    @property
    def ifnum(self) :
        """Interfaces to bind to the VMAC, specified in (slot/port) notation (for example, 1/2).Use spaces to separate multiple entries."""
        try :
            return self._ifnum
        except Exception as e:
            raise e

    @ifnum.setter
    def ifnum(self, ifnum) :
        """Interfaces to bind to the VMAC, specified in (slot/port) notation (for example, 1/2).Use spaces to separate multiple entries.

        :param ifnum: 

        """
        try :
            self._ifnum = ifnum
        except Exception as e:
            raise e

    @property
    def trackifnum(self) :
        """Interfaces which need to be tracked for this vrID."""
        try :
            return self._trackifnum
        except Exception as e:
            raise e

    @trackifnum.setter
    def trackifnum(self, trackifnum) :
        """Interfaces which need to be tracked for this vrID.

        :param trackifnum: 

        """
        try :
            self._trackifnum = trackifnum
        except Exception as e:
            raise e

    @property
    def ifaces(self) :
        """Interfaces bound to this VRID."""
        try :
            return self._ifaces
        except Exception as e:
            raise e

    @ifaces.setter
    def ifaces(self, ifaces) :
        """Interfaces bound to this VRID.

        :param ifaces: 

        """
        try :
            self._ifaces = ifaces
        except Exception as e:
            raise e

    @property
    def id(self) :
        """Integer that uniquely identifies the VMAC address. The generic VMAC address is in the form of 00:00:5e:00:01:<VRID>. For example, if you add a VRID with a value of 60 and bind it to an interface, the resulting VMAC address is 00:00:5e:00:01:3c, where 3c is the hexadecimal representation of 60.<br/>Minimum value =  1<br/>Maximum value =  255."""
        try :
            return self._id
        except Exception as e:
            raise e

    @id.setter
    def id(self, id) :
        """Integer that uniquely identifies the VMAC address. The generic VMAC address is in the form of 00:00:5e:00:01:<VRID>. For example, if you add a VRID with a value of 60 and bind it to an interface, the resulting VMAC address is 00:00:5e:00:01:3c, where 3c is the hexadecimal representation of 60.<br/>Minimum value =  1<br/>Maximum value =  255

        :param id: 

        """
        try :
            self._id = id
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
    def vlan(self) :
        """The VLAN in which this VRID resides."""
        try :
            return self._vlan
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(vrid_interface_binding_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.vrid_interface_binding
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
                updateresource = vrid_interface_binding()
                updateresource.id = resource.id
                updateresource.ifnum = resource.ifnum
                updateresource.trackifnum = resource.trackifnum
                return updateresource.update_resource(client)
            else :
                if resource and len(resource) > 0 :
                    updateresources = [vrid_interface_binding() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        updateresources[i].id = resource[i].id
                        updateresources[i].ifnum = resource[i].ifnum
                        updateresources[i].trackifnum = resource[i].trackifnum
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
                deleteresource = vrid_interface_binding()
                deleteresource.id = resource.id
                deleteresource.ifnum = resource.ifnum
                deleteresource.trackifnum = resource.trackifnum
                return deleteresource.delete_resource(client)
            else :
                if resource and len(resource) > 0 :
                    deleteresources = [vrid_interface_binding() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        deleteresources[i].id = resource[i].id
                        deleteresources[i].ifnum = resource[i].ifnum
                        deleteresources[i].trackifnum = resource[i].trackifnum
                return cls.delete_bulk_request(client, deleteresources)
        except Exception as e :
            raise e

    @classmethod
    def get(cls, service, id) :
        """Use this API to fetch vrid_interface_binding resources.

        :param service: 
        :param id: 

        """
        try :
            obj = vrid_interface_binding()
            obj.id = id
            response = obj.get_resources(service)
            return response
        except Exception as e:
            raise e

    @classmethod
    def get_filtered(cls, service, id, filter_) :
        """Use this API to fetch filtered set of vrid_interface_binding resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param service: 
        :param id: 
        :param filter_: 

        """
        try :
            obj = vrid_interface_binding()
            obj.id = id
            option_ = options()
            option_.filter = filter_
            response = obj.getfiltered(service, option_)
            return response
        except Exception as e:
            raise e

    @classmethod
    def count(cls, service, id) :
        """Use this API to count vrid_interface_binding resources configued on NetScaler.

        :param service: 
        :param id: 

        """
        try :
            obj = vrid_interface_binding()
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
        """Use this API to count the filtered set of vrid_interface_binding resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param service: 
        :param id: 
        :param filter_: 

        """
        try :
            obj = vrid_interface_binding()
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

class vrid_interface_binding_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.vrid_interface_binding = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.vrid_interface_binding = [vrid_interface_binding() for _ in range(length)]

