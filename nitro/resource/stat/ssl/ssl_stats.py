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

class ssl_stats(base_resource) :
    """ """
    def __init__(self) :
        self._clearstats = ""
        self._sslcryptoutilizationstat = 0
        self._sslnumcardsup = 0
        self._sslcardstatus = 0
        self._sslcards = 0
        self._sslenginestatus = 0
        self._ssltotsessions = 0
        self._sslsessionsrate = 0
        self._ssltottransactions = 0
        self._ssltransactionsrate = 0
        self._ssltotsslv2transactions = 0
        self._sslsslv2transactionsrate = 0
        self._ssltotsslv3transactions = 0
        self._sslsslv3transactionsrate = 0
        self._ssltottlsv1transactions = 0
        self._ssltlsv1transactionsrate = 0
        self._ssltottlsv11transactions = 0
        self._ssltlsv11transactionsrate = 0
        self._ssltottlsv12transactions = 0
        self._ssltlsv12transactionsrate = 0
        self._ssltotsslv2sessions = 0
        self._sslsslv2sessionsrate = 0
        self._ssltotsslv3sessions = 0
        self._sslsslv3sessionsrate = 0
        self._ssltottlsv1sessions = 0
        self._ssltlsv1sessionsrate = 0
        self._ssltottlsv11sessions = 0
        self._ssltlsv11sessionsrate = 0
        self._ssltottlsv12sessions = 0
        self._ssltlsv12sessionsrate = 0
        self._ssltotnewsessions = 0
        self._sslnewsessionsrate = 0
        self._ssltotsessionmiss = 0
        self._sslsessionmissrate = 0
        self._ssltotsessionhits = 0
        self._sslsessionhitsrate = 0
        self._sslbetotsessions = 0
        self._sslbesessionsrate = 0
        self._sslbetotsslv3sessions = 0
        self._sslbesslv3sessionsrate = 0
        self._sslbetottlsv1sessions = 0
        self._sslbetlsv1sessionsrate = 0
        self._sslbetottlsv11sessions = 0
        self._sslbetlsv11sessionsrate = 0
        self._sslbetottlsv12sessions = 0
        self._sslbetlsv12sessionsrate = 0
        self._sslbetotsessionmultiplexattempts = 0
        self._sslbesessionmultiplexattemptsrate = 0
        self._sslbetotsessionmultiplexattemptsuccess = 0
        self._sslbesessionmultiplexattemptsuccessrate = 0
        self._sslbetotsessionmultiplexattemptfails = 0
        self._sslbesessionmultiplexattemptfailsrate = 0
        self._ssltotenc = 0
        self._sslencrate = 0
        self._ssltotdec = 0
        self._ssldecrate = 0
        self._ssltotrenegsessions = 0
        self._sslrenegsessionsrate = 0
        self._ssltotsslv3renegsessions = 0
        self._sslsslv3renegsessionsrate = 0
        self._ssltottlsv1renegsessions = 0
        self._ssltlsv1renegsessionsrate = 0
        self._ssltottlsv11renegsessions = 0
        self._ssltlsv11renegsessionsrate = 0
        self._ssltottlsv12renegsessions = 0
        self._ssltlsv12renegsessionsrate = 0
        self._ssltotrsa512keyexchanges = 0
        self._sslrsa512keyexchangesrate = 0
        self._ssltotrsa1024keyexchanges = 0
        self._sslrsa1024keyexchangesrate = 0
        self._ssltotrsa2048keyexchanges = 0
        self._sslrsa2048keyexchangesrate = 0
        self._ssltotrsa4096keyexchanges = 0
        self._sslrsa4096keyexchangesrate = 0
        self._ssltotdh512keyexchanges = 0
        self._ssldh512keyexchangesrate = 0
        self._ssltotdh1024keyexchanges = 0
        self._ssldh1024keyexchangesrate = 0
        self._ssltotdh2048keyexchanges = 0
        self._ssldh2048keyexchangesrate = 0
        self._ssltotecdhe521keyexchanges = 0
        self._sslecdhe521keyexchangesrate = 0
        self._ssltotecdhe384keyexchanges = 0
        self._sslecdhe384keyexchangesrate = 0
        self._ssltotecdhe256keyexchanges = 0
        self._sslecdhe256keyexchangesrate = 0
        self._ssltotecdhe224keyexchanges = 0
        self._sslecdhe224keyexchangesrate = 0
        self._ssltot40bitrc4ciphers = 0
        self._ssl40bitrc4ciphersrate = 0
        self._ssltot56bitrc4ciphers = 0
        self._ssl56bitrc4ciphersrate = 0
        self._ssltot64bitrc4ciphers = 0
        self._ssl64bitrc4ciphersrate = 0
        self._ssltot128bitrc4ciphers = 0
        self._ssl128bitrc4ciphersrate = 0
        self._ssltot40bitdesciphers = 0
        self._ssl40bitdesciphersrate = 0
        self._ssltot56bitdesciphers = 0
        self._ssl56bitdesciphersrate = 0
        self._ssltot168bit3desciphers = 0
        self._ssl168bit3desciphersrate = 0
        self._ssltotcipheraes128 = 0
        self._sslcipheraes128rate = 0
        self._ssltotcipheraes256 = 0
        self._sslcipheraes256rate = 0
        self._ssltot40bitrc2ciphers = 0
        self._ssl40bitrc2ciphersrate = 0
        self._ssltot56bitrc2ciphers = 0
        self._ssl56bitrc2ciphersrate = 0
        self._ssltot128bitrc2ciphers = 0
        self._ssl128bitrc2ciphersrate = 0
        self._ssltot128bitaesgcmciphers = 0
        self._ssl128bitaesgcmciphersrate = 0
        self._ssltot256bitaesgcmciphers = 0
        self._ssl256bitaesgcmciphersrate = 0
        self._ssltotnullciphers = 0
        self._sslnullciphersrate = 0
        self._ssltotmd5mac = 0
        self._sslmd5macrate = 0
        self._ssltotshamac = 0
        self._sslshamacrate = 0
        self._ssltotsslv2handshakes = 0
        self._sslsslv2handshakesrate = 0
        self._ssltotsslv3handshakes = 0
        self._sslsslv3handshakesrate = 0
        self._ssltottlsv1handshakes = 0
        self._ssltlsv1handshakesrate = 0
        self._ssltottlsv11handshakes = 0
        self._ssltlsv11handshakesrate = 0
        self._ssltottlsv12handshakes = 0
        self._ssltlsv12handshakesrate = 0
        self._ssltotsslv2clientauthentications = 0
        self._sslsslv2clientauthenticationsrate = 0
        self._ssltotsslv3clientauthentications = 0
        self._sslsslv3clientauthenticationsrate = 0
        self._ssltottlsv1clientauthentications = 0
        self._ssltlsv1clientauthenticationsrate = 0
        self._ssltottlsv11clientauthentications = 0
        self._ssltlsv11clientauthenticationsrate = 0
        self._ssltottlsv12clientauthentications = 0
        self._ssltlsv12clientauthenticationsrate = 0
        self._ssltotrsaauthorizations = 0
        self._sslrsaauthorizationsrate = 0
        self._ssltotdhauthorizations = 0
        self._ssldhauthorizationsrate = 0
        self._ssltotdssauthorizations = 0
        self._ssldssauthorizationsrate = 0
        self._ssltotnullauthorizations = 0
        self._sslnullauthorizationsrate = 0
        self._ssltotbkendsessionrenegotiate = 0
        self._sslbkendsessionrenegotiaterate = 0
        self._ssltotbkendsslv3renego = 0
        self._sslbkendsslv3renegorate = 0
        self._ssltotbkendtlsvlrenego = 0
        self._sslbkendtlsvlrenegorate = 0
        self._ssltotbkendtlsv11renego = 0
        self._sslbkendtlsv11renegorate = 0
        self._ssltotbkendtlsv12renego = 0
        self._sslbkendtlsv12renegorate = 0
        self._sslbetotrsa512keyexchanges = 0
        self._sslbersa512keyexchangesrate = 0
        self._sslbetotrsa1024keyexchanges = 0
        self._sslbersa1024keyexchangesrate = 0
        self._sslbetotrsa2048keyexchanges = 0
        self._sslbersa2048keyexchangesrate = 0
        self._sslbetotdh512keyexchanges = 0
        self._sslbedh512keyexchangesrate = 0
        self._sslbetotdh1024keyexchanges = 0
        self._sslbedh1024keyexchangesrate = 0
        self._sslbetotdh2048keyexchanges = 0
        self._sslbedh2048keyexchangesrate = 0
        self._sslbetotecdhecurve521 = 0
        self._sslbeecdhecurve521rate = 0
        self._sslbetotecdhecurve384 = 0
        self._sslbeecdhecurve384rate = 0
        self._sslbetotecdhecurve256 = 0
        self._sslbeecdhecurve256rate = 0
        self._sslbetotecdhecurve224 = 0
        self._sslbeecdhecurve224rate = 0
        self._sslbetot40bitrc4ciphers = 0
        self._sslbe40bitrc4ciphersrate = 0
        self._sslbetot56bitrc4ciphers = 0
        self._sslbe56bitrc4ciphersrate = 0
        self._sslbetot64bitrc4ciphers = 0
        self._sslbe64bitrc4ciphersrate = 0
        self._sslbetot128bitrc4ciphers = 0
        self._sslbe128bitrc4ciphersrate = 0
        self._sslbetot40bitdesciphers = 0
        self._sslbe40bitdesciphersrate = 0
        self._sslbetot56bitdesciphers = 0
        self._sslbe56bitdesciphersrate = 0
        self._sslbetot168bit3desciphers = 0
        self._sslbe168bit3desciphersrate = 0
        self._ssltotbkendcipheraes128 = 0
        self._sslbkendcipheraes128rate = 0
        self._ssltotbkendcipheraes256 = 0
        self._sslbkendcipheraes256rate = 0
        self._sslbetot40bitrc2ciphers = 0
        self._sslbe40bitrc2ciphersrate = 0
        self._sslbetot56bitrc2ciphers = 0
        self._sslbe56bitrc2ciphersrate = 0
        self._sslbetot128bitrc2ciphers = 0
        self._sslbe128bitrc2ciphersrate = 0
        self._sslbetotnullciphers = 0
        self._sslbenullciphersrate = 0
        self._sslbetotmd5mac = 0
        self._sslbemd5macrate = 0
        self._sslbetotshamac = 0
        self._sslbeshamacrate = 0
        self._sslbetotsslv3handshakes = 0
        self._sslbesslv3handshakesrate = 0
        self._sslbetottlsv1handshakes = 0
        self._sslbetlsv1handshakesrate = 0
        self._sslbetotsslv3clientauthentications = 0
        self._sslbesslv3clientauthenticationsrate = 0
        self._sslbetottlsv1clientauthentications = 0
        self._sslbetlsv1clientauthenticationsrate = 0
        self._sslbetotrsaauthorizations = 0
        self._sslbersaauthorizationsrate = 0
        self._sslbetotdhauthorizations = 0
        self._sslbedhauthorizationsrate = 0
        self._sslbetotdssauthorizations = 0
        self._sslbedssauthorizationsrate = 0
        self._sslbetotnullauthorizations = 0
        self._sslbenullauthorizationsrate = 0
        self._ssltotoffloadrsakeyexchanges = 0
        self._ssloffloadrsakeyexchangesrate = 0
        self._ssltotoffloadsignrsa = 0
        self._ssloffloadsignrsarate = 0
        self._ssltotoffloaddhkeyexchanges = 0
        self._ssloffloaddhkeyexchangesrate = 0
        self._ssltotoffloadbulkrc4 = 0
        self._ssloffloadbulkrc4rate = 0
        self._ssltotoffloadbulkdes = 0
        self._ssloffloadbulkdesrate = 0
        self._ssltotoffloadbulkaes = 0
        self._ssloffloadbulkaesrate = 0
        self._ssltotoffloadbulkaesgcm128 = 0
        self._ssloffloadbulkaesgcm128rate = 0
        self._ssltotoffloadbulkaesgcm256 = 0
        self._ssloffloadbulkaesgcm256rate = 0
        self._ssltotenchw = 0
        self._sslenchwrate = 0
        self._ssltotencsw = 0
        self._sslencswrate = 0
        self._ssltotencfe = 0
        self._sslencferate = 0
        self._ssltothwencfe = 0
        self._sslhwencferate = 0
        self._ssltotswencfe = 0
        self._sslswencferate = 0
        self._ssltotencbe = 0
        self._sslencberate = 0
        self._ssltothwencbe = 0
        self._sslhwencberate = 0
        self._ssltotswencbe = 0
        self._sslswencberate = 0
        self._ssltotdechw = 0
        self._ssldechwrate = 0
        self._ssltotdecsw = 0
        self._ssldecswrate = 0
        self._ssltotdecfe = 0
        self._ssldecferate = 0
        self._ssltothwdecfe = 0
        self._sslhwdecferate = 0
        self._ssltotswdecfe = 0
        self._sslswdecferate = 0
        self._ssltotdecbe = 0
        self._ssldecberate = 0
        self._ssltothwdecbe = 0
        self._sslhwdecberate = 0
        self._ssltotswdecbe = 0
        self._sslswdecberate = 0
        self._sslbemaxmultiplexedsessions = 0
        self._sslbemaxmultiplexedsessionsrate = 0
        self._ssltot128bitideaciphers = 0
        self._ssl128bitideaciphersrate = 0
        self._sslbetot128bitideaciphers = 0
        self._sslbe128bitideaciphersrate = 0

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
    def ssltlsv11handshakesrate(self) :
        """Rate (/s) counter for ssltottlsv11handshakes."""
        try :
            return self._ssltlsv11handshakesrate
        except Exception as e:
            raise e

    @property
    def ssldh512keyexchangesrate(self) :
        """Rate (/s) counter for ssltotdh512keyexchanges."""
        try :
            return self._ssldh512keyexchangesrate
        except Exception as e:
            raise e

    @property
    def sslbetottlsv1handshakes(self) :
        """Number of back-end TLSv1 handshakes on the NetScaler appliance."""
        try :
            return self._sslbetottlsv1handshakes
        except Exception as e:
            raise e

    @property
    def sslswdecberate(self) :
        """Rate (/s) counter for ssltotswdecbe."""
        try :
            return self._sslswdecberate
        except Exception as e:
            raise e

    @property
    def ssltottransactions(self) :
        """Number of SSL transactions on the NetScaler appliance."""
        try :
            return self._ssltottransactions
        except Exception as e:
            raise e

    @property
    def sslbetot40bitrc4ciphers(self) :
        """Number of back-end RC4 40-bit cipher encryptions on the NetScaler appliance."""
        try :
            return self._sslbetot40bitrc4ciphers
        except Exception as e:
            raise e

    @property
    def sslnumcardsup(self) :
        """Number of SSL cards that are UP. If the number of cards UP is lower than a threshold, a failover is initiated."""
        try :
            return self._sslnumcardsup
        except Exception as e:
            raise e

    @property
    def sslbetlsv1clientauthenticationsrate(self) :
        """Rate (/s) counter for sslbetottlsv1clientauthentications."""
        try :
            return self._sslbetlsv1clientauthenticationsrate
        except Exception as e:
            raise e

    @property
    def sslrenegsessionsrate(self) :
        """Rate (/s) counter for ssltotrenegsessions."""
        try :
            return self._sslrenegsessionsrate
        except Exception as e:
            raise e

    @property
    def ssltottlsv11handshakes(self) :
        """Number of SSL handshakes on TLSv1.1 on the NetScaler appliance."""
        try :
            return self._ssltottlsv11handshakes
        except Exception as e:
            raise e

    @property
    def sslbetotsessions(self) :
        """Number of back-end SSL sessions on the NetScaler appliance."""
        try :
            return self._sslbetotsessions
        except Exception as e:
            raise e

    @property
    def sslbetot64bitrc4ciphers(self) :
        """Number of back-end RC4 64-bit cipher encryptions on the NetScaler appliance."""
        try :
            return self._sslbetot64bitrc4ciphers
        except Exception as e:
            raise e

    @property
    def sslbersa2048keyexchangesrate(self) :
        """Rate (/s) counter for sslbetotrsa2048keyexchanges."""
        try :
            return self._sslbersa2048keyexchangesrate
        except Exception as e:
            raise e

    @property
    def sslbetottlsv1clientauthentications(self) :
        """Number of back-end TLSv1 client authentications on the NetScaler appliance."""
        try :
            return self._sslbetottlsv1clientauthentications
        except Exception as e:
            raise e

    @property
    def ssltothwencbe(self) :
        """Number of bytes encrypted in hardware on the back end."""
        try :
            return self._ssltothwencbe
        except Exception as e:
            raise e

    @property
    def sslbetotdh512keyexchanges(self) :
        """Number of back-end DH 512-bit key exchanges on the NetScaler appliance."""
        try :
            return self._sslbetotdh512keyexchanges
        except Exception as e:
            raise e

    @property
    def ssltotrsaauthorizations(self) :
        """Number of RSA authentications on the NetScaler appliance."""
        try :
            return self._ssltotrsaauthorizations
        except Exception as e:
            raise e

    @property
    def sslecdhe384keyexchangesrate(self) :
        """Rate (/s) counter for ssltotecdhe384keyexchanges."""
        try :
            return self._sslecdhe384keyexchangesrate
        except Exception as e:
            raise e

    @property
    def sslcipheraes128rate(self) :
        """Rate (/s) counter for ssltotcipheraes128."""
        try :
            return self._sslcipheraes128rate
        except Exception as e:
            raise e

    @property
    def ssltotsslv2sessions(self) :
        """Number of SSLv2 sessions on the NetScaler appliance."""
        try :
            return self._ssltotsslv2sessions
        except Exception as e:
            raise e

    @property
    def ssltothwdecfe(self) :
        """Number of bytes decrypted in hardware on the front end."""
        try :
            return self._ssltothwdecfe
        except Exception as e:
            raise e

    @property
    def ssloffloadbulkrc4rate(self) :
        """Rate (/s) counter for ssltotoffloadbulkrc4."""
        try :
            return self._ssloffloadbulkrc4rate
        except Exception as e:
            raise e

    @property
    def ssltotbkendtlsv11renego(self) :
        """Number of back-end TLSv1.1 session renegotiations on the NetScaler appliance."""
        try :
            return self._ssltotbkendtlsv11renego
        except Exception as e:
            raise e

    @property
    def sslbe128bitrc4ciphersrate(self) :
        """Rate (/s) counter for sslbetot128bitrc4ciphers."""
        try :
            return self._sslbe128bitrc4ciphersrate
        except Exception as e:
            raise e

    @property
    def ssltotdecsw(self) :
        """Number of bytes decrypted in software."""
        try :
            return self._ssltotdecsw
        except Exception as e:
            raise e

    @property
    def ssl128bitrc2ciphersrate(self) :
        """Rate (/s) counter for ssltot128bitrc2ciphers."""
        try :
            return self._ssl128bitrc2ciphersrate
        except Exception as e:
            raise e

    @property
    def ssloffloadbulkaesrate(self) :
        """Rate (/s) counter for ssltotoffloadbulkaes."""
        try :
            return self._ssloffloadbulkaesrate
        except Exception as e:
            raise e

    @property
    def sslrsa512keyexchangesrate(self) :
        """Rate (/s) counter for ssltotrsa512keyexchanges."""
        try :
            return self._sslrsa512keyexchangesrate
        except Exception as e:
            raise e

    @property
    def sslbe56bitrc2ciphersrate(self) :
        """Rate (/s) counter for sslbetot56bitrc2ciphers."""
        try :
            return self._sslbe56bitrc2ciphersrate
        except Exception as e:
            raise e

    @property
    def ssltotrsa4096keyexchanges(self) :
        """Number of RSA 4096-bit key exchanges on the NetScaler appliance."""
        try :
            return self._ssltotrsa4096keyexchanges
        except Exception as e:
            raise e

    @property
    def sslbetotsslv3clientauthentications(self) :
        """Number of back-end SSLv3 client authentications on the NetScaler appliance."""
        try :
            return self._sslbetotsslv3clientauthentications
        except Exception as e:
            raise e

    @property
    def sslbeecdhecurve256rate(self) :
        """Rate (/s) counter for sslbetotecdhecurve256."""
        try :
            return self._sslbeecdhecurve256rate
        except Exception as e:
            raise e

    @property
    def ssltotsslv2clientauthentications(self) :
        """Number of client authentications done on SSLv2."""
        try :
            return self._ssltotsslv2clientauthentications
        except Exception as e:
            raise e

    @property
    def sslbetlsv11sessionsrate(self) :
        """Rate (/s) counter for sslbetottlsv11sessions."""
        try :
            return self._sslbetlsv11sessionsrate
        except Exception as e:
            raise e

    @property
    def sslbkendtlsv11renegorate(self) :
        """Rate (/s) counter for ssltotbkendtlsv11renego."""
        try :
            return self._sslbkendtlsv11renegorate
        except Exception as e:
            raise e

    @property
    def ssldh1024keyexchangesrate(self) :
        """Rate (/s) counter for ssltotdh1024keyexchanges."""
        try :
            return self._ssldh1024keyexchangesrate
        except Exception as e:
            raise e

    @property
    def ssltotmd5mac(self) :
        """Number of MD5 hashes on the NetScaler appliance."""
        try :
            return self._ssltotmd5mac
        except Exception as e:
            raise e

    @property
    def sslbetotnullauthorizations(self) :
        """Number of back-end null authentications on the NetScaler appliance."""
        try :
            return self._sslbetotnullauthorizations
        except Exception as e:
            raise e

    @property
    def sslbesessionmultiplexattemptsrate(self) :
        """Rate (/s) counter for sslbetotsessionmultiplexattempts."""
        try :
            return self._sslbesessionmultiplexattemptsrate
        except Exception as e:
            raise e

    @property
    def sslsslv2handshakesrate(self) :
        """Rate (/s) counter for ssltotsslv2handshakes."""
        try :
            return self._sslsslv2handshakesrate
        except Exception as e:
            raise e

    @property
    def ssldssauthorizationsrate(self) :
        """Rate (/s) counter for ssltotdssauthorizations."""
        try :
            return self._ssldssauthorizationsrate
        except Exception as e:
            raise e

    @property
    def sslbemaxmultiplexedsessionsrate(self) :
        """Rate (/s) counter for sslbemaxmultiplexedsessions."""
        try :
            return self._sslbemaxmultiplexedsessionsrate
        except Exception as e:
            raise e

    @property
    def sslbkendsessionrenegotiaterate(self) :
        """Rate (/s) counter for ssltotbkendsessionrenegotiate."""
        try :
            return self._sslbkendsessionrenegotiaterate
        except Exception as e:
            raise e

    @property
    def sslbetotrsa512keyexchanges(self) :
        """Number of back-end RSA 512-bit key exchanges on the NetScaler appliance."""
        try :
            return self._sslbetotrsa512keyexchanges
        except Exception as e:
            raise e

    @property
    def ssltlsv1renegsessionsrate(self) :
        """Rate (/s) counter for ssltottlsv1renegsessions."""
        try :
            return self._ssltlsv1renegsessionsrate
        except Exception as e:
            raise e

    @property
    def ssltot168bit3desciphers(self) :
        """Number of DES 168-bit cipher encryptions on the NetScaler appliance."""
        try :
            return self._ssltot168bit3desciphers
        except Exception as e:
            raise e

    @property
    def ssltottlsv1handshakes(self) :
        """Number of SSL handshakes on TLSv1 on the NetScaler appliance."""
        try :
            return self._ssltottlsv1handshakes
        except Exception as e:
            raise e

    @property
    def sslbetot56bitdesciphers(self) :
        """Number of back-end DES 56-bit cipher encryptions on the NetScaler appliance."""
        try :
            return self._sslbetot56bitdesciphers
        except Exception as e:
            raise e

    @property
    def sslbe128bitrc2ciphersrate(self) :
        """Rate (/s) counter for sslbetot128bitrc2ciphers."""
        try :
            return self._sslbe128bitrc2ciphersrate
        except Exception as e:
            raise e

    @property
    def ssltottlsv12handshakes(self) :
        """Number of SSL handshakes on TLSv1.2 on the NetScaler appliance."""
        try :
            return self._ssltottlsv12handshakes
        except Exception as e:
            raise e

    @property
    def sslrsa2048keyexchangesrate(self) :
        """Rate (/s) counter for ssltotrsa2048keyexchanges."""
        try :
            return self._sslrsa2048keyexchangesrate
        except Exception as e:
            raise e

    @property
    def ssltotsessionhits(self) :
        """Number of SSL session reuse hits on the NetScaler appliance."""
        try :
            return self._ssltotsessionhits
        except Exception as e:
            raise e

    @property
    def ssl40bitdesciphersrate(self) :
        """Rate (/s) counter for ssltot40bitdesciphers."""
        try :
            return self._ssl40bitdesciphersrate
        except Exception as e:
            raise e

    @property
    def ssltotencfe(self) :
        """Number of bytes encrypted on the front end."""
        try :
            return self._ssltotencfe
        except Exception as e:
            raise e

    @property
    def ssl40bitrc4ciphersrate(self) :
        """Rate (/s) counter for ssltot40bitrc4ciphers."""
        try :
            return self._ssl40bitrc4ciphersrate
        except Exception as e:
            raise e

    @property
    def sslbe56bitrc4ciphersrate(self) :
        """Rate (/s) counter for sslbetot56bitrc4ciphers."""
        try :
            return self._sslbe56bitrc4ciphersrate
        except Exception as e:
            raise e

    @property
    def ssltottlsv11renegsessions(self) :
        """Number of SSL session renegotiations done on TLSv1.1."""
        try :
            return self._ssltottlsv11renegsessions
        except Exception as e:
            raise e

    @property
    def ssldecferate(self) :
        """Rate (/s) counter for ssltotdecfe."""
        try :
            return self._ssldecferate
        except Exception as e:
            raise e

    @property
    def ssltottlsv12sessions(self) :
        """Number of TLSv1.2 sessions on the NetScaler appliance."""
        try :
            return self._ssltottlsv12sessions
        except Exception as e:
            raise e

    @property
    def ssltotrsa2048keyexchanges(self) :
        """Number of RSA 2048-bit key exchanges on the NetScaler appliance."""
        try :
            return self._ssltotrsa2048keyexchanges
        except Exception as e:
            raise e

    @property
    def sslbetotsessionmultiplexattemptfails(self) :
        """Number of back-end SSL session multiplex failures on the NetScaler appliance."""
        try :
            return self._sslbetotsessionmultiplexattemptfails
        except Exception as e:
            raise e

    @property
    def ssltotoffloadbulkdes(self) :
        """Number of DES encryptions offloaded to the cryptography card."""
        try :
            return self._ssltotoffloadbulkdes
        except Exception as e:
            raise e

    @property
    def ssltotnullciphers(self) :
        """Number of Null cipher encryptions on the NetScaler appliance."""
        try :
            return self._ssltotnullciphers
        except Exception as e:
            raise e

    @property
    def ssltlsv12sessionsrate(self) :
        """Rate (/s) counter for ssltottlsv12sessions."""
        try :
            return self._ssltlsv12sessionsrate
        except Exception as e:
            raise e

    @property
    def ssltothwdecbe(self) :
        """Number of bytes decrypted in hardware on the back end."""
        try :
            return self._ssltothwdecbe
        except Exception as e:
            raise e

    @property
    def ssltotoffloadsignrsa(self) :
        """Number of RSA sign operations offloaded to the cryptography card."""
        try :
            return self._ssltotoffloadsignrsa
        except Exception as e:
            raise e

    @property
    def sslswencferate(self) :
        """Rate (/s) counter for ssltotswencfe."""
        try :
            return self._sslswencferate
        except Exception as e:
            raise e

    @property
    def sslbeecdhecurve224rate(self) :
        """Rate (/s) counter for sslbetotecdhecurve224."""
        try :
            return self._sslbeecdhecurve224rate
        except Exception as e:
            raise e

    @property
    def sslbetotshamac(self) :
        """Number of back-end SHA hashes on the NetScaler appliance."""
        try :
            return self._sslbetotshamac
        except Exception as e:
            raise e

    @property
    def ssltotcipheraes128(self) :
        """Number of AES 128-bit cipher encryptions on the NetScaler appliance."""
        try :
            return self._ssltotcipheraes128
        except Exception as e:
            raise e

    @property
    def ssltotbkendsslv3renego(self) :
        """Number of back-end SSLv3 session renegotiations on the NetScaler appliance."""
        try :
            return self._ssltotbkendsslv3renego
        except Exception as e:
            raise e

    @property
    def ssltot128bitrc4ciphers(self) :
        """Number of RC4 128-bit cipher encryptions on the NetScaler appliance."""
        try :
            return self._ssltot128bitrc4ciphers
        except Exception as e:
            raise e

    @property
    def sslbetotdssauthorizations(self) :
        """Number of back-end DSS authentications on the NetScaler appliance."""
        try :
            return self._sslbetotdssauthorizations
        except Exception as e:
            raise e

    @property
    def sslbetot56bitrc4ciphers(self) :
        """Number of back-end RC4 56-bit cipher encryptions on the NetScaler appliance."""
        try :
            return self._sslbetot56bitrc4ciphers
        except Exception as e:
            raise e

    @property
    def sslbetot40bitdesciphers(self) :
        """Number of back-end DES 40-bit cipher encryptions on the NetScaler appliance."""
        try :
            return self._sslbetot40bitdesciphers
        except Exception as e:
            raise e

    @property
    def ssltotsslv3renegsessions(self) :
        """Number of session renegotiations done on SSLv3."""
        try :
            return self._ssltotsslv3renegsessions
        except Exception as e:
            raise e

    @property
    def sslbersaauthorizationsrate(self) :
        """Rate (/s) counter for sslbetotrsaauthorizations."""
        try :
            return self._sslbersaauthorizationsrate
        except Exception as e:
            raise e

    @property
    def ssltot128bitaesgcmciphers(self) :
        """Number of AEC-GCM 128-bit cipher encryptions on the NetScaler appliance."""
        try :
            return self._ssltot128bitaesgcmciphers
        except Exception as e:
            raise e

    @property
    def ssltotsslv2transactions(self) :
        """Number of SSLv2 transactions on the NetScaler appliance."""
        try :
            return self._ssltotsslv2transactions
        except Exception as e:
            raise e

    @property
    def sslbedh1024keyexchangesrate(self) :
        """Rate (/s) counter for sslbetotdh1024keyexchanges."""
        try :
            return self._sslbedh1024keyexchangesrate
        except Exception as e:
            raise e

    @property
    def ssl64bitrc4ciphersrate(self) :
        """Rate (/s) counter for ssltot64bitrc4ciphers."""
        try :
            return self._ssl64bitrc4ciphersrate
        except Exception as e:
            raise e

    @property
    def sslsslv3clientauthenticationsrate(self) :
        """Rate (/s) counter for ssltotsslv3clientauthentications."""
        try :
            return self._sslsslv3clientauthenticationsrate
        except Exception as e:
            raise e

    @property
    def sslbetottlsv11sessions(self) :
        """Number of back-end TLSv1.1 sessions on the NetScaler appliance."""
        try :
            return self._sslbetottlsv11sessions
        except Exception as e:
            raise e

    @property
    def sslsessionmissrate(self) :
        """Rate (/s) counter for ssltotsessionmiss."""
        try :
            return self._sslsessionmissrate
        except Exception as e:
            raise e

    @property
    def sslbetotdhauthorizations(self) :
        """Number of back-end DH authentications on the NetScaler appliance."""
        try :
            return self._sslbetotdhauthorizations
        except Exception as e:
            raise e

    @property
    def sslbemd5macrate(self) :
        """Rate (/s) counter for sslbetotmd5mac."""
        try :
            return self._sslbemd5macrate
        except Exception as e:
            raise e

    @property
    def sslecdhe256keyexchangesrate(self) :
        """Rate (/s) counter for ssltotecdhe256keyexchanges."""
        try :
            return self._sslecdhe256keyexchangesrate
        except Exception as e:
            raise e

    @property
    def sslbetotmd5mac(self) :
        """Number of back-end MD5 hashes on the NetScaler appliance."""
        try :
            return self._sslbetotmd5mac
        except Exception as e:
            raise e

    @property
    def ssldhauthorizationsrate(self) :
        """Rate (/s) counter for ssltotdhauthorizations."""
        try :
            return self._ssldhauthorizationsrate
        except Exception as e:
            raise e

    @property
    def ssloffloadbulkaesgcm128rate(self) :
        """Rate (/s) counter for ssltotoffloadbulkaesgcm128."""
        try :
            return self._ssloffloadbulkaesgcm128rate
        except Exception as e:
            raise e

    @property
    def sslshamacrate(self) :
        """Rate (/s) counter for ssltotshamac."""
        try :
            return self._sslshamacrate
        except Exception as e:
            raise e

    @property
    def sslhwdecberate(self) :
        """Rate (/s) counter for ssltothwdecbe."""
        try :
            return self._sslhwdecberate
        except Exception as e:
            raise e

    @property
    def sslnullauthorizationsrate(self) :
        """Rate (/s) counter for ssltotnullauthorizations."""
        try :
            return self._sslnullauthorizationsrate
        except Exception as e:
            raise e

    @property
    def sslbetot128bitrc2ciphers(self) :
        """Number of back-end RC2 128-bit cipher encryptions on the NetScaler appliance."""
        try :
            return self._sslbetot128bitrc2ciphers
        except Exception as e:
            raise e

    @property
    def sslsslv3sessionsrate(self) :
        """Rate (/s) counter for ssltotsslv3sessions."""
        try :
            return self._sslsslv3sessionsrate
        except Exception as e:
            raise e

    @property
    def ssltotdh1024keyexchanges(self) :
        """Number of Diffie-Helman 1024-bit key exchanges on the NetScaler appliance."""
        try :
            return self._ssltotdh1024keyexchanges
        except Exception as e:
            raise e

    @property
    def ssltotbkendsessionrenegotiate(self) :
        """Number of back-end SSL session renegotiations on the NetScaler appliance."""
        try :
            return self._ssltotbkendsessionrenegotiate
        except Exception as e:
            raise e

    @property
    def sslbkendtlsv12renegorate(self) :
        """Rate (/s) counter for ssltotbkendtlsv12renego."""
        try :
            return self._sslbkendtlsv12renegorate
        except Exception as e:
            raise e

    @property
    def sslsessionhitsrate(self) :
        """Rate (/s) counter for ssltotsessionhits."""
        try :
            return self._sslsessionhitsrate
        except Exception as e:
            raise e

    @property
    def sslsslv3renegsessionsrate(self) :
        """Rate (/s) counter for ssltotsslv3renegsessions."""
        try :
            return self._sslsslv3renegsessionsrate
        except Exception as e:
            raise e

    @property
    def ssldechwrate(self) :
        """Rate (/s) counter for ssltotdechw."""
        try :
            return self._ssldechwrate
        except Exception as e:
            raise e

    @property
    def ssltotsslv3clientauthentications(self) :
        """Number of client authentications done on SSLv3."""
        try :
            return self._ssltotsslv3clientauthentications
        except Exception as e:
            raise e

    @property
    def ssldecrate(self) :
        """Rate (/s) counter for ssltotdec."""
        try :
            return self._ssldecrate
        except Exception as e:
            raise e

    @property
    def ssltlsv11clientauthenticationsrate(self) :
        """Rate (/s) counter for ssltottlsv11clientauthentications."""
        try :
            return self._ssltlsv11clientauthenticationsrate
        except Exception as e:
            raise e

    @property
    def ssldh2048keyexchangesrate(self) :
        """Rate (/s) counter for ssltotdh2048keyexchanges."""
        try :
            return self._ssldh2048keyexchangesrate
        except Exception as e:
            raise e

    @property
    def sslbesslv3sessionsrate(self) :
        """Rate (/s) counter for sslbetotsslv3sessions."""
        try :
            return self._sslbesslv3sessionsrate
        except Exception as e:
            raise e

    @property
    def ssltotoffloadbulkaesgcm256(self) :
        """Number of AES-GCM 256-bit encryptions offloaded to the cryptography card."""
        try :
            return self._ssltotoffloadbulkaesgcm256
        except Exception as e:
            raise e

    @property
    def ssl40bitrc2ciphersrate(self) :
        """Rate (/s) counter for ssltot40bitrc2ciphers."""
        try :
            return self._ssl40bitrc2ciphersrate
        except Exception as e:
            raise e

    @property
    def sslbe40bitdesciphersrate(self) :
        """Rate (/s) counter for sslbetot40bitdesciphers."""
        try :
            return self._sslbe40bitdesciphersrate
        except Exception as e:
            raise e

    @property
    def sslbetotsessionmultiplexattemptsuccess(self) :
        """Number of back-end SSL session multiplex successes on the NetScaler appliance."""
        try :
            return self._sslbetotsessionmultiplexattemptsuccess
        except Exception as e:
            raise e

    @property
    def ssloffloadrsakeyexchangesrate(self) :
        """Rate (/s) counter for ssltotoffloadrsakeyexchanges."""
        try :
            return self._ssloffloadrsakeyexchangesrate
        except Exception as e:
            raise e

    @property
    def sslbetotdh2048keyexchanges(self) :
        """Number of back-end DH 2048-bit key exchanges on the NetScaler appliance."""
        try :
            return self._sslbetotdh2048keyexchanges
        except Exception as e:
            raise e

    @property
    def sslbesessionmultiplexattemptsuccessrate(self) :
        """Rate (/s) counter for sslbetotsessionmultiplexattemptsuccess."""
        try :
            return self._sslbesessionmultiplexattemptsuccessrate
        except Exception as e:
            raise e

    @property
    def sslbe40bitrc4ciphersrate(self) :
        """Rate (/s) counter for sslbetot40bitrc4ciphers."""
        try :
            return self._sslbe40bitrc4ciphersrate
        except Exception as e:
            raise e

    @property
    def ssltotoffloadbulkaes(self) :
        """Number of AES encryptions offloaded to the cryptography card."""
        try :
            return self._ssltotoffloadbulkaes
        except Exception as e:
            raise e

    @property
    def sslbetot168bit3desciphers(self) :
        """Number of back-end 3DES 168-bit cipher encryptions on the NetScaler appliance."""
        try :
            return self._sslbetot168bit3desciphers
        except Exception as e:
            raise e

    @property
    def ssltottlsv12renegsessions(self) :
        """Number of SSL session renegotiations done on TLSv1.2."""
        try :
            return self._ssltottlsv12renegsessions
        except Exception as e:
            raise e

    @property
    def ssltotrenegsessions(self) :
        """Number of SSL session renegotiations on the NetScaler appliance."""
        try :
            return self._ssltotrenegsessions
        except Exception as e:
            raise e

    @property
    def sslbkendsslv3renegorate(self) :
        """Rate (/s) counter for ssltotbkendsslv3renego."""
        try :
            return self._sslbkendsslv3renegorate
        except Exception as e:
            raise e

    @property
    def sslsslv3transactionsrate(self) :
        """Rate (/s) counter for ssltotsslv3transactions."""
        try :
            return self._sslsslv3transactionsrate
        except Exception as e:
            raise e

    @property
    def sslecdhe521keyexchangesrate(self) :
        """Rate (/s) counter for ssltotecdhe521keyexchanges."""
        try :
            return self._sslecdhe521keyexchangesrate
        except Exception as e:
            raise e

    @property
    def ssltottlsv11clientauthentications(self) :
        """Number of client authentications done on TLSv1.1."""
        try :
            return self._ssltottlsv11clientauthentications
        except Exception as e:
            raise e

    @property
    def sslsslv2clientauthenticationsrate(self) :
        """Rate (/s) counter for ssltotsslv2clientauthentications."""
        try :
            return self._sslsslv2clientauthenticationsrate
        except Exception as e:
            raise e

    @property
    def sslbetotrsa2048keyexchanges(self) :
        """Number of back-end RSA 2048-bit key exchanges on the NetScaler appliance."""
        try :
            return self._sslbetotrsa2048keyexchanges
        except Exception as e:
            raise e

    @property
    def sslrsaauthorizationsrate(self) :
        """Rate (/s) counter for ssltotrsaauthorizations."""
        try :
            return self._sslrsaauthorizationsrate
        except Exception as e:
            raise e

    @property
    def ssltot40bitrc2ciphers(self) :
        """Number of RC2 40-bit cipher encryptions on the NetScaler appliance."""
        try :
            return self._ssltot40bitrc2ciphers
        except Exception as e:
            raise e

    @property
    def ssltot56bitrc2ciphers(self) :
        """Number of RC2 56-bit cipher encryptions on the NetScaler appliance."""
        try :
            return self._ssltot56bitrc2ciphers
        except Exception as e:
            raise e

    @property
    def ssl128bitrc4ciphersrate(self) :
        """Rate (/s) counter for ssltot128bitrc4ciphers."""
        try :
            return self._ssl128bitrc4ciphersrate
        except Exception as e:
            raise e

    @property
    def ssltothwencfe(self) :
        """Number of bytes encrypted in hardware on the front end."""
        try :
            return self._ssltothwencfe
        except Exception as e:
            raise e

    @property
    def ssltot40bitdesciphers(self) :
        """Number of DES 40-bit cipher encryptions on the NetScaler appliance."""
        try :
            return self._ssltot40bitdesciphers
        except Exception as e:
            raise e

    @property
    def sslbeshamacrate(self) :
        """Rate (/s) counter for sslbetotshamac."""
        try :
            return self._sslbeshamacrate
        except Exception as e:
            raise e

    @property
    def sslbkendcipheraes128rate(self) :
        """Rate (/s) counter for ssltotbkendcipheraes128."""
        try :
            return self._sslbkendcipheraes128rate
        except Exception as e:
            raise e

    @property
    def ssltottlsv1transactions(self) :
        """Number of TLSv1 transactions on the NetScaler appliance."""
        try :
            return self._ssltottlsv1transactions
        except Exception as e:
            raise e

    @property
    def ssltotrsa512keyexchanges(self) :
        """Number of RSA 512-bit key exchanges on the NetScaler appliance."""
        try :
            return self._ssltotrsa512keyexchanges
        except Exception as e:
            raise e

    @property
    def ssltlsv12renegsessionsrate(self) :
        """Rate (/s) counter for ssltottlsv12renegsessions."""
        try :
            return self._ssltlsv12renegsessionsrate
        except Exception as e:
            raise e

    @property
    def sslbetotecdhecurve224(self) :
        """Number of back-end ECDHE 224 curve Key exchanges  on the NetScaler appliance."""
        try :
            return self._sslbetotecdhecurve224
        except Exception as e:
            raise e

    @property
    def sslbetotnullciphers(self) :
        """Number of back-end null cipher encryptions on the NetScaler appliance."""
        try :
            return self._sslbetotnullciphers
        except Exception as e:
            raise e

    @property
    def sslencrate(self) :
        """Rate (/s) counter for ssltotenc."""
        try :
            return self._sslencrate
        except Exception as e:
            raise e

    @property
    def ssltotencsw(self) :
        """Number of bytes encrypted in software."""
        try :
            return self._ssltotencsw
        except Exception as e:
            raise e

    @property
    def ssltottlsv1renegsessions(self) :
        """Number of SSL session renegotiations done on TLSv1."""
        try :
            return self._ssltottlsv1renegsessions
        except Exception as e:
            raise e

    @property
    def ssltotbkendcipheraes128(self) :
        """Back-end AES 128-bit cipher encryptions on the NetScaler appliance."""
        try :
            return self._ssltotbkendcipheraes128
        except Exception as e:
            raise e

    @property
    def ssltlsv11transactionsrate(self) :
        """Rate (/s) counter for ssltottlsv11transactions."""
        try :
            return self._ssltlsv11transactionsrate
        except Exception as e:
            raise e

    @property
    def ssltlsv12clientauthenticationsrate(self) :
        """Rate (/s) counter for ssltottlsv12clientauthentications."""
        try :
            return self._ssltlsv12clientauthenticationsrate
        except Exception as e:
            raise e

    @property
    def ssltotcipheraes256(self) :
        """Number of AES 256-bit cipher encryptions on the NetScaler appliance."""
        try :
            return self._ssltotcipheraes256
        except Exception as e:
            raise e

    @property
    def ssltotsslv3transactions(self) :
        """Total number of SSLv3 transactions on the NetScaler appliance."""
        try :
            return self._ssltotsslv3transactions
        except Exception as e:
            raise e

    @property
    def ssltotdecbe(self) :
        """Number of bytes decrypted on the back end."""
        try :
            return self._ssltotdecbe
        except Exception as e:
            raise e

    @property
    def ssloffloadbulkdesrate(self) :
        """Rate (/s) counter for ssltotoffloadbulkdes."""
        try :
            return self._ssloffloadbulkdesrate
        except Exception as e:
            raise e

    @property
    def ssltotbkendtlsv12renego(self) :
        """Number of back-end TLSv1.2 session renegotiations on the NetScaler appliance."""
        try :
            return self._ssltotbkendtlsv12renego
        except Exception as e:
            raise e

    @property
    def sslbesessionsrate(self) :
        """Rate (/s) counter for sslbetotsessions."""
        try :
            return self._sslbesessionsrate
        except Exception as e:
            raise e

    @property
    def ssltot128bitideaciphers(self) :
        """Number of IDEA 128-bit cipher encryptions on the NetScaler appliance."""
        try :
            return self._ssltot128bitideaciphers
        except Exception as e:
            raise e

    @property
    def ssltotdec(self) :
        """Number of bytes decrypted on the NetScaler appliance."""
        try :
            return self._ssltotdec
        except Exception as e:
            raise e

    @property
    def ssl56bitdesciphersrate(self) :
        """Rate (/s) counter for ssltot56bitdesciphers."""
        try :
            return self._ssl56bitdesciphersrate
        except Exception as e:
            raise e

    @property
    def sslbetot56bitrc2ciphers(self) :
        """Number of back-end RC2 56-bit cipher encryptions on the NetScaler appliance."""
        try :
            return self._sslbetot56bitrc2ciphers
        except Exception as e:
            raise e

    @property
    def sslbkendcipheraes256rate(self) :
        """Rate (/s) counter for ssltotbkendcipheraes256."""
        try :
            return self._sslbkendcipheraes256rate
        except Exception as e:
            raise e

    @property
    def sslbetotrsaauthorizations(self) :
        """Number of back-end RSA authentications on the NetScaler appliance."""
        try :
            return self._sslbetotrsaauthorizations
        except Exception as e:
            raise e

    @property
    def sslbedh2048keyexchangesrate(self) :
        """Rate (/s) counter for sslbetotdh2048keyexchanges."""
        try :
            return self._sslbedh2048keyexchangesrate
        except Exception as e:
            raise e

    @property
    def sslbe168bit3desciphersrate(self) :
        """Rate (/s) counter for sslbetot168bit3desciphers."""
        try :
            return self._sslbe168bit3desciphersrate
        except Exception as e:
            raise e

    @property
    def sslsslv2transactionsrate(self) :
        """Rate (/s) counter for ssltotsslv2transactions."""
        try :
            return self._sslsslv2transactionsrate
        except Exception as e:
            raise e

    @property
    def sslrsa1024keyexchangesrate(self) :
        """Rate (/s) counter for ssltotrsa1024keyexchanges."""
        try :
            return self._sslrsa1024keyexchangesrate
        except Exception as e:
            raise e

    @property
    def sslbedh512keyexchangesrate(self) :
        """Rate (/s) counter for sslbetotdh512keyexchanges."""
        try :
            return self._sslbedh512keyexchangesrate
        except Exception as e:
            raise e

    @property
    def ssltottlsv1clientauthentications(self) :
        """Number of client authentications done on TLSv1."""
        try :
            return self._ssltottlsv1clientauthentications
        except Exception as e:
            raise e

    @property
    def sslbetot40bitrc2ciphers(self) :
        """Number of back-end RC2 40-bit cipher encryptions on the NetScaler appliance."""
        try :
            return self._sslbetot40bitrc2ciphers
        except Exception as e:
            raise e

    @property
    def ssl168bit3desciphersrate(self) :
        """Rate (/s) counter for ssltot168bit3desciphers."""
        try :
            return self._ssl168bit3desciphersrate
        except Exception as e:
            raise e

    @property
    def ssltot64bitrc4ciphers(self) :
        """Number of RC4 64-bit cipher encryptions on the NetScaler appliance."""
        try :
            return self._ssltot64bitrc4ciphers
        except Exception as e:
            raise e

    @property
    def ssltotswencfe(self) :
        """Number of bytes encrypted in software on the front end."""
        try :
            return self._ssltotswencfe
        except Exception as e:
            raise e

    @property
    def ssldecswrate(self) :
        """Rate (/s) counter for ssltotdecsw."""
        try :
            return self._ssldecswrate
        except Exception as e:
            raise e

    @property
    def ssltot256bitaesgcmciphers(self) :
        """Number of AEC-GCM 256-bit cipher encryptions on the NetScaler appliance."""
        try :
            return self._ssltot256bitaesgcmciphers
        except Exception as e:
            raise e

    @property
    def ssltotdhauthorizations(self) :
        """Number of Diffie-Helman authentications on the NetScaler appliance."""
        try :
            return self._ssltotdhauthorizations
        except Exception as e:
            raise e

    @property
    def ssltotsessionmiss(self) :
        """Number of SSL session reuse misses on the NetScaler appliance."""
        try :
            return self._ssltotsessionmiss
        except Exception as e:
            raise e

    @property
    def ssltotdecfe(self) :
        """Number of bytes decrypted on the front end."""
        try :
            return self._ssltotdecfe
        except Exception as e:
            raise e

    @property
    def sslbesslv3handshakesrate(self) :
        """Rate (/s) counter for sslbetotsslv3handshakes."""
        try :
            return self._sslbesslv3handshakesrate
        except Exception as e:
            raise e

    @property
    def sslbeecdhecurve521rate(self) :
        """Rate (/s) counter for sslbetotecdhecurve521."""
        try :
            return self._sslbeecdhecurve521rate
        except Exception as e:
            raise e

    @property
    def sslencswrate(self) :
        """Rate (/s) counter for ssltotencsw."""
        try :
            return self._sslencswrate
        except Exception as e:
            raise e

    @property
    def sslhwencferate(self) :
        """Rate (/s) counter for ssltothwencfe."""
        try :
            return self._sslhwencferate
        except Exception as e:
            raise e

    @property
    def sslbesessionmultiplexattemptfailsrate(self) :
        """Rate (/s) counter for sslbetotsessionmultiplexattemptfails."""
        try :
            return self._sslbesessionmultiplexattemptfailsrate
        except Exception as e:
            raise e

    @property
    def sslbe128bitideaciphersrate(self) :
        """Rate (/s) counter for sslbetot128bitideaciphers."""
        try :
            return self._sslbe128bitideaciphersrate
        except Exception as e:
            raise e

    @property
    def ssltotecdhe224keyexchanges(self) :
        """Number of 224 Elliptical Curve Diffie-Helman on the NetScaler appliance."""
        try :
            return self._ssltotecdhe224keyexchanges
        except Exception as e:
            raise e

    @property
    def ssltotoffloaddhkeyexchanges(self) :
        """Number of DH key exchanges offloaded to the cryptography card.d."""
        try :
            return self._ssltotoffloaddhkeyexchanges
        except Exception as e:
            raise e

    @property
    def ssltlsv1clientauthenticationsrate(self) :
        """Rate (/s) counter for ssltottlsv1clientauthentications."""
        try :
            return self._ssltlsv1clientauthenticationsrate
        except Exception as e:
            raise e

    @property
    def ssltot56bitrc4ciphers(self) :
        """Number of RC4 56-bit cipher encryptions on the NetScaler appliance."""
        try :
            return self._ssltot56bitrc4ciphers
        except Exception as e:
            raise e

    @property
    def sslbe40bitrc2ciphersrate(self) :
        """Rate (/s) counter for sslbetot40bitrc2ciphers."""
        try :
            return self._sslbe40bitrc2ciphersrate
        except Exception as e:
            raise e

    @property
    def sslenchwrate(self) :
        """Rate (/s) counter for ssltotenchw."""
        try :
            return self._sslenchwrate
        except Exception as e:
            raise e

    @property
    def sslbetlsv1handshakesrate(self) :
        """Rate (/s) counter for sslbetottlsv1handshakes."""
        try :
            return self._sslbetlsv1handshakesrate
        except Exception as e:
            raise e

    @property
    def ssltotsslv3handshakes(self) :
        """Number of handshakes on SSLv3 on the NetScaler appliance."""
        try :
            return self._ssltotsslv3handshakes
        except Exception as e:
            raise e

    @property
    def sslbenullciphersrate(self) :
        """Rate (/s) counter for sslbetotnullciphers."""
        try :
            return self._sslbenullciphersrate
        except Exception as e:
            raise e

    @property
    def sslsessionsrate(self) :
        """Rate (/s) counter for ssltotsessions."""
        try :
            return self._sslsessionsrate
        except Exception as e:
            raise e

    @property
    def ssltottlsv12transactions(self) :
        """Number of TLSv1.2 transactions on the NetScaler appliance."""
        try :
            return self._ssltottlsv12transactions
        except Exception as e:
            raise e

    @property
    def ssltottlsv11sessions(self) :
        """Number of TLSv1.1 sessions on the NetScaler appliance."""
        try :
            return self._ssltottlsv11sessions
        except Exception as e:
            raise e

    @property
    def ssl56bitrc4ciphersrate(self) :
        """Rate (/s) counter for ssltot56bitrc4ciphers."""
        try :
            return self._ssl56bitrc4ciphersrate
        except Exception as e:
            raise e

    @property
    def ssldecberate(self) :
        """Rate (/s) counter for ssltotdecbe."""
        try :
            return self._ssldecberate
        except Exception as e:
            raise e

    @property
    def sslbedssauthorizationsrate(self) :
        """Rate (/s) counter for sslbetotdssauthorizations."""
        try :
            return self._sslbedssauthorizationsrate
        except Exception as e:
            raise e

    @property
    def ssltot56bitdesciphers(self) :
        """Number of DES 56-bit cipher encryptions on the NetScaler appliance."""
        try :
            return self._ssltot56bitdesciphers
        except Exception as e:
            raise e

    @property
    def sslbkendtlsvlrenegorate(self) :
        """Rate (/s) counter for ssltotbkendtlsvlrenego."""
        try :
            return self._sslbkendtlsvlrenegorate
        except Exception as e:
            raise e

    @property
    def sslbenullauthorizationsrate(self) :
        """Rate (/s) counter for sslbetotnullauthorizations."""
        try :
            return self._sslbenullauthorizationsrate
        except Exception as e:
            raise e

    @property
    def ssltotenchw(self) :
        """Number of bytes encrypted in hardware."""
        try :
            return self._ssltotenchw
        except Exception as e:
            raise e

    @property
    def ssltlsv11sessionsrate(self) :
        """Rate (/s) counter for ssltottlsv11sessions."""
        try :
            return self._ssltlsv11sessionsrate
        except Exception as e:
            raise e

    @property
    def sslbetotecdhecurve256(self) :
        """Number of back-end ECDHE 256 curve Key exchanges  on the NetScaler appliance."""
        try :
            return self._sslbetotecdhecurve256
        except Exception as e:
            raise e

    @property
    def ssltotdh512keyexchanges(self) :
        """Number of Diffie-Helman 512-bit key exchanges on the NetScaler appliance."""
        try :
            return self._ssltotdh512keyexchanges
        except Exception as e:
            raise e

    @property
    def ssltlsv1sessionsrate(self) :
        """Rate (/s) counter for ssltottlsv1sessions."""
        try :
            return self._ssltlsv1sessionsrate
        except Exception as e:
            raise e

    @property
    def ssltotencbe(self) :
        """Number of bytes encrypted on the back end."""
        try :
            return self._ssltotencbe
        except Exception as e:
            raise e

    @property
    def sslcryptoutilizationstat(self) :
        """Utilization of the hardware crypto resource. Only valid values are 0-100%. Only works for platform with N3 chips."""
        try :
            return self._sslcryptoutilizationstat
        except Exception as e:
            raise e

    @property
    def ssltotecdhe384keyexchanges(self) :
        """Number of 384 Elliptical Curve Diffie-Helman on the NetScaler appliance."""
        try :
            return self._ssltotecdhe384keyexchanges
        except Exception as e:
            raise e

    @property
    def sslcipheraes256rate(self) :
        """Rate (/s) counter for ssltotcipheraes256."""
        try :
            return self._sslcipheraes256rate
        except Exception as e:
            raise e

    @property
    def ssltotsslv2handshakes(self) :
        """Number of handshakes on SSLv2 on the NetScaler appliance."""
        try :
            return self._ssltotsslv2handshakes
        except Exception as e:
            raise e

    @property
    def ssltotenc(self) :
        """Number of bytes encrypted on the NetScaler appliance."""
        try :
            return self._ssltotenc
        except Exception as e:
            raise e

    @property
    def sslbetotsslv3sessions(self) :
        """Number of back-end SSLv3 sessions on the NetScaler appliance."""
        try :
            return self._sslbetotsslv3sessions
        except Exception as e:
            raise e

    @property
    def sslencberate(self) :
        """Rate (/s) counter for ssltotencbe."""
        try :
            return self._sslencberate
        except Exception as e:
            raise e

    @property
    def ssltottlsv11transactions(self) :
        """Number of TLSv1.1 transactions on the NetScaler appliance."""
        try :
            return self._ssltottlsv11transactions
        except Exception as e:
            raise e

    @property
    def sslbemaxmultiplexedsessions(self) :
        """Number of back-end SSL sessions reused on the NetScaler appliance."""
        try :
            return self._sslbemaxmultiplexedsessions
        except Exception as e:
            raise e

    @property
    def ssl128bitaesgcmciphersrate(self) :
        """Rate (/s) counter for ssltot128bitaesgcmciphers."""
        try :
            return self._ssl128bitaesgcmciphersrate
        except Exception as e:
            raise e

    @property
    def sslbetotecdhecurve384(self) :
        """Number of back-end ECDHE 384 curve Key exchanges  on the NetScaler appliance."""
        try :
            return self._sslbetotecdhecurve384
        except Exception as e:
            raise e

    @property
    def ssltotsessions(self) :
        """Number of SSL sessions on the NetScaler appliance."""
        try :
            return self._ssltotsessions
        except Exception as e:
            raise e

    @property
    def ssltot40bitrc4ciphers(self) :
        """Number of RC4 40-bit cipher encryptions on the NetScaler appliance."""
        try :
            return self._ssltot40bitrc4ciphers
        except Exception as e:
            raise e

    @property
    def ssloffloadbulkaesgcm256rate(self) :
        """Rate (/s) counter for ssltotoffloadbulkaesgcm256."""
        try :
            return self._ssloffloadbulkaesgcm256rate
        except Exception as e:
            raise e

    @property
    def ssltotecdhe256keyexchanges(self) :
        """Number of 256 Elliptical Curve Diffie-Helman on the NetScaler appliance."""
        try :
            return self._ssltotecdhe256keyexchanges
        except Exception as e:
            raise e

    @property
    def sslcardstatus(self) :
        """Status of the SSL card(s). The value should be interpreted in binary form, with each set bit indicates a card as UP."""
        try :
            return self._sslcardstatus
        except Exception as e:
            raise e

    @property
    def sslnewsessionsrate(self) :
        """Rate (/s) counter for ssltotnewsessions."""
        try :
            return self._sslnewsessionsrate
        except Exception as e:
            raise e

    @property
    def sslbetot128bitideaciphers(self) :
        """Number of back-end IDEA 128-bit cipher encryptions on the NetScaler appliance."""
        try :
            return self._sslbetot128bitideaciphers
        except Exception as e:
            raise e

    @property
    def ssltransactionsrate(self) :
        """Rate (/s) counter for ssltottransactions."""
        try :
            return self._ssltransactionsrate
        except Exception as e:
            raise e

    @property
    def ssltotdechw(self) :
        """Number of bytes decrypted in hardware."""
        try :
            return self._ssltotdechw
        except Exception as e:
            raise e

    @property
    def sslhwdecferate(self) :
        """Rate (/s) counter for ssltothwdecfe."""
        try :
            return self._sslhwdecferate
        except Exception as e:
            raise e

    @property
    def ssltotbkendtlsvlrenego(self) :
        """Number of back-end TLSv1 session renegotiations on the NetScaler appliance."""
        try :
            return self._ssltotbkendtlsvlrenego
        except Exception as e:
            raise e

    @property
    def sslbetlsv1sessionsrate(self) :
        """Rate (/s) counter for sslbetottlsv1sessions."""
        try :
            return self._sslbetlsv1sessionsrate
        except Exception as e:
            raise e

    @property
    def sslbetotsslv3handshakes(self) :
        """Number of back-end SSLv3 handshakes on the NetScaler appliance."""
        try :
            return self._sslbetotsslv3handshakes
        except Exception as e:
            raise e

    @property
    def ssltlsv12transactionsrate(self) :
        """Rate (/s) counter for ssltottlsv12transactions."""
        try :
            return self._ssltlsv12transactionsrate
        except Exception as e:
            raise e

    @property
    def sslbetlsv12sessionsrate(self) :
        """Rate (/s) counter for sslbetottlsv12sessions."""
        try :
            return self._sslbetlsv12sessionsrate
        except Exception as e:
            raise e

    @property
    def sslsslv3handshakesrate(self) :
        """Rate (/s) counter for ssltotsslv3handshakes."""
        try :
            return self._sslsslv3handshakesrate
        except Exception as e:
            raise e

    @property
    def sslbetotsessionmultiplexattempts(self) :
        """Number of back-end SSL session multiplex attempts on the NetScaler appliance."""
        try :
            return self._sslbetotsessionmultiplexattempts
        except Exception as e:
            raise e

    @property
    def ssltotdssauthorizations(self) :
        """Total number of times DSS authorization is used on the NetScaler appliance."""
        try :
            return self._ssltotdssauthorizations
        except Exception as e:
            raise e

    @property
    def ssltotshamac(self) :
        """Number of SHA hashes on the NetScaler appliance."""
        try :
            return self._ssltotshamac
        except Exception as e:
            raise e

    @property
    def sslrsa4096keyexchangesrate(self) :
        """Rate (/s) counter for ssltotrsa4096keyexchanges."""
        try :
            return self._sslrsa4096keyexchangesrate
        except Exception as e:
            raise e

    @property
    def ssltotswdecfe(self) :
        """Number of bytes decrypted in software on the front end."""
        try :
            return self._ssltotswdecfe
        except Exception as e:
            raise e

    @property
    def ssltotrsa1024keyexchanges(self) :
        """Number of RSA 1024-bit key exchanges on the NetScaler appliance."""
        try :
            return self._ssltotrsa1024keyexchanges
        except Exception as e:
            raise e

    @property
    def ssltotnullauthorizations(self) :
        """Number of Null authentications on the NetScaler appliance."""
        try :
            return self._ssltotnullauthorizations
        except Exception as e:
            raise e

    @property
    def ssltotoffloadrsakeyexchanges(self) :
        """Number of RSA key exchanges offloaded to the cryptography card."""
        try :
            return self._ssltotoffloadrsakeyexchanges
        except Exception as e:
            raise e

    @property
    def sslbedhauthorizationsrate(self) :
        """Rate (/s) counter for sslbetotdhauthorizations."""
        try :
            return self._sslbedhauthorizationsrate
        except Exception as e:
            raise e

    @property
    def ssltotecdhe521keyexchanges(self) :
        """Number of 521 Elliptical Curve Diffie-Helman on the NetScaler appliance."""
        try :
            return self._ssltotecdhe521keyexchanges
        except Exception as e:
            raise e

    @property
    def sslmd5macrate(self) :
        """Rate (/s) counter for ssltotmd5mac."""
        try :
            return self._sslmd5macrate
        except Exception as e:
            raise e

    @property
    def sslswdecferate(self) :
        """Rate (/s) counter for ssltotswdecfe."""
        try :
            return self._sslswdecferate
        except Exception as e:
            raise e

    @property
    def sslcards(self) :
        """Number of SSL crypto cards present on the NetScaler appliance."""
        try :
            return self._sslcards
        except Exception as e:
            raise e

    @property
    def sslhwencberate(self) :
        """Rate (/s) counter for ssltothwencbe."""
        try :
            return self._sslhwencberate
        except Exception as e:
            raise e

    @property
    def ssltotoffloadbulkaesgcm128(self) :
        """Number of AES-GCM 128-bit encryptions offloaded to the cryptography card."""
        try :
            return self._ssltotoffloadbulkaesgcm128
        except Exception as e:
            raise e

    @property
    def sslnullciphersrate(self) :
        """Rate (/s) counter for ssltotnullciphers."""
        try :
            return self._sslnullciphersrate
        except Exception as e:
            raise e

    @property
    def sslbetot128bitrc4ciphers(self) :
        """Number of back-end RC4 128-bit cipher encryptions on the NetScaler appliance."""
        try :
            return self._sslbetot128bitrc4ciphers
        except Exception as e:
            raise e

    @property
    def ssltotsslv3sessions(self) :
        """Number of SSLv3 sessions on the NetScaler appliance."""
        try :
            return self._ssltotsslv3sessions
        except Exception as e:
            raise e

    @property
    def ssltotdh2048keyexchanges(self) :
        """Number of Diffie-Helman 2048-bit key exchanges on the NetScaler appliance."""
        try :
            return self._ssltotdh2048keyexchanges
        except Exception as e:
            raise e

    @property
    def ssltlsv1handshakesrate(self) :
        """Rate (/s) counter for ssltottlsv1handshakes."""
        try :
            return self._ssltlsv1handshakesrate
        except Exception as e:
            raise e

    @property
    def sslbetotdh1024keyexchanges(self) :
        """Number of back-end DH 1024-bit key exchanges on the NetScaler appliance."""
        try :
            return self._sslbetotdh1024keyexchanges
        except Exception as e:
            raise e

    @property
    def ssltotswdecbe(self) :
        """Number of bytes decrypted in software on back-end."""
        try :
            return self._ssltotswdecbe
        except Exception as e:
            raise e

    @property
    def ssltotnewsessions(self) :
        """Number of new SSL sessions created on the NetScaler appliance."""
        try :
            return self._ssltotnewsessions
        except Exception as e:
            raise e

    @property
    def sslecdhe224keyexchangesrate(self) :
        """Rate (/s) counter for ssltotecdhe224keyexchanges."""
        try :
            return self._sslecdhe224keyexchangesrate
        except Exception as e:
            raise e

    @property
    def ssltottlsv1sessions(self) :
        """Number of TLSv1 sessions on the NetScaler appliance."""
        try :
            return self._ssltottlsv1sessions
        except Exception as e:
            raise e

    @property
    def ssltot128bitrc2ciphers(self) :
        """Number of RC2 128-bit cipher encryptions on the NetScaler appliance."""
        try :
            return self._ssltot128bitrc2ciphers
        except Exception as e:
            raise e

    @property
    def sslbe64bitrc4ciphersrate(self) :
        """Rate (/s) counter for sslbetot64bitrc4ciphers."""
        try :
            return self._sslbe64bitrc4ciphersrate
        except Exception as e:
            raise e

    @property
    def sslbetotrsa1024keyexchanges(self) :
        """Number of back-end RSA 1024-bit key exchanges on the NetScaler appliance."""
        try :
            return self._sslbetotrsa1024keyexchanges
        except Exception as e:
            raise e

    @property
    def sslbetottlsv1sessions(self) :
        """Number of back-end TLSv1 sessions on the NetScaler appliance."""
        try :
            return self._sslbetottlsv1sessions
        except Exception as e:
            raise e

    @property
    def sslbersa1024keyexchangesrate(self) :
        """Rate (/s) counter for sslbetotrsa1024keyexchanges."""
        try :
            return self._sslbersa1024keyexchangesrate
        except Exception as e:
            raise e

    @property
    def ssltotbkendcipheraes256(self) :
        """Back-end AES 256-bit cipher encryptions on the NetScaler appliance."""
        try :
            return self._ssltotbkendcipheraes256
        except Exception as e:
            raise e

    @property
    def sslenginestatus(self) :
        """State of the SSL Engine (1=UP/0=DOWN). This state is decided based on SSL Feature/License status and minimum number of cards UP."""
        try :
            return self._sslenginestatus
        except Exception as e:
            raise e

    @property
    def ssltotswencbe(self) :
        """Number of bytes encrypted in software on the back end."""
        try :
            return self._ssltotswencbe
        except Exception as e:
            raise e

    @property
    def sslbersa512keyexchangesrate(self) :
        """Rate (/s) counter for sslbetotrsa512keyexchanges."""
        try :
            return self._sslbersa512keyexchangesrate
        except Exception as e:
            raise e

    @property
    def sslbetottlsv12sessions(self) :
        """Number of back-end TLSv1.2 sessions on the NetScaler appliance."""
        try :
            return self._sslbetottlsv12sessions
        except Exception as e:
            raise e

    @property
    def ssltlsv1transactionsrate(self) :
        """Rate (/s) counter for ssltottlsv1transactions."""
        try :
            return self._ssltlsv1transactionsrate
        except Exception as e:
            raise e

    @property
    def sslbetotecdhecurve521(self) :
        """Number of back-end ECDHE 521 curve Key exchanges  on the NetScaler appliance."""
        try :
            return self._sslbetotecdhecurve521
        except Exception as e:
            raise e

    @property
    def sslbe56bitdesciphersrate(self) :
        """Rate (/s) counter for sslbetot56bitdesciphers."""
        try :
            return self._sslbe56bitdesciphersrate
        except Exception as e:
            raise e

    @property
    def ssltlsv11renegsessionsrate(self) :
        """Rate (/s) counter for ssltottlsv11renegsessions."""
        try :
            return self._ssltlsv11renegsessionsrate
        except Exception as e:
            raise e

    @property
    def ssltlsv12handshakesrate(self) :
        """Rate (/s) counter for ssltottlsv12handshakes."""
        try :
            return self._ssltlsv12handshakesrate
        except Exception as e:
            raise e

    @property
    def sslbeecdhecurve384rate(self) :
        """Rate (/s) counter for sslbetotecdhecurve384."""
        try :
            return self._sslbeecdhecurve384rate
        except Exception as e:
            raise e

    @property
    def ssl56bitrc2ciphersrate(self) :
        """Rate (/s) counter for ssltot56bitrc2ciphers."""
        try :
            return self._ssl56bitrc2ciphersrate
        except Exception as e:
            raise e

    @property
    def ssloffloaddhkeyexchangesrate(self) :
        """Rate (/s) counter for ssltotoffloaddhkeyexchanges."""
        try :
            return self._ssloffloaddhkeyexchangesrate
        except Exception as e:
            raise e

    @property
    def sslsslv2sessionsrate(self) :
        """Rate (/s) counter for ssltotsslv2sessions."""
        try :
            return self._sslsslv2sessionsrate
        except Exception as e:
            raise e

    @property
    def sslswencberate(self) :
        """Rate (/s) counter for ssltotswencbe."""
        try :
            return self._sslswencberate
        except Exception as e:
            raise e

    @property
    def ssl256bitaesgcmciphersrate(self) :
        """Rate (/s) counter for ssltot256bitaesgcmciphers."""
        try :
            return self._ssl256bitaesgcmciphersrate
        except Exception as e:
            raise e

    @property
    def ssltottlsv12clientauthentications(self) :
        """Number of client authentications done on TLSv1.2."""
        try :
            return self._ssltottlsv12clientauthentications
        except Exception as e:
            raise e

    @property
    def ssloffloadsignrsarate(self) :
        """Rate (/s) counter for ssltotoffloadsignrsa."""
        try :
            return self._ssloffloadsignrsarate
        except Exception as e:
            raise e

    @property
    def sslencferate(self) :
        """Rate (/s) counter for ssltotencfe."""
        try :
            return self._sslencferate
        except Exception as e:
            raise e

    @property
    def sslbesslv3clientauthenticationsrate(self) :
        """Rate (/s) counter for sslbetotsslv3clientauthentications."""
        try :
            return self._sslbesslv3clientauthenticationsrate
        except Exception as e:
            raise e

    @property
    def ssltotoffloadbulkrc4(self) :
        """Number of RC4 encryptions offloaded to the cryptography card."""
        try :
            return self._ssltotoffloadbulkrc4
        except Exception as e:
            raise e

    @property
    def ssl128bitideaciphersrate(self) :
        """Rate (/s) counter for ssltot128bitideaciphers."""
        try :
            return self._ssl128bitideaciphersrate
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(ssl_response, response, self.__class__.__name__.replace('_stats',''))
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.ssl
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
        """Use this API to fetch the statistics of all ssl_stats resources that are configured on netscaler.

        :param service: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            obj = ssl_stats()
            if not name :
                response = obj.stat_resources(service, option_)
            return response
        except Exception as e:
            raise e

    class Clearstats:
        """ """
        basic = "basic"
        full = "full"

class ssl_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.ssl = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.ssl = [ssl_stats() for _ in range(length)]

