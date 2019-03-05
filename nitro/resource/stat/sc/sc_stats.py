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

class sc_stats(base_resource) :
    """ """
    def __init__(self) :
        self._clearstats = ""
        self._sctotcondtriggered = 0
        self._sccondtriggeredrate = 0
        self._scpolicyurlhits = 0
        self._scpolicyurlhitsrate = 0
        self._scpopups = 0
        self._scpopupsrate = 0
        self._sctotreissuedrequests = 0
        self._screissuedrequestsrate = 0
        self._scsessionreqs = 0
        self._scsessionreqsrate = 0
        self._scaltconturls = 0
        self._scaltconturlsrate = 0
        self._scpostreqs = 0
        self._scpostreqsrate = 0
        self._scresetstats = 0
        self._scresetstatsrate = 0
        self._scunsupbrow = 0
        self._scunsupbrowrate = 0
        self._scfaultycookies = 0
        self._scfaultycookiesrate = 0

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
    def scpopups(self) :
        """Total number of in-memory java script  served which throws the pop-up window."""
        try :
            return self._scpopups
        except Exception as e:
            raise e

    @property
    def scfaultycookiesrate(self) :
        """Rate (/s) counter for scfaultycookies."""
        try :
            return self._scfaultycookiesrate
        except Exception as e:
            raise e

    @property
    def screissuedrequestsrate(self) :
        """Rate (/s) counter for sctotreissuedrequests."""
        try :
            return self._screissuedrequestsrate
        except Exception as e:
            raise e

    @property
    def scpostreqs(self) :
        """Total number of   HTTP POST requests that triggered SureConnect feature."""
        try :
            return self._scpostreqs
        except Exception as e:
            raise e

    @property
    def scaltconturls(self) :
        """Total number of alternate content served which throws the pop-up window."""
        try :
            return self._scaltconturls
        except Exception as e:
            raise e

    @property
    def scresetstatsrate(self) :
        """Rate (/s) counter for scresetstats."""
        try :
            return self._scresetstatsrate
        except Exception as e:
            raise e

    @property
    def scpopupsrate(self) :
        """Rate (/s) counter for scpopups."""
        try :
            return self._scpopupsrate
        except Exception as e:
            raise e

    @property
    def sctotreissuedrequests(self) :
        """Total number of reissued SureConnect requests."""
        try :
            return self._sctotreissuedrequests
        except Exception as e:
            raise e

    @property
    def scunsupbrow(self) :
        """Total number of requests that came from all unsupported browsers."""
        try :
            return self._scunsupbrow
        except Exception as e:
            raise e

    @property
    def scpolicyurlhitsrate(self) :
        """Rate (/s) counter for scpolicyurlhits."""
        try :
            return self._scpolicyurlhitsrate
        except Exception as e:
            raise e

    @property
    def sccondtriggeredrate(self) :
        """Rate (/s) counter for sctotcondtriggered."""
        try :
            return self._sccondtriggeredrate
        except Exception as e:
            raise e

    @property
    def scpolicyurlhits(self) :
        """Total number of incoming requests that matched configured sureconnect policies."""
        try :
            return self._scpolicyurlhits
        except Exception as e:
            raise e

    @property
    def scsessionreqsrate(self) :
        """Rate (/s) counter for scsessionreqs."""
        try :
            return self._scsessionreqsrate
        except Exception as e:
            raise e

    @property
    def scresetstats(self) :
        """Toal number of times that SureConnect statistics were reset."""
        try :
            return self._scresetstats
        except Exception as e:
            raise e

    @property
    def sctotcondtriggered(self) :
        """Number of times that SureConnect conditions were triggered."""
        try :
            return self._sctotcondtriggered
        except Exception as e:
            raise e

    @property
    def scfaultycookies(self) :
        """Total number of corrupted SureConnect cookies."""
        try :
            return self._scfaultycookies
        except Exception as e:
            raise e

    @property
    def scsessionreqs(self) :
        """Total number of requests that were  handled in a single SureConnect session."""
        try :
            return self._scsessionreqs
        except Exception as e:
            raise e

    @property
    def scaltconturlsrate(self) :
        """Rate (/s) counter for scaltconturls."""
        try :
            return self._scaltconturlsrate
        except Exception as e:
            raise e

    @property
    def scunsupbrowrate(self) :
        """Rate (/s) counter for scunsupbrow."""
        try :
            return self._scunsupbrowrate
        except Exception as e:
            raise e

    @property
    def scpostreqsrate(self) :
        """Rate (/s) counter for scpostreqs."""
        try :
            return self._scpostreqsrate
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(sc_response, response, self.__class__.__name__.replace('_stats',''))
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.sc
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
        """Use this API to fetch the statistics of all sc_stats resources that are configured on netscaler.

        :param service: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            obj = sc_stats()
            if not name :
                response = obj.stat_resources(service, option_)
            return response
        except Exception as e:
            raise e

    class Clearstats:
        """ """
        basic = "basic"
        full = "full"

class sc_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.sc = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.sc = [sc_stats() for _ in range(length)]

