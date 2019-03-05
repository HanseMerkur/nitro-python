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

class nsdiameter(base_resource) :
    """Configuration for Diameter Parameters resource."""
    def __init__(self) :
        self._identity = ""
        self._realm = ""
        self._serverclosepropagation = ""

    @property
    def identity(self) :
        """DiameterIdentity to be used by NS. DiameterIdentity is used to identify a Diameter node uniquely. Before setting up diameter configuration, Netscaler (as a Diameter node) MUST be assigned a unique DiameterIdentity.
        example =>
        set ns diameter -identity netscaler.com
        Now whenever Netscaler system needs to use identity in diameter messages. It will use 'netscaler.com' as Origin-Host AVP as defined in RFC3588
        .<br/>Minimum length =  1.


        """
        try :
            return self._identity
        except Exception as e:
            raise e

    @identity.setter
    def identity(self, identity) :
        """DiameterIdentity to be used by NS. DiameterIdentity is used to identify a Diameter node uniquely. Before setting up diameter configuration, Netscaler (as a Diameter node) MUST be assigned a unique DiameterIdentity.
        example =>
        set ns diameter -identity netscaler.com
        Now whenever Netscaler system needs to use identity in diameter messages. It will use 'netscaler.com' as Origin-Host AVP as defined in RFC3588
        .<br/>Minimum length =  1

        :param identity: 

        """
        try :
            self._identity = identity
        except Exception as e:
            raise e

    @property
    def realm(self) :
        """Diameter Realm to be used by NS.
        example =>
        set ns diameter -realm com
        Now whenever Netscaler system needs to use realm in diameter messages. It will use 'com' as Origin-Realm AVP as defined in RFC3588
        .<br/>Minimum length =  1.


        """
        try :
            return self._realm
        except Exception as e:
            raise e

    @realm.setter
    def realm(self, realm) :
        """Diameter Realm to be used by NS.
        example =>
        set ns diameter -realm com
        Now whenever Netscaler system needs to use realm in diameter messages. It will use 'com' as Origin-Realm AVP as defined in RFC3588
        .<br/>Minimum length =  1

        :param realm: 

        """
        try :
            self._realm = realm
        except Exception as e:
            raise e

    @property
    def serverclosepropagation(self) :
        """when a Server connection goes down, whether to close the corresponding client connection if there were requests pending on the server.<br/>Default value: NO<br/>Possible values = YES, NO."""
        try :
            return self._serverclosepropagation
        except Exception as e:
            raise e

    @serverclosepropagation.setter
    def serverclosepropagation(self, serverclosepropagation) :
        """when a Server connection goes down, whether to close the corresponding client connection if there were requests pending on the server.<br/>Default value: NO<br/>Possible values = YES, NO

        :param serverclosepropagation: 

        """
        try :
            self._serverclosepropagation = serverclosepropagation
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(nsdiameter_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.nsdiameter
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
        """Use this API to update nsdiameter.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                updateresource = nsdiameter()
                updateresource.identity = resource.identity
                updateresource.realm = resource.realm
                updateresource.serverclosepropagation = resource.serverclosepropagation
                return updateresource.update_resource(client)
        except Exception as e :
            raise e

    @classmethod
    def unset(cls, client, resource, args) :
        """Use this API to unset the properties of nsdiameter resource.
        Properties that need to be unset are specified in args array.

        :param client: 
        :param resource: 
        :param args: 

        """
        try :
            if type(resource) is not list :
                unsetresource = nsdiameter()
                return unsetresource.unset_resource(client, args)
        except Exception as e :
            raise e

    @classmethod
    def get(cls, client, name="", option_="") :
        """Use this API to fetch all the nsdiameter resources that are configured on netscaler.

        :param client: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            if not name :
                obj = nsdiameter()
                response = obj.get_resources(client, option_)
            return response
        except Exception as e :
            raise e


    class Serverclosepropagation:
        """ """
        YES = "YES"
        NO = "NO"

class nsdiameter_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.nsdiameter = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.nsdiameter = [nsdiameter() for _ in range(length)]

