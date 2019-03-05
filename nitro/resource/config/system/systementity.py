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

class systementity(base_resource) :
    """Configuration for entity resource."""
    def __init__(self) :
        self._type = ""
        self._datasource = ""
        self._core = 0
        self._response = ""

    @property
    def type(self) :
        """Specify the entity type."""
        try :
            return self._type
        except Exception as e:
            raise e

    @type.setter
    def type(self, type) :
        """Specify the entity type.

        :param type: 

        """
        try :
            self._type = type
        except Exception as e:
            raise e

    @property
    def datasource(self) :
        """Specifies the source which contains all the stored counter values."""
        try :
            return self._datasource
        except Exception as e:
            raise e

    @datasource.setter
    def datasource(self, datasource) :
        """Specifies the source which contains all the stored counter values.

        :param datasource: 

        """
        try :
            self._datasource = datasource
        except Exception as e:
            raise e

    @property
    def core(self) :
        """Specify core ID of the PE in nCore."""
        try :
            return self._core
        except Exception as e:
            raise e

    @core.setter
    def core(self, core) :
        """Specify core ID of the PE in nCore.

        :param core: 

        """
        try :
            self._core = core
        except Exception as e:
            raise e

    @property
    def response(self) :
        """ """
        try :
            return self._response
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(systementity_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.systementity
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
        """Use this API to fetch all the systementity resources that are configured on netscaler.

        :param client: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            if type(name) == cls :
                if type(name) is not list :
                    option_ = options()
                    option_.args = nitro_util.object_to_string_withoutquotes(name)
                    response = name.get_resource(client, option_)
                return response
        except Exception as e :
            raise e


    @classmethod
    def get_args(cls, client, args) :
        """Use this API to fetch all the systementity resources that are configured on netscaler.
            # This uses systementity_args which is a way to provide additional arguments while fetching the resources.

        :param client: 
        :param args: 

        """
        try :
            obj = systementity()
            option_ = options()
            option_.args = nitro_util.object_to_string_withoutquotes(args)
            response = obj.get_resources(client, option_)
            return response
        except Exception as e :
            raise e


class systementity_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.systementity = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.systementity = [systementity() for _ in range(length)]

