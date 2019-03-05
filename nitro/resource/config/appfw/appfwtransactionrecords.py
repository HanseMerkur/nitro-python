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

class appfwtransactionrecords(base_resource) :
    """Configuration for Application firewall transaction record resource."""

        #------- Read only Parameter ---------

    def __init__(self) :
        self._httptransactionid = 0
        self._packetengineid = 0
        self._appfwsessionid = ""
        self._profilename = ""
        self._url = ""
        self._clientip = ""
        self._destip = ""
        self._starttime = ""
        self._endtime = ""
        self._requestcontentlength = 0
        self._requestyields = 0
        self._requestmaxprocessingtime = 0
        self._responsecontentlength = 0
        self._responseyields = 0
        self._responsemaxprocessingtime = 0
        self.___count = 0

    @property
    def httptransactionid(self) :
        """The http transaction identifier."""
        try :
            return self._httptransactionid
        except Exception as e:
            raise e

    @property
    def packetengineid(self) :
        """The packet engine identifier."""
        try :
            return self._packetengineid
        except Exception as e:
            raise e

    @property
    def appfwsessionid(self) :
        """The session identifier set by the Application Firewall to track the user session."""
        try :
            return self._appfwsessionid
        except Exception as e:
            raise e

    @property
    def profilename(self) :
        """Application Firewall profile name."""
        try :
            return self._profilename
        except Exception as e:
            raise e

    @property
    def url(self) :
        """Request URL."""
        try :
            return self._url
        except Exception as e:
            raise e

    @property
    def clientip(self) :
        """The IP address of client."""
        try :
            return self._clientip
        except Exception as e:
            raise e

    @property
    def destip(self) :
        """The IP address of destination."""
        try :
            return self._destip
        except Exception as e:
            raise e

    @property
    def starttime(self) :
        """Conveys time at which request processing started."""
        try :
            return self._starttime
        except Exception as e:
            raise e

    @property
    def endtime(self) :
        """Conveys time at which request processing end."""
        try :
            return self._endtime
        except Exception as e:
            raise e

    @property
    def requestcontentlength(self) :
        """The content length of request."""
        try :
            return self._requestcontentlength
        except Exception as e:
            raise e

    @property
    def requestyields(self) :
        """The number of times yielded during request processing to send heart beat packets."""
        try :
            return self._requestyields
        except Exception as e:
            raise e

    @property
    def requestmaxprocessingtime(self) :
        """The maximum processing time across yields during request processing."""
        try :
            return self._requestmaxprocessingtime
        except Exception as e:
            raise e

    @property
    def responsecontentlength(self) :
        """The content length of response."""
        try :
            return self._responsecontentlength
        except Exception as e:
            raise e

    @property
    def responseyields(self) :
        """The number of times yielded during response processing to send heart beat packets."""
        try :
            return self._responseyields
        except Exception as e:
            raise e

    @property
    def responsemaxprocessingtime(self) :
        """The maximum processing time across yields during response processing."""
        try :
            return self._responsemaxprocessingtime
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(appfwtransactionrecords_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.appfwtransactionrecords
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
        """Use this API to fetch all the appfwtransactionrecords resources that are configured on netscaler.

        :param client: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            if not name :
                obj = appfwtransactionrecords()
                response = obj.get_resources(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def get_filtered(cls, client, filter_) :
        """Use this API to fetch filtered set of appfwtransactionrecords resources.
        filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = appfwtransactionrecords()
            option_ = options()
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def count(cls, client) :
        """Use this API to count the appfwtransactionrecords resources configured on NetScaler.

        :param client: 

        """
        try :
            obj = appfwtransactionrecords()
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
        """Use this API to count filtered the set of appfwtransactionrecords resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = appfwtransactionrecords()
            option_ = options()
            option_.count = True
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            if response :
                return response[0].__dict__['___count']
            return 0
        except Exception as e :
            raise e


class appfwtransactionrecords_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.appfwtransactionrecords = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.appfwtransactionrecords = [appfwtransactionrecords() for _ in range(length)]

