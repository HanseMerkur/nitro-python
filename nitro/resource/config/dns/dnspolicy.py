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

class dnspolicy(base_resource) :
    """Configuration for DNS policy resource."""
    def __init__(self) :
        self._name = ""
        self._rule = ""
        self._viewname = ""
        self._preferredlocation = ""
        self._preferredloclist = []
        self._drop = ""
        self._cachebypass = ""
        self._actionname = ""
        self._logaction = ""
        self._hits = 0
        self._undefhits = 0
        self._description = ""
        self._builtin = []
        self.___count = 0

    @property
    def name(self) :
        """Name for the DNS policy."""
        try :
            return self._name
        except Exception as e:
            raise e

    @name.setter
    def name(self, name) :
        """Name for the DNS policy.

        :param name: 

        """
        try :
            self._name = name
        except Exception as e:
            raise e

    @property
    def rule(self) :
        """Expression against which DNS traffic is evaluated. Written in the default syntax.
        Note:
        * On the command line interface, if the expression includes blank spaces, the entire expression must be enclosed in double quotation marks.
        * If the expression itself includes double quotation marks, you must escape the quotations by using the  character.
        * Alternatively, you can use single quotation marks to enclose the rule, in which case you do not have to escape the double quotation marks.
        Maximum length of a string literal in the expression is 255 characters. A longer string can be split into smaller strings of up to 255 characters each, and the smaller strings concatenated with the + operator. For example, you can create a 500-character string as follows: '"<string of 255 characters>" + "<string of 245 characters>"'
        Example: CLIENT.UDP.DNS.DOMAIN.EQ("domainname").


        """
        try :
            return self._rule
        except Exception as e:
            raise e

    @rule.setter
    def rule(self, rule) :
        """Expression against which DNS traffic is evaluated. Written in the default syntax.
        Note:
        * On the command line interface, if the expression includes blank spaces, the entire expression must be enclosed in double quotation marks.
        * If the expression itself includes double quotation marks, you must escape the quotations by using the  character.
        * Alternatively, you can use single quotation marks to enclose the rule, in which case you do not have to escape the double quotation marks.
        Maximum length of a string literal in the expression is 255 characters. A longer string can be split into smaller strings of up to 255 characters each, and the smaller strings concatenated with the + operator. For example, you can create a 500-character string as follows: '"<string of 255 characters>" + "<string of 245 characters>"'
        Example: CLIENT.UDP.DNS.DOMAIN.EQ("domainname").

        :param rule: 

        """
        try :
            self._rule = rule
        except Exception as e:
            raise e

    @property
    def viewname(self) :
        """The view name that must be used for the given policy."""
        try :
            return self._viewname
        except Exception as e:
            raise e

    @viewname.setter
    def viewname(self, viewname) :
        """The view name that must be used for the given policy.

        :param viewname: 

        """
        try :
            self._viewname = viewname
        except Exception as e:
            raise e

    @property
    def preferredlocation(self) :
        """The location used for the given policy. This is deprecated attribute. Please use -prefLocList."""
        try :
            return self._preferredlocation
        except Exception as e:
            raise e

    @preferredlocation.setter
    def preferredlocation(self, preferredlocation) :
        """The location used for the given policy. This is deprecated attribute. Please use -prefLocList.

        :param preferredlocation: 

        """
        try :
            self._preferredlocation = preferredlocation
        except Exception as e:
            raise e

    @property
    def preferredloclist(self) :
        """The location list in priority order used for the given policy.<br/>Minimum length =  1."""
        try :
            return self._preferredloclist
        except Exception as e:
            raise e

    @preferredloclist.setter
    def preferredloclist(self, preferredloclist) :
        """The location list in priority order used for the given policy.<br/>Minimum length =  1

        :param preferredloclist: 

        """
        try :
            self._preferredloclist = preferredloclist
        except Exception as e:
            raise e

    @property
    def drop(self) :
        """The dns packet must be dropped.<br/>Possible values = YES, NO."""
        try :
            return self._drop
        except Exception as e:
            raise e

    @drop.setter
    def drop(self, drop) :
        """The dns packet must be dropped.<br/>Possible values = YES, NO

        :param drop: 

        """
        try :
            self._drop = drop
        except Exception as e:
            raise e

    @property
    def cachebypass(self) :
        """By pass dns cache for this.<br/>Possible values = YES, NO."""
        try :
            return self._cachebypass
        except Exception as e:
            raise e

    @cachebypass.setter
    def cachebypass(self, cachebypass) :
        """By pass dns cache for this.<br/>Possible values = YES, NO

        :param cachebypass: 

        """
        try :
            self._cachebypass = cachebypass
        except Exception as e:
            raise e

    @property
    def actionname(self) :
        """Name of the DNS action to perform when the rule evaluates to TRUE. The built in actions function as follows:
        * dns_default_act_Drop. Drop the DNS request.
        * dns_default_act_Cachebypass. Bypass the DNS cache and forward the request to the name server.
        You can create custom actions by using the add dns action command in the CLI or the DNS > Actions > Create DNS Action dialog box in the NetScaler configuration utility.


        """
        try :
            return self._actionname
        except Exception as e:
            raise e

    @actionname.setter
    def actionname(self, actionname) :
        """Name of the DNS action to perform when the rule evaluates to TRUE. The built in actions function as follows:
        * dns_default_act_Drop. Drop the DNS request.
        * dns_default_act_Cachebypass. Bypass the DNS cache and forward the request to the name server.
        You can create custom actions by using the add dns action command in the CLI or the DNS > Actions > Create DNS Action dialog box in the NetScaler configuration utility.

        :param actionname: 

        """
        try :
            self._actionname = actionname
        except Exception as e:
            raise e

    @property
    def logaction(self) :
        """Name of the messagelog action to use for requests that match this policy."""
        try :
            return self._logaction
        except Exception as e:
            raise e

    @logaction.setter
    def logaction(self, logaction) :
        """Name of the messagelog action to use for requests that match this policy.

        :param logaction: 

        """
        try :
            self._logaction = logaction
        except Exception as e:
            raise e

    @property
    def hits(self) :
        """The number of times the policy has been hit."""
        try :
            return self._hits
        except Exception as e:
            raise e

    @property
    def undefhits(self) :
        """Number of Undef hits."""
        try :
            return self._undefhits
        except Exception as e:
            raise e

    @property
    def description(self) :
        """Description of the policy."""
        try :
            return self._description
        except Exception as e:
            raise e

    @property
    def builtin(self) :
        """Flag to determine whether DNS policy is default or not.<br/>Possible values = MODIFIABLE, DELETABLE, IMMUTABLE, PARTITION_ALL."""
        try :
            return self._builtin
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(dnspolicy_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.dnspolicy
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
        """Use this API to add dnspolicy.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                addresource = dnspolicy()
                addresource.name = resource.name
                addresource.rule = resource.rule
                addresource.viewname = resource.viewname
                addresource.preferredlocation = resource.preferredlocation
                addresource.preferredloclist = resource.preferredloclist
                addresource.drop = resource.drop
                addresource.cachebypass = resource.cachebypass
                addresource.actionname = resource.actionname
                addresource.logaction = resource.logaction
                return addresource.add_resource(client)
            else :
                if (resource and len(resource) > 0) :
                    addresources = [ dnspolicy() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        addresources[i].name = resource[i].name
                        addresources[i].rule = resource[i].rule
                        addresources[i].viewname = resource[i].viewname
                        addresources[i].preferredlocation = resource[i].preferredlocation
                        addresources[i].preferredloclist = resource[i].preferredloclist
                        addresources[i].drop = resource[i].drop
                        addresources[i].cachebypass = resource[i].cachebypass
                        addresources[i].actionname = resource[i].actionname
                        addresources[i].logaction = resource[i].logaction
                result = cls.add_bulk_request(client, addresources)
            return result
        except Exception as e :
            raise e

    @classmethod
    def delete(cls, client, resource) :
        """Use this API to delete dnspolicy.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                deleteresource = dnspolicy()
                if type(resource) !=  type(deleteresource):
                    deleteresource.name = resource
                else :
                    deleteresource.name = resource.name
                return deleteresource.delete_resource(client)
            else :
                if type(resource[0]) != cls :
                    if (resource and len(resource) > 0) :
                        deleteresources = [ dnspolicy() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            deleteresources[i].name = resource[i]
                else :
                    if (resource and len(resource) > 0) :
                        deleteresources = [ dnspolicy() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            deleteresources[i].name = resource[i].name
                result = cls.delete_bulk_request(client, deleteresources)
            return result
        except Exception as e :
            raise e

    @classmethod
    def update(cls, client, resource) :
        """Use this API to update dnspolicy.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                updateresource = dnspolicy()
                updateresource.name = resource.name
                updateresource.rule = resource.rule
                updateresource.viewname = resource.viewname
                updateresource.preferredlocation = resource.preferredlocation
                updateresource.preferredloclist = resource.preferredloclist
                updateresource.drop = resource.drop
                updateresource.cachebypass = resource.cachebypass
                updateresource.actionname = resource.actionname
                updateresource.logaction = resource.logaction
                return updateresource.update_resource(client)
            else :
                if (resource and len(resource) > 0) :
                    updateresources = [ dnspolicy() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        updateresources[i].name = resource[i].name
                        updateresources[i].rule = resource[i].rule
                        updateresources[i].viewname = resource[i].viewname
                        updateresources[i].preferredlocation = resource[i].preferredlocation
                        updateresources[i].preferredloclist = resource[i].preferredloclist
                        updateresources[i].drop = resource[i].drop
                        updateresources[i].cachebypass = resource[i].cachebypass
                        updateresources[i].actionname = resource[i].actionname
                        updateresources[i].logaction = resource[i].logaction
                result = cls.update_bulk_request(client, updateresources)
            return result
        except Exception as e :
            raise e

    @classmethod
    def unset(cls, client, resource, args) :
        """Use this API to unset the properties of dnspolicy resource.
        Properties that need to be unset are specified in args array.

        :param client: 
        :param resource: 
        :param args: 

        """
        try :
            if type(resource) is not list :
                unsetresource = dnspolicy()
                if type(resource) !=  type(unsetresource):
                    unsetresource.name = resource
                else :
                    unsetresource.name = resource.name
                return unsetresource.unset_resource(client, args)
            else :
                if type(resource[0]) != cls :
                    if (resource and len(resource) > 0) :
                        unsetresources = [ dnspolicy() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            unsetresources[i].name = resource[i]
                else :
                    if (resource and len(resource) > 0) :
                        unsetresources = [ dnspolicy() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            unsetresources[i].name = resource[i].name
                result = cls.unset_bulk_request(client, unsetresources, args)
            return result
        except Exception as e :
            raise e

    @classmethod
    def get(cls, client, name="", option_="") :
        """Use this API to fetch all the dnspolicy resources that are configured on netscaler.

        :param client: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            if not name :
                obj = dnspolicy()
                response = obj.get_resources(client, option_)
            else :
                if type(name) != cls :
                    if type(name) is not list :
                        obj = dnspolicy()
                        obj.name = name
                        response = obj.get_resource(client, option_)
                    else :
                        if name and len(name) > 0 :
                            response = [dnspolicy() for _ in range(len(name))]
                            obj = [dnspolicy() for _ in range(len(name))]
                            for i in range(len(name)) :
                                obj[i] = dnspolicy()
                                obj[i].name = name[i]
                                response[i] = obj[i].get_resource(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def get_filtered(cls, client, filter_) :
        """Use this API to fetch filtered set of dnspolicy resources.
        filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = dnspolicy()
            option_ = options()
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def count(cls, client) :
        """Use this API to count the dnspolicy resources configured on NetScaler.

        :param client: 

        """
        try :
            obj = dnspolicy()
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
        """Use this API to count filtered the set of dnspolicy resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = dnspolicy()
            option_ = options()
            option_.count = True
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            if response :
                return response[0].__dict__['___count']
            return 0
        except Exception as e :
            raise e


    class Cachebypass:
        """ """
        YES = "YES"
        NO = "NO"

    class Builtin:
        """ """
        MODIFIABLE = "MODIFIABLE"
        DELETABLE = "DELETABLE"
        IMMUTABLE = "IMMUTABLE"
        PARTITION_ALL = "PARTITION_ALL"

    class Drop:
        """ """
        YES = "YES"
        NO = "NO"

class dnspolicy_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.dnspolicy = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.dnspolicy = [dnspolicy() for _ in range(length)]

