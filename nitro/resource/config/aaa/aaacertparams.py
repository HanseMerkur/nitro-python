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

class aaacertparams(base_resource) :
    """Configuration for certificate parameter resource."""
    def __init__(self) :
        self._usernamefield = ""
        self._groupnamefield = ""
        self._defaultauthenticationgroup = ""
        self._twofactor = ""

    @property
    def usernamefield(self) :
        """Client certificate field that contains the username, in the format <field>:<subfield>. ."""
        try :
            return self._usernamefield
        except Exception as e:
            raise e

    @usernamefield.setter
    def usernamefield(self, usernamefield) :
        """Client certificate field that contains the username, in the format <field>:<subfield>. .

        :param usernamefield: 

        """
        try :
            self._usernamefield = usernamefield
        except Exception as e:
            raise e

    @property
    def groupnamefield(self) :
        """Client certificate field that specifies the group, in the format <field>:<subfield>."""
        try :
            return self._groupnamefield
        except Exception as e:
            raise e

    @groupnamefield.setter
    def groupnamefield(self, groupnamefield) :
        """Client certificate field that specifies the group, in the format <field>:<subfield>.

        :param groupnamefield: 

        """
        try :
            self._groupnamefield = groupnamefield
        except Exception as e:
            raise e

    @property
    def defaultauthenticationgroup(self) :
        """This is the default group that is chosen when the authentication succeeds in addition to extracted groups.<br/>Maximum length =  64."""
        try :
            return self._defaultauthenticationgroup
        except Exception as e:
            raise e

    @defaultauthenticationgroup.setter
    def defaultauthenticationgroup(self, defaultauthenticationgroup) :
        """This is the default group that is chosen when the authentication succeeds in addition to extracted groups.<br/>Maximum length =  64

        :param defaultauthenticationgroup: 

        """
        try :
            self._defaultauthenticationgroup = defaultauthenticationgroup
        except Exception as e:
            raise e

    @property
    def twofactor(self) :
        """The state of the two-factor authentication.<br/>Possible values = ON, OFF."""
        try :
            return self._twofactor
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(aaacertparams_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.aaacertparams
        except Exception as e :
            raise e

    def _get_object_name(self) :
        """Returns the value of object identifier argument"""
        try :
            return 0
        except Exception as e :
            raise e



    @classmethod
    def update(cls, client, resource) :
        """Use this API to update aaacertparams.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                updateresource = aaacertparams()
                updateresource.usernamefield = resource.usernamefield
                updateresource.groupnamefield = resource.groupnamefield
                updateresource.defaultauthenticationgroup = resource.defaultauthenticationgroup
                return updateresource.update_resource(client)
        except Exception as e :
            raise e

    @classmethod
    def unset(cls, client, resource, args) :
        """Use this API to unset the properties of aaacertparams resource.
        Properties that need to be unset are specified in args array.

        :param client: 
        :param resource: 
        :param args: 

        """
        try :
            if type(resource) is not list :
                unsetresource = aaacertparams()
                return unsetresource.unset_resource(client, args)
        except Exception as e :
            raise e

    @classmethod
    def get(cls, client, name="", option_="") :
        """Use this API to fetch all the aaacertparams resources that are configured on netscaler.

        :param client: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            if not name :
                obj = aaacertparams()
                response = obj.get_resources(client, option_)
            return response
        except Exception as e :
            raise e


    class Twofactor:
        """ """
        ON = "ON"
        OFF = "OFF"

class aaacertparams_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.aaacertparams = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.aaacertparams = [aaacertparams() for _ in range(length)]

