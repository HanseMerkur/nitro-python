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

class nsmemory_stats(base_resource) :
    """Statistics for  resource."""
    def __init__(self) :
        self._pool = ""
        self._clearstats = ""
        self._allocf = 0
        self._memcurallocper = 0
        self._memcurinkb = 0

    @property
    def pool(self) :
        """Feature name for which to display memory statistics.<br/>Minimum length =  1."""
        try :
            return self._pool
        except Exception as e:
            raise e

    @pool.setter
    def pool(self, pool) :
        """Feature name for which to display memory statistics.

        :param pool: 

        """
        try :
            self._pool = pool
        except Exception as e:
            raise e

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
    def memcurinkb(self) :
        """Total current NetScaler memory available for use by the feature, in kilobytes."""
        try :
            return self._memcurinkb
        except Exception as e:
            raise e

    @property
    def allocf(self) :
        """Memory allocation failure for particular feature."""
        try :
            return self._allocf
        except Exception as e:
            raise e

    @property
    def memcurallocper(self) :
        """Percentage of NetScaler memory used by the feature."""
        try :
            return self._memcurallocper
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(nsmemory_response, response, self.__class__.__name__.replace('_stats',''))
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.nsmemory
        except Exception as e :
            raise e

    def _get_object_name(self) :
        """Returns the value of object identifier argument"""
        try :
            if self.pool is not None :
                return str(self.pool)
            return None
        except Exception as e :
            raise e



    @classmethod
    def  get(cls, service, name="", option_="") :
        """Use this API to fetch the statistics of all nsmemory_stats resources that are configured on netscaler.

        :param service: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            obj = nsmemory_stats()
            if not name :
                response = obj.stat_resources(service, option_)
            else :
                obj.pool = name
                response = obj.stat_resource(service, option_)
            return response
        except Exception as e:
            raise e

    class Clearstats:
        """ """
        basic = "basic"
        full = "full"

class nsmemory_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.nsmemory = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.nsmemory = [nsmemory_stats() for _ in range(length)]

