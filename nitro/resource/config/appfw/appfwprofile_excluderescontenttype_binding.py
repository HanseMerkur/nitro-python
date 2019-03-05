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

class appfwprofile_excluderescontenttype_binding(base_resource) :
    """Binding class showing the excluderescontenttype that can be bound to appfwprofile."""
    def __init__(self) :
        self._excluderescontenttype = ""
        self._state = ""
        self._comment = ""
        self._name = ""
        self.___count = 0

    @property
    def excluderescontenttype(self) :
        """A regular expression that represents the content type of the response that are to be excluded from inspection."""
        try :
            return self._excluderescontenttype
        except Exception as e:
            raise e

    @excluderescontenttype.setter
    def excluderescontenttype(self, excluderescontenttype) :
        """A regular expression that represents the content type of the response that are to be excluded from inspection.

        :param excluderescontenttype: 

        """
        try :
            self._excluderescontenttype = excluderescontenttype
        except Exception as e:
            raise e

    @property
    def name(self) :
        """Name of the profile to which to bind an exemption or rule.<br/>Minimum length =  1."""
        try :
            return self._name
        except Exception as e:
            raise e

    @name.setter
    def name(self, name) :
        """Name of the profile to which to bind an exemption or rule.<br/>Minimum length =  1

        :param name: 

        """
        try :
            self._name = name
        except Exception as e:
            raise e

    @property
    def state(self) :
        """Enabled.<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._state
        except Exception as e:
            raise e

    @state.setter
    def state(self, state) :
        """Enabled.<br/>Possible values = ENABLED, DISABLED

        :param state: 

        """
        try :
            self._state = state
        except Exception as e:
            raise e

    @property
    def comment(self) :
        """Any comments about the purpose of profile, or other useful information about the profile."""
        try :
            return self._comment
        except Exception as e:
            raise e

    @comment.setter
    def comment(self, comment) :
        """Any comments about the purpose of profile, or other useful information about the profile.

        :param comment: 

        """
        try :
            self._comment = comment
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(appfwprofile_excluderescontenttype_binding_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.appfwprofile_excluderescontenttype_binding
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
        """

        :param client: 
        :param resource: 

        """
        try :
            if resource and type(resource) is not list :
                updateresource = appfwprofile_excluderescontenttype_binding()
                updateresource.name = resource.name
                updateresource.comment = resource.comment
                updateresource.state = resource.state
                updateresource.excluderescontenttype = resource.excluderescontenttype
                return updateresource.update_resource(client)
            else :
                if resource and len(resource) > 0 :
                    updateresources = [appfwprofile_excluderescontenttype_binding() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        updateresources[i].name = resource[i].name
                        updateresources[i].comment = resource[i].comment
                        updateresources[i].state = resource[i].state
                        updateresources[i].excluderescontenttype = resource[i].excluderescontenttype
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
                deleteresource = appfwprofile_excluderescontenttype_binding()
                deleteresource.name = resource.name
                deleteresource.excluderescontenttype = resource.excluderescontenttype
                return deleteresource.delete_resource(client)
            else :
                if resource and len(resource) > 0 :
                    deleteresources = [appfwprofile_excluderescontenttype_binding() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        deleteresources[i].name = resource[i].name
                        deleteresources[i].excluderescontenttype = resource[i].excluderescontenttype
                return cls.delete_bulk_request(client, deleteresources)
        except Exception as e :
            raise e

    @classmethod
    def get(cls, service, name) :
        """Use this API to fetch appfwprofile_excluderescontenttype_binding resources.

        :param service: 
        :param name: 

        """
        try :
            obj = appfwprofile_excluderescontenttype_binding()
            obj.name = name
            response = obj.get_resources(service)
            return response
        except Exception as e:
            raise e

    @classmethod
    def get_filtered(cls, service, name, filter_) :
        """Use this API to fetch filtered set of appfwprofile_excluderescontenttype_binding resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param service: 
        :param name: 
        :param filter_: 

        """
        try :
            obj = appfwprofile_excluderescontenttype_binding()
            obj.name = name
            option_ = options()
            option_.filter = filter_
            response = obj.getfiltered(service, option_)
            return response
        except Exception as e:
            raise e

    @classmethod
    def count(cls, service, name) :
        """Use this API to count appfwprofile_excluderescontenttype_binding resources configued on NetScaler.

        :param service: 
        :param name: 

        """
        try :
            obj = appfwprofile_excluderescontenttype_binding()
            obj.name = name
            option_ = options()
            option_.count = True
            response = obj.get_resources(service, option_)
            if response :
                return response[0].__dict__['___count']
            return 0
        except Exception as e:
            raise e

    @classmethod
    def count_filtered(cls, service, name, filter_) :
        """Use this API to count the filtered set of appfwprofile_excluderescontenttype_binding resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param service: 
        :param name: 
        :param filter_: 

        """
        try :
            obj = appfwprofile_excluderescontenttype_binding()
            obj.name = name
            option_ = options()
            option_.count = True
            option_.filter = filter_
            response = obj.getfiltered(service, option_)
            if response :
                return response[0].__dict__['___count']
            return 0
        except Exception as e:
            raise e

    class As_scan_location_xmlsql:
        """ """
        ELEMENT = "ELEMENT"
        ATTRIBUTE = "ATTRIBUTE"

    class Xmlmaxelementdepthcheck:
        """ """
        ON = "ON"
        OFF = "OFF"

    class Xmlmaxattachmentsizecheck:
        """ """
        ON = "ON"
        OFF = "OFF"

    class Xmlsoaparraycheck:
        """ """
        ON = "ON"
        OFF = "OFF"

    class State:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Xmlmaxelementnamelengthcheck:
        """ """
        ON = "ON"
        OFF = "OFF"

    class Isregex_ff:
        """ """
        REGEX = "REGEX"
        NOTREGEX = "NOTREGEX"

    class Xmlmaxelementscheck:
        """ """
        ON = "ON"
        OFF = "OFF"

    class Xmlendpointcheck:
        """ """
        ABSOLUTE = "ABSOLUTE"
        RELATIVE = "RELATIVE"

    class Xmlmaxnamespacescheck:
        """ """
        ON = "ON"
        OFF = "OFF"

    class Xmlmaxfilesizecheck:
        """ """
        ON = "ON"
        OFF = "OFF"

    class Xmlmaxattributenamelengthcheck:
        """ """
        ON = "ON"
        OFF = "OFF"

    class Isvalueregex_xss:
        """ """
        REGEX = "REGEX"
        NOTREGEX = "NOTREGEX"

    class Xmlblockdtd:
        """ """
        ON = "ON"
        OFF = "OFF"

    class Xmlblockpi:
        """ """
        ON = "ON"
        OFF = "OFF"

    class Isregex_sql:
        """ """
        REGEX = "REGEX"
        NOTREGEX = "NOTREGEX"

    class Xmlvalidateresponse:
        """ """
        ON = "ON"
        OFF = "OFF"

    class Xmlmaxelementchildrencheck:
        """ """
        ON = "ON"
        OFF = "OFF"

    class Isregex:
        """ """
        REGEX = "REGEX"
        NOTREGEX = "NOTREGEX"

    class Xmlmaxentityexpansionscheck:
        """ """
        ON = "ON"
        OFF = "OFF"

    class Xmlmaxnamespaceurilengthcheck:
        """ """
        ON = "ON"
        OFF = "OFF"

    class As_scan_location_xss:
        """ """
        FORMFIELD = "FORMFIELD"
        HEADER = "HEADER"
        COOKIE = "COOKIE"

    class Xmlmaxentityexpansiondepthcheck:
        """ """
        ON = "ON"
        OFF = "OFF"

    class As_scan_location_xmlxss:
        """ """
        ELEMENT = "ELEMENT"
        ATTRIBUTE = "ATTRIBUTE"

    class Isregex_ffc:
        """ """
        REGEX = "REGEX"
        NOTREGEX = "NOTREGEX"

    class As_scan_location_sql:
        """ """
        FORMFIELD = "FORMFIELD"
        HEADER = "HEADER"
        COOKIE = "COOKIE"

    class Isvalueregex_sql:
        """ """
        REGEX = "REGEX"
        NOTREGEX = "NOTREGEX"

    class Xmlmaxattributevaluelengthcheck:
        """ """
        ON = "ON"
        OFF = "OFF"

    class Xmlattachmentcontenttypecheck:
        """ """
        ON = "ON"
        OFF = "OFF"

    class Isregex_xmlsql:
        """ """
        REGEX = "REGEX"
        NOTREGEX = "NOTREGEX"

    class Xmlvalidatesoapenvelope:
        """ """
        ON = "ON"
        OFF = "OFF"

    class Xmlmaxchardatalengthcheck:
        """ """
        ON = "ON"
        OFF = "OFF"

    class Xmlminfilesizecheck:
        """ """
        ON = "ON"
        OFF = "OFF"

    class Isregex_xss:
        """ """
        REGEX = "REGEX"
        NOTREGEX = "NOTREGEX"

    class As_value_type_sql:
        """ """
        Keyword = "Keyword"
        SpecialString = "SpecialString"
        Wildchar = "Wildchar"

    class Isregex_xmlxss:
        """ """
        REGEX = "REGEX"
        NOTREGEX = "NOTREGEX"

    class Xmladditionalsoapheaders:
        """ """
        ON = "ON"
        OFF = "OFF"

    class Xmlmaxattributescheck:
        """ """
        ON = "ON"
        OFF = "OFF"

    class Action:
        """ """
        none = "none"
        block = "block"
        log = "log"
        remove = "remove"
        stats = "stats"
        xout = "xout"

    class As_value_type_xss:
        """ """
        Tag = "Tag"
        Attribute = "Attribute"
        Pattern = "Pattern"

    class Xmlblockexternalentities:
        """ """
        ON = "ON"
        OFF = "OFF"

class appfwprofile_excluderescontenttype_binding_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.appfwprofile_excluderescontenttype_binding = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.appfwprofile_excluderescontenttype_binding = [appfwprofile_excluderescontenttype_binding() for _ in range(length)]

