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

class systemparameter(base_resource) :
    """Configuration for system parameter resource."""
    def __init__(self) :
        self._rbaonresponse = ""
        self._promptstring = ""
        self._natpcbforceflushlimit = 0
        self._natpcbrstontimeout = ""
        self._timeout = 0
        self._localauth = ""
        self._minpasswordlen = 0
        self._strongpassword = ""
        self._restrictedtimeout = ""
        self._fipsusermode = ""
        self._doppler = ""
        self._googleanalytics = ""
        self._cliloglevel = ""
        self._maxclient = 0

    @property
    def rbaonresponse(self) :
        """Enable or disable Role-Based Authentication (RBA) on responses.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._rbaonresponse
        except Exception as e:
            raise e

    @rbaonresponse.setter
    def rbaonresponse(self, rbaonresponse) :
        """Enable or disable Role-Based Authentication (RBA) on responses.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED

        :param rbaonresponse: 

        """
        try :
            self._rbaonresponse = rbaonresponse
        except Exception as e:
            raise e

    @property
    def promptstring(self) :
        """String to display at the command-line prompt. Can consist of letters, numbers, hyphen (-), period (.), hash (#), space ( ), at (@), equal (=), colon (:), underscore (_), and the following variables:
        * %u - Will be replaced by the user name.
        * %h - Will be replaced by the hostname of the NetScaler appliance.
        * %t - Will be replaced by the current time in 12-hour format.
        * %T - Will be replaced by the current time in 24-hour format.
        * %d - Will be replaced by the current date.
        * %s - Will be replaced by the state of the NetScaler appliance.
        Note: The 63-character limit for the length of the string does not apply to the characters that replace the variables.<br/>Minimum length =  1.


        """
        try :
            return self._promptstring
        except Exception as e:
            raise e

    @promptstring.setter
    def promptstring(self, promptstring) :
        """String to display at the command-line prompt. Can consist of letters, numbers, hyphen (-), period (.), hash (#), space ( ), at (@), equal (=), colon (:), underscore (_), and the following variables:
        * %u - Will be replaced by the user name.
        * %h - Will be replaced by the hostname of the NetScaler appliance.
        * %t - Will be replaced by the current time in 12-hour format.
        * %T - Will be replaced by the current time in 24-hour format.
        * %d - Will be replaced by the current date.
        * %s - Will be replaced by the state of the NetScaler appliance.
        Note: The 63-character limit for the length of the string does not apply to the characters that replace the variables.<br/>Minimum length =  1

        :param promptstring: 

        """
        try :
            self._promptstring = promptstring
        except Exception as e:
            raise e

    @property
    def natpcbforceflushlimit(self) :
        """Flush the system if the number of Network Address Translation Protocol Control Blocks (NATPCBs) exceeds this value.<br/>Default value: 2147483647<br/>Minimum length =  1000."""
        try :
            return self._natpcbforceflushlimit
        except Exception as e:
            raise e

    @natpcbforceflushlimit.setter
    def natpcbforceflushlimit(self, natpcbforceflushlimit) :
        """Flush the system if the number of Network Address Translation Protocol Control Blocks (NATPCBs) exceeds this value.<br/>Default value: 2147483647<br/>Minimum length =  1000

        :param natpcbforceflushlimit: 

        """
        try :
            self._natpcbforceflushlimit = natpcbforceflushlimit
        except Exception as e:
            raise e

    @property
    def natpcbrstontimeout(self) :
        """Send a reset signal to client and server connections when their NATPCBs time out. Avoids the buildup of idle TCP connections on both the sides.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._natpcbrstontimeout
        except Exception as e:
            raise e

    @natpcbrstontimeout.setter
    def natpcbrstontimeout(self, natpcbrstontimeout) :
        """Send a reset signal to client and server connections when their NATPCBs time out. Avoids the buildup of idle TCP connections on both the sides.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED

        :param natpcbrstontimeout: 

        """
        try :
            self._natpcbrstontimeout = natpcbrstontimeout
        except Exception as e:
            raise e

    @property
    def timeout(self) :
        """CLI session inactivity timeout, in seconds. If Restrictedtimeout argument is enabled, Timeout can have values in the range [300-86400] seconds.
        If Restrictedtimeout argument is disabled, Timeout can have values in the range [0, 10-100000000] seconds. Default value is 900 seconds.


        """
        try :
            return self._timeout
        except Exception as e:
            raise e

    @timeout.setter
    def timeout(self, timeout) :
        """CLI session inactivity timeout, in seconds. If Restrictedtimeout argument is enabled, Timeout can have values in the range [300-86400] seconds.
        If Restrictedtimeout argument is disabled, Timeout can have values in the range [0, 10-100000000] seconds. Default value is 900 seconds.

        :param timeout: 

        """
        try :
            self._timeout = timeout
        except Exception as e:
            raise e

    @property
    def localauth(self) :
        """When enabled, local users can access NetScaler even when external authentication is configured. When disabled, local users are not allowed to access the NetScaler, Local users can access the NetScaler only when the configured external authentication servers are unavailable.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._localauth
        except Exception as e:
            raise e

    @localauth.setter
    def localauth(self, localauth) :
        """When enabled, local users can access NetScaler even when external authentication is configured. When disabled, local users are not allowed to access the NetScaler, Local users can access the NetScaler only when the configured external authentication servers are unavailable.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED

        :param localauth: 

        """
        try :
            self._localauth = localauth
        except Exception as e:
            raise e

    @property
    def minpasswordlen(self) :
        """Minimum length of system user password. When strong password is enabled default minimum length is 4. User entered value can be greater than or equal to 4. Default mininum value is 1 when strong password is disabled. Maximum value is 127 in both cases.<br/>Minimum length =  1<br/>Maximum length =  127."""
        try :
            return self._minpasswordlen
        except Exception as e:
            raise e

    @minpasswordlen.setter
    def minpasswordlen(self, minpasswordlen) :
        """Minimum length of system user password. When strong password is enabled default minimum length is 4. User entered value can be greater than or equal to 4. Default mininum value is 1 when strong password is disabled. Maximum value is 127 in both cases.<br/>Minimum length =  1<br/>Maximum length =  127

        :param minpasswordlen: 

        """
        try :
            self._minpasswordlen = minpasswordlen
        except Exception as e:
            raise e

    @property
    def strongpassword(self) :
        """Option to enable/disable strong password. When this is enabled, system user password should contain atleast one lower case character, one upper case character, one numeric character and one special character from the set (!, @, #, (, ), $, %, ^, &, *).<br/>Default value: disabled<br/>Possible values = enableall, enablelocal, disabled."""
        try :
            return self._strongpassword
        except Exception as e:
            raise e

    @strongpassword.setter
    def strongpassword(self, strongpassword) :
        """Option to enable/disable strong password. When this is enabled, system user password should contain atleast one lower case character, one upper case character, one numeric character and one special character from the set (!, @, #, (, ), $, %, ^, &, *).<br/>Default value: disabled<br/>Possible values = enableall, enablelocal, disabled

        :param strongpassword: 

        """
        try :
            self._strongpassword = strongpassword
        except Exception as e:
            raise e

    @property
    def restrictedtimeout(self) :
        """Enable/Disable the restricted timeout behaviour. When enabled, timeout cannot be configured beyond admin configured timeout and also it will have the [minimum - maximum] range check. When disabled, timeout will have the old behaviour. By default the value is disabled.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._restrictedtimeout
        except Exception as e:
            raise e

    @restrictedtimeout.setter
    def restrictedtimeout(self, restrictedtimeout) :
        """Enable/Disable the restricted timeout behaviour. When enabled, timeout cannot be configured beyond admin configured timeout and also it will have the [minimum - maximum] range check. When disabled, timeout will have the old behaviour. By default the value is disabled.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED

        :param restrictedtimeout: 

        """
        try :
            self._restrictedtimeout = restrictedtimeout
        except Exception as e:
            raise e

    @property
    def fipsusermode(self) :
        """Use this option to set the FIPS mode for key user-land processes. When enabled, these user-land processes will operate in FIPS mode. In this mode, theses processes will use FIPS 140-2 Level-1 certified crypto algorithms. Default is disabled, wherein, these user-land processes will not operate in FIPS mode.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._fipsusermode
        except Exception as e:
            raise e

    @fipsusermode.setter
    def fipsusermode(self, fipsusermode) :
        """Use this option to set the FIPS mode for key user-land processes. When enabled, these user-land processes will operate in FIPS mode. In this mode, theses processes will use FIPS 140-2 Level-1 certified crypto algorithms. Default is disabled, wherein, these user-land processes will not operate in FIPS mode.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED

        :param fipsusermode: 

        """
        try :
            self._fipsusermode = fipsusermode
        except Exception as e:
            raise e

    @property
    def doppler(self) :
        """Enable or disable Doppler.<br/>Default value: 0<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._doppler
        except Exception as e:
            raise e

    @doppler.setter
    def doppler(self, doppler) :
        """Enable or disable Doppler.<br/>Default value: 0<br/>Possible values = ENABLED, DISABLED

        :param doppler: 

        """
        try :
            self._doppler = doppler
        except Exception as e:
            raise e

    @property
    def googleanalytics(self) :
        """Enable or disable Google analytics.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._googleanalytics
        except Exception as e:
            raise e

    @googleanalytics.setter
    def googleanalytics(self, googleanalytics) :
        """Enable or disable Google analytics.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED

        :param googleanalytics: 

        """
        try :
            self._googleanalytics = googleanalytics
        except Exception as e:
            raise e

    @property
    def cliloglevel(self) :
        """Audit log level, which specifies the types of events to log for cli executed commands.
        Available values function as follows:
        * EMERGENCY - Events that indicate an immediate crisis on the server.
        * ALERT - Events that might require action.
        * CRITICAL - Events that indicate an imminent server crisis.
        * ERROR - Events that indicate some type of error.
        * WARNING - Events that require action in the near future.
        * NOTICE - Events that the administrator should know about.
        * INFORMATIONAL - All but low-level events.
        * DEBUG - All events, in extreme detail.<br/>Default value: DEFAULT_LOGLEVEL_CLI<br/>Possible values = EMERGENCY, ALERT, CRITICAL, ERROR, WARNING, NOTICE, INFORMATIONAL, DEBUG.


        """
        try :
            return self._cliloglevel
        except Exception as e:
            raise e

    @cliloglevel.setter
    def cliloglevel(self, cliloglevel) :
        """Audit log level, which specifies the types of events to log for cli executed commands.
        Available values function as follows:
        * EMERGENCY - Events that indicate an immediate crisis on the server.
        * ALERT - Events that might require action.
        * CRITICAL - Events that indicate an imminent server crisis.
        * ERROR - Events that indicate some type of error.
        * WARNING - Events that require action in the near future.
        * NOTICE - Events that the administrator should know about.
        * INFORMATIONAL - All but low-level events.
        * DEBUG - All events, in extreme detail.<br/>Default value: DEFAULT_LOGLEVEL_CLI<br/>Possible values = EMERGENCY, ALERT, CRITICAL, ERROR, WARNING, NOTICE, INFORMATIONAL, DEBUG

        :param cliloglevel: 

        """
        try :
            self._cliloglevel = cliloglevel
        except Exception as e:
            raise e

    @property
    def maxclient(self) :
        """Maximum number of client connection allowed by the system.<br/>Minimum value =  20<br/>Maximum value =  40."""
        try :
            return self._maxclient
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(systemparameter_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.systemparameter
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
        """Use this API to update systemparameter.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                updateresource = systemparameter()
                updateresource.rbaonresponse = resource.rbaonresponse
                updateresource.promptstring = resource.promptstring
                updateresource.natpcbforceflushlimit = resource.natpcbforceflushlimit
                updateresource.natpcbrstontimeout = resource.natpcbrstontimeout
                updateresource.timeout = resource.timeout
                updateresource.localauth = resource.localauth
                updateresource.minpasswordlen = resource.minpasswordlen
                updateresource.strongpassword = resource.strongpassword
                updateresource.restrictedtimeout = resource.restrictedtimeout
                updateresource.fipsusermode = resource.fipsusermode
                updateresource.doppler = resource.doppler
                updateresource.googleanalytics = resource.googleanalytics
                updateresource.cliloglevel = resource.cliloglevel
                return updateresource.update_resource(client)
        except Exception as e :
            raise e

    @classmethod
    def unset(cls, client, resource, args) :
        """Use this API to unset the properties of systemparameter resource.
        Properties that need to be unset are specified in args array.

        :param client: 
        :param resource: 
        :param args: 

        """
        try :
            if type(resource) is not list :
                unsetresource = systemparameter()
                return unsetresource.unset_resource(client, args)
        except Exception as e :
            raise e

    @classmethod
    def get(cls, client, name="", option_="") :
        """Use this API to fetch all the systemparameter resources that are configured on netscaler.

        :param client: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            if not name :
                obj = systemparameter()
                response = obj.get_resources(client, option_)
            return response
        except Exception as e :
            raise e


    class Strongpassword:
        """ """
        enableall = "enableall"
        enablelocal = "enablelocal"
        disabled = "disabled"

    class Localauth:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Fipsusermode:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Doppler:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Googleanalytics:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Restrictedtimeout:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Rbaonresponse:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Cliloglevel:
        """ """
        EMERGENCY = "EMERGENCY"
        ALERT = "ALERT"
        CRITICAL = "CRITICAL"
        ERROR = "ERROR"
        WARNING = "WARNING"
        NOTICE = "NOTICE"
        INFORMATIONAL = "INFORMATIONAL"
        DEBUG = "DEBUG"

    class Natpcbrstontimeout:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

class systemparameter_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.systemparameter = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.systemparameter = [systemparameter() for _ in range(length)]

