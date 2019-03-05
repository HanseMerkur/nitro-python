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

class servicegroup_servicegroupmember_binding(base_resource) :
    """Binding class showing the servicegroupmember that can be bound to servicegroup."""
    def __init__(self) :
        self._ip = ""
        self._port = 0
        self._svrstate = ""
        self._statechangetimesec = ""
        self._tickssincelaststatechange = 0
        self._weight = 0
        self._servername = ""
        self._customserverid = ""
        self._serverid = 0
        self._state = ""
        self._hashid = 0
        self._graceful = ""
        self._delay = 0
        self._servicegroupname = ""
        self.___count = 0

    @property
    def servicegroupname(self) :
        """Name of the service group.<br/>Minimum length =  1."""
        try :
            return self._servicegroupname
        except Exception as e:
            raise e

    @servicegroupname.setter
    def servicegroupname(self, servicegroupname) :
        """Name of the service group.<br/>Minimum length =  1

        :param servicegroupname: 

        """
        try :
            self._servicegroupname = servicegroupname
        except Exception as e:
            raise e

    @property
    def ip(self) :
        """IP Address."""
        try :
            return self._ip
        except Exception as e:
            raise e

    @ip.setter
    def ip(self, ip) :
        """IP Address.

        :param ip: 

        """
        try :
            self._ip = ip
        except Exception as e:
            raise e

    @property
    def port(self) :
        """Server port number.<br/>Range 1 - 65535."""
        try :
            return self._port
        except Exception as e:
            raise e

    @port.setter
    def port(self, port) :
        """Server port number.<br/>Range 1 - 65535

        :param port: 

        """
        try :
            self._port = port
        except Exception as e:
            raise e

    @property
    def state(self) :
        """Initial state of the service group.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._state
        except Exception as e:
            raise e

    @state.setter
    def state(self, state) :
        """Initial state of the service group.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED

        :param state: 

        """
        try :
            self._state = state
        except Exception as e:
            raise e

    @property
    def hashid(self) :
        """The hash identifier for the service. This must be unique for each service. This parameter is used by hash based load balancing methods.<br/>Minimum value =  1."""
        try :
            return self._hashid
        except Exception as e:
            raise e

    @hashid.setter
    def hashid(self, hashid) :
        """The hash identifier for the service. This must be unique for each service. This parameter is used by hash based load balancing methods.<br/>Minimum value =  1

        :param hashid: 

        """
        try :
            self._hashid = hashid
        except Exception as e:
            raise e

    @property
    def serverid(self) :
        """The  identifier for the service. This is used when the persistency type is set to Custom Server ID."""
        try :
            return self._serverid
        except Exception as e:
            raise e

    @serverid.setter
    def serverid(self, serverid) :
        """The  identifier for the service. This is used when the persistency type is set to Custom Server ID.

        :param serverid: 

        """
        try :
            self._serverid = serverid
        except Exception as e:
            raise e

    @property
    def servername(self) :
        """Name of the server to which to bind the service group.<br/>Minimum length =  1."""
        try :
            return self._servername
        except Exception as e:
            raise e

    @servername.setter
    def servername(self, servername) :
        """Name of the server to which to bind the service group.<br/>Minimum length =  1

        :param servername: 

        """
        try :
            self._servername = servername
        except Exception as e:
            raise e

    @property
    def customserverid(self) :
        """The identifier for this IP:Port pair. Used when the persistency type is set to Custom Server ID.<br/>Default value: "None"."""
        try :
            return self._customserverid
        except Exception as e:
            raise e

    @customserverid.setter
    def customserverid(self, customserverid) :
        """The identifier for this IP:Port pair. Used when the persistency type is set to Custom Server ID.<br/>Default value: "None"

        :param customserverid: 

        """
        try :
            self._customserverid = customserverid
        except Exception as e:
            raise e

    @property
    def weight(self) :
        """Weight to assign to the servers in the service group. Specifies the capacity of the servers relative to the other servers in the load balancing configuration. The higher the weight, the higher the percentage of requests sent to the service.<br/>Minimum value =  1<br/>Maximum value =  100."""
        try :
            return self._weight
        except Exception as e:
            raise e

    @weight.setter
    def weight(self, weight) :
        """Weight to assign to the servers in the service group. Specifies the capacity of the servers relative to the other servers in the load balancing configuration. The higher the weight, the higher the percentage of requests sent to the service.<br/>Minimum value =  1<br/>Maximum value =  100

        :param weight: 

        """
        try :
            self._weight = weight
        except Exception as e:
            raise e

    @property
    def delay(self) :
        """Time, in seconds, allocated for a shutdown of the services in the service group. During this period, new requests are sent to the service only for clients who already have persistent sessions on the appliance. Requests from new clients are load balanced among other available services. After the delay time expires, no requests are sent to the service, and the service is marked as unavailable (OUT OF SERVICE)."""
        try :
            return self._delay
        except Exception as e:
            raise e

    @property
    def statechangetimesec(self) :
        """Time when last state change occurred. Seconds part."""
        try :
            return self._statechangetimesec
        except Exception as e:
            raise e

    @property
    def svrstate(self) :
        """The state of the service.<br/>Possible values = UP, DOWN, UNKNOWN, BUSY, OUT OF SERVICE, GOING OUT OF SERVICE, DOWN WHEN GOING OUT OF SERVICE, NS_EMPTY_STR, Unknown, DISABLED."""
        try :
            return self._svrstate
        except Exception as e:
            raise e

    @property
    def tickssincelaststatechange(self) :
        """Time in 10 millisecond ticks since the last state change."""
        try :
            return self._tickssincelaststatechange
        except Exception as e:
            raise e

    @property
    def graceful(self) :
        """Wait for all existing connections to the service to terminate before shutting down the service.<br/>Default value: NO<br/>Possible values = YES, NO."""
        try :
            return self._graceful
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(servicegroup_servicegroupmember_binding_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.servicegroup_servicegroupmember_binding
        except Exception as e :
            raise e

    def _get_object_name(self) :
        """Returns the value of object identifier argument"""
        try :
            if self.servicegroupname is not None :
                return str(self.servicegroupname)
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
                updateresource = servicegroup_servicegroupmember_binding()
                updateresource.servicegroupname = resource.servicegroupname
                updateresource.ip = resource.ip
                updateresource.servername = resource.servername
                updateresource.port = resource.port
                updateresource.weight = resource.weight
                updateresource.customserverid = resource.customserverid
                updateresource.serverid = resource.serverid
                updateresource.state = resource.state
                updateresource.hashid = resource.hashid
                return updateresource.update_resource(client)
            else :
                if resource and len(resource) > 0 :
                    updateresources = [servicegroup_servicegroupmember_binding() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        updateresources[i].servicegroupname = resource[i].servicegroupname
                        updateresources[i].ip = resource[i].ip
                        updateresources[i].servername = resource[i].servername
                        updateresources[i].port = resource[i].port
                        updateresources[i].weight = resource[i].weight
                        updateresources[i].customserverid = resource[i].customserverid
                        updateresources[i].serverid = resource[i].serverid
                        updateresources[i].state = resource[i].state
                        updateresources[i].hashid = resource[i].hashid
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
                deleteresource = servicegroup_servicegroupmember_binding()
                deleteresource.servicegroupname = resource.servicegroupname
                deleteresource.ip = resource.ip
                deleteresource.servername = resource.servername
                deleteresource.port = resource.port
                return deleteresource.delete_resource(client)
            else :
                if resource and len(resource) > 0 :
                    deleteresources = [servicegroup_servicegroupmember_binding() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        deleteresources[i].servicegroupname = resource[i].servicegroupname
                        deleteresources[i].ip = resource[i].ip
                        deleteresources[i].servername = resource[i].servername
                        deleteresources[i].port = resource[i].port
                return cls.delete_bulk_request(client, deleteresources)
        except Exception as e :
            raise e

    @classmethod
    def get(cls, service, servicegroupname) :
        """Use this API to fetch servicegroup_servicegroupmember_binding resources.

        :param service: 
        :param servicegroupname: 

        """
        try :
            obj = servicegroup_servicegroupmember_binding()
            obj.servicegroupname = servicegroupname
            response = obj.get_resources(service)
            return response
        except Exception as e:
            raise e

    @classmethod
    def get_filtered(cls, service, servicegroupname, filter_) :
        """Use this API to fetch filtered set of servicegroup_servicegroupmember_binding resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param service: 
        :param servicegroupname: 
        :param filter_: 

        """
        try :
            obj = servicegroup_servicegroupmember_binding()
            obj.servicegroupname = servicegroupname
            option_ = options()
            option_.filter = filter_
            response = obj.getfiltered(service, option_)
            return response
        except Exception as e:
            raise e

    @classmethod
    def count(cls, service, servicegroupname) :
        """Use this API to count servicegroup_servicegroupmember_binding resources configued on NetScaler.

        :param service: 
        :param servicegroupname: 

        """
        try :
            obj = servicegroup_servicegroupmember_binding()
            obj.servicegroupname = servicegroupname
            option_ = options()
            option_.count = True
            response = obj.get_resources(service, option_)
            if response :
                return response[0].__dict__['___count']
            return 0
        except Exception as e:
            raise e

    @classmethod
    def count_filtered(cls, service, servicegroupname, filter_) :
        """Use this API to count the filtered set of servicegroup_servicegroupmember_binding resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param service: 
        :param servicegroupname: 
        :param filter_: 

        """
        try :
            obj = servicegroup_servicegroupmember_binding()
            obj.servicegroupname = servicegroupname
            option_ = options()
            option_.count = True
            option_.filter = filter_
            response = obj.getfiltered(service, option_)
            if response :
                return response[0].__dict__['___count']
            return 0
        except Exception as e:
            raise e

    class Svrstate:
        """ """
        UP = "UP"
        DOWN = "DOWN"
        UNKNOWN = "UNKNOWN"
        BUSY = "BUSY"
        OUT_OF_SERVICE = "OUT OF SERVICE"
        GOING_OUT_OF_SERVICE = "GOING OUT OF SERVICE"
        DOWN_WHEN_GOING_OUT_OF_SERVICE = "DOWN WHEN GOING OUT OF SERVICE"
        NS_EMPTY_STR = "NS_EMPTY_STR"
        Unknown = "Unknown"
        DISABLED = "DISABLED"

    class State:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Monstate:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Graceful:
        """ """
        YES = "YES"
        NO = "NO"

class servicegroup_servicegroupmember_binding_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.servicegroup_servicegroupmember_binding = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.servicegroup_servicegroupmember_binding = [servicegroup_servicegroupmember_binding() for _ in range(length)]

