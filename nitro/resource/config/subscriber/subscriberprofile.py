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

class subscriberprofile(base_resource) :
    """Configuration for Subscriber Profile resource."""
    def __init__(self) :
        self._ip = ""
        self._subscriberrules = []
        self._subscriptionidtype = ""
        self._subscriptionidvalue = ""
        self._servicepath = ""
        self._flags = 0
        self._ttl = 0
        self._avpdisplaybuffer = ""
        self.___count = 0

    @property
    def ip(self) :
        """Subscriber ip address."""
        try :
            return self._ip
        except Exception as e:
            raise e

    @ip.setter
    def ip(self, ip) :
        """Subscriber ip address.

        :param ip: 

        """
        try :
            self._ip = ip
        except Exception as e:
            raise e

    @property
    def subscriberrules(self) :
        """Rules configured for this subscriber. This is similar to rules received from PCRF for dynamic subscriber sessions."""
        try :
            return self._subscriberrules
        except Exception as e:
            raise e

    @subscriberrules.setter
    def subscriberrules(self, subscriberrules) :
        """Rules configured for this subscriber. This is similar to rules received from PCRF for dynamic subscriber sessions.

        :param subscriberrules: 

        """
        try :
            self._subscriberrules = subscriberrules
        except Exception as e:
            raise e

    @property
    def subscriptionidtype(self) :
        """Subscription-Id type.<br/>Possible values = E164, IMSI, SIP_URI, NAI, PRIVATE."""
        try :
            return self._subscriptionidtype
        except Exception as e:
            raise e

    @subscriptionidtype.setter
    def subscriptionidtype(self, subscriptionidtype) :
        """Subscription-Id type.<br/>Possible values = E164, IMSI, SIP_URI, NAI, PRIVATE

        :param subscriptionidtype: 

        """
        try :
            self._subscriptionidtype = subscriptionidtype
        except Exception as e:
            raise e

    @property
    def subscriptionidvalue(self) :
        """Subscription-Id value."""
        try :
            return self._subscriptionidvalue
        except Exception as e:
            raise e

    @subscriptionidvalue.setter
    def subscriptionidvalue(self, subscriptionidvalue) :
        """Subscription-Id value.

        :param subscriptionidvalue: 

        """
        try :
            self._subscriptionidvalue = subscriptionidvalue
        except Exception as e:
            raise e

    @property
    def servicepath(self) :
        """Name of the servicepath to be taken for this subscriber."""
        try :
            return self._servicepath
        except Exception as e:
            raise e

    @servicepath.setter
    def servicepath(self, servicepath) :
        """Name of the servicepath to be taken for this subscriber.

        :param servicepath: 

        """
        try :
            self._servicepath = servicepath
        except Exception as e:
            raise e

    @property
    def flags(self) :
        """Subscriber Session flags."""
        try :
            return self._flags
        except Exception as e:
            raise e

    @property
    def ttl(self) :
        """Subscriber Session TTL."""
        try :
            return self._ttl
        except Exception as e:
            raise e

    @property
    def avpdisplaybuffer(self) :
        """Subscriber Attributes Display."""
        try :
            return self._avpdisplaybuffer
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(subscriberprofile_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.subscriberprofile
        except Exception as e :
            raise e

    def _get_object_name(self) :
        """Returns the value of object identifier argument"""
        try :
            if self.ip is not None :
                return str(self.ip)
            return None
        except Exception as e :
            raise e



    @classmethod
    def add(cls, client, resource) :
        """Use this API to add subscriberprofile.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                addresource = subscriberprofile()
                addresource.ip = resource.ip
                addresource.subscriberrules = resource.subscriberrules
                addresource.subscriptionidtype = resource.subscriptionidtype
                addresource.subscriptionidvalue = resource.subscriptionidvalue
                addresource.servicepath = resource.servicepath
                return addresource.add_resource(client)
            else :
                if (resource and len(resource) > 0) :
                    addresources = [ subscriberprofile() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        addresources[i].ip = resource[i].ip
                        addresources[i].subscriberrules = resource[i].subscriberrules
                        addresources[i].subscriptionidtype = resource[i].subscriptionidtype
                        addresources[i].subscriptionidvalue = resource[i].subscriptionidvalue
                        addresources[i].servicepath = resource[i].servicepath
                result = cls.add_bulk_request(client, addresources)
            return result
        except Exception as e :
            raise e

    @classmethod
    def update(cls, client, resource) :
        """Use this API to update subscriberprofile.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                updateresource = subscriberprofile()
                updateresource.ip = resource.ip
                updateresource.subscriberrules = resource.subscriberrules
                updateresource.subscriptionidtype = resource.subscriptionidtype
                updateresource.subscriptionidvalue = resource.subscriptionidvalue
                updateresource.servicepath = resource.servicepath
                return updateresource.update_resource(client)
            else :
                if (resource and len(resource) > 0) :
                    updateresources = [ subscriberprofile() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        updateresources[i].ip = resource[i].ip
                        updateresources[i].subscriberrules = resource[i].subscriberrules
                        updateresources[i].subscriptionidtype = resource[i].subscriptionidtype
                        updateresources[i].subscriptionidvalue = resource[i].subscriptionidvalue
                        updateresources[i].servicepath = resource[i].servicepath
                result = cls.update_bulk_request(client, updateresources)
            return result
        except Exception as e :
            raise e

    @classmethod
    def unset(cls, client, resource, args) :
        """Use this API to unset the properties of subscriberprofile resource.
        Properties that need to be unset are specified in args array.

        :param client: 
        :param resource: 
        :param args: 

        """
        try :
            if type(resource) is not list :
                unsetresource = subscriberprofile()
                if type(resource) !=  type(unsetresource):
                    unsetresource.ip = resource
                else :
                    unsetresource.ip = resource.ip
                return unsetresource.unset_resource(client, args)
            else :
                if type(resource[0]) != cls :
                    if (resource and len(resource) > 0) :
                        unsetresources = [ subscriberprofile() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            unsetresources[i].ip = resource[i]
                else :
                    if (resource and len(resource) > 0) :
                        unsetresources = [ subscriberprofile() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            unsetresources[i].ip = resource[i].ip
                result = cls.unset_bulk_request(client, unsetresources, args)
            return result
        except Exception as e :
            raise e

    @classmethod
    def delete(cls, client, resource) :
        """Use this API to delete subscriberprofile.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                deleteresource = subscriberprofile()
                if type(resource) !=  type(deleteresource):
                    deleteresource.ip = resource
                else :
                    deleteresource.ip = resource.ip
                return deleteresource.delete_resource(client)
            else :
                if type(resource[0]) != cls :
                    if (resource and len(resource) > 0) :
                        deleteresources = [ subscriberprofile() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            deleteresources[i].ip = resource[i]
                else :
                    if (resource and len(resource) > 0) :
                        deleteresources = [ subscriberprofile() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            deleteresources[i].ip = resource[i].ip
                result = cls.delete_bulk_request(client, deleteresources)
            return result
        except Exception as e :
            raise e

    @classmethod
    def get(cls, client, name="", option_="") :
        """Use this API to fetch all the subscriberprofile resources that are configured on netscaler.

        :param client: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            if not name :
                obj = subscriberprofile()
                response = obj.get_resources(client, option_)
            else :
                if type(name) != cls :
                    if type(name) is not list :
                        obj = subscriberprofile()
                        obj.ip = name
                        response = obj.get_resource(client, option_)
                    else :
                        if name and len(name) > 0 :
                            response = [subscriberprofile() for _ in range(len(name))]
                            obj = [subscriberprofile() for _ in range(len(name))]
                            for i in range(len(name)) :
                                obj[i] = subscriberprofile()
                                obj[i].ip = name[i]
                                response[i] = obj[i].get_resource(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def get_filtered(cls, client, filter_) :
        """Use this API to fetch filtered set of subscriberprofile resources.
        filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = subscriberprofile()
            option_ = options()
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def count(cls, client) :
        """Use this API to count the subscriberprofile resources configured on NetScaler.

        :param client: 

        """
        try :
            obj = subscriberprofile()
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
        """Use this API to count filtered the set of subscriberprofile resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = subscriberprofile()
            option_ = options()
            option_.count = True
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            if response :
                return response[0].__dict__['___count']
            return 0
        except Exception as e :
            raise e


    class Subscriptionidtype:
        """ """
        E164 = "E164"
        IMSI = "IMSI"
        SIP_URI = "SIP_URI"
        NAI = "NAI"
        PRIVATE = "PRIVATE"

class subscriberprofile_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.subscriberprofile = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.subscriberprofile = [subscriberprofile() for _ in range(length)]

