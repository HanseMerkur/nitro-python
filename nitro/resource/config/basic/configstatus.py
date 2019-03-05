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

class configstatus(base_resource) :
    """Configuration for packet engines status resource."""

        #------- Read only Parameter ---------

    def __init__(self) :
        self._consistent = ""
        self._culpritcore = 0
        self._core = 0
        self._culpritcoreconfstring = ""
        self._coreconfstring = ""
        self.___count = 0

    @property
    def consistent(self) :
        """State of packet engines.<br/>Possible values = YES, NO."""
        try :
            return self._consistent
        except Exception as e:
            raise e

    @property
    def culpritcore(self) :
        """Culprit core id."""
        try :
            return self._culpritcore
        except Exception as e:
            raise e

    @property
    def core(self) :
        """Core id."""
        try :
            return self._core
        except Exception as e:
            raise e

    @property
    def culpritcoreconfstring(self) :
        """ """
        try :
            return self._culpritcoreconfstring
        except Exception as e:
            raise e

    @property
    def coreconfstring(self) :
        """ """
        try :
            return self._coreconfstring
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(configstatus_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.configstatus
        except Exception as e :
            raise e

    def _get_object_name(self) :
        """Returns the value of object identifier argument"""
        try :
            return 0
        except Exception as e :
            raise e



    @classmethod
    def get(cls, client, name="", option_="") :
        """Use this API to fetch all the configstatus resources that are configured on netscaler.

        :param client: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            if not name :
                obj = configstatus()
                response = obj.get_resources(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def get_filtered(cls, client, filter_) :
        """Use this API to fetch filtered set of configstatus resources.
        filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = configstatus()
            option_ = options()
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def count(cls, client) :
        """Use this API to count the configstatus resources configured on NetScaler.

        :param client: 

        """
        try :
            obj = configstatus()
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
        """Use this API to count filtered the set of configstatus resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = configstatus()
            option_ = options()
            option_.count = True
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            if response :
                return response[0].__dict__['___count']
            return 0
        except Exception as e :
            raise e


    class Consistent:
        """ """
        YES = "YES"
        NO = "NO"

class configstatus_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.configstatus = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.configstatus = [configstatus() for _ in range(length)]

