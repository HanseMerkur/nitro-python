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

class routerdynamicrouting(base_resource) :
    """Configuration for dynamic routing config resource."""
    def __init__(self) :
        self._commandstring = ""
        self._output = ""
        self.___count = 0

    @property
    def commandstring(self) :
        """command to be executed."""
        try :
            return self._commandstring
        except Exception as e:
            raise e

    @commandstring.setter
    def commandstring(self, commandstring) :
        """command to be executed.

        :param commandstring: 

        """
        try :
            self._commandstring = commandstring
        except Exception as e:
            raise e

    @property
    def output(self) :
        """command output."""
        try :
            return self._output
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(routerdynamicrouting_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.routerdynamicrouting
        except Exception as e :
            raise e

    def _get_object_name(self) :
        """Returns the value of object identifier argument"""
        try :
            return 0
        except Exception as e :
            raise e



    @classmethod
    def apply(cls, client, resource) :
        """Use this API to apply routerdynamicrouting.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                applyresource = routerdynamicrouting()
                applyresource.commandstring = resource.commandstring
                return applyresource.perform_operation(client,"apply")
            else :
                if (resource and len(resource) > 0) :
                    applyresources = [ routerdynamicrouting() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        applyresources[i].commandstring = resource[i].commandstring
                result = cls.perform_operation_bulk_request(client, applyresources,"apply")
            return result
        except Exception as e :
            raise e

    @classmethod
    def get(cls, client, name="", option_="") :
        """Use this API to fetch all the routerdynamicrouting resources that are configured on netscaler.

        :param client: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            if not name :
                obj = routerdynamicrouting()
                response = obj.get_resources(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def get_args(cls, client, args) :
        """Use this API to fetch all the routerdynamicrouting resources that are configured on netscaler.
            # This uses routerdynamicrouting_args which is a way to provide additional arguments while fetching the resources.

        :param client: 
        :param args: 

        """
        try :
            obj = routerdynamicrouting()
            option_ = options()
            option_.args = nitro_util.object_to_string_withoutquotes(args)
            response = obj.get_resources(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def get_filtered(cls, client, filter_) :
        """Use this API to fetch filtered set of routerdynamicrouting resources.
        filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = routerdynamicrouting()
            option_ = options()
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def count(cls, client) :
        """Use this API to count the routerdynamicrouting resources configured on NetScaler.

        :param client: 

        """
        try :
            obj = routerdynamicrouting()
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
        """Use this API to count filtered the set of routerdynamicrouting resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = routerdynamicrouting()
            option_ = options()
            option_.count = True
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            if response :
                return response[0].__dict__['___count']
            return 0
        except Exception as e :
            raise e


class routerdynamicrouting_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.routerdynamicrouting = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.routerdynamicrouting = [routerdynamicrouting() for _ in range(length)]

