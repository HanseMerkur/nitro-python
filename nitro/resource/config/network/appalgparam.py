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

class appalgparam(base_resource) :
    """Configuration for AppAlg Param resource."""
    def __init__(self) :
        self._pptpgreidletimeout = 0

    @property
    def pptpgreidletimeout(self) :
        """Interval in sec, after which data sessions of PPTP GRE is cleared.<br/>Default value: 9000<br/>Minimum length =  1<br/>Maximum length =  9000."""
        try :
            return self._pptpgreidletimeout
        except Exception as e:
            raise e

    @pptpgreidletimeout.setter
    def pptpgreidletimeout(self, pptpgreidletimeout) :
        """Interval in sec, after which data sessions of PPTP GRE is cleared.<br/>Default value: 9000<br/>Minimum length =  1<br/>Maximum length =  9000

        :param pptpgreidletimeout: 

        """
        try :
            self._pptpgreidletimeout = pptpgreidletimeout
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(appalgparam_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.appalgparam
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
        """Use this API to update appalgparam.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                updateresource = appalgparam()
                updateresource.pptpgreidletimeout = resource.pptpgreidletimeout
                return updateresource.update_resource(client)
        except Exception as e :
            raise e

    @classmethod
    def unset(cls, client, resource, args) :
        """Use this API to unset the properties of appalgparam resource.
        Properties that need to be unset are specified in args array.

        :param client: 
        :param resource: 
        :param args: 

        """
        try :
            if type(resource) is not list :
                unsetresource = appalgparam()
                return unsetresource.unset_resource(client, args)
        except Exception as e :
            raise e

    @classmethod
    def get(cls, client, name="", option_="") :
        """Use this API to fetch all the appalgparam resources that are configured on netscaler.

        :param client: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            if not name :
                obj = appalgparam()
                response = obj.get_resources(client, option_)
            return response
        except Exception as e :
            raise e


class appalgparam_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.appalgparam = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.appalgparam = [appalgparam() for _ in range(length)]

