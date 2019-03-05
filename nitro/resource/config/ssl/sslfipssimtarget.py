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

class sslfipssimtarget(base_resource) :
    """Configuration for FIPS SIM Target resource."""
    def __init__(self) :
        self._keyvector = ""
        self._sourcesecret = ""
        self._certfile = ""
        self._targetsecret = ""

    @property
    def keyvector(self) :
        """Name of and, optionally, path to the target FIPS appliance's key vector. /nsconfig/ssl/ is the default path.<br/>Minimum length =  1."""
        try :
            return self._keyvector
        except Exception as e:
            raise e

    @keyvector.setter
    def keyvector(self, keyvector) :
        """Name of and, optionally, path to the target FIPS appliance's key vector. /nsconfig/ssl/ is the default path.<br/>Minimum length =  1

        :param keyvector: 

        """
        try :
            self._keyvector = keyvector
        except Exception as e:
            raise e

    @property
    def sourcesecret(self) :
        """Name of and, optionally, path to the source FIPS appliance's secret data. /nsconfig/ssl/ is the default path.<br/>Minimum length =  1."""
        try :
            return self._sourcesecret
        except Exception as e:
            raise e

    @sourcesecret.setter
    def sourcesecret(self, sourcesecret) :
        """Name of and, optionally, path to the source FIPS appliance's secret data. /nsconfig/ssl/ is the default path.<br/>Minimum length =  1

        :param sourcesecret: 

        """
        try :
            self._sourcesecret = sourcesecret
        except Exception as e:
            raise e

    @property
    def certfile(self) :
        """Name of and, optionally, path to the source FIPS appliance's certificate file. /nsconfig/ssl/ is the default path.<br/>Minimum length =  1."""
        try :
            return self._certfile
        except Exception as e:
            raise e

    @certfile.setter
    def certfile(self, certfile) :
        """Name of and, optionally, path to the source FIPS appliance's certificate file. /nsconfig/ssl/ is the default path.<br/>Minimum length =  1

        :param certfile: 

        """
        try :
            self._certfile = certfile
        except Exception as e:
            raise e

    @property
    def targetsecret(self) :
        """Name for and, optionally, path to the target FIPS appliance's secret data. The default input path for the secret data is /nsconfig/ssl/.<br/>Minimum length =  1."""
        try :
            return self._targetsecret
        except Exception as e:
            raise e

    @targetsecret.setter
    def targetsecret(self, targetsecret) :
        """Name for and, optionally, path to the target FIPS appliance's secret data. The default input path for the secret data is /nsconfig/ssl/.<br/>Minimum length =  1

        :param targetsecret: 

        """
        try :
            self._targetsecret = targetsecret
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(sslfipssimtarget_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.sslfipssimtarget
        except Exception as e :
            raise e

    def _get_object_name(self) :
        """Returns the value of object identifier argument"""
        try :
            return 0
        except Exception as e :
            raise e



    @classmethod
    def enable(cls, client, resource) :
        """Use this API to enable sslfipssimtarget.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                enableresource = sslfipssimtarget()
                enableresource.keyvector = resource.keyvector
                enableresource.sourcesecret = resource.sourcesecret
                return enableresource.perform_operation(client,"enable")
        except Exception as e :
            raise e

    @classmethod
    def init(cls, client, resource) :
        """Use this API to init sslfipssimtarget.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                initresource = sslfipssimtarget()
                initresource.certfile = resource.certfile
                initresource.keyvector = resource.keyvector
                initresource.targetsecret = resource.targetsecret
                return initresource.perform_operation(client,"init")
        except Exception as e :
            raise e

class sslfipssimtarget_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.sslfipssimtarget = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.sslfipssimtarget = [sslfipssimtarget() for _ in range(length)]

