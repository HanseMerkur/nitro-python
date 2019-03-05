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

class locationparameter(base_resource) :
    """Configuration for location parameter resource."""
    def __init__(self) :
        self._context = ""
        self._q1label = ""
        self._q2label = ""
        self._q3label = ""
        self._q4label = ""
        self._q5label = ""
        self._q6label = ""
        self._Locationfile = ""
        self._format = ""
        self._custom = 0
        self._Static = 0
        self._lines = 0
        self._errors = 0
        self._warnings = 0
        self._entries = 0
        self._locationfile6 = ""
        self._format6 = ""
        self._custom6 = 0
        self._static6 = 0
        self._lines6 = 0
        self._errors6 = 0
        self._warnings6 = 0
        self._entries6 = 0
        self._flags = 0
        self._status = 0
        self._databasemode = ""
        self._flushing = ""
        self._loading = ""

    @property
    def context(self) :
        """Context for describing locations. In geographic context, qualifier labels are assigned by default in the following sequence: Continent.Country.Region.City.ISP.Organization. In custom context, the qualifiers labels can have any meaning that you designate.<br/>Possible values = geographic, custom."""
        try :
            return self._context
        except Exception as e:
            raise e

    @context.setter
    def context(self, context) :
        """Context for describing locations. In geographic context, qualifier labels are assigned by default in the following sequence: Continent.Country.Region.City.ISP.Organization. In custom context, the qualifiers labels can have any meaning that you designate.<br/>Possible values = geographic, custom

        :param context: 

        """
        try :
            self._context = context
        except Exception as e:
            raise e

    @property
    def q1label(self) :
        """Label specifying the meaning of the first qualifier. Can be specified for custom context only.<br/>Minimum length =  1."""
        try :
            return self._q1label
        except Exception as e:
            raise e

    @q1label.setter
    def q1label(self, q1label) :
        """Label specifying the meaning of the first qualifier. Can be specified for custom context only.<br/>Minimum length =  1

        :param q1label: 

        """
        try :
            self._q1label = q1label
        except Exception as e:
            raise e

    @property
    def q2label(self) :
        """Label specifying the meaning of the second qualifier. Can be specified for custom context only.<br/>Minimum length =  1."""
        try :
            return self._q2label
        except Exception as e:
            raise e

    @q2label.setter
    def q2label(self, q2label) :
        """Label specifying the meaning of the second qualifier. Can be specified for custom context only.<br/>Minimum length =  1

        :param q2label: 

        """
        try :
            self._q2label = q2label
        except Exception as e:
            raise e

    @property
    def q3label(self) :
        """Label specifying the meaning of the third qualifier. Can be specified for custom context only.<br/>Minimum length =  1."""
        try :
            return self._q3label
        except Exception as e:
            raise e

    @q3label.setter
    def q3label(self, q3label) :
        """Label specifying the meaning of the third qualifier. Can be specified for custom context only.<br/>Minimum length =  1

        :param q3label: 

        """
        try :
            self._q3label = q3label
        except Exception as e:
            raise e

    @property
    def q4label(self) :
        """Label specifying the meaning of the fourth qualifier. Can be specified for custom context only.<br/>Minimum length =  1."""
        try :
            return self._q4label
        except Exception as e:
            raise e

    @q4label.setter
    def q4label(self, q4label) :
        """Label specifying the meaning of the fourth qualifier. Can be specified for custom context only.<br/>Minimum length =  1

        :param q4label: 

        """
        try :
            self._q4label = q4label
        except Exception as e:
            raise e

    @property
    def q5label(self) :
        """Label specifying the meaning of the fifth qualifier. Can be specified for custom context only.<br/>Minimum length =  1."""
        try :
            return self._q5label
        except Exception as e:
            raise e

    @q5label.setter
    def q5label(self, q5label) :
        """Label specifying the meaning of the fifth qualifier. Can be specified for custom context only.<br/>Minimum length =  1

        :param q5label: 

        """
        try :
            self._q5label = q5label
        except Exception as e:
            raise e

    @property
    def q6label(self) :
        """Label specifying the meaning of the sixth qualifier. Can be specified for custom context only.<br/>Minimum length =  1."""
        try :
            return self._q6label
        except Exception as e:
            raise e

    @q6label.setter
    def q6label(self, q6label) :
        """Label specifying the meaning of the sixth qualifier. Can be specified for custom context only.<br/>Minimum length =  1

        :param q6label: 

        """
        try :
            self._q6label = q6label
        except Exception as e:
            raise e

    @property
    def Locationfile(self) :
        """Currently loaded location database file."""
        try :
            return self._Locationfile
        except Exception as e:
            raise e

    @property
    def format(self) :
        """Location file format.<br/>Possible values = netscaler, ip-country, ip-country-isp, ip-country-region-city, ip-country-region-city-isp, geoip-country, geoip-region, geoip-city, geoip-country-org, geoip-country-isp, geoip-city-isp-org."""
        try :
            return self._format
        except Exception as e:
            raise e

    @property
    def custom(self) :
        """Number of configured custom locations."""
        try :
            return self._custom
        except Exception as e:
            raise e

    @property
    def Static(self) :
        """Number of configured locations in the database file (static locations)."""
        try :
            return self._Static
        except Exception as e:
            raise e

    @property
    def lines(self) :
        """Number of lines in the databse files."""
        try :
            return self._lines
        except Exception as e:
            raise e

    @property
    def errors(self) :
        """Number of errros encountered while reading the database file."""
        try :
            return self._errors
        except Exception as e:
            raise e

    @property
    def warnings(self) :
        """Number of warnings encountered while reading the database file."""
        try :
            return self._warnings
        except Exception as e:
            raise e

    @property
    def entries(self) :
        """Number of successfully added entries."""
        try :
            return self._entries
        except Exception as e:
            raise e

    @property
    def locationfile6(self) :
        """Currently loaded location database file."""
        try :
            return self._locationfile6
        except Exception as e:
            raise e

    @property
    def format6(self) :
        """Location file format.<br/>Possible values = netscaler6, geoip-country6."""
        try :
            return self._format6
        except Exception as e:
            raise e

    @property
    def custom6(self) :
        """Number of configured custom locations."""
        try :
            return self._custom6
        except Exception as e:
            raise e

    @property
    def static6(self) :
        """Number of configured locations in the database file (static locations)."""
        try :
            return self._static6
        except Exception as e:
            raise e

    @property
    def lines6(self) :
        """Number of lines in the databse files."""
        try :
            return self._lines6
        except Exception as e:
            raise e

    @property
    def errors6(self) :
        """Number of errros encountered while reading the database file."""
        try :
            return self._errors6
        except Exception as e:
            raise e

    @property
    def warnings6(self) :
        """Number of warnings encountered while reading the database file."""
        try :
            return self._warnings6
        except Exception as e:
            raise e

    @property
    def entries6(self) :
        """Number of successfully added entries."""
        try :
            return self._entries6
        except Exception as e:
            raise e

    @property
    def flags(self) :
        """Information needed for display. This argument passes information from the kernel to the user space."""
        try :
            return self._flags
        except Exception as e:
            raise e

    @property
    def status(self) :
        """This argument displays when the status (success or failure) of database loading."""
        try :
            return self._status
        except Exception as e:
            raise e

    @property
    def databasemode(self) :
        """This argument displays the database mode.<br/>Possible values = File, Internal, Not applicable."""
        try :
            return self._databasemode
        except Exception as e:
            raise e

    @property
    def flushing(self) :
        """This argument displays the state of flushing.<br/>Possible values = In progress, Idle."""
        try :
            return self._flushing
        except Exception as e:
            raise e

    @property
    def loading(self) :
        """This argument displays the state of loading.<br/>Possible values = In progress, Idle."""
        try :
            return self._loading
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(locationparameter_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.locationparameter
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
        """Use this API to update locationparameter.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                updateresource = locationparameter()
                updateresource.context = resource.context
                updateresource.q1label = resource.q1label
                updateresource.q2label = resource.q2label
                updateresource.q3label = resource.q3label
                updateresource.q4label = resource.q4label
                updateresource.q5label = resource.q5label
                updateresource.q6label = resource.q6label
                return updateresource.update_resource(client)
        except Exception as e :
            raise e

    @classmethod
    def unset(cls, client, resource, args) :
        """Use this API to unset the properties of locationparameter resource.
        Properties that need to be unset are specified in args array.

        :param client: 
        :param resource: 
        :param args: 

        """
        try :
            if type(resource) is not list :
                unsetresource = locationparameter()
                return unsetresource.unset_resource(client, args)
        except Exception as e :
            raise e

    @classmethod
    def get(cls, client, name="", option_="") :
        """Use this API to fetch all the locationparameter resources that are configured on netscaler.

        :param client: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            if not name :
                obj = locationparameter()
                response = obj.get_resources(client, option_)
            return response
        except Exception as e :
            raise e


    class Loading:
        """ """
        In_progress = "In progress"
        Idle = "Idle"

    class Databasemode:
        """ """
        File = "File"
        Internal = "Internal"
        Not_applicable = "Not applicable"

    class Format:
        """ """
        netscaler = "netscaler"
        ip_country = "ip-country"
        ip_country_isp = "ip-country-isp"
        ip_country_region_city = "ip-country-region-city"
        ip_country_region_city_isp = "ip-country-region-city-isp"
        geoip_country = "geoip-country"
        geoip_region = "geoip-region"
        geoip_city = "geoip-city"
        geoip_country_org = "geoip-country-org"
        geoip_country_isp = "geoip-country-isp"
        geoip_city_isp_org = "geoip-city-isp-org"

    class Context:
        """ """
        geographic = "geographic"
        custom = "custom"

    class Flushing:
        """ """
        In_progress = "In progress"
        Idle = "Idle"

    class Format6:
        """ """
        netscaler6 = "netscaler6"
        geoip_country6 = "geoip-country6"

class locationparameter_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.locationparameter = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.locationparameter = [locationparameter() for _ in range(length)]

