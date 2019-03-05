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


class cacheobject_args :
    """Provides additional arguments required for fetching the cacheobject resource."""
    def __init__(self) :
        self._url = ""
        self._locator = 0
        self._httpstatus = 0
        self._host = ""
        self._port = 0
        self._groupname = ""
        self._httpmethod = ""
        self._group = ""
        self._ignoremarkerobjects = ""
        self._includenotreadyobjects = ""

    @property
    def url(self) :
        """URL of the particular object whose details is required. Parameter "host" must be specified along with the URL.<br/>Minimum length =  1."""
        try :
            return self._url
        except Exception as e:
            raise e

    @url.setter
    def url(self, url) :
        """URL of the particular object whose details is required. Parameter "host" must be specified along with the URL.<br/>Minimum length =  1

        :param url: 

        """
        try :
            self._url = url
        except Exception as e:
            raise e

    @property
    def locator(self) :
        """ID of the cached object."""
        try :
            return self._locator
        except Exception as e:
            raise e

    @locator.setter
    def locator(self, locator) :
        """ID of the cached object.

        :param locator: 

        """
        try :
            self._locator = locator
        except Exception as e:
            raise e

    @property
    def httpstatus(self) :
        """HTTP status of the object."""
        try :
            return self._httpstatus
        except Exception as e:
            raise e

    @httpstatus.setter
    def httpstatus(self, httpstatus) :
        """HTTP status of the object.

        :param httpstatus: 

        """
        try :
            self._httpstatus = httpstatus
        except Exception as e:
            raise e

    @property
    def host(self) :
        """Host name of the object. Parameter "url" must be specified.<br/>Minimum length =  1."""
        try :
            return self._host
        except Exception as e:
            raise e

    @host.setter
    def host(self, host) :
        """Host name of the object. Parameter "url" must be specified.<br/>Minimum length =  1

        :param host: 

        """
        try :
            self._host = host
        except Exception as e:
            raise e

    @property
    def port(self) :
        """Host port of the object. You must also set the Host parameter.<br/>Default value: 80<br/>Minimum value =  1."""
        try :
            return self._port
        except Exception as e:
            raise e

    @port.setter
    def port(self, port) :
        """Host port of the object. You must also set the Host parameter.<br/>Default value: 80<br/>Minimum value =  1

        :param port: 

        """
        try :
            self._port = port
        except Exception as e:
            raise e

    @property
    def groupname(self) :
        """Name of the content group to which the object belongs. It will display only the objects belonging to the specified content group. You must also set the Host parameter."""
        try :
            return self._groupname
        except Exception as e:
            raise e

    @groupname.setter
    def groupname(self, groupname) :
        """Name of the content group to which the object belongs. It will display only the objects belonging to the specified content group. You must also set the Host parameter.

        :param groupname: 

        """
        try :
            self._groupname = groupname
        except Exception as e:
            raise e

    @property
    def httpmethod(self) :
        """HTTP request method that caused the object to be stored.<br/>Default value: GET<br/>Possible values = GET, POST."""
        try :
            return self._httpmethod
        except Exception as e:
            raise e

    @httpmethod.setter
    def httpmethod(self, httpmethod) :
        """HTTP request method that caused the object to be stored.<br/>Default value: GET<br/>Possible values = GET, POST

        :param httpmethod: 

        """
        try :
            self._httpmethod = httpmethod
        except Exception as e:
            raise e

    @property
    def group(self) :
        """Name of the content group whose objects should be listed."""
        try :
            return self._group
        except Exception as e:
            raise e

    @group.setter
    def group(self, group) :
        """Name of the content group whose objects should be listed.

        :param group: 

        """
        try :
            self._group = group
        except Exception as e:
            raise e

    @property
    def ignoremarkerobjects(self) :
        """Ignore marker objects. Marker objects are created when a response exceeds the maximum or minimum response size for the content group or has not yet received the minimum number of hits for the content group.<br/>Possible values = ON, OFF."""
        try :
            return self._ignoremarkerobjects
        except Exception as e:
            raise e

    @ignoremarkerobjects.setter
    def ignoremarkerobjects(self, ignoremarkerobjects) :
        """Ignore marker objects. Marker objects are created when a response exceeds the maximum or minimum response size for the content group or has not yet received the minimum number of hits for the content group.<br/>Possible values = ON, OFF

        :param ignoremarkerobjects: 

        """
        try :
            self._ignoremarkerobjects = ignoremarkerobjects
        except Exception as e:
            raise e

    @property
    def includenotreadyobjects(self) :
        """Include responses that have not yet reached a minimum number of hits before being cached.<br/>Possible values = ON, OFF."""
        try :
            return self._includenotreadyobjects
        except Exception as e:
            raise e

    @includenotreadyobjects.setter
    def includenotreadyobjects(self, includenotreadyobjects) :
        """Include responses that have not yet reached a minimum number of hits before being cached.<br/>Possible values = ON, OFF

        :param includenotreadyobjects: 

        """
        try :
            self._includenotreadyobjects = includenotreadyobjects
        except Exception as e:
            raise e

    class Includenotreadyobjects:
        """ """
        ON = "ON"
        OFF = "OFF"

    class Httpmethod:
        """ """
        GET = "GET"
        POST = "POST"

    class Ignoremarkerobjects:
        """ """
        ON = "ON"
        OFF = "OFF"

