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

class nstimeout(base_resource) :
    """Configuration for timeout resource."""
    def __init__(self) :
        self._zombie = 0
        self._client = 0
        self._server = 0
        self._httpclient = 0
        self._httpserver = 0
        self._tcpclient = 0
        self._tcpserver = 0
        self._anyclient = 0
        self._anyserver = 0
        self._anytcpclient = 0
        self._anytcpserver = 0
        self._halfclose = 0
        self._nontcpzombie = 0
        self._reducedfintimeout = 0
        self._reducedrsttimeout = 0
        self._newconnidletimeout = 0

    @property
    def zombie(self) :
        """Interval, in seconds, at which the NetScaler zombie cleanup process must run. This process cleans up inactive TCP connections.<br/>Default value: 120<br/>Minimum length =  1<br/>Maximum length =  600."""
        try :
            return self._zombie
        except Exception as e:
            raise e

    @zombie.setter
    def zombie(self, zombie) :
        """Interval, in seconds, at which the NetScaler zombie cleanup process must run. This process cleans up inactive TCP connections.<br/>Default value: 120<br/>Minimum length =  1<br/>Maximum length =  600

        :param zombie: 

        """
        try :
            self._zombie = zombie
        except Exception as e:
            raise e

    @property
    def client(self) :
        """Client idle timeout (in seconds). If zero, the service-type default value is taken when service is created.<br/>Default value: 0<br/>Maximum length =  18000."""
        try :
            return self._client
        except Exception as e:
            raise e

    @client.setter
    def client(self, client) :
        """Client idle timeout (in seconds). If zero, the service-type default value is taken when service is created.<br/>Default value: 0<br/>Maximum length =  18000

        :param client: 

        """
        try :
            self._client = client
        except Exception as e:
            raise e

    @property
    def server(self) :
        """Server idle timeout (in seconds).  If zero, the service-type default value is taken when service is created.<br/>Default value: 0<br/>Maximum length =  18000."""
        try :
            return self._server
        except Exception as e:
            raise e

    @server.setter
    def server(self, server) :
        """Server idle timeout (in seconds).  If zero, the service-type default value is taken when service is created.<br/>Default value: 0<br/>Maximum length =  18000

        :param server: 

        """
        try :
            self._server = server
        except Exception as e:
            raise e

    @property
    def httpclient(self) :
        """Global idle timeout, in seconds, for client connections of HTTP service type. This value is over ridden by the client timeout that is configured on individual entities.<br/>Default value: 0<br/>Maximum length =  18000."""
        try :
            return self._httpclient
        except Exception as e:
            raise e

    @httpclient.setter
    def httpclient(self, httpclient) :
        """Global idle timeout, in seconds, for client connections of HTTP service type. This value is over ridden by the client timeout that is configured on individual entities.<br/>Default value: 0<br/>Maximum length =  18000

        :param httpclient: 

        """
        try :
            self._httpclient = httpclient
        except Exception as e:
            raise e

    @property
    def httpserver(self) :
        """Global idle timeout, in seconds, for server connections of HTTP service type. This value is over ridden by the server timeout that is configured on individual entities.<br/>Default value: 0<br/>Maximum length =  18000."""
        try :
            return self._httpserver
        except Exception as e:
            raise e

    @httpserver.setter
    def httpserver(self, httpserver) :
        """Global idle timeout, in seconds, for server connections of HTTP service type. This value is over ridden by the server timeout that is configured on individual entities.<br/>Default value: 0<br/>Maximum length =  18000

        :param httpserver: 

        """
        try :
            self._httpserver = httpserver
        except Exception as e:
            raise e

    @property
    def tcpclient(self) :
        """Global idle timeout, in seconds, for non-HTTP client connections of TCP service type. This value is over ridden by the client timeout that is configured on individual entities.<br/>Default value: 0<br/>Maximum length =  18000."""
        try :
            return self._tcpclient
        except Exception as e:
            raise e

    @tcpclient.setter
    def tcpclient(self, tcpclient) :
        """Global idle timeout, in seconds, for non-HTTP client connections of TCP service type. This value is over ridden by the client timeout that is configured on individual entities.<br/>Default value: 0<br/>Maximum length =  18000

        :param tcpclient: 

        """
        try :
            self._tcpclient = tcpclient
        except Exception as e:
            raise e

    @property
    def tcpserver(self) :
        """Global idle timeout, in seconds, for non-HTTP server connections of TCP service type. This value is over ridden by the server timeout that is configured on entities.<br/>Default value: 0<br/>Maximum length =  18000."""
        try :
            return self._tcpserver
        except Exception as e:
            raise e

    @tcpserver.setter
    def tcpserver(self, tcpserver) :
        """Global idle timeout, in seconds, for non-HTTP server connections of TCP service type. This value is over ridden by the server timeout that is configured on entities.<br/>Default value: 0<br/>Maximum length =  18000

        :param tcpserver: 

        """
        try :
            self._tcpserver = tcpserver
        except Exception as e:
            raise e

    @property
    def anyclient(self) :
        """Global idle timeout, in seconds, for non-TCP client connections. This value is over ridden by the client timeout that is configured on individual entities.<br/>Default value: 0<br/>Maximum length =  31536000."""
        try :
            return self._anyclient
        except Exception as e:
            raise e

    @anyclient.setter
    def anyclient(self, anyclient) :
        """Global idle timeout, in seconds, for non-TCP client connections. This value is over ridden by the client timeout that is configured on individual entities.<br/>Default value: 0<br/>Maximum length =  31536000

        :param anyclient: 

        """
        try :
            self._anyclient = anyclient
        except Exception as e:
            raise e

    @property
    def anyserver(self) :
        """Global idle timeout, in seconds, for non TCP server connections. This value is over ridden by the server timeout that is configured on individual entities.<br/>Default value: 0<br/>Maximum length =  31536000."""
        try :
            return self._anyserver
        except Exception as e:
            raise e

    @anyserver.setter
    def anyserver(self, anyserver) :
        """Global idle timeout, in seconds, for non TCP server connections. This value is over ridden by the server timeout that is configured on individual entities.<br/>Default value: 0<br/>Maximum length =  31536000

        :param anyserver: 

        """
        try :
            self._anyserver = anyserver
        except Exception as e:
            raise e

    @property
    def anytcpclient(self) :
        """Global idle timeout, in seconds, for TCP client connections. This value takes precedence over  entity level timeout settings (vserver/service). This is applicable only to transport protocol TCP.<br/>Default value: 0<br/>Maximum length =  31536000."""
        try :
            return self._anytcpclient
        except Exception as e:
            raise e

    @anytcpclient.setter
    def anytcpclient(self, anytcpclient) :
        """Global idle timeout, in seconds, for TCP client connections. This value takes precedence over  entity level timeout settings (vserver/service). This is applicable only to transport protocol TCP.<br/>Default value: 0<br/>Maximum length =  31536000

        :param anytcpclient: 

        """
        try :
            self._anytcpclient = anytcpclient
        except Exception as e:
            raise e

    @property
    def anytcpserver(self) :
        """Global idle timeout, in seconds, for TCP server connections. This value takes precedence over entity level timeout settings ( vserver/service). This is applicable only to transport protocol TCP.<br/>Default value: 0<br/>Maximum length =  31536000."""
        try :
            return self._anytcpserver
        except Exception as e:
            raise e

    @anytcpserver.setter
    def anytcpserver(self, anytcpserver) :
        """Global idle timeout, in seconds, for TCP server connections. This value takes precedence over entity level timeout settings ( vserver/service). This is applicable only to transport protocol TCP.<br/>Default value: 0<br/>Maximum length =  31536000

        :param anytcpserver: 

        """
        try :
            self._anytcpserver = anytcpserver
        except Exception as e:
            raise e

    @property
    def halfclose(self) :
        """Idle timeout, in seconds, for connections that are in TCP half-closed state.<br/>Default value: 10<br/>Minimum length =  1<br/>Maximum length =  600."""
        try :
            return self._halfclose
        except Exception as e:
            raise e

    @halfclose.setter
    def halfclose(self, halfclose) :
        """Idle timeout, in seconds, for connections that are in TCP half-closed state.<br/>Default value: 10<br/>Minimum length =  1<br/>Maximum length =  600

        :param halfclose: 

        """
        try :
            self._halfclose = halfclose
        except Exception as e:
            raise e

    @property
    def nontcpzombie(self) :
        """Interval at which the zombie clean-up process for non-TCP connections should run. Inactive IP NAT connections will be cleaned up.<br/>Default value: 60<br/>Minimum length =  1<br/>Maximum length =  600."""
        try :
            return self._nontcpzombie
        except Exception as e:
            raise e

    @nontcpzombie.setter
    def nontcpzombie(self, nontcpzombie) :
        """Interval at which the zombie clean-up process for non-TCP connections should run. Inactive IP NAT connections will be cleaned up.<br/>Default value: 60<br/>Minimum length =  1<br/>Maximum length =  600

        :param nontcpzombie: 

        """
        try :
            self._nontcpzombie = nontcpzombie
        except Exception as e:
            raise e

    @property
    def reducedfintimeout(self) :
        """Alternative idle timeout, in seconds, for closed TCP NATPCB connections.<br/>Default value: 30<br/>Minimum length =  1<br/>Maximum length =  300."""
        try :
            return self._reducedfintimeout
        except Exception as e:
            raise e

    @reducedfintimeout.setter
    def reducedfintimeout(self, reducedfintimeout) :
        """Alternative idle timeout, in seconds, for closed TCP NATPCB connections.<br/>Default value: 30<br/>Minimum length =  1<br/>Maximum length =  300

        :param reducedfintimeout: 

        """
        try :
            self._reducedfintimeout = reducedfintimeout
        except Exception as e:
            raise e

    @property
    def reducedrsttimeout(self) :
        """Timer interval, in seconds, for abruptly terminated TCP NATPCB connections.<br/>Default value: 0<br/>Maximum length =  300."""
        try :
            return self._reducedrsttimeout
        except Exception as e:
            raise e

    @reducedrsttimeout.setter
    def reducedrsttimeout(self, reducedrsttimeout) :
        """Timer interval, in seconds, for abruptly terminated TCP NATPCB connections.<br/>Default value: 0<br/>Maximum length =  300

        :param reducedrsttimeout: 

        """
        try :
            self._reducedrsttimeout = reducedrsttimeout
        except Exception as e:
            raise e

    @property
    def newconnidletimeout(self) :
        """Timer interval, in seconds, for new TCP NATPCB connections on which no data was received.<br/>Default value: 4<br/>Minimum length =  1<br/>Maximum length =  120."""
        try :
            return self._newconnidletimeout
        except Exception as e:
            raise e

    @newconnidletimeout.setter
    def newconnidletimeout(self, newconnidletimeout) :
        """Timer interval, in seconds, for new TCP NATPCB connections on which no data was received.<br/>Default value: 4<br/>Minimum length =  1<br/>Maximum length =  120

        :param newconnidletimeout: 

        """
        try :
            self._newconnidletimeout = newconnidletimeout
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(nstimeout_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.nstimeout
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
        """Use this API to update nstimeout.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                updateresource = nstimeout()
                updateresource.zombie = resource.zombie
                updateresource.client = resource.client
                updateresource.server = resource.server
                updateresource.httpclient = resource.httpclient
                updateresource.httpserver = resource.httpserver
                updateresource.tcpclient = resource.tcpclient
                updateresource.tcpserver = resource.tcpserver
                updateresource.anyclient = resource.anyclient
                updateresource.anyserver = resource.anyserver
                updateresource.anytcpclient = resource.anytcpclient
                updateresource.anytcpserver = resource.anytcpserver
                updateresource.halfclose = resource.halfclose
                updateresource.nontcpzombie = resource.nontcpzombie
                updateresource.reducedfintimeout = resource.reducedfintimeout
                updateresource.reducedrsttimeout = resource.reducedrsttimeout
                updateresource.newconnidletimeout = resource.newconnidletimeout
                return updateresource.update_resource(client)
        except Exception as e :
            raise e

    @classmethod
    def unset(cls, client, resource, args) :
        """Use this API to unset the properties of nstimeout resource.
        Properties that need to be unset are specified in args array.

        :param client: 
        :param resource: 
        :param args: 

        """
        try :
            if type(resource) is not list :
                unsetresource = nstimeout()
                return unsetresource.unset_resource(client, args)
        except Exception as e :
            raise e

    @classmethod
    def get(cls, client, name="", option_="") :
        """Use this API to fetch all the nstimeout resources that are configured on netscaler.

        :param client: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            if not name :
                obj = nstimeout()
                response = obj.get_resources(client, option_)
            return response
        except Exception as e :
            raise e


class nstimeout_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.nstimeout = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.nstimeout = [nstimeout() for _ in range(length)]

