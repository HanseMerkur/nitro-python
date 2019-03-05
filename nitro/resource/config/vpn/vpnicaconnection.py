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

class vpnicaconnection(base_resource) :
    """Configuration for active ica connections resource."""
    def __init__(self) :
        self._username = ""
        self._all = False
        self._domain = ""
        self._srcip = ""
        self._srcport = 0
        self._destip = ""
        self._destport = 0
        self._peid = 0
        self.___count = 0

    @property
    def username(self) :
        """User name for which to display connections.<br/>Minimum length =  1."""
        try :
            return self._username
        except Exception as e:
            raise e

    @username.setter
    def username(self, username) :
        """User name for which to display connections.<br/>Minimum length =  1

        :param username: 

        """
        try :
            self._username = username
        except Exception as e:
            raise e

    @property
    def all(self) :
        """Terminate all active icaconnections."""
        try :
            return self._all
        except Exception as e:
            raise e

    @all.setter
    def all(self, all) :
        """Terminate all active icaconnections.

        :param all: 

        """
        try :
            self._all = all
        except Exception as e:
            raise e

    @property
    def domain(self) :
        """The domain name."""
        try :
            return self._domain
        except Exception as e:
            raise e

    @property
    def srcip(self) :
        """The client IP address."""
        try :
            return self._srcip
        except Exception as e:
            raise e

    @property
    def srcport(self) :
        """The client port.<br/>Range 1 - 65535."""
        try :
            return self._srcport
        except Exception as e:
            raise e

    @property
    def destip(self) :
        """The CPS server IP address."""
        try :
            return self._destip
        except Exception as e:
            raise e

    @property
    def destport(self) :
        """The CPS server port.<br/>Range 1 - 65535."""
        try :
            return self._destport
        except Exception as e:
            raise e

    @property
    def peid(self) :
        """Core id of the session owner."""
        try :
            return self._peid
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(vpnicaconnection_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.vpnicaconnection
        except Exception as e :
            raise e

    def _get_object_name(self) :
        """Returns the value of object identifier argument"""
        try :
            return 0
        except Exception as e :
            raise e



    @classmethod
    def kill(cls, client, resource) :
        """Use this API to kill vpnicaconnection.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                killresource = vpnicaconnection()
                killresource.username = resource.username
                killresource.all = resource.all
                return killresource.perform_operation(client,"kill")
            else :
                if (resource and len(resource) > 0) :
                    killresources = [ vpnicaconnection() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        killresources[i].username = resource[i].username
                        killresources[i].all = resource[i].all
                result = cls.perform_operation_bulk_request(client, killresources,"kill")
            return result
        except Exception as e :
            raise e

    @classmethod
    def get(cls, client, name="", option_="") :
        """Use this API to fetch all the vpnicaconnection resources that are configured on netscaler.

        :param client: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            if not name :
                obj = vpnicaconnection()
                response = obj.get_resources(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def get_args(cls, client, args) :
        """Use this API to fetch all the vpnicaconnection resources that are configured on netscaler.
            # This uses vpnicaconnection_args which is a way to provide additional arguments while fetching the resources.

        :param client: 
        :param args: 

        """
        try :
            obj = vpnicaconnection()
            option_ = options()
            option_.args = nitro_util.object_to_string_withoutquotes(args)
            response = obj.get_resources(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def get_filtered(cls, client, filter_) :
        """Use this API to fetch filtered set of vpnicaconnection resources.
        filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = vpnicaconnection()
            option_ = options()
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def count(cls, client) :
        """Use this API to count the vpnicaconnection resources configured on NetScaler.

        :param client: 

        """
        try :
            obj = vpnicaconnection()
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
        """Use this API to count filtered the set of vpnicaconnection resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = vpnicaconnection()
            option_ = options()
            option_.count = True
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            if response :
                return response[0].__dict__['___count']
            return 0
        except Exception as e :
            raise e


class vpnicaconnection_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.vpnicaconnection = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.vpnicaconnection = [vpnicaconnection() for _ in range(length)]

