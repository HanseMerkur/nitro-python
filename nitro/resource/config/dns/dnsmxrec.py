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

class dnsmxrec(base_resource) :
    """Configuration for MX record resource."""
    def __init__(self) :
        self._domain = ""
        self._mx = ""
        self._pref = 0
        self._ttl = 0
        self._type = ""
        self._authtype = ""
        self.___count = 0

    @property
    def domain(self) :
        """Domain name for which to add the MX record.<br/>Minimum length =  1."""
        try :
            return self._domain
        except Exception as e:
            raise e

    @domain.setter
    def domain(self, domain) :
        """Domain name for which to add the MX record.<br/>Minimum length =  1

        :param domain: 

        """
        try :
            self._domain = domain
        except Exception as e:
            raise e

    @property
    def mx(self) :
        """Host name of the mail exchange server.<br/>Minimum length =  1."""
        try :
            return self._mx
        except Exception as e:
            raise e

    @mx.setter
    def mx(self, mx) :
        """Host name of the mail exchange server.<br/>Minimum length =  1

        :param mx: 

        """
        try :
            self._mx = mx
        except Exception as e:
            raise e

    @property
    def pref(self) :
        """Priority number to assign to the mail exchange server. A domain name can have multiple mail servers, with a priority number assigned to each server. The lower the priority number, the higher the mail server's priority. When other mail servers have to deliver mail to the specified domain, they begin with the mail server with the lowest priority number, and use other configured mail servers, in priority order, as backups.<br/>Maximum length =  65535."""
        try :
            return self._pref
        except Exception as e:
            raise e

    @pref.setter
    def pref(self, pref) :
        """Priority number to assign to the mail exchange server. A domain name can have multiple mail servers, with a priority number assigned to each server. The lower the priority number, the higher the mail server's priority. When other mail servers have to deliver mail to the specified domain, they begin with the mail server with the lowest priority number, and use other configured mail servers, in priority order, as backups.<br/>Maximum length =  65535

        :param pref: 

        """
        try :
            self._pref = pref
        except Exception as e:
            raise e

    @property
    def ttl(self) :
        """Time to Live (TTL), in seconds, for the record. TTL is the time for which the record must be cached by DNS proxies. The specified TTL is applied to all the resource records that are of the same record type and belong to the specified domain name. For example, if you add an address record, with a TTL of 36000, to the domain name example.com, the TTLs of all the address records of example.com are changed to 36000. If the TTL is not specified, the NetScaler appliance uses either the DNS zone's minimum TTL or, if the SOA record is not available on the appliance, the default value of 3600.<br/>Default value: 3600<br/>Maximum length =  2147483647."""
        try :
            return self._ttl
        except Exception as e:
            raise e

    @ttl.setter
    def ttl(self, ttl) :
        """Time to Live (TTL), in seconds, for the record. TTL is the time for which the record must be cached by DNS proxies. The specified TTL is applied to all the resource records that are of the same record type and belong to the specified domain name. For example, if you add an address record, with a TTL of 36000, to the domain name example.com, the TTLs of all the address records of example.com are changed to 36000. If the TTL is not specified, the NetScaler appliance uses either the DNS zone's minimum TTL or, if the SOA record is not available on the appliance, the default value of 3600.<br/>Default value: 3600<br/>Maximum length =  2147483647

        :param ttl: 

        """
        try :
            self._ttl = ttl
        except Exception as e:
            raise e

    @property
    def type(self) :
        """Type of records to display. Available settings function as follows:
        * ADNS - Display all authoritative address records.
        * PROXY - Display all proxy address records.
        * ALL - Display all address records.<br/>Default value: ADNS<br/>Possible values = ALL, ADNS, PROXY.


        """
        try :
            return self._type
        except Exception as e:
            raise e

    @type.setter
    def type(self, type) :
        """Type of records to display. Available settings function as follows:
        * ADNS - Display all authoritative address records.
        * PROXY - Display all proxy address records.
        * ALL - Display all address records.<br/>Default value: ADNS<br/>Possible values = ALL, ADNS, PROXY

        :param type: 

        """
        try :
            self._type = type
        except Exception as e:
            raise e

    @property
    def authtype(self) :
        """Record type.<br/>Possible values = ALL, ADNS, PROXY."""
        try :
            return self._authtype
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(dnsmxrec_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.dnsmxrec
        except Exception as e :
            raise e

    def _get_object_name(self) :
        """Returns the value of object identifier argument"""
        try :
            if self.domain is not None :
                return str(self.domain)
            return None
        except Exception as e :
            raise e



    @classmethod
    def add(cls, client, resource) :
        """Use this API to add dnsmxrec.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                addresource = dnsmxrec()
                addresource.domain = resource.domain
                addresource.mx = resource.mx
                addresource.pref = resource.pref
                addresource.ttl = resource.ttl
                return addresource.add_resource(client)
            else :
                if (resource and len(resource) > 0) :
                    addresources = [ dnsmxrec() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        addresources[i].domain = resource[i].domain
                        addresources[i].mx = resource[i].mx
                        addresources[i].pref = resource[i].pref
                        addresources[i].ttl = resource[i].ttl
                result = cls.add_bulk_request(client, addresources)
            return result
        except Exception as e :
            raise e

    @classmethod
    def delete(cls, client, resource) :
        """Use this API to delete dnsmxrec.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                deleteresource = dnsmxrec()
                if type(resource) !=  type(deleteresource):
                    deleteresource.domain = resource
                else :
                    deleteresource.domain = resource.domain
                    deleteresource.mx = resource.mx
                return deleteresource.delete_resource(client)
            else :
                if type(resource[0]) != cls :
                    if (resource and len(resource) > 0) :
                        deleteresources = [ dnsmxrec() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            deleteresources[i].domain = resource[i]
                else :
                    if (resource and len(resource) > 0) :
                        deleteresources = [ dnsmxrec() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            deleteresources[i].domain = resource[i].domain
                            deleteresources[i].mx = resource[i].mx
                result = cls.delete_bulk_request(client, deleteresources)
            return result
        except Exception as e :
            raise e

    @classmethod
    def update(cls, client, resource) :
        """Use this API to update dnsmxrec.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                updateresource = dnsmxrec()
                updateresource.domain = resource.domain
                updateresource.mx = resource.mx
                updateresource.pref = resource.pref
                updateresource.ttl = resource.ttl
                return updateresource.update_resource(client)
            else :
                if (resource and len(resource) > 0) :
                    updateresources = [ dnsmxrec() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        updateresources[i].domain = resource[i].domain
                        updateresources[i].mx = resource[i].mx
                        updateresources[i].pref = resource[i].pref
                        updateresources[i].ttl = resource[i].ttl
                result = cls.update_bulk_request(client, updateresources)
            return result
        except Exception as e :
            raise e

    @classmethod
    def unset(cls, client, resource, args) :
        """Use this API to unset the properties of dnsmxrec resource.
        Properties that need to be unset are specified in args array.

        :param client: 
        :param resource: 
        :param args: 

        """
        try :
            if type(resource) is not list :
                unsetresource = dnsmxrec()
                unsetresource.domain = resource.domain
                unsetresource.mx = resource.mx
                return unsetresource.unset_resource(client, args)
            else :
                if type(resource[0]) == cls :
                    if (resource and len(resource) > 0) :
                        unsetresources = [ dnsmxrec() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            unsetresources[i].domain = resource[i].domain
                            unsetresources[i].mx = resource[i].mx
                result = cls.unset_bulk_request(client, unsetresources, args)
            return result
        except Exception as e :
            raise e

    @classmethod
    def get(cls, client, name="", option_="") :
        """Use this API to fetch all the dnsmxrec resources that are configured on netscaler.

        :param client: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            if not name :
                obj = dnsmxrec()
                response = obj.get_resources(client, option_)
            else :
                if type(name) != cls :
                    if type(name) is not list :
                        obj = dnsmxrec()
                        obj.domain = name
                        response = obj.get_resource(client, option_)
                    else :
                        if name and len(name) > 0 :
                            response = [dnsmxrec() for _ in range(len(name))]
                            obj = [dnsmxrec() for _ in range(len(name))]
                            for i in range(len(name)) :
                                obj[i] = dnsmxrec()
                                obj[i].domain = name[i]
                                response[i] = obj[i].get_resource(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def get_args(cls, client, args) :
        """Use this API to fetch all the dnsmxrec resources that are configured on netscaler.
            # This uses dnsmxrec_args which is a way to provide additional arguments while fetching the resources.

        :param client: 
        :param args: 

        """
        try :
            obj = dnsmxrec()
            option_ = options()
            option_.args = nitro_util.object_to_string_withoutquotes(args)
            response = obj.get_resources(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def get_filtered(cls, client, filter_) :
        """Use this API to fetch filtered set of dnsmxrec resources.
        filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = dnsmxrec()
            option_ = options()
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def count(cls, client) :
        """Use this API to count the dnsmxrec resources configured on NetScaler.

        :param client: 

        """
        try :
            obj = dnsmxrec()
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
        """Use this API to count filtered the set of dnsmxrec resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = dnsmxrec()
            option_ = options()
            option_.count = True
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            if response :
                return response[0].__dict__['___count']
            return 0
        except Exception as e :
            raise e


    class Authtype:
        """ """
        ALL = "ALL"
        ADNS = "ADNS"
        PROXY = "PROXY"

    class Type:
        """ """
        ALL = "ALL"
        ADNS = "ADNS"
        PROXY = "PROXY"

class dnsmxrec_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.dnsmxrec = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.dnsmxrec = [dnsmxrec() for _ in range(length)]

