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

class cacheobject(base_resource) :
    """Configuration for cache object resource."""
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
        self._tosecondary = ""
        self._cacheressize = 0
        self._cachereshdrsize = 0
        self._cacheetag = ""
        self._httpstatusoutput = 0
        self._cachereslastmod = ""
        self._cachecontrol = ""
        self._cacheresdate = ""
        self._contentgroup = ""
        self._destipv46 = ""
        self._destport = 0
        self._cachecellcomplex = ""
        self._hitparams = []
        self._hitvalues = []
        self._cachecellreqtime = 0
        self._cachecellrestime = 0
        self._cachecurage = 0
        self._cachecellexpires = 0
        self._cachecellexpiresmillisec = 0
        self._flushed = ""
        self._prefetch = ""
        self._prefetchperiod = 0
        self._prefetchperiodmillisec = 0
        self._cachecellcurreaders = 0
        self._cachecellcurmisses = 0
        self._cachecellhits = 0
        self._cachecellmisses = 0
        self._cachecelldhits = 0
        self._cachecellcompressionformat = ""
        self._cachecellappfwmetadataexists = ""
        self._cachecellhttp11 = ""
        self._cachecellweaketag = ""
        self._cachecellresbadsize = ""
        self._markerreason = ""
        self._cachecellpolleverytime = ""
        self._cachecelletaginserted = ""
        self._cachecellreadywithlastbyte = ""
        self._cacheinmemory = ""
        self._cacheindisk = ""
        self._cacheinsecondary = ""
        self._cachedirname = ""
        self._cachefilename = ""
        self._cachecelldestipverified = ""
        self._cachecellfwpxyobj = ""
        self._cachecellbasefile = ""
        self._cachecellminhitflag = ""
        self._cachecellminhit = 0
        self._policy = 0
        self._policyname = ""
        self._selectorname = []
        self._rule = []
        self._selectorvalue = []
        self._cacheurls = ""
        self._warnbucketskip = 0
        self._totalobjs = 0
        self._httpcalloutcell = ""
        self._httpcalloutname = ""
        self._returntype = ""
        self._httpcalloutresult = ""
        self._locatorshow = 0
        self._ceflags = 0
        self.___count = 0

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
        """Host port of the object. You must also set the Host parameter.<br/>Default value: 80<br/>Minimum length =  1."""
        try :
            return self._port
        except Exception as e:
            raise e

    @port.setter
    def port(self, port) :
        """Host port of the object. You must also set the Host parameter.<br/>Default value: 80<br/>Minimum length =  1

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

    @property
    def tosecondary(self) :
        """Object will be saved onto Secondary.<br/>Default value: NO<br/>Possible values = YES, NO."""
        try :
            return self._tosecondary
        except Exception as e:
            raise e

    @tosecondary.setter
    def tosecondary(self, tosecondary) :
        """Object will be saved onto Secondary.<br/>Default value: NO<br/>Possible values = YES, NO

        :param tosecondary: 

        """
        try :
            self._tosecondary = tosecondary
        except Exception as e:
            raise e

    @property
    def cacheressize(self) :
        """Cache response size of the object."""
        try :
            return self._cacheressize
        except Exception as e:
            raise e

    @property
    def cachereshdrsize(self) :
        """Cache response header size of the object."""
        try :
            return self._cachereshdrsize
        except Exception as e:
            raise e

    @property
    def cacheetag(self) :
        """Cache ETag of the object."""
        try :
            return self._cacheetag
        except Exception as e:
            raise e

    @property
    def httpstatusoutput(self) :
        """HTTP status of the object."""
        try :
            return self._httpstatusoutput
        except Exception as e:
            raise e

    @property
    def cachereslastmod(self) :
        """Value of "Last-modified" header."""
        try :
            return self._cachereslastmod
        except Exception as e:
            raise e

    @property
    def cachecontrol(self) :
        """Cache-Control header of the object."""
        try :
            return self._cachecontrol
        except Exception as e:
            raise e

    @property
    def cacheresdate(self) :
        """Value of "Date" header."""
        try :
            return self._cacheresdate
        except Exception as e:
            raise e

    @property
    def contentgroup(self) :
        """Name of the contentgroup in which it is stored."""
        try :
            return self._contentgroup
        except Exception as e:
            raise e

    @property
    def destipv46(self) :
        """Destination IP."""
        try :
            return self._destipv46
        except Exception as e:
            raise e

    @property
    def destport(self) :
        """Destination Port.<br/>Range 1 - 65535."""
        try :
            return self._destport
        except Exception as e:
            raise e

    @property
    def cachecellcomplex(self) :
        """The state of the parameterized caching on this cell.<br/>Possible values = YES, NO."""
        try :
            return self._cachecellcomplex
        except Exception as e:
            raise e

    @property
    def hitparams(self) :
        """Parameterized hit evaluation of an object."""
        try :
            return self._hitparams
        except Exception as e:
            raise e

    @property
    def hitvalues(self) :
        """Values of hitparams for this object."""
        try :
            return self._hitvalues
        except Exception as e:
            raise e

    @property
    def cachecellreqtime(self) :
        """Required time of the cache cell object."""
        try :
            return self._cachecellreqtime
        except Exception as e:
            raise e

    @property
    def cachecellrestime(self) :
        """Response time to the cache cell object."""
        try :
            return self._cachecellrestime
        except Exception as e:
            raise e

    @property
    def cachecurage(self) :
        """Current age of the cache object."""
        try :
            return self._cachecurage
        except Exception as e:
            raise e

    @property
    def cachecellexpires(self) :
        """Expiry time of the cache cell object in seconds."""
        try :
            return self._cachecellexpires
        except Exception as e:
            raise e

    @property
    def cachecellexpiresmillisec(self) :
        """Expiry time of the cache cell object in milliseconds."""
        try :
            return self._cachecellexpiresmillisec
        except Exception as e:
            raise e

    @property
    def flushed(self) :
        """Specifies whether the object is flushed.<br/>Possible values = YES, NO."""
        try :
            return self._flushed
        except Exception as e:
            raise e

    @property
    def prefetch(self) :
        """Specifies whether Integrated Cache should attempt to refresh an object immediately before it goes stale.<br/>Possible values = YES, NO."""
        try :
            return self._prefetch
        except Exception as e:
            raise e

    @property
    def prefetchperiod(self) :
        """The duration in seconds of the period during which prefetch should be attempted, immediately before the object's calculated expiry time."""
        try :
            return self._prefetchperiod
        except Exception as e:
            raise e

    @property
    def prefetchperiodmillisec(self) :
        """The duration in milliseconds of the period during which prefetch should be attempted, immediately before the object's calculated expiry time."""
        try :
            return self._prefetchperiodmillisec
        except Exception as e:
            raise e

    @property
    def cachecellcurreaders(self) :
        """Current readers of the cache cell object."""
        try :
            return self._cachecellcurreaders
        except Exception as e:
            raise e

    @property
    def cachecellcurmisses(self) :
        """Current misses of the cache cell object."""
        try :
            return self._cachecellcurmisses
        except Exception as e:
            raise e

    @property
    def cachecellhits(self) :
        """Cache cell hits."""
        try :
            return self._cachecellhits
        except Exception as e:
            raise e

    @property
    def cachecellmisses(self) :
        """Cache cell misses."""
        try :
            return self._cachecellmisses
        except Exception as e:
            raise e

    @property
    def cachecelldhits(self) :
        """Cache cell disk hits."""
        try :
            return self._cachecelldhits
        except Exception as e:
            raise e

    @property
    def cachecellcompressionformat(self) :
        """Compression format of this object. Identity means not compressed."""
        try :
            return self._cachecellcompressionformat
        except Exception as e:
            raise e

    @property
    def cachecellappfwmetadataexists(self) :
        """AppFirewall cache object.<br/>Possible values = YES, NO."""
        try :
            return self._cachecellappfwmetadataexists
        except Exception as e:
            raise e

    @property
    def cachecellhttp11(self) :
        """The state of the response to be HTTP/1.1.<br/>Possible values = YES, NO."""
        try :
            return self._cachecellhttp11
        except Exception as e:
            raise e

    @property
    def cachecellweaketag(self) :
        """The state of the weak HTTP Entity Tag in the cell.<br/>Possible values = YES, NO."""
        try :
            return self._cachecellweaketag
        except Exception as e:
            raise e

    @property
    def cachecellresbadsize(self) :
        """The marked state of the cell.<br/>Possible values = YES, NO."""
        try :
            return self._cachecellresbadsize
        except Exception as e:
            raise e

    @property
    def markerreason(self) :
        """Reason for marking the cell.<br/>Possible values = Waiting for min hit, Response header is too big, Content-length header said response size is not in group size limit, Content-length response received more data, Content-length response received less data, Content-length response data is not in group size limit, Chunk response received more data, Chunk response data is not in group size limit, Bad chunk format, Fin terminated response data is not in group size limit."""
        try :
            return self._markerreason
        except Exception as e:
            raise e

    @property
    def cachecellpolleverytime(self) :
        """The state to poll every time on object.<br/>Possible values = YES, NO."""
        try :
            return self._cachecellpolleverytime
        except Exception as e:
            raise e

    @property
    def cachecelletaginserted(self) :
        """The state of the ETag to be inserted by IC for this object.<br/>Possible values = YES, NO."""
        try :
            return self._cachecelletaginserted
        except Exception as e:
            raise e

    @property
    def cachecellreadywithlastbyte(self) :
        """The state of the complete arrived response.<br/>Possible values = YES, NO."""
        try :
            return self._cachecellreadywithlastbyte
        except Exception as e:
            raise e

    @property
    def cacheinmemory(self) :
        """The cache data is available in memory.<br/>Possible values = YES, NO."""
        try :
            return self._cacheinmemory
        except Exception as e:
            raise e

    @property
    def cacheindisk(self) :
        """The cache data is available in disk.<br/>Possible values = YES, NO."""
        try :
            return self._cacheindisk
        except Exception as e:
            raise e

    @property
    def cacheinsecondary(self) :
        """The cache data is available in secondary in HA deployment.<br/>Possible values = YES, NO."""
        try :
            return self._cacheinsecondary
        except Exception as e:
            raise e

    @property
    def cachedirname(self) :
        """The directory name used if saved."""
        try :
            return self._cachedirname
        except Exception as e:
            raise e

    @property
    def cachefilename(self) :
        """The filename used if saved."""
        try :
            return self._cachefilename
        except Exception as e:
            raise e

    @property
    def cachecelldestipverified(self) :
        """The state of DNS verification.<br/>Possible values = YES, NO."""
        try :
            return self._cachecelldestipverified
        except Exception as e:
            raise e

    @property
    def cachecellfwpxyobj(self) :
        """The state of the object to be stored on a request to a forward proxy.<br/>Possible values = YES, NO."""
        try :
            return self._cachecellfwpxyobj
        except Exception as e:
            raise e

    @property
    def cachecellbasefile(self) :
        """The state of delta being used as a basefile.<br/>Possible values = YES, NO."""
        try :
            return self._cachecellbasefile
        except Exception as e:
            raise e

    @property
    def cachecellminhitflag(self) :
        """The state of the minhit feature on this cell.<br/>Possible values = YES, NO."""
        try :
            return self._cachecellminhitflag
        except Exception as e:
            raise e

    @property
    def cachecellminhit(self) :
        """Min hit value for the object."""
        try :
            return self._cachecellminhit
        except Exception as e:
            raise e

    @property
    def policy(self) :
        """Policy info for the object."""
        try :
            return self._policy
        except Exception as e:
            raise e

    @property
    def policyname(self) :
        """Policy which created the object."""
        try :
            return self._policyname
        except Exception as e:
            raise e

    @property
    def selectorname(self) :
        """The hit selector for the object."""
        try :
            return self._selectorname
        except Exception as e:
            raise e

    @property
    def rule(self) :
        """Selectors for this object."""
        try :
            return self._rule
        except Exception as e:
            raise e

    @property
    def selectorvalue(self) :
        """The HTTP request method that caused the object to be stored."""
        try :
            return self._selectorvalue
        except Exception as e:
            raise e

    @property
    def cacheurls(self) :
        """List of cache object URLs."""
        try :
            return self._cacheurls
        except Exception as e:
            raise e

    @property
    def warnbucketskip(self) :
        """Bucket skipped warning."""
        try :
            return self._warnbucketskip
        except Exception as e:
            raise e

    @property
    def totalobjs(self) :
        """Total objects."""
        try :
            return self._totalobjs
        except Exception as e:
            raise e

    @property
    def httpcalloutcell(self) :
        """Is it a http callout cell ?.<br/>Possible values = YES, NO."""
        try :
            return self._httpcalloutcell
        except Exception as e:
            raise e

    @property
    def httpcalloutname(self) :
        """Name of the http callout."""
        try :
            return self._httpcalloutname
        except Exception as e:
            raise e

    @property
    def returntype(self) :
        """ """
        try :
            return self._returntype
        except Exception as e:
            raise e

    @property
    def httpcalloutresult(self) :
        """First few bytes of http callout response."""
        try :
            return self._httpcalloutresult
        except Exception as e:
            raise e

    @property
    def locatorshow(self) :
        """ID of the cached object."""
        try :
            return self._locatorshow
        except Exception as e:
            raise e

    @property
    def ceflags(self) :
        """Indicates state and type of cached cell."""
        try :
            return self._ceflags
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(cacheobject_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.cacheobject
        except Exception as e :
            raise e

    def _get_object_name(self) :
        """Returns the value of object identifier argument"""
        try :
            return 0
        except Exception as e :
            raise e



    @classmethod
    def expire(cls, client, resource) :
        """Use this API to expire cacheobject.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                expireresource = cacheobject()
                expireresource.locator = resource.locator
                expireresource.url = resource.url
                expireresource.host = resource.host
                expireresource.port = resource.port
                expireresource.groupname = resource.groupname
                expireresource.httpmethod = resource.httpmethod
                return expireresource.perform_operation(client,"expire")
            else :
                if (resource and len(resource) > 0) :
                    expireresources = [ cacheobject() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        expireresources[i].locator = resource[i].locator
                        expireresources[i].url = resource[i].url
                        expireresources[i].host = resource[i].host
                        expireresources[i].port = resource[i].port
                        expireresources[i].groupname = resource[i].groupname
                        expireresources[i].httpmethod = resource[i].httpmethod
                result = cls.perform_operation_bulk_request(client, expireresources,"expire")
            return result
        except Exception as e :
            raise e

    @classmethod
    def flush(cls, client, resource) :
        """Use this API to flush cacheobject.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                flushresource = cacheobject()
                flushresource.locator = resource.locator
                flushresource.url = resource.url
                flushresource.host = resource.host
                flushresource.port = resource.port
                flushresource.groupname = resource.groupname
                flushresource.httpmethod = resource.httpmethod
                return flushresource.perform_operation(client,"flush")
            else :
                if (resource and len(resource) > 0) :
                    flushresources = [ cacheobject() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        flushresources[i].locator = resource[i].locator
                        flushresources[i].url = resource[i].url
                        flushresources[i].host = resource[i].host
                        flushresources[i].port = resource[i].port
                        flushresources[i].groupname = resource[i].groupname
                        flushresources[i].httpmethod = resource[i].httpmethod
                result = cls.perform_operation_bulk_request(client, flushresources,"flush")
            return result
        except Exception as e :
            raise e

    @classmethod
    def save(cls, client, resource) :
        """Use this API to save cacheobject.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                saveresource = cacheobject()
                saveresource.locator = resource.locator
                saveresource.tosecondary = resource.tosecondary
                return saveresource.perform_operation(client,"save")
            else :
                if (resource and len(resource) > 0) :
                    saveresources = [ cacheobject() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        saveresources[i].locator = resource[i].locator
                        saveresources[i].tosecondary = resource[i].tosecondary
                result = cls.perform_operation_bulk_request(client, saveresources,"save")
            return result
        except Exception as e :
            raise e

    @classmethod
    def get(cls, client, name="", option_="") :
        """Use this API to fetch all the cacheobject resources that are configured on netscaler.

        :param client: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            if not name :
                obj = cacheobject()
                response = obj.get_resources(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def get_args(cls, client, args) :
        """Use this API to fetch all the cacheobject resources that are configured on netscaler.
            # This uses cacheobject_args which is a way to provide additional arguments while fetching the resources.

        :param client: 
        :param args: 

        """
        try :
            obj = cacheobject()
            option_ = options()
            option_.args = nitro_util.object_to_string_withoutquotes(args)
            response = obj.get_resources(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def get_filtered(cls, client, filter_) :
        """Use this API to fetch filtered set of cacheobject resources.
        filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = cacheobject()
            option_ = options()
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def count(cls, client) :
        """Use this API to count the cacheobject resources configured on NetScaler.

        :param client: 

        """
        try :
            obj = cacheobject()
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
        """Use this API to count filtered the set of cacheobject resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = cacheobject()
            option_ = options()
            option_.count = True
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            if response :
                return response[0].__dict__['___count']
            return 0
        except Exception as e :
            raise e


    class Cachecellfwpxyobj:
        """ """
        YES = "YES"
        NO = "NO"

    class Tosecondary:
        """ """
        YES = "YES"
        NO = "NO"

    class Cachecellbasefile:
        """ """
        YES = "YES"
        NO = "NO"

    class Cachecellcomplex:
        """ """
        YES = "YES"
        NO = "NO"

    class Cachecellweaketag:
        """ """
        YES = "YES"
        NO = "NO"

    class Ignoremarkerobjects:
        """ """
        ON = "ON"
        OFF = "OFF"

    class Cachecellreadywithlastbyte:
        """ """
        YES = "YES"
        NO = "NO"

    class Flushed:
        """ """
        YES = "YES"
        NO = "NO"

    class Cachecelldestipverified:
        """ """
        YES = "YES"
        NO = "NO"

    class Cachecellhttp11:
        """ """
        YES = "YES"
        NO = "NO"

    class Includenotreadyobjects:
        """ """
        ON = "ON"
        OFF = "OFF"

    class Cachecellminhitflag:
        """ """
        YES = "YES"
        NO = "NO"

    class Cacheindisk:
        """ """
        YES = "YES"
        NO = "NO"

    class Markerreason:
        """ """
        Waiting_for_min_hit = "Waiting for min hit"
        Response_header_is_too_big = "Response header is too big"
        Content_length_header_said_response_size_is_not_in_group_size_limit = "Content-length header said response size is not in group size limit"
        Content_length_response_received_more_data = "Content-length response received more data"
        Content_length_response_received_less_data = "Content-length response received less data"
        Content_length_response_data_is_not_in_group_size_limit = "Content-length response data is not in group size limit"
        Chunk_response_received_more_data = "Chunk response received more data"
        Chunk_response_data_is_not_in_group_size_limit = "Chunk response data is not in group size limit"
        Bad_chunk_format = "Bad chunk format"
        Fin_terminated_response_data_is_not_in_group_size_limit = "Fin terminated response data is not in group size limit"

    class Cachecellpolleverytime:
        """ """
        YES = "YES"
        NO = "NO"

    class Httpmethod:
        """ """
        GET = "GET"
        POST = "POST"

    class Returntype:
        """ """
        BOOL = "BOOL"
        NUM = "NUM"
        TEXT = "TEXT"

    class Httpcalloutcell:
        """ """
        YES = "YES"
        NO = "NO"

    class Cachecelletaginserted:
        """ """
        YES = "YES"
        NO = "NO"

    class Cacheinmemory:
        """ """
        YES = "YES"
        NO = "NO"

    class Cachecellappfwmetadataexists:
        """ """
        YES = "YES"
        NO = "NO"

    class Cachecellresbadsize:
        """ """
        YES = "YES"
        NO = "NO"

    class Prefetch:
        """ """
        YES = "YES"
        NO = "NO"

    class Cacheinsecondary:
        """ """
        YES = "YES"
        NO = "NO"

class cacheobject_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.cacheobject = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.cacheobject = [cacheobject() for _ in range(length)]

