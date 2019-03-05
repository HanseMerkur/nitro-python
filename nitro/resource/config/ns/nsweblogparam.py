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

class nsweblogparam(base_resource) :
    """Configuration for Web log parameters resource."""
    def __init__(self) :
        self._buffersizemb = 0
        self._customreqhdrs = []
        self._customrsphdrs = []

    @property
    def buffersizemb(self) :
        """Buffer size, in MB, allocated for log transaction data on the system. The maximum value is limited to the memory available on the system.<br/>Default value: 16<br/>Minimum length =  1<br/>Maximum length =  4294967294LU."""
        try :
            return self._buffersizemb
        except Exception as e:
            raise e

    @buffersizemb.setter
    def buffersizemb(self, buffersizemb) :
        """Buffer size, in MB, allocated for log transaction data on the system. The maximum value is limited to the memory available on the system.<br/>Default value: 16<br/>Minimum length =  1<br/>Maximum length =  4294967294LU

        :param buffersizemb: 

        """
        try :
            self._buffersizemb = buffersizemb
        except Exception as e:
            raise e

    @property
    def customreqhdrs(self) :
        """Name(s) of HTTP request headers whose values should be exported by the Web Logging feature.<br/>Minimum length =  1."""
        try :
            return self._customreqhdrs
        except Exception as e:
            raise e

    @customreqhdrs.setter
    def customreqhdrs(self, customreqhdrs) :
        """Name(s) of HTTP request headers whose values should be exported by the Web Logging feature.<br/>Minimum length =  1

        :param customreqhdrs: 

        """
        try :
            self._customreqhdrs = customreqhdrs
        except Exception as e:
            raise e

    @property
    def customrsphdrs(self) :
        """Name(s) of HTTP response headers whose values should be exported by the Web Logging feature.<br/>Minimum length =  1."""
        try :
            return self._customrsphdrs
        except Exception as e:
            raise e

    @customrsphdrs.setter
    def customrsphdrs(self, customrsphdrs) :
        """Name(s) of HTTP response headers whose values should be exported by the Web Logging feature.<br/>Minimum length =  1

        :param customrsphdrs: 

        """
        try :
            self._customrsphdrs = customrsphdrs
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(nsweblogparam_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.nsweblogparam
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
        """Use this API to update nsweblogparam.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                updateresource = nsweblogparam()
                updateresource.buffersizemb = resource.buffersizemb
                updateresource.customreqhdrs = resource.customreqhdrs
                updateresource.customrsphdrs = resource.customrsphdrs
                return updateresource.update_resource(client)
        except Exception as e :
            raise e

    @classmethod
    def unset(cls, client, resource, args) :
        """Use this API to unset the properties of nsweblogparam resource.
        Properties that need to be unset are specified in args array.

        :param client: 
        :param resource: 
        :param args: 

        """
        try :
            if type(resource) is not list :
                unsetresource = nsweblogparam()
                return unsetresource.unset_resource(client, args)
        except Exception as e :
            raise e

    @classmethod
    def get(cls, client, name="", option_="") :
        """Use this API to fetch all the nsweblogparam resources that are configured on netscaler.

        :param client: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            if not name :
                obj = nsweblogparam()
                response = obj.get_resources(client, option_)
            return response
        except Exception as e :
            raise e


class nsweblogparam_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.nsweblogparam = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.nsweblogparam = [nsweblogparam() for _ in range(length)]

