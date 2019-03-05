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

class auditnslogparams(base_resource) :
    """Configuration for ns log parameters resource."""
    def __init__(self) :
        self._serverip = ""
        self._serverport = 0
        self._dateformat = ""
        self._loglevel = []
        self._logfacility = ""
        self._tcp = ""
        self._acl = ""
        self._timezone = ""
        self._userdefinedauditlog = ""
        self._appflowexport = ""
        self._lsn = ""
        self._alg = ""
        self._subscriberlog = ""
        self._builtin = []

    @property
    def serverip(self) :
        """IP address of the nslog server.<br/>Minimum length =  1."""
        try :
            return self._serverip
        except Exception as e:
            raise e

    @serverip.setter
    def serverip(self, serverip) :
        """IP address of the nslog server.<br/>Minimum length =  1

        :param serverip: 

        """
        try :
            self._serverip = serverip
        except Exception as e:
            raise e

    @property
    def serverport(self) :
        """Port on which the nslog server accepts connections.<br/>Minimum length =  1."""
        try :
            return self._serverport
        except Exception as e:
            raise e

    @serverport.setter
    def serverport(self, serverport) :
        """Port on which the nslog server accepts connections.<br/>Minimum length =  1

        :param serverport: 

        """
        try :
            self._serverport = serverport
        except Exception as e:
            raise e

    @property
    def dateformat(self) :
        """Format of dates in the logs.
        Supported formats are:
        * MMDDYYYY - U.S. style month/date/year format.
        * DDMMYYYY - European style date/month/year format.
        * YYYYMMDD - ISO style year/month/date format.<br/>Possible values = MMDDYYYY, DDMMYYYY, YYYYMMDD.


        """
        try :
            return self._dateformat
        except Exception as e:
            raise e

    @dateformat.setter
    def dateformat(self, dateformat) :
        """Format of dates in the logs.
        Supported formats are:
        * MMDDYYYY - U.S. style month/date/year format.
        * DDMMYYYY - European style date/month/year format.
        * YYYYMMDD - ISO style year/month/date format.<br/>Possible values = MMDDYYYY, DDMMYYYY, YYYYMMDD

        :param dateformat: 

        """
        try :
            self._dateformat = dateformat
        except Exception as e:
            raise e

    @property
    def loglevel(self) :
        """Types of information to be logged.
        Available settings function as follows:
        * ALL - All events.
        * EMERGENCY - Events that indicate an immediate crisis on the server.
        * ALERT - Events that might require action.
        * CRITICAL - Events that indicate an imminent server crisis.
        * ERROR - Events that indicate some type of error.
        * WARNING - Events that require action in the near future.
        * NOTICE - Events that the administrator should know about.
        * INFORMATIONAL - All but low-level events.
        * DEBUG - All events, in extreme detail.
        * NONE - No events.<br/>Possible values = ALL, EMERGENCY, ALERT, CRITICAL, ERROR, WARNING, NOTICE, INFORMATIONAL, DEBUG, NONE.


        """
        try :
            return self._loglevel
        except Exception as e:
            raise e

    @loglevel.setter
    def loglevel(self, loglevel) :
        """Types of information to be logged.
        Available settings function as follows:
        * ALL - All events.
        * EMERGENCY - Events that indicate an immediate crisis on the server.
        * ALERT - Events that might require action.
        * CRITICAL - Events that indicate an imminent server crisis.
        * ERROR - Events that indicate some type of error.
        * WARNING - Events that require action in the near future.
        * NOTICE - Events that the administrator should know about.
        * INFORMATIONAL - All but low-level events.
        * DEBUG - All events, in extreme detail.
        * NONE - No events.<br/>Possible values = ALL, EMERGENCY, ALERT, CRITICAL, ERROR, WARNING, NOTICE, INFORMATIONAL, DEBUG, NONE

        :param loglevel: 

        """
        try :
            self._loglevel = loglevel
        except Exception as e:
            raise e

    @property
    def logfacility(self) :
        """Facility value, as defined in RFC 3164, assigned to the log message.
        Log facility values are numbers 0 to 7 (LOCAL0 through LOCAL7). Each number indicates where a specific message originated from, such as the NetScaler appliance itself, the VPN, or external.<br/>Possible values = LOCAL0, LOCAL1, LOCAL2, LOCAL3, LOCAL4, LOCAL5, LOCAL6, LOCAL7.


        """
        try :
            return self._logfacility
        except Exception as e:
            raise e

    @logfacility.setter
    def logfacility(self, logfacility) :
        """Facility value, as defined in RFC 3164, assigned to the log message.
        Log facility values are numbers 0 to 7 (LOCAL0 through LOCAL7). Each number indicates where a specific message originated from, such as the NetScaler appliance itself, the VPN, or external.<br/>Possible values = LOCAL0, LOCAL1, LOCAL2, LOCAL3, LOCAL4, LOCAL5, LOCAL6, LOCAL7

        :param logfacility: 

        """
        try :
            self._logfacility = logfacility
        except Exception as e:
            raise e

    @property
    def tcp(self) :
        """Configure auditing to log TCP messages.<br/>Possible values = NONE, ALL."""
        try :
            return self._tcp
        except Exception as e:
            raise e

    @tcp.setter
    def tcp(self, tcp) :
        """Configure auditing to log TCP messages.<br/>Possible values = NONE, ALL

        :param tcp: 

        """
        try :
            self._tcp = tcp
        except Exception as e:
            raise e

    @property
    def acl(self) :
        """Configure auditing to log access control list (ACL) messages.<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._acl
        except Exception as e:
            raise e

    @acl.setter
    def acl(self, acl) :
        """Configure auditing to log access control list (ACL) messages.<br/>Possible values = ENABLED, DISABLED

        :param acl: 

        """
        try :
            self._acl = acl
        except Exception as e:
            raise e

    @property
    def timezone(self) :
        """Time zone used for date and timestamps in the logs.
        Supported settings are:
        * GMT_TIME - Coordinated Universal Time.
        * LOCAL_TIME - Use the server's timezone setting.<br/>Possible values = GMT_TIME, LOCAL_TIME.


        """
        try :
            return self._timezone
        except Exception as e:
            raise e

    @timezone.setter
    def timezone(self, timezone) :
        """Time zone used for date and timestamps in the logs.
        Supported settings are:
        * GMT_TIME - Coordinated Universal Time.
        * LOCAL_TIME - Use the server's timezone setting.<br/>Possible values = GMT_TIME, LOCAL_TIME

        :param timezone: 

        """
        try :
            self._timezone = timezone
        except Exception as e:
            raise e

    @property
    def userdefinedauditlog(self) :
        """Log user-configurable log messages to nslog.
        Setting this parameter to NO causes auditing to ignore all user-configured message actions. Setting this parameter to YES causes auditing to log user-configured message actions that meet the other logging criteria.<br/>Possible values = YES, NO.


        """
        try :
            return self._userdefinedauditlog
        except Exception as e:
            raise e

    @userdefinedauditlog.setter
    def userdefinedauditlog(self, userdefinedauditlog) :
        """Log user-configurable log messages to nslog.
        Setting this parameter to NO causes auditing to ignore all user-configured message actions. Setting this parameter to YES causes auditing to log user-configured message actions that meet the other logging criteria.<br/>Possible values = YES, NO

        :param userdefinedauditlog: 

        """
        try :
            self._userdefinedauditlog = userdefinedauditlog
        except Exception as e:
            raise e

    @property
    def appflowexport(self) :
        """Export log messages to AppFlow collectors.
        Appflow collectors are entities to which log messages can be sent so that some action can be performed on them.<br/>Possible values = ENABLED, DISABLED.


        """
        try :
            return self._appflowexport
        except Exception as e:
            raise e

    @appflowexport.setter
    def appflowexport(self, appflowexport) :
        """Export log messages to AppFlow collectors.
        Appflow collectors are entities to which log messages can be sent so that some action can be performed on them.<br/>Possible values = ENABLED, DISABLED

        :param appflowexport: 

        """
        try :
            self._appflowexport = appflowexport
        except Exception as e:
            raise e

    @property
    def lsn(self) :
        """Log the LSN messages.<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._lsn
        except Exception as e:
            raise e

    @lsn.setter
    def lsn(self, lsn) :
        """Log the LSN messages.<br/>Possible values = ENABLED, DISABLED

        :param lsn: 

        """
        try :
            self._lsn = lsn
        except Exception as e:
            raise e

    @property
    def alg(self) :
        """Log the ALG messages.<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._alg
        except Exception as e:
            raise e

    @alg.setter
    def alg(self, alg) :
        """Log the ALG messages.<br/>Possible values = ENABLED, DISABLED

        :param alg: 

        """
        try :
            self._alg = alg
        except Exception as e:
            raise e

    @property
    def subscriberlog(self) :
        """Log subscriber session event information.<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._subscriberlog
        except Exception as e:
            raise e

    @subscriberlog.setter
    def subscriberlog(self, subscriberlog) :
        """Log subscriber session event information.<br/>Possible values = ENABLED, DISABLED

        :param subscriberlog: 

        """
        try :
            self._subscriberlog = subscriberlog
        except Exception as e:
            raise e

    @property
    def builtin(self) :
        """Indicates that a variable is a built-in (SYSTEM INTERNAL) type.<br/>Possible values = MODIFIABLE, DELETABLE, IMMUTABLE, PARTITION_ALL."""
        try :
            return self._builtin
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(auditnslogparams_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.auditnslogparams
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
        """Use this API to update auditnslogparams.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                updateresource = auditnslogparams()
                updateresource.serverip = resource.serverip
                updateresource.serverport = resource.serverport
                updateresource.dateformat = resource.dateformat
                updateresource.loglevel = resource.loglevel
                updateresource.logfacility = resource.logfacility
                updateresource.tcp = resource.tcp
                updateresource.acl = resource.acl
                updateresource.timezone = resource.timezone
                updateresource.userdefinedauditlog = resource.userdefinedauditlog
                updateresource.appflowexport = resource.appflowexport
                updateresource.lsn = resource.lsn
                updateresource.alg = resource.alg
                updateresource.subscriberlog = resource.subscriberlog
                return updateresource.update_resource(client)
        except Exception as e :
            raise e

    @classmethod
    def unset(cls, client, resource, args) :
        """Use this API to unset the properties of auditnslogparams resource.
        Properties that need to be unset are specified in args array.

        :param client: 
        :param resource: 
        :param args: 

        """
        try :
            if type(resource) is not list :
                unsetresource = auditnslogparams()
                return unsetresource.unset_resource(client, args)
        except Exception as e :
            raise e

    @classmethod
    def get(cls, client, name="", option_="") :
        """Use this API to fetch all the auditnslogparams resources that are configured on netscaler.

        :param client: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            if not name :
                obj = auditnslogparams()
                response = obj.get_resources(client, option_)
            return response
        except Exception as e :
            raise e


    class Userdefinedauditlog:
        """ """
        YES = "YES"
        NO = "NO"

    class Builtin:
        """ """
        MODIFIABLE = "MODIFIABLE"
        DELETABLE = "DELETABLE"
        IMMUTABLE = "IMMUTABLE"
        PARTITION_ALL = "PARTITION_ALL"

    class Timezone:
        """ """
        GMT_TIME = "GMT_TIME"
        LOCAL_TIME = "LOCAL_TIME"

    class Dateformat:
        """ """
        MMDDYYYY = "MMDDYYYY"
        DDMMYYYY = "DDMMYYYY"
        YYYYMMDD = "YYYYMMDD"

    class Acl:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Lsn:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Subscriberlog:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Alg:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Logfacility:
        """ """
        LOCAL0 = "LOCAL0"
        LOCAL1 = "LOCAL1"
        LOCAL2 = "LOCAL2"
        LOCAL3 = "LOCAL3"
        LOCAL4 = "LOCAL4"
        LOCAL5 = "LOCAL5"
        LOCAL6 = "LOCAL6"
        LOCAL7 = "LOCAL7"

    class Loglevel:
        """ """
        ALL = "ALL"
        EMERGENCY = "EMERGENCY"
        ALERT = "ALERT"
        CRITICAL = "CRITICAL"
        ERROR = "ERROR"
        WARNING = "WARNING"
        NOTICE = "NOTICE"
        INFORMATIONAL = "INFORMATIONAL"
        DEBUG = "DEBUG"
        NONE = "NONE"

    class Tcp:
        """ """
        NONE = "NONE"
        ALL = "ALL"

    class Appflowexport:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

class auditnslogparams_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.auditnslogparams = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.auditnslogparams = [auditnslogparams() for _ in range(length)]

