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

class pqbinding(base_resource) :
    """Configuration for PQ bindings resource."""
    def __init__(self) :
        self._vservername = ""
        self._policyname = ""
        self._rule = ""
        self._priority = 0
        self._weight = 0
        self._qdepth = 0
        self._polqdepth = 0
        self._hits = 0
        self.___count = 0

    @property
    def vservername(self) :
        """Name of the load balancing virtual server for which to display the priority queuing policy.<br/>Minimum length =  1."""
        try :
            return self._vservername
        except Exception as e:
            raise e

    @vservername.setter
    def vservername(self, vservername) :
        """Name of the load balancing virtual server for which to display the priority queuing policy.<br/>Minimum length =  1

        :param vservername: 

        """
        try :
            self._vservername = vservername
        except Exception as e:
            raise e

    @property
    def policyname(self) :
        """The name of the priority queuing policy."""
        try :
            return self._policyname
        except Exception as e:
            raise e

    @property
    def rule(self) :
        """The condition for applying the policy."""
        try :
            return self._rule
        except Exception as e:
            raise e

    @property
    def priority(self) :
        """The priority of queuing the request."""
        try :
            return self._priority
        except Exception as e:
            raise e

    @property
    def weight(self) :
        """Weight."""
        try :
            return self._weight
        except Exception as e:
            raise e

    @property
    def qdepth(self) :
        """Queue Depth."""
        try :
            return self._qdepth
        except Exception as e:
            raise e

    @property
    def polqdepth(self) :
        """Policy Queue Depth."""
        try :
            return self._polqdepth
        except Exception as e:
            raise e

    @property
    def hits(self) :
        """Total number of hits."""
        try :
            return self._hits
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(pqbinding_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.pqbinding
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
        """Use this API to fetch all the pqbinding resources that are configured on netscaler.

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
                else :
                    if name and len(name) > 0 :
                        response = [pqbinding() for _ in range(len(name))]
                        for i in range(len(name)) :
                            option_ = options()
                            option_.args = nitro_util.object_to_string_withoutquotes(name[i])
                            response[i] = name[i].get_resource(client, option_)
                return response
        except Exception as e :
            raise e


    @classmethod
    def get_args(cls, client, args) :
        """Use this API to fetch all the pqbinding resources that are configured on netscaler.
            # This uses pqbinding_args which is a way to provide additional arguments while fetching the resources.

        :param client: 
        :param args: 

        """
        try :
            obj = pqbinding()
            option_ = options()
            option_.args = nitro_util.object_to_string_withoutquotes(args)
            response = obj.get_resources(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def get_filtered(cls, client, filter_, obj) :
        """Use this API to fetch filtered set of pqbinding resources.
        filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 
        :param obj: 

        """
        try :
            option_ = options()
            option_.filter = filter_
            option_.args = nitro_util.object_to_string_withoutquotes(obj)
            response = obj.getfiltered(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def count(cls, client, obj) :
        """Use this API to count the pqbinding resources configured on NetScaler.

        :param client: 
        :param obj: 

        """
        try :
            option_ = options()
            option_.count = True
            option_.args = nitro_util.object_to_string_withoutquotes(obj)
            response = obj.get_resources(client, option_)
            if response :
                return response[0].__dict__['___count']
            return 0
        except Exception as e :
            raise e

    @classmethod
    def count_filtered(cls, client, filter_, obj) :
        """Use this API to count filtered the set of pqbinding resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 
        :param obj: 

        """
        try :
            option_ = options()
            option_.count = True
            option_.filter = filter_
            option_.args = nitro_util.object_to_string_withoutquotes(obj)
            response = obj.getfiltered(client, option_)
            if response :
                return response[0].__dict__['___count']
            return 0
        except Exception as e :
            raise e


class pqbinding_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.pqbinding = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.pqbinding = [pqbinding() for _ in range(length)]

