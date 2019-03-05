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

class protocolhttp_stats(base_resource) :
    """Statistics for HTTP resource."""
    def __init__(self) :
        self._clearstats = ""
        self._spdytotstreams = 0
        self._spdystreamsrate = 0
        self._httptotrequests = 0
        self._httprequestsrate = 0
        self._httptotresponses = 0
        self._httpresponsesrate = 0
        self._httptotrxrequestbytes = 0
        self._httprxrequestbytesrate = 0
        self._httptotrxresponsebytes = 0
        self._httprxresponsebytesrate = 0
        self._httptotgets = 0
        self._httpgetsrate = 0
        self._httptotposts = 0
        self._httppostsrate = 0
        self._httptotothers = 0
        self._httptohersrate = 0
        self._httptot10requests = 0
        self._http10requestsrate = 0
        self._httptot11requests = 0
        self._http11requestsrate = 0
        self._httptotclenrequests = 0
        self._httpclenrequestsrate = 0
        self._httptotchunkedrequests = 0
        self._httpchunkedrequestsrate = 0
        self._httptottxrequestbytes = 0
        self._httptxrequestbytesrate = 0
        self._httptot10responses = 0
        self._http10responsesrate = 0
        self._httptot11responses = 0
        self._http11responsesrate = 0
        self._httptotclenresponses = 0
        self._httpclenresponsesrate = 0
        self._httptotchunkedresponses = 0
        self._httpchunkedresponsesrate = 0
        self._httperrnoreusemultipart = 0
        self._httperrnoreusemultipartrate = 0
        self._httptotnoclenchunkresponses = 0
        self._httpnoclenchunkresponsesrate = 0
        self._httptottxresponsebytes = 0
        self._httptxresponsebytesrate = 0
        self._httperrincompleteheaders = 0
        self._httperrincompleterequests = 0
        self._httperrincompleterequestsrate = 0
        self._httperrincompleteresponses = 0
        self._httperrincompleteresponsesrate = 0
        self._httperrserverbusy = 0
        self._httperrserverbusyrate = 0
        self._httperrlargecontent = 0
        self._httperrlargechunk = 0
        self._httperrlargectlen = 0
        self._spdyv2totstreams = 0
        self._spdyv2streamsrate = 0
        self._spdyv3totstreams = 0
        self._spdyv3streamsrate = 0

    @property
    def clearstats(self) :
        """Clear the statsistics / counters.<br/>Possible values = basic, full."""
        try :
            return self._clearstats
        except Exception as e:
            raise e

    @clearstats.setter
    def clearstats(self, clearstats) :
        """Clear the statsistics / counters

        :param clearstats: 

        """
        try :
            self._clearstats = clearstats
        except Exception as e:
            raise e

    @property
    def httptotclenresponses(self) :
        """Total number of HTTP responses sent in which the Content-length field of the HTTP header has been set. Content-length specifies the length of the content, in bytes, in the associated HTTP body."""
        try :
            return self._httptotclenresponses
        except Exception as e:
            raise e

    @property
    def httperrnoreusemultipart(self) :
        """Total number of HTTP multi-part responses sent. In multi-part responses, one or more entities are encapsulated within the body of a single message."""
        try :
            return self._httperrnoreusemultipart
        except Exception as e:
            raise e

    @property
    def spdyv3streamsrate(self) :
        """Rate (/s) counter for spdyv3totstreams."""
        try :
            return self._spdyv3streamsrate
        except Exception as e:
            raise e

    @property
    def httprxrequestbytesrate(self) :
        """Rate (/s) counter for httptotrxrequestbytes."""
        try :
            return self._httprxrequestbytesrate
        except Exception as e:
            raise e

    @property
    def httptotrxresponsebytes(self) :
        """Total number of bytes of HTTP response data received."""
        try :
            return self._httptotrxresponsebytes
        except Exception as e:
            raise e

    @property
    def httptotchunkedresponses(self) :
        """Total number of HTTP responses sent in which the Transfer-Encoding field of the HTTP header has been set to chunked. This setting is used when the server wants to start sending the response before knowing its total length. The server breaks the response into chunks and sends them in sequence, inserting the length of each chunk before the actual data. The message ends with a chunk of size zero."""
        try :
            return self._httptotchunkedresponses
        except Exception as e:
            raise e

    @property
    def httperrincompleterequests(self) :
        """Total number of HTTP requests received in which the header spans more than one packet."""
        try :
            return self._httperrincompleterequests
        except Exception as e:
            raise e

    @property
    def httptot10requests(self) :
        """Total number of HTTP/1.0 requests received."""
        try :
            return self._httptot10requests
        except Exception as e:
            raise e

    @property
    def httptotgets(self) :
        """Total number of HTTP requests received with the GET method."""
        try :
            return self._httptotgets
        except Exception as e:
            raise e

    @property
    def httperrlargecontent(self) :
        """Total number of requests and responses received with large body."""
        try :
            return self._httperrlargecontent
        except Exception as e:
            raise e

    @property
    def http10responsesrate(self) :
        """Rate (/s) counter for httptot10responses."""
        try :
            return self._http10responsesrate
        except Exception as e:
            raise e

    @property
    def httperrserverbusy(self) :
        """Total number of HTTP error responses received. Some of the error responses are:
        500     Internal Server Error
        501     Not Implemented
        502     Bad Gateway
        503     Service Unavailable
        504     Gateway Timeout
        505     HTTP Version Not Supported.


        """
        try :
            return self._httperrserverbusy
        except Exception as e:
            raise e

    @property
    def httptxrequestbytesrate(self) :
        """Rate (/s) counter for httptottxrequestbytes."""
        try :
            return self._httptxrequestbytesrate
        except Exception as e:
            raise e

    @property
    def httptotposts(self) :
        """Total number of HTTP requests received with the POST method."""
        try :
            return self._httptotposts
        except Exception as e:
            raise e

    @property
    def httptotclenrequests(self) :
        """Total number of HTTP requests in which the Content-length field of the HTTP header has been set. Content-length specifies the length of the content, in bytes, in the associated HTTP body."""
        try :
            return self._httptotclenrequests
        except Exception as e:
            raise e

    @property
    def httprxresponsebytesrate(self) :
        """Rate (/s) counter for httptotrxresponsebytes."""
        try :
            return self._httprxresponsebytesrate
        except Exception as e:
            raise e

    @property
    def spdyv2streamsrate(self) :
        """Rate (/s) counter for spdyv2totstreams."""
        try :
            return self._spdyv2streamsrate
        except Exception as e:
            raise e

    @property
    def httperrincompleteresponsesrate(self) :
        """Rate (/s) counter for httperrincompleteresponses."""
        try :
            return self._httperrincompleteresponsesrate
        except Exception as e:
            raise e

    @property
    def httpnoclenchunkresponsesrate(self) :
        """Rate (/s) counter for httptotnoclenchunkresponses."""
        try :
            return self._httpnoclenchunkresponsesrate
        except Exception as e:
            raise e

    @property
    def httpchunkedrequestsrate(self) :
        """Rate (/s) counter for httptotchunkedrequests."""
        try :
            return self._httpchunkedrequestsrate
        except Exception as e:
            raise e

    @property
    def http11responsesrate(self) :
        """Rate (/s) counter for httptot11responses."""
        try :
            return self._http11responsesrate
        except Exception as e:
            raise e

    @property
    def httptotrequests(self) :
        """Total number of HTTP requests received."""
        try :
            return self._httptotrequests
        except Exception as e:
            raise e

    @property
    def httptotresponses(self) :
        """Total number of HTTP responses sent."""
        try :
            return self._httptotresponses
        except Exception as e:
            raise e

    @property
    def httperrincompleteresponses(self) :
        """Total number of HTTP responses received in which the header spans more than one packet."""
        try :
            return self._httperrincompleteresponses
        except Exception as e:
            raise e

    @property
    def spdytotstreams(self) :
        """Total number of requests received over SPDYv2 and SPDYv3."""
        try :
            return self._spdytotstreams
        except Exception as e:
            raise e

    @property
    def httptottxrequestbytes(self) :
        """Total number of bytes of HTTP request data transmitted."""
        try :
            return self._httptottxrequestbytes
        except Exception as e:
            raise e

    @property
    def httperrserverbusyrate(self) :
        """Rate (/s) counter for httperrserverbusy."""
        try :
            return self._httperrserverbusyrate
        except Exception as e:
            raise e

    @property
    def http11requestsrate(self) :
        """Rate (/s) counter for httptot11requests."""
        try :
            return self._http11requestsrate
        except Exception as e:
            raise e

    @property
    def spdystreamsrate(self) :
        """Rate (/s) counter for spdytotstreams."""
        try :
            return self._spdystreamsrate
        except Exception as e:
            raise e

    @property
    def httptxresponsebytesrate(self) :
        """Rate (/s) counter for httptottxresponsebytes."""
        try :
            return self._httptxresponsebytesrate
        except Exception as e:
            raise e

    @property
    def httptohersrate(self) :
        """Rate (/s) counter for httptotothers."""
        try :
            return self._httptohersrate
        except Exception as e:
            raise e

    @property
    def httpchunkedresponsesrate(self) :
        """Rate (/s) counter for httptotchunkedresponses."""
        try :
            return self._httpchunkedresponsesrate
        except Exception as e:
            raise e

    @property
    def httptot11responses(self) :
        """Total number of HTTP/1.1 responses sent."""
        try :
            return self._httptot11responses
        except Exception as e:
            raise e

    @property
    def http10requestsrate(self) :
        """Rate (/s) counter for httptot10requests."""
        try :
            return self._http10requestsrate
        except Exception as e:
            raise e

    @property
    def httprequestsrate(self) :
        """Rate (/s) counter for httptotrequests."""
        try :
            return self._httprequestsrate
        except Exception as e:
            raise e

    @property
    def httpresponsesrate(self) :
        """Rate (/s) counter for httptotresponses."""
        try :
            return self._httpresponsesrate
        except Exception as e:
            raise e

    @property
    def httptot10responses(self) :
        """Total number of HTTP/1.0 responses sent."""
        try :
            return self._httptot10responses
        except Exception as e:
            raise e

    @property
    def httptotnoclenchunkresponses(self) :
        """Total number of FIN-terminated responses sent. In FIN-terminated responses, the server finishes sending the data and closes the connection."""
        try :
            return self._httptotnoclenchunkresponses
        except Exception as e:
            raise e

    @property
    def httperrlargechunk(self) :
        """Total number of requests received with large chunk size, in which the Transfer-Encoding field of the HTTP header has been set to chunked."""
        try :
            return self._httperrlargechunk
        except Exception as e:
            raise e

    @property
    def httperrnoreusemultipartrate(self) :
        """Rate (/s) counter for httperrnoreusemultipart."""
        try :
            return self._httperrnoreusemultipartrate
        except Exception as e:
            raise e

    @property
    def spdyv3totstreams(self) :
        """Total number of requests received over SPDYv3."""
        try :
            return self._spdyv3totstreams
        except Exception as e:
            raise e

    @property
    def httperrincompleteheaders(self) :
        """Total number of HTTP requests and responses received in which the HTTP header spans more than one packet."""
        try :
            return self._httperrincompleteheaders
        except Exception as e:
            raise e

    @property
    def httptot11requests(self) :
        """Total number of HTTP/1.1 requests received."""
        try :
            return self._httptot11requests
        except Exception as e:
            raise e

    @property
    def httppostsrate(self) :
        """Rate (/s) counter for httptotposts."""
        try :
            return self._httppostsrate
        except Exception as e:
            raise e

    @property
    def httpgetsrate(self) :
        """Rate (/s) counter for httptotgets."""
        try :
            return self._httpgetsrate
        except Exception as e:
            raise e

    @property
    def httpclenresponsesrate(self) :
        """Rate (/s) counter for httptotclenresponses."""
        try :
            return self._httpclenresponsesrate
        except Exception as e:
            raise e

    @property
    def httperrlargectlen(self) :
        """Total number of requests received with large content, in which the Content-length field of the HTTP header has been set. Content-length specifies the length of the content, in bytes, in the associated HTTP body."""
        try :
            return self._httperrlargectlen
        except Exception as e:
            raise e

    @property
    def httptottxresponsebytes(self) :
        """Total number of bytes of HTTP response data transmitted."""
        try :
            return self._httptottxresponsebytes
        except Exception as e:
            raise e

    @property
    def spdyv2totstreams(self) :
        """Total number of requests received over SPDYv2."""
        try :
            return self._spdyv2totstreams
        except Exception as e:
            raise e

    @property
    def httptotchunkedrequests(self) :
        """Total number of HTTP requests in which the Transfer-Encoding field of the HTTP header has been set to chunked."""
        try :
            return self._httptotchunkedrequests
        except Exception as e:
            raise e

    @property
    def httperrincompleterequestsrate(self) :
        """Rate (/s) counter for httperrincompleterequests."""
        try :
            return self._httperrincompleterequestsrate
        except Exception as e:
            raise e

    @property
    def httpclenrequestsrate(self) :
        """Rate (/s) counter for httptotclenrequests."""
        try :
            return self._httpclenrequestsrate
        except Exception as e:
            raise e

    @property
    def httptotrxrequestbytes(self) :
        """Total number of bytes of HTTP request data received."""
        try :
            return self._httptotrxrequestbytes
        except Exception as e:
            raise e

    @property
    def httptotothers(self) :
        """Total number of HTTP requests received with methods other than GET and POST. Some of the other well-defined HTTP methods are HEAD, PUT, DELETE, OPTIONS, and TRACE. User-defined methods are also allowed."""
        try :
            return self._httptotothers
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(protocolhttp_response, response, self.__class__.__name__.replace('_stats',''))
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.protocolhttp
        except Exception as e :
            raise e

    def _get_object_name(self) :
        """Returns the value of object identifier argument"""
        try :
            return 0
        except Exception as e :
            raise e



    @classmethod
    def  get(cls, service, name="", option_="") :
        """Use this API to fetch the statistics of all protocolhttp_stats resources that are configured on netscaler.

        :param service: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            obj = protocolhttp_stats()
            if not name :
                response = obj.stat_resources(service, option_)
            return response
        except Exception as e:
            raise e

    class Clearstats:
        """ """
        basic = "basic"
        full = "full"

class protocolhttp_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.protocolhttp = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.protocolhttp = [protocolhttp_stats() for _ in range(length)]

