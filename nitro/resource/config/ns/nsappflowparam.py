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

class nsappflowparam(base_resource) :
    """Configuration for appflowParam resource."""
    def __init__(self) :
        self._templaterefresh = 0
        self._udppmtu = 0
        self._httpurl = ""
        self._httpcookie = ""
        self._httpreferer = ""
        self._httpmethod = ""
        self._httphost = ""
        self._httpuseragent = ""
        self._clienttrafficonly = ""

    @property
    def templaterefresh(self) :
        """IPFIX template refresh interval (in seconds).<br/>Default value: 600<br/>Minimum length =  60<br/>Maximum length =  3600."""
        try :
            return self._templaterefresh
        except Exception as e:
            raise e

    @templaterefresh.setter
    def templaterefresh(self, templaterefresh) :
        """IPFIX template refresh interval (in seconds).<br/>Default value: 600<br/>Minimum length =  60<br/>Maximum length =  3600

        :param templaterefresh: 

        """
        try :
            self._templaterefresh = templaterefresh
        except Exception as e:
            raise e

    @property
    def udppmtu(self) :
        """MTU to be used for IPFIX UDP packets.<br/>Default value: 1472<br/>Minimum length =  128<br/>Maximum length =  1472."""
        try :
            return self._udppmtu
        except Exception as e:
            raise e

    @udppmtu.setter
    def udppmtu(self, udppmtu) :
        """MTU to be used for IPFIX UDP packets.<br/>Default value: 1472<br/>Minimum length =  128<br/>Maximum length =  1472

        :param udppmtu: 

        """
        try :
            self._udppmtu = udppmtu
        except Exception as e:
            raise e

    @property
    def httpurl(self) :
        """Enable AppFlow HTTP URL logging.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._httpurl
        except Exception as e:
            raise e

    @httpurl.setter
    def httpurl(self, httpurl) :
        """Enable AppFlow HTTP URL logging.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED

        :param httpurl: 

        """
        try :
            self._httpurl = httpurl
        except Exception as e:
            raise e

    @property
    def httpcookie(self) :
        """Enable AppFlow HTTP cookie logging.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._httpcookie
        except Exception as e:
            raise e

    @httpcookie.setter
    def httpcookie(self, httpcookie) :
        """Enable AppFlow HTTP cookie logging.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED

        :param httpcookie: 

        """
        try :
            self._httpcookie = httpcookie
        except Exception as e:
            raise e

    @property
    def httpreferer(self) :
        """Enable AppFlow HTTP referer logging.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._httpreferer
        except Exception as e:
            raise e

    @httpreferer.setter
    def httpreferer(self, httpreferer) :
        """Enable AppFlow HTTP referer logging.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED

        :param httpreferer: 

        """
        try :
            self._httpreferer = httpreferer
        except Exception as e:
            raise e

    @property
    def httpmethod(self) :
        """Enable AppFlow HTTP method logging.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._httpmethod
        except Exception as e:
            raise e

    @httpmethod.setter
    def httpmethod(self, httpmethod) :
        """Enable AppFlow HTTP method logging.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED

        :param httpmethod: 

        """
        try :
            self._httpmethod = httpmethod
        except Exception as e:
            raise e

    @property
    def httphost(self) :
        """Enable AppFlow HTTP host logging.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._httphost
        except Exception as e:
            raise e

    @httphost.setter
    def httphost(self, httphost) :
        """Enable AppFlow HTTP host logging.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED

        :param httphost: 

        """
        try :
            self._httphost = httphost
        except Exception as e:
            raise e

    @property
    def httpuseragent(self) :
        """Enable AppFlow HTTP user-agent logging.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._httpuseragent
        except Exception as e:
            raise e

    @httpuseragent.setter
    def httpuseragent(self, httpuseragent) :
        """Enable AppFlow HTTP user-agent logging.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED

        :param httpuseragent: 

        """
        try :
            self._httpuseragent = httpuseragent
        except Exception as e:
            raise e

    @property
    def clienttrafficonly(self) :
        """Control whether AppFlow records should be generated only for client-side traffic.<br/>Default value: NO<br/>Possible values = YES, NO."""
        try :
            return self._clienttrafficonly
        except Exception as e:
            raise e

    @clienttrafficonly.setter
    def clienttrafficonly(self, clienttrafficonly) :
        """Control whether AppFlow records should be generated only for client-side traffic.<br/>Default value: NO<br/>Possible values = YES, NO

        :param clienttrafficonly: 

        """
        try :
            self._clienttrafficonly = clienttrafficonly
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(nsappflowparam_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.nsappflowparam
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
        """Use this API to update nsappflowparam.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                updateresource = nsappflowparam()
                updateresource.templaterefresh = resource.templaterefresh
                updateresource.udppmtu = resource.udppmtu
                updateresource.httpurl = resource.httpurl
                updateresource.httpcookie = resource.httpcookie
                updateresource.httpreferer = resource.httpreferer
                updateresource.httpmethod = resource.httpmethod
                updateresource.httphost = resource.httphost
                updateresource.httpuseragent = resource.httpuseragent
                updateresource.clienttrafficonly = resource.clienttrafficonly
                return updateresource.update_resource(client)
        except Exception as e :
            raise e

    @classmethod
    def unset(cls, client, resource, args) :
        """Use this API to unset the properties of nsappflowparam resource.
        Properties that need to be unset are specified in args array.

        :param client: 
        :param resource: 
        :param args: 

        """
        try :
            if type(resource) is not list :
                unsetresource = nsappflowparam()
                return unsetresource.unset_resource(client, args)
        except Exception as e :
            raise e

    @classmethod
    def get(cls, client, name="", option_="") :
        """Use this API to fetch all the nsappflowparam resources that are configured on netscaler.

        :param client: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            if not name :
                obj = nsappflowparam()
                response = obj.get_resources(client, option_)
            return response
        except Exception as e :
            raise e


    class Httpreferer:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Clienttrafficonly:
        """ """
        YES = "YES"
        NO = "NO"

    class Httpmethod:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Httpcookie:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Httpurl:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Httpuseragent:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Httphost:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

class nsappflowparam_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.nsappflowparam = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.nsappflowparam = [nsappflowparam() for _ in range(length)]

