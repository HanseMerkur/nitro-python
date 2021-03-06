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

class sslprofile(base_resource) :
    """Configuration for SSL profile resource."""
    def __init__(self) :
        self._name = ""
        self._sslprofiletype = ""
        self._dhcount = 0
        self._dh = ""
        self._dhfile = ""
        self._ersa = ""
        self._ersacount = 0
        self._sessreuse = ""
        self._sesstimeout = 0
        self._cipherredirect = ""
        self._cipherurl = ""
        self._clientauth = ""
        self._clientcert = ""
        self._dhkeyexpsizelimit = ""
        self._sslredirect = ""
        self._redirectportrewrite = ""
        self._nonfipsciphers = ""
        self._ssl3 = ""
        self._tls1 = ""
        self._tls11 = ""
        self._tls12 = ""
        self._snienable = ""
        self._serverauth = ""
        self._commonname = ""
        self._pushenctrigger = ""
        self._sendclosenotify = ""
        self._cleartextport = 0
        self._insertionencoding = ""
        self._denysslreneg = ""
        self._quantumsize = ""
        self._strictcachecks = ""
        self._encrypttriggerpktcount = 0
        self._pushflag = 0
        self._dropreqwithnohostheader = ""
        self._pushenctriggertimeout = 0
        self._ssltriggertimeout = 0
        self._clientauthuseboundcachain = ""
        self._ciphername = ""
        self._cipherpriority = 0
        self._crlcheck = ""
        self._ocspcheck = ""
        self._snicert = False
        self._skipcaname = False
        self._invoke = False
        self._labeltype = ""
        self._service = 0
        self._builtin = []
        self.___count = 0

    @property
    def name(self) :
        """Name for the SSL profile. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the profile is created.<br/>Minimum length =  1<br/>Maximum length =  127."""
        try :
            return self._name
        except Exception as e:
            raise e

    @name.setter
    def name(self, name) :
        """Name for the SSL profile. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the profile is created.<br/>Minimum length =  1<br/>Maximum length =  127

        :param name: 

        """
        try :
            self._name = name
        except Exception as e:
            raise e

    @property
    def sslprofiletype(self) :
        """Type of profile. Front end profiles apply to the entity that receives requests from a client. Backend profiles apply to the entity that sends client requests to a server.<br/>Default value: FrontEnd<br/>Possible values = BackEnd, FrontEnd."""
        try :
            return self._sslprofiletype
        except Exception as e:
            raise e

    @sslprofiletype.setter
    def sslprofiletype(self, sslprofiletype) :
        """Type of profile. Front end profiles apply to the entity that receives requests from a client. Backend profiles apply to the entity that sends client requests to a server.<br/>Default value: FrontEnd<br/>Possible values = BackEnd, FrontEnd

        :param sslprofiletype: 

        """
        try :
            self._sslprofiletype = sslprofiletype
        except Exception as e:
            raise e

    @property
    def dhcount(self) :
        """Number of interactions, between the client and the NetScaler appliance, after which the DH private-public pair is regenerated. A value of zero (0) specifies infinite use (no refresh).
        This parameter is not applicable when configuring a backend profile.<br/>Maximum length =  65534.


        """
        try :
            return self._dhcount
        except Exception as e:
            raise e

    @dhcount.setter
    def dhcount(self, dhcount) :
        """Number of interactions, between the client and the NetScaler appliance, after which the DH private-public pair is regenerated. A value of zero (0) specifies infinite use (no refresh).
        This parameter is not applicable when configuring a backend profile.<br/>Maximum length =  65534

        :param dhcount: 

        """
        try :
            self._dhcount = dhcount
        except Exception as e:
            raise e

    @property
    def dh(self) :
        """State of Diffie-Hellman (DH) key exchange.
        This parameter is not applicable when configuring a backend profile.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.


        """
        try :
            return self._dh
        except Exception as e:
            raise e

    @dh.setter
    def dh(self, dh) :
        """State of Diffie-Hellman (DH) key exchange.
        This parameter is not applicable when configuring a backend profile.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED

        :param dh: 

        """
        try :
            self._dh = dh
        except Exception as e:
            raise e

    @property
    def dhfile(self) :
        """The file name and path for the DH parameter.<br/>Minimum length =  1."""
        try :
            return self._dhfile
        except Exception as e:
            raise e

    @dhfile.setter
    def dhfile(self, dhfile) :
        """The file name and path for the DH parameter.<br/>Minimum length =  1

        :param dhfile: 

        """
        try :
            self._dhfile = dhfile
        except Exception as e:
            raise e

    @property
    def ersa(self) :
        """State of Ephemeral RSA (eRSA) key exchange. Ephemeral RSA allows clients that support only export ciphers to communicate with the secure server even if the server certificate does not support export clients. The ephemeral RSA key is automatically generated when you bind an export cipher to an SSL or TCP-based SSL virtual server or service. When you remove the export cipher, the eRSA key is not deleted. It is reused at a later date when another export cipher is bound to an SSL or TCP-based SSL virtual server or service. The eRSA key is deleted when the appliance restarts.
        This parameter is not applicable when configuring a backend profile.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED.


        """
        try :
            return self._ersa
        except Exception as e:
            raise e

    @ersa.setter
    def ersa(self, ersa) :
        """State of Ephemeral RSA (eRSA) key exchange. Ephemeral RSA allows clients that support only export ciphers to communicate with the secure server even if the server certificate does not support export clients. The ephemeral RSA key is automatically generated when you bind an export cipher to an SSL or TCP-based SSL virtual server or service. When you remove the export cipher, the eRSA key is not deleted. It is reused at a later date when another export cipher is bound to an SSL or TCP-based SSL virtual server or service. The eRSA key is deleted when the appliance restarts.
        This parameter is not applicable when configuring a backend profile.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED

        :param ersa: 

        """
        try :
            self._ersa = ersa
        except Exception as e:
            raise e

    @property
    def ersacount(self) :
        """The  refresh  count  for the re-generation of RSA public-key and private-key pair.<br/>Maximum length =  65534."""
        try :
            return self._ersacount
        except Exception as e:
            raise e

    @ersacount.setter
    def ersacount(self, ersacount) :
        """The  refresh  count  for the re-generation of RSA public-key and private-key pair.<br/>Maximum length =  65534

        :param ersacount: 

        """
        try :
            self._ersacount = ersacount
        except Exception as e:
            raise e

    @property
    def sessreuse(self) :
        """State of session reuse. Establishing the initial handshake requires CPU-intensive public key encryption operations. With the ENABLED setting, session key exchange is avoided for session resumption requests received from the client.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._sessreuse
        except Exception as e:
            raise e

    @sessreuse.setter
    def sessreuse(self, sessreuse) :
        """State of session reuse. Establishing the initial handshake requires CPU-intensive public key encryption operations. With the ENABLED setting, session key exchange is avoided for session resumption requests received from the client.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED

        :param sessreuse: 

        """
        try :
            self._sessreuse = sessreuse
        except Exception as e:
            raise e

    @property
    def sesstimeout(self) :
        """The Session timeout value in seconds.<br/>Default value: 120<br/>Maximum length =  0xFFFFFFFE."""
        try :
            return self._sesstimeout
        except Exception as e:
            raise e

    @sesstimeout.setter
    def sesstimeout(self, sesstimeout) :
        """The Session timeout value in seconds.<br/>Default value: 120<br/>Maximum length =  0xFFFFFFFE

        :param sesstimeout: 

        """
        try :
            self._sesstimeout = sesstimeout
        except Exception as e:
            raise e

    @property
    def cipherredirect(self) :
        """State of Cipher Redirect. If this parameter is set to ENABLED, you can configure an SSL virtual server or service to display meaningful error messages if the SSL handshake fails because of a cipher mismatch between the virtual server or service and the client.
        This parameter is not applicable when configuring a backend profile.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.


        """
        try :
            return self._cipherredirect
        except Exception as e:
            raise e

    @cipherredirect.setter
    def cipherredirect(self, cipherredirect) :
        """State of Cipher Redirect. If this parameter is set to ENABLED, you can configure an SSL virtual server or service to display meaningful error messages if the SSL handshake fails because of a cipher mismatch between the virtual server or service and the client.
        This parameter is not applicable when configuring a backend profile.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED

        :param cipherredirect: 

        """
        try :
            self._cipherredirect = cipherredirect
        except Exception as e:
            raise e

    @property
    def cipherurl(self) :
        """The redirect URL to be used with the Cipher Redirect feature."""
        try :
            return self._cipherurl
        except Exception as e:
            raise e

    @cipherurl.setter
    def cipherurl(self, cipherurl) :
        """The redirect URL to be used with the Cipher Redirect feature.

        :param cipherurl: 

        """
        try :
            self._cipherurl = cipherurl
        except Exception as e:
            raise e

    @property
    def clientauth(self) :
        """State of client authentication. In service-based SSL offload, the service terminates the SSL handshake if the SSL client does not provide a valid certificate.
        This parameter is not applicable when configuring a backend profile.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.


        """
        try :
            return self._clientauth
        except Exception as e:
            raise e

    @clientauth.setter
    def clientauth(self, clientauth) :
        """State of client authentication. In service-based SSL offload, the service terminates the SSL handshake if the SSL client does not provide a valid certificate.
        This parameter is not applicable when configuring a backend profile.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED

        :param clientauth: 

        """
        try :
            self._clientauth = clientauth
        except Exception as e:
            raise e

    @property
    def clientcert(self) :
        """The rule for client certificate requirement in client authentication.<br/>Possible values = Mandatory, Optional."""
        try :
            return self._clientcert
        except Exception as e:
            raise e

    @clientcert.setter
    def clientcert(self, clientcert) :
        """The rule for client certificate requirement in client authentication.<br/>Possible values = Mandatory, Optional

        :param clientcert: 

        """
        try :
            self._clientcert = clientcert
        except Exception as e:
            raise e

    @property
    def dhkeyexpsizelimit(self) :
        """This option enables the use of NIST recommended (NIST Special Publication 800-56A) bit size for private-key size. For example, for DH params of size 2048bit, the private-key size recommended is 224bits. This is rounded-up to 256bits.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._dhkeyexpsizelimit
        except Exception as e:
            raise e

    @dhkeyexpsizelimit.setter
    def dhkeyexpsizelimit(self, dhkeyexpsizelimit) :
        """This option enables the use of NIST recommended (NIST Special Publication 800-56A) bit size for private-key size. For example, for DH params of size 2048bit, the private-key size recommended is 224bits. This is rounded-up to 256bits.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED

        :param dhkeyexpsizelimit: 

        """
        try :
            self._dhkeyexpsizelimit = dhkeyexpsizelimit
        except Exception as e:
            raise e

    @property
    def sslredirect(self) :
        """State of HTTPS redirects for the SSL service.
        For an SSL session, if the client browser receives a redirect message, the browser tries to connect to the new location. However, the secure SSL session breaks if the object has moved from a secure site (https://) to an unsecure site (http://). Typically, a warning message appears on the screen, prompting the user to continue or disconnect.
        If SSL Redirect is ENABLED, the redirect message is automatically converted from http:// to https:// and the SSL session does not break.
        This parameter is not applicable when configuring a backend profile.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED.


        """
        try :
            return self._sslredirect
        except Exception as e:
            raise e

    @sslredirect.setter
    def sslredirect(self, sslredirect) :
        """State of HTTPS redirects for the SSL service.
        For an SSL session, if the client browser receives a redirect message, the browser tries to connect to the new location. However, the secure SSL session breaks if the object has moved from a secure site (https://) to an unsecure site (http://). Typically, a warning message appears on the screen, prompting the user to continue or disconnect.
        If SSL Redirect is ENABLED, the redirect message is automatically converted from http:// to https:// and the SSL session does not break.
        This parameter is not applicable when configuring a backend profile.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED

        :param sslredirect: 

        """
        try :
            self._sslredirect = sslredirect
        except Exception as e:
            raise e

    @property
    def redirectportrewrite(self) :
        """State of the port rewrite while performing HTTPS redirect. If this parameter is set to ENABLED, and the URL from the server does not contain the standard port, the port is rewritten to the standard.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._redirectportrewrite
        except Exception as e:
            raise e

    @redirectportrewrite.setter
    def redirectportrewrite(self, redirectportrewrite) :
        """State of the port rewrite while performing HTTPS redirect. If this parameter is set to ENABLED, and the URL from the server does not contain the standard port, the port is rewritten to the standard.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED

        :param redirectportrewrite: 

        """
        try :
            self._redirectportrewrite = redirectportrewrite
        except Exception as e:
            raise e

    @property
    def nonfipsciphers(self) :
        """State of usage of ciphers that are not FIPS approved. Valid only for an SSL service bound with a FIPS key and certificate.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._nonfipsciphers
        except Exception as e:
            raise e

    @nonfipsciphers.setter
    def nonfipsciphers(self, nonfipsciphers) :
        """State of usage of ciphers that are not FIPS approved. Valid only for an SSL service bound with a FIPS key and certificate.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED

        :param nonfipsciphers: 

        """
        try :
            self._nonfipsciphers = nonfipsciphers
        except Exception as e:
            raise e

    @property
    def ssl3(self) :
        """State of SSLv3 protocol support for the SSL profile.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._ssl3
        except Exception as e:
            raise e

    @ssl3.setter
    def ssl3(self, ssl3) :
        """State of SSLv3 protocol support for the SSL profile.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED

        :param ssl3: 

        """
        try :
            self._ssl3 = ssl3
        except Exception as e:
            raise e

    @property
    def tls1(self) :
        """State of TLSv1.0 protocol support for the SSL profile.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._tls1
        except Exception as e:
            raise e

    @tls1.setter
    def tls1(self, tls1) :
        """State of TLSv1.0 protocol support for the SSL profile.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED

        :param tls1: 

        """
        try :
            self._tls1 = tls1
        except Exception as e:
            raise e

    @property
    def tls11(self) :
        """State of TLSv1.1 protocol support for the SSL profile.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._tls11
        except Exception as e:
            raise e

    @tls11.setter
    def tls11(self, tls11) :
        """State of TLSv1.1 protocol support for the SSL profile.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED

        :param tls11: 

        """
        try :
            self._tls11 = tls11
        except Exception as e:
            raise e

    @property
    def tls12(self) :
        """State of TLSv1.2 protocol support for the SSL profile.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._tls12
        except Exception as e:
            raise e

    @tls12.setter
    def tls12(self, tls12) :
        """State of TLSv1.2 protocol support for the SSL profile.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED

        :param tls12: 

        """
        try :
            self._tls12 = tls12
        except Exception as e:
            raise e

    @property
    def snienable(self) :
        """State of the Server Name Indication (SNI) feature on the virtual server and service-based offload. SNI helps to enable SSL encryption on multiple domains on a single virtual server or service if the domains are controlled by the same organization and share the same second-level domain name. For example, *.sports.net can be used to secure domains such as login.sports.net and help.sports.net.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._snienable
        except Exception as e:
            raise e

    @snienable.setter
    def snienable(self, snienable) :
        """State of the Server Name Indication (SNI) feature on the virtual server and service-based offload. SNI helps to enable SSL encryption on multiple domains on a single virtual server or service if the domains are controlled by the same organization and share the same second-level domain name. For example, *.sports.net can be used to secure domains such as login.sports.net and help.sports.net.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED

        :param snienable: 

        """
        try :
            self._snienable = snienable
        except Exception as e:
            raise e

    @property
    def serverauth(self) :
        """State of server authentication support for the SSL Backend profile.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._serverauth
        except Exception as e:
            raise e

    @serverauth.setter
    def serverauth(self, serverauth) :
        """State of server authentication support for the SSL Backend profile.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED

        :param serverauth: 

        """
        try :
            self._serverauth = serverauth
        except Exception as e:
            raise e

    @property
    def commonname(self) :
        """Name to be checked against the CommonName (CN) field in the server certificate bound to the SSL server.<br/>Minimum length =  1."""
        try :
            return self._commonname
        except Exception as e:
            raise e

    @commonname.setter
    def commonname(self, commonname) :
        """Name to be checked against the CommonName (CN) field in the server certificate bound to the SSL server.<br/>Minimum length =  1

        :param commonname: 

        """
        try :
            self._commonname = commonname
        except Exception as e:
            raise e

    @property
    def pushenctrigger(self) :
        """Trigger encryption on the basis of the PUSH flag value. Available settings function as follows:
        * ALWAYS - Any PUSH packet triggers encryption.
        * IGNORE - Ignore PUSH packet for triggering encryption.
        * MERGE - For a consecutive sequence of PUSH packets, the last PUSH packet triggers encryption.
        * TIMER - PUSH packet triggering encryption is delayed by the time defined in the set ssl parameter command or in the Change Advanced SSL Settings dialog box.<br/>Possible values = Always, Merge, Ignore, Timer.


        """
        try :
            return self._pushenctrigger
        except Exception as e:
            raise e

    @pushenctrigger.setter
    def pushenctrigger(self, pushenctrigger) :
        """Trigger encryption on the basis of the PUSH flag value. Available settings function as follows:
        * ALWAYS - Any PUSH packet triggers encryption.
        * IGNORE - Ignore PUSH packet for triggering encryption.
        * MERGE - For a consecutive sequence of PUSH packets, the last PUSH packet triggers encryption.
        * TIMER - PUSH packet triggering encryption is delayed by the time defined in the set ssl parameter command or in the Change Advanced SSL Settings dialog box.<br/>Possible values = Always, Merge, Ignore, Timer

        :param pushenctrigger: 

        """
        try :
            self._pushenctrigger = pushenctrigger
        except Exception as e:
            raise e

    @property
    def sendclosenotify(self) :
        """Enable sending SSL Close-Notify at the end of a transaction.<br/>Default value: YES<br/>Possible values = YES, NO."""
        try :
            return self._sendclosenotify
        except Exception as e:
            raise e

    @sendclosenotify.setter
    def sendclosenotify(self, sendclosenotify) :
        """Enable sending SSL Close-Notify at the end of a transaction.<br/>Default value: YES<br/>Possible values = YES, NO

        :param sendclosenotify: 

        """
        try :
            self._sendclosenotify = sendclosenotify
        except Exception as e:
            raise e

    @property
    def cleartextport(self) :
        """Port on which clear-text data is sent by the appliance to the server. Do not specify this parameter for SSL offloading with end-to-end encryption.<br/>Range 1 - 65535."""
        try :
            return self._cleartextport
        except Exception as e:
            raise e

    @cleartextport.setter
    def cleartextport(self, cleartextport) :
        """Port on which clear-text data is sent by the appliance to the server. Do not specify this parameter for SSL offloading with end-to-end encryption.<br/>Range 1 - 65535

        :param cleartextport: 

        """
        try :
            self._cleartextport = cleartextport
        except Exception as e:
            raise e

    @property
    def insertionencoding(self) :
        """Encoding method used to insert the subject or issuer's name in HTTP requests to servers.<br/>Default value: Unicode<br/>Possible values = Unicode, UTF-8."""
        try :
            return self._insertionencoding
        except Exception as e:
            raise e

    @insertionencoding.setter
    def insertionencoding(self, insertionencoding) :
        """Encoding method used to insert the subject or issuer's name in HTTP requests to servers.<br/>Default value: Unicode<br/>Possible values = Unicode, UTF-8

        :param insertionencoding: 

        """
        try :
            self._insertionencoding = insertionencoding
        except Exception as e:
            raise e

    @property
    def denysslreneg(self) :
        """Deny renegotiation in specified circumstances. Available settings function as follows:
        * NO - Allow SSL renegotiation.
        * FRONTEND_CLIENT - Deny secure and nonsecure SSL renegotiation initiated by the client.
        * FRONTEND_CLIENTSERVER - Deny secure and nonsecure SSL renegotiation initiated by the client or the NetScaler during policy-based client authentication.
        * ALL - Deny all secure and nonsecure SSL renegotiation.
        * NONSECURE - Deny nonsecure SSL renegotiation. Allows only clients that support RFC 5746.<br/>Default value: ALL<br/>Possible values = NO, FRONTEND_CLIENT, FRONTEND_CLIENTSERVER, ALL, NONSECURE.


        """
        try :
            return self._denysslreneg
        except Exception as e:
            raise e

    @denysslreneg.setter
    def denysslreneg(self, denysslreneg) :
        """Deny renegotiation in specified circumstances. Available settings function as follows:
        * NO - Allow SSL renegotiation.
        * FRONTEND_CLIENT - Deny secure and nonsecure SSL renegotiation initiated by the client.
        * FRONTEND_CLIENTSERVER - Deny secure and nonsecure SSL renegotiation initiated by the client or the NetScaler during policy-based client authentication.
        * ALL - Deny all secure and nonsecure SSL renegotiation.
        * NONSECURE - Deny nonsecure SSL renegotiation. Allows only clients that support RFC 5746.<br/>Default value: ALL<br/>Possible values = NO, FRONTEND_CLIENT, FRONTEND_CLIENTSERVER, ALL, NONSECURE

        :param denysslreneg: 

        """
        try :
            self._denysslreneg = denysslreneg
        except Exception as e:
            raise e

    @property
    def quantumsize(self) :
        """Amount of data to collect before the data is pushed to the crypto hardware for encryption. For large downloads, a larger quantum size better utilizes the crypto resources.<br/>Default value: 8192<br/>Possible values = 4096, 8192, 16384."""
        try :
            return self._quantumsize
        except Exception as e:
            raise e

    @quantumsize.setter
    def quantumsize(self, quantumsize) :
        """Amount of data to collect before the data is pushed to the crypto hardware for encryption. For large downloads, a larger quantum size better utilizes the crypto resources.<br/>Default value: 8192<br/>Possible values = 4096, 8192, 16384

        :param quantumsize: 

        """
        try :
            self._quantumsize = quantumsize
        except Exception as e:
            raise e

    @property
    def strictcachecks(self) :
        """Enable strict CA certificate checks on the appliance.<br/>Default value: NO<br/>Possible values = YES, NO."""
        try :
            return self._strictcachecks
        except Exception as e:
            raise e

    @strictcachecks.setter
    def strictcachecks(self, strictcachecks) :
        """Enable strict CA certificate checks on the appliance.<br/>Default value: NO<br/>Possible values = YES, NO

        :param strictcachecks: 

        """
        try :
            self._strictcachecks = strictcachecks
        except Exception as e:
            raise e

    @property
    def encrypttriggerpktcount(self) :
        """Maximum number of queued packets after which encryption is triggered. Use this setting for SSL transactions that send small packets from server to NetScaler.<br/>Default value: 45<br/>Minimum length =  10<br/>Maximum length =  50."""
        try :
            return self._encrypttriggerpktcount
        except Exception as e:
            raise e

    @encrypttriggerpktcount.setter
    def encrypttriggerpktcount(self, encrypttriggerpktcount) :
        """Maximum number of queued packets after which encryption is triggered. Use this setting for SSL transactions that send small packets from server to NetScaler.<br/>Default value: 45<br/>Minimum length =  10<br/>Maximum length =  50

        :param encrypttriggerpktcount: 

        """
        try :
            self._encrypttriggerpktcount = encrypttriggerpktcount
        except Exception as e:
            raise e

    @property
    def pushflag(self) :
        """Insert PUSH flag into decrypted, encrypted, or all records. If the PUSH flag is set to a value other than 0, the buffered records are forwarded on the basis of the value of the PUSH flag. Available settings function as follows:
        0 - Auto (PUSH flag is not set.)
        1 - Insert PUSH flag into every decrypted record.
        2 -Insert PUSH flag into every encrypted record.
        3 - Insert PUSH flag into every decrypted and encrypted record.<br/>Maximum length =  3.


        """
        try :
            return self._pushflag
        except Exception as e:
            raise e

    @pushflag.setter
    def pushflag(self, pushflag) :
        """Insert PUSH flag into decrypted, encrypted, or all records. If the PUSH flag is set to a value other than 0, the buffered records are forwarded on the basis of the value of the PUSH flag. Available settings function as follows:
        0 - Auto (PUSH flag is not set.)
        1 - Insert PUSH flag into every decrypted record.
        2 -Insert PUSH flag into every encrypted record.
        3 - Insert PUSH flag into every decrypted and encrypted record.<br/>Maximum length =  3

        :param pushflag: 

        """
        try :
            self._pushflag = pushflag
        except Exception as e:
            raise e

    @property
    def dropreqwithnohostheader(self) :
        """Host header check for SNI enabled sessions. If this check is enabled and the HTTP request does not contain the host header for SNI enabled sessions, the request is dropped.<br/>Default value: NO<br/>Possible values = YES, NO."""
        try :
            return self._dropreqwithnohostheader
        except Exception as e:
            raise e

    @dropreqwithnohostheader.setter
    def dropreqwithnohostheader(self, dropreqwithnohostheader) :
        """Host header check for SNI enabled sessions. If this check is enabled and the HTTP request does not contain the host header for SNI enabled sessions, the request is dropped.<br/>Default value: NO<br/>Possible values = YES, NO

        :param dropreqwithnohostheader: 

        """
        try :
            self._dropreqwithnohostheader = dropreqwithnohostheader
        except Exception as e:
            raise e

    @property
    def pushenctriggertimeout(self) :
        """PUSH encryption trigger timeout value. The timeout value is applied only if you set the Push Encryption Trigger parameter to Timer in the SSL virtual server settings.<br/>Default value: 1<br/>Minimum length =  1<br/>Maximum length =  200."""
        try :
            return self._pushenctriggertimeout
        except Exception as e:
            raise e

    @pushenctriggertimeout.setter
    def pushenctriggertimeout(self, pushenctriggertimeout) :
        """PUSH encryption trigger timeout value. The timeout value is applied only if you set the Push Encryption Trigger parameter to Timer in the SSL virtual server settings.<br/>Default value: 1<br/>Minimum length =  1<br/>Maximum length =  200

        :param pushenctriggertimeout: 

        """
        try :
            self._pushenctriggertimeout = pushenctriggertimeout
        except Exception as e:
            raise e

    @property
    def ssltriggertimeout(self) :
        """Time, in milliseconds, after which encryption is triggered for transactions that are not tracked on the NetScaler appliance because their length is not known. There can be a delay of up to 10ms from the specified timeout value before the packet is pushed into the queue.<br/>Default value: 100<br/>Minimum length =  1<br/>Maximum length =  200."""
        try :
            return self._ssltriggertimeout
        except Exception as e:
            raise e

    @ssltriggertimeout.setter
    def ssltriggertimeout(self, ssltriggertimeout) :
        """Time, in milliseconds, after which encryption is triggered for transactions that are not tracked on the NetScaler appliance because their length is not known. There can be a delay of up to 10ms from the specified timeout value before the packet is pushed into the queue.<br/>Default value: 100<br/>Minimum length =  1<br/>Maximum length =  200

        :param ssltriggertimeout: 

        """
        try :
            self._ssltriggertimeout = ssltriggertimeout
        except Exception as e:
            raise e

    @property
    def clientauthuseboundcachain(self) :
        """Certficates bound on the VIP are used for validating the client cert. Certficates came along with client cert are not used for validating the client cert.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._clientauthuseboundcachain
        except Exception as e:
            raise e

    @clientauthuseboundcachain.setter
    def clientauthuseboundcachain(self, clientauthuseboundcachain) :
        """Certficates bound on the VIP are used for validating the client cert. Certficates came along with client cert are not used for validating the client cert.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED

        :param clientauthuseboundcachain: 

        """
        try :
            self._clientauthuseboundcachain = clientauthuseboundcachain
        except Exception as e:
            raise e

    @property
    def ciphername(self) :
        """The cipher group/alias/individual cipher configuration."""
        try :
            return self._ciphername
        except Exception as e:
            raise e

    @ciphername.setter
    def ciphername(self, ciphername) :
        """The cipher group/alias/individual cipher configuration.

        :param ciphername: 

        """
        try :
            self._ciphername = ciphername
        except Exception as e:
            raise e

    @property
    def cipherpriority(self) :
        """cipher priority.<br/>Minimum length =  1."""
        try :
            return self._cipherpriority
        except Exception as e:
            raise e

    @cipherpriority.setter
    def cipherpriority(self, cipherpriority) :
        """cipher priority.<br/>Minimum length =  1

        :param cipherpriority: 

        """
        try :
            self._cipherpriority = cipherpriority
        except Exception as e:
            raise e

    @property
    def crlcheck(self) :
        """The state of the CRL check parameter. (Mandatory/Optional).<br/>Possible values = Mandatory, Optional."""
        try :
            return self._crlcheck
        except Exception as e:
            raise e

    @property
    def ocspcheck(self) :
        """The state of the OCSP check parameter. (Mandatory/Optional).<br/>Possible values = Mandatory, Optional."""
        try :
            return self._ocspcheck
        except Exception as e:
            raise e

    @property
    def snicert(self) :
        """The name of the CertKey. Use this option to bind Certkey(s) which will be used in SNI processing."""
        try :
            return self._snicert
        except Exception as e:
            raise e

    @property
    def skipcaname(self) :
        """The flag is used to indicate whether this
        particular CA certificate's CA_Name needs to be sent to
        the SSL client while requesting for client certificate
        in a SSL handshake.


        """
        try :
            return self._skipcaname
        except Exception as e:
            raise e

    @property
    def invoke(self) :
        """Invoke flag. This attribute is relevant only for ADVANCED policies."""
        try :
            return self._invoke
        except Exception as e:
            raise e

    @property
    def labeltype(self) :
        """Type of policy label invocation.<br/>Possible values = vserver, service, policylabel."""
        try :
            return self._labeltype
        except Exception as e:
            raise e

    @property
    def service(self) :
        """Service."""
        try :
            return self._service
        except Exception as e:
            raise e

    @property
    def builtin(self) :
        """Flag to determine whether ssl profile is built-in or not.<br/>Possible values = MODIFIABLE, DELETABLE, IMMUTABLE, PARTITION_ALL."""
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
            result = service.payload_formatter.string_to_resource(sslprofile_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.sslprofile
        except Exception as e :
            raise e

    def _get_object_name(self) :
        """Returns the value of object identifier argument"""
        try :
            if self.name is not None :
                return str(self.name)
            return None
        except Exception as e :
            raise e



    @classmethod
    def add(cls, client, resource) :
        """Use this API to add sslprofile.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                addresource = sslprofile()
                addresource.name = resource.name
                addresource.sslprofiletype = resource.sslprofiletype
                addresource.dhcount = resource.dhcount
                addresource.dh = resource.dh
                addresource.dhfile = resource.dhfile
                addresource.ersa = resource.ersa
                addresource.ersacount = resource.ersacount
                addresource.sessreuse = resource.sessreuse
                addresource.sesstimeout = resource.sesstimeout
                addresource.cipherredirect = resource.cipherredirect
                addresource.cipherurl = resource.cipherurl
                addresource.clientauth = resource.clientauth
                addresource.clientcert = resource.clientcert
                addresource.dhkeyexpsizelimit = resource.dhkeyexpsizelimit
                addresource.sslredirect = resource.sslredirect
                addresource.redirectportrewrite = resource.redirectportrewrite
                addresource.nonfipsciphers = resource.nonfipsciphers
                addresource.ssl3 = resource.ssl3
                addresource.tls1 = resource.tls1
                addresource.tls11 = resource.tls11
                addresource.tls12 = resource.tls12
                addresource.snienable = resource.snienable
                addresource.serverauth = resource.serverauth
                addresource.commonname = resource.commonname
                addresource.pushenctrigger = resource.pushenctrigger
                addresource.sendclosenotify = resource.sendclosenotify
                addresource.cleartextport = resource.cleartextport
                addresource.insertionencoding = resource.insertionencoding
                addresource.denysslreneg = resource.denysslreneg
                addresource.quantumsize = resource.quantumsize
                addresource.strictcachecks = resource.strictcachecks
                addresource.encrypttriggerpktcount = resource.encrypttriggerpktcount
                addresource.pushflag = resource.pushflag
                addresource.dropreqwithnohostheader = resource.dropreqwithnohostheader
                addresource.pushenctriggertimeout = resource.pushenctriggertimeout
                addresource.ssltriggertimeout = resource.ssltriggertimeout
                addresource.clientauthuseboundcachain = resource.clientauthuseboundcachain
                return addresource.add_resource(client)
            else :
                if (resource and len(resource) > 0) :
                    addresources = [ sslprofile() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        addresources[i].name = resource[i].name
                        addresources[i].sslprofiletype = resource[i].sslprofiletype
                        addresources[i].dhcount = resource[i].dhcount
                        addresources[i].dh = resource[i].dh
                        addresources[i].dhfile = resource[i].dhfile
                        addresources[i].ersa = resource[i].ersa
                        addresources[i].ersacount = resource[i].ersacount
                        addresources[i].sessreuse = resource[i].sessreuse
                        addresources[i].sesstimeout = resource[i].sesstimeout
                        addresources[i].cipherredirect = resource[i].cipherredirect
                        addresources[i].cipherurl = resource[i].cipherurl
                        addresources[i].clientauth = resource[i].clientauth
                        addresources[i].clientcert = resource[i].clientcert
                        addresources[i].dhkeyexpsizelimit = resource[i].dhkeyexpsizelimit
                        addresources[i].sslredirect = resource[i].sslredirect
                        addresources[i].redirectportrewrite = resource[i].redirectportrewrite
                        addresources[i].nonfipsciphers = resource[i].nonfipsciphers
                        addresources[i].ssl3 = resource[i].ssl3
                        addresources[i].tls1 = resource[i].tls1
                        addresources[i].tls11 = resource[i].tls11
                        addresources[i].tls12 = resource[i].tls12
                        addresources[i].snienable = resource[i].snienable
                        addresources[i].serverauth = resource[i].serverauth
                        addresources[i].commonname = resource[i].commonname
                        addresources[i].pushenctrigger = resource[i].pushenctrigger
                        addresources[i].sendclosenotify = resource[i].sendclosenotify
                        addresources[i].cleartextport = resource[i].cleartextport
                        addresources[i].insertionencoding = resource[i].insertionencoding
                        addresources[i].denysslreneg = resource[i].denysslreneg
                        addresources[i].quantumsize = resource[i].quantumsize
                        addresources[i].strictcachecks = resource[i].strictcachecks
                        addresources[i].encrypttriggerpktcount = resource[i].encrypttriggerpktcount
                        addresources[i].pushflag = resource[i].pushflag
                        addresources[i].dropreqwithnohostheader = resource[i].dropreqwithnohostheader
                        addresources[i].pushenctriggertimeout = resource[i].pushenctriggertimeout
                        addresources[i].ssltriggertimeout = resource[i].ssltriggertimeout
                        addresources[i].clientauthuseboundcachain = resource[i].clientauthuseboundcachain
                result = cls.add_bulk_request(client, addresources)
            return result
        except Exception as e :
            raise e

    @classmethod
    def delete(cls, client, resource) :
        """Use this API to delete sslprofile.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                deleteresource = sslprofile()
                if type(resource) !=  type(deleteresource):
                    deleteresource.name = resource
                else :
                    deleteresource.name = resource.name
                return deleteresource.delete_resource(client)
            else :
                if type(resource[0]) != cls :
                    if (resource and len(resource) > 0) :
                        deleteresources = [ sslprofile() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            deleteresources[i].name = resource[i]
                else :
                    if (resource and len(resource) > 0) :
                        deleteresources = [ sslprofile() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            deleteresources[i].name = resource[i].name
                result = cls.delete_bulk_request(client, deleteresources)
            return result
        except Exception as e :
            raise e

    @classmethod
    def update(cls, client, resource) :
        """Use this API to update sslprofile.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                updateresource = sslprofile()
                updateresource.name = resource.name
                updateresource.dh = resource.dh
                updateresource.dhfile = resource.dhfile
                updateresource.dhcount = resource.dhcount
                updateresource.dhkeyexpsizelimit = resource.dhkeyexpsizelimit
                updateresource.ersa = resource.ersa
                updateresource.ersacount = resource.ersacount
                updateresource.sessreuse = resource.sessreuse
                updateresource.sesstimeout = resource.sesstimeout
                updateresource.cipherredirect = resource.cipherredirect
                updateresource.cipherurl = resource.cipherurl
                updateresource.clientauth = resource.clientauth
                updateresource.clientcert = resource.clientcert
                updateresource.sslredirect = resource.sslredirect
                updateresource.redirectportrewrite = resource.redirectportrewrite
                updateresource.nonfipsciphers = resource.nonfipsciphers
                updateresource.ssl3 = resource.ssl3
                updateresource.tls1 = resource.tls1
                updateresource.tls11 = resource.tls11
                updateresource.tls12 = resource.tls12
                updateresource.snienable = resource.snienable
                updateresource.serverauth = resource.serverauth
                updateresource.commonname = resource.commonname
                updateresource.pushenctrigger = resource.pushenctrigger
                updateresource.sendclosenotify = resource.sendclosenotify
                updateresource.cleartextport = resource.cleartextport
                updateresource.insertionencoding = resource.insertionencoding
                updateresource.denysslreneg = resource.denysslreneg
                updateresource.quantumsize = resource.quantumsize
                updateresource.strictcachecks = resource.strictcachecks
                updateresource.encrypttriggerpktcount = resource.encrypttriggerpktcount
                updateresource.pushflag = resource.pushflag
                updateresource.dropreqwithnohostheader = resource.dropreqwithnohostheader
                updateresource.pushenctriggertimeout = resource.pushenctriggertimeout
                updateresource.ssltriggertimeout = resource.ssltriggertimeout
                updateresource.clientauthuseboundcachain = resource.clientauthuseboundcachain
                updateresource.ciphername = resource.ciphername
                updateresource.cipherpriority = resource.cipherpriority
                return updateresource.update_resource(client)
            else :
                if (resource and len(resource) > 0) :
                    updateresources = [ sslprofile() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        updateresources[i].name = resource[i].name
                        updateresources[i].dh = resource[i].dh
                        updateresources[i].dhfile = resource[i].dhfile
                        updateresources[i].dhcount = resource[i].dhcount
                        updateresources[i].dhkeyexpsizelimit = resource[i].dhkeyexpsizelimit
                        updateresources[i].ersa = resource[i].ersa
                        updateresources[i].ersacount = resource[i].ersacount
                        updateresources[i].sessreuse = resource[i].sessreuse
                        updateresources[i].sesstimeout = resource[i].sesstimeout
                        updateresources[i].cipherredirect = resource[i].cipherredirect
                        updateresources[i].cipherurl = resource[i].cipherurl
                        updateresources[i].clientauth = resource[i].clientauth
                        updateresources[i].clientcert = resource[i].clientcert
                        updateresources[i].sslredirect = resource[i].sslredirect
                        updateresources[i].redirectportrewrite = resource[i].redirectportrewrite
                        updateresources[i].nonfipsciphers = resource[i].nonfipsciphers
                        updateresources[i].ssl3 = resource[i].ssl3
                        updateresources[i].tls1 = resource[i].tls1
                        updateresources[i].tls11 = resource[i].tls11
                        updateresources[i].tls12 = resource[i].tls12
                        updateresources[i].snienable = resource[i].snienable
                        updateresources[i].serverauth = resource[i].serverauth
                        updateresources[i].commonname = resource[i].commonname
                        updateresources[i].pushenctrigger = resource[i].pushenctrigger
                        updateresources[i].sendclosenotify = resource[i].sendclosenotify
                        updateresources[i].cleartextport = resource[i].cleartextport
                        updateresources[i].insertionencoding = resource[i].insertionencoding
                        updateresources[i].denysslreneg = resource[i].denysslreneg
                        updateresources[i].quantumsize = resource[i].quantumsize
                        updateresources[i].strictcachecks = resource[i].strictcachecks
                        updateresources[i].encrypttriggerpktcount = resource[i].encrypttriggerpktcount
                        updateresources[i].pushflag = resource[i].pushflag
                        updateresources[i].dropreqwithnohostheader = resource[i].dropreqwithnohostheader
                        updateresources[i].pushenctriggertimeout = resource[i].pushenctriggertimeout
                        updateresources[i].ssltriggertimeout = resource[i].ssltriggertimeout
                        updateresources[i].clientauthuseboundcachain = resource[i].clientauthuseboundcachain
                        updateresources[i].ciphername = resource[i].ciphername
                        updateresources[i].cipherpriority = resource[i].cipherpriority
                result = cls.update_bulk_request(client, updateresources)
            return result
        except Exception as e :
            raise e

    @classmethod
    def unset(cls, client, resource, args) :
        """Use this API to unset the properties of sslprofile resource.
        Properties that need to be unset are specified in args array.

        :param client: 
        :param resource: 
        :param args: 

        """
        try :
            if type(resource) is not list :
                unsetresource = sslprofile()
                if type(resource) !=  type(unsetresource):
                    unsetresource.name = resource
                else :
                    unsetresource.name = resource.name
                return unsetresource.unset_resource(client, args)
            else :
                if type(resource[0]) != cls :
                    if (resource and len(resource) > 0) :
                        unsetresources = [ sslprofile() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            unsetresources[i].name = resource[i]
                else :
                    if (resource and len(resource) > 0) :
                        unsetresources = [ sslprofile() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            unsetresources[i].name = resource[i].name
                result = cls.unset_bulk_request(client, unsetresources, args)
            return result
        except Exception as e :
            raise e

    @classmethod
    def get(cls, client, name="", option_="") :
        """Use this API to fetch all the sslprofile resources that are configured on netscaler.

        :param client: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            if not name :
                obj = sslprofile()
                response = obj.get_resources(client, option_)
            else :
                if type(name) != cls :
                    if type(name) is not list :
                        obj = sslprofile()
                        obj.name = name
                        response = obj.get_resource(client, option_)
                    else :
                        if name and len(name) > 0 :
                            response = [sslprofile() for _ in range(len(name))]
                            obj = [sslprofile() for _ in range(len(name))]
                            for i in range(len(name)) :
                                obj[i] = sslprofile()
                                obj[i].name = name[i]
                                response[i] = obj[i].get_resource(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def get_filtered(cls, client, filter_) :
        """Use this API to fetch filtered set of sslprofile resources.
        filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = sslprofile()
            option_ = options()
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def count(cls, client) :
        """Use this API to count the sslprofile resources configured on NetScaler.

        :param client: 

        """
        try :
            obj = sslprofile()
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
        """Use this API to count filtered the set of sslprofile resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = sslprofile()
            option_ = options()
            option_.count = True
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            if response :
                return response[0].__dict__['___count']
            return 0
        except Exception as e :
            raise e


    class Denysslreneg:
        """ """
        NO = "NO"
        FRONTEND_CLIENT = "FRONTEND_CLIENT"
        FRONTEND_CLIENTSERVER = "FRONTEND_CLIENTSERVER"
        ALL = "ALL"
        NONSECURE = "NONSECURE"

    class Insertionencoding:
        """ """
        Unicode = "Unicode"
        UTF_8 = "UTF-8"

    class Sslredirect:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Ersa:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Strictcachecks:
        """ """
        YES = "YES"
        NO = "NO"

    class Quantumsize:
        """ """
        _4096 = "4096"
        _8192 = "8192"
        _16384 = "16384"

    class Redirectportrewrite:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Sessreuse:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Ssl3:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Tls1:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Builtin:
        """ """
        MODIFIABLE = "MODIFIABLE"
        DELETABLE = "DELETABLE"
        IMMUTABLE = "IMMUTABLE"
        PARTITION_ALL = "PARTITION_ALL"

    class Clientauthuseboundcachain:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Sendclosenotify:
        """ """
        YES = "YES"
        NO = "NO"

    class Tls11:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Dropreqwithnohostheader:
        """ """
        YES = "YES"
        NO = "NO"

    class Dh:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Tls12:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Serverauth:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Nonfipsciphers:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Snienable:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Cipherredirect:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Labeltype:
        """ """
        vserver = "vserver"
        service = "service"
        policylabel = "policylabel"

    class Clientcert:
        """ """
        Mandatory = "Mandatory"
        Optional = "Optional"

    class Dhkeyexpsizelimit:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Pushenctrigger:
        """ """
        Always = "Always"
        Merge = "Merge"
        Ignore = "Ignore"
        Timer = "Timer"

    class Crlcheck:
        """ """
        Mandatory = "Mandatory"
        Optional = "Optional"

    class Clientauth:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Ocspcheck:
        """ """
        Mandatory = "Mandatory"
        Optional = "Optional"

    class Sslprofiletype:
        """ """
        BackEnd = "BackEnd"
        FrontEnd = "FrontEnd"

class sslprofile_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.sslprofile = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.sslprofile = [sslprofile() for _ in range(length)]

