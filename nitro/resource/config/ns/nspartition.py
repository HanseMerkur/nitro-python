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

class nspartition(base_resource) :
    """Configuration for admin partition resource."""
    def __init__(self) :
        self._partitionname = ""
        self._maxbandwidth = 0
        self._minbandwidth = 0
        self._maxconn = 0
        self._maxmemlimit = 0
        self._partitionid = 0
        self._partitiontype = ""
        self.___count = 0

    @property
    def partitionname(self) :
        """Name of the Partition. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.<br/>Minimum length =  1."""
        try :
            return self._partitionname
        except Exception as e:
            raise e

    @partitionname.setter
    def partitionname(self, partitionname) :
        """Name of the Partition. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters.<br/>Minimum length =  1

        :param partitionname: 

        """
        try :
            self._partitionname = partitionname
        except Exception as e:
            raise e

    @property
    def maxbandwidth(self) :
        """Maximum bandwidth in Kbps, permitted on this partition.<br/>Default value: 10240."""
        try :
            return self._maxbandwidth
        except Exception as e:
            raise e

    @maxbandwidth.setter
    def maxbandwidth(self, maxbandwidth) :
        """Maximum bandwidth in Kbps, permitted on this partition.<br/>Default value: 10240

        :param maxbandwidth: 

        """
        try :
            self._maxbandwidth = maxbandwidth
        except Exception as e:
            raise e

    @property
    def minbandwidth(self) :
        """Minimum bandwidth in Kbps, permitted on this partition.<br/>Default value: 10240."""
        try :
            return self._minbandwidth
        except Exception as e:
            raise e

    @minbandwidth.setter
    def minbandwidth(self, minbandwidth) :
        """Minimum bandwidth in Kbps, permitted on this partition.<br/>Default value: 10240

        :param minbandwidth: 

        """
        try :
            self._minbandwidth = minbandwidth
        except Exception as e:
            raise e

    @property
    def maxconn(self) :
        """Maximum number of connections permitted on this partition.<br/>Default value: 1024."""
        try :
            return self._maxconn
        except Exception as e:
            raise e

    @maxconn.setter
    def maxconn(self, maxconn) :
        """Maximum number of connections permitted on this partition.<br/>Default value: 1024

        :param maxconn: 

        """
        try :
            self._maxconn = maxconn
        except Exception as e:
            raise e

    @property
    def maxmemlimit(self) :
        """Maximum memory allowed for this partition in megabytes.<br/>Default value: 10<br/>Minimum length =  5."""
        try :
            return self._maxmemlimit
        except Exception as e:
            raise e

    @maxmemlimit.setter
    def maxmemlimit(self, maxmemlimit) :
        """Maximum memory allowed for this partition in megabytes.<br/>Default value: 10<br/>Minimum length =  5

        :param maxmemlimit: 

        """
        try :
            self._maxmemlimit = maxmemlimit
        except Exception as e:
            raise e

    @property
    def partitionid(self) :
        """Partition Id.<br/>Minimum value =  1."""
        try :
            return self._partitionid
        except Exception as e:
            raise e

    @property
    def partitiontype(self) :
        """Type of the Partition.<br/>Possible values = Default Partition, Current Partition."""
        try :
            return self._partitiontype
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(nspartition_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.nspartition
        except Exception as e :
            raise e

    def _get_object_name(self) :
        """Returns the value of object identifier argument"""
        try :
            if self.partitionname is not None :
                return str(self.partitionname)
            return None
        except Exception as e :
            raise e



    @classmethod
    def add(cls, client, resource) :
        """Use this API to add nspartition.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                addresource = nspartition()
                addresource.partitionname = resource.partitionname
                addresource.maxbandwidth = resource.maxbandwidth
                addresource.minbandwidth = resource.minbandwidth
                addresource.maxconn = resource.maxconn
                addresource.maxmemlimit = resource.maxmemlimit
                return addresource.add_resource(client)
            else :
                if (resource and len(resource) > 0) :
                    addresources = [ nspartition() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        addresources[i].partitionname = resource[i].partitionname
                        addresources[i].maxbandwidth = resource[i].maxbandwidth
                        addresources[i].minbandwidth = resource[i].minbandwidth
                        addresources[i].maxconn = resource[i].maxconn
                        addresources[i].maxmemlimit = resource[i].maxmemlimit
                result = cls.add_bulk_request(client, addresources)
            return result
        except Exception as e :
            raise e

    @classmethod
    def delete(cls, client, resource) :
        """Use this API to delete nspartition.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                deleteresource = nspartition()
                if type(resource) !=  type(deleteresource):
                    deleteresource.partitionname = resource
                else :
                    deleteresource.partitionname = resource.partitionname
                return deleteresource.delete_resource(client)
            else :
                if type(resource[0]) != cls :
                    if (resource and len(resource) > 0) :
                        deleteresources = [ nspartition() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            deleteresources[i].partitionname = resource[i]
                else :
                    if (resource and len(resource) > 0) :
                        deleteresources = [ nspartition() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            deleteresources[i].partitionname = resource[i].partitionname
                result = cls.delete_bulk_request(client, deleteresources)
            return result
        except Exception as e :
            raise e

    @classmethod
    def update(cls, client, resource) :
        """Use this API to update nspartition.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                updateresource = nspartition()
                updateresource.partitionname = resource.partitionname
                updateresource.maxbandwidth = resource.maxbandwidth
                updateresource.minbandwidth = resource.minbandwidth
                updateresource.maxconn = resource.maxconn
                updateresource.maxmemlimit = resource.maxmemlimit
                return updateresource.update_resource(client)
            else :
                if (resource and len(resource) > 0) :
                    updateresources = [ nspartition() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        updateresources[i].partitionname = resource[i].partitionname
                        updateresources[i].maxbandwidth = resource[i].maxbandwidth
                        updateresources[i].minbandwidth = resource[i].minbandwidth
                        updateresources[i].maxconn = resource[i].maxconn
                        updateresources[i].maxmemlimit = resource[i].maxmemlimit
                result = cls.update_bulk_request(client, updateresources)
            return result
        except Exception as e :
            raise e

    @classmethod
    def unset(cls, client, resource, args) :
        """Use this API to unset the properties of nspartition resource.
        Properties that need to be unset are specified in args array.

        :param client: 
        :param resource: 
        :param args: 

        """
        try :
            if type(resource) is not list :
                unsetresource = nspartition()
                if type(resource) !=  type(unsetresource):
                    unsetresource.partitionname = resource
                else :
                    unsetresource.partitionname = resource.partitionname
                return unsetresource.unset_resource(client, args)
            else :
                if type(resource[0]) != cls :
                    if (resource and len(resource) > 0) :
                        unsetresources = [ nspartition() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            unsetresources[i].partitionname = resource[i]
                else :
                    if (resource and len(resource) > 0) :
                        unsetresources = [ nspartition() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            unsetresources[i].partitionname = resource[i].partitionname
                result = cls.unset_bulk_request(client, unsetresources, args)
            return result
        except Exception as e :
            raise e

    @classmethod
    def Switch(cls, client, resource) :
        """Use this API to Switch nspartition.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                Switchresource = nspartition()
                Switchresource.partitionname = resource.partitionname
                return Switchresource.perform_operation(client,"Switch")
            else :
                if (resource and len(resource) > 0) :
                    Switchresources = [ nspartition() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        Switchresources[i].partitionname = resource[i].partitionname
                result = cls.perform_operation_bulk_request(client, Switchresources,"Switch")
            return result
        except Exception as e :
            raise e

    @classmethod
    def get(cls, client, name="", option_="") :
        """Use this API to fetch all the nspartition resources that are configured on netscaler.

        :param client: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            if not name :
                obj = nspartition()
                response = obj.get_resources(client, option_)
            else :
                if type(name) != cls :
                    if type(name) is not list :
                        obj = nspartition()
                        obj.partitionname = name
                        response = obj.get_resource(client, option_)
                    else :
                        if name and len(name) > 0 :
                            response = [nspartition() for _ in range(len(name))]
                            obj = [nspartition() for _ in range(len(name))]
                            for i in range(len(name)) :
                                obj[i] = nspartition()
                                obj[i].partitionname = name[i]
                                response[i] = obj[i].get_resource(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def get_filtered(cls, client, filter_) :
        """Use this API to fetch filtered set of nspartition resources.
        filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = nspartition()
            option_ = options()
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def count(cls, client) :
        """Use this API to count the nspartition resources configured on NetScaler.

        :param client: 

        """
        try :
            obj = nspartition()
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
        """Use this API to count filtered the set of nspartition resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = nspartition()
            option_ = options()
            option_.count = True
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            if response :
                return response[0].__dict__['___count']
            return 0
        except Exception as e :
            raise e


    class Partitiontype:
        """ """
        Default_Partition = "Default Partition"
        Current_Partition = "Current Partition"

class nspartition_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.nspartition = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.nspartition = [nspartition() for _ in range(length)]

