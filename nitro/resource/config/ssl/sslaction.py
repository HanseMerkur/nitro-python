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

class sslaction(base_resource) :
    """Configuration for SSL action resource."""
    def __init__(self) :
        self._name = ""
        self._clientauth = ""
        self._clientcert = ""
        self._certheader = ""
        self._clientcertserialnumber = ""
        self._certserialheader = ""
        self._clientcertsubject = ""
        self._certsubjectheader = ""
        self._clientcerthash = ""
        self._certhashheader = ""
        self._clientcertissuer = ""
        self._certissuerheader = ""
        self._sessionid = ""
        self._sessionidheader = ""
        self._cipher = ""
        self._cipherheader = ""
        self._clientcertnotbefore = ""
        self._certnotbeforeheader = ""
        self._clientcertnotafter = ""
        self._certnotafterheader = ""
        self._owasupport = ""
        self._hits = 0
        self._undefhits = 0
        self._referencecount = 0
        self._description = ""
        self._builtin = []
        self.___count = 0

    @property
    def name(self) :
        """Name for the SSL action. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the action is created.
        The following requirement applies only to the NetScaler CLI:
        If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my action" or 'my action').<br/>Minimum length =  1.


        """
        try :
            return self._name
        except Exception as e:
            raise e

    @name.setter
    def name(self, name) :
        """Name for the SSL action. Must begin with an ASCII alphanumeric or underscore (_) character, and must contain only ASCII alphanumeric, underscore, hash (#), period (.), space, colon (:), at (@), equals (=), and hyphen (-) characters. Cannot be changed after the action is created.
        The following requirement applies only to the NetScaler CLI:
        If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my action" or 'my action').<br/>Minimum length =  1

        :param name: 

        """
        try :
            self._name = name
        except Exception as e:
            raise e

    @property
    def clientauth(self) :
        """Perform client certificate authentication.<br/>Possible values = DOCLIENTAUTH, NOCLIENTAUTH."""
        try :
            return self._clientauth
        except Exception as e:
            raise e

    @clientauth.setter
    def clientauth(self, clientauth) :
        """Perform client certificate authentication.<br/>Possible values = DOCLIENTAUTH, NOCLIENTAUTH

        :param clientauth: 

        """
        try :
            self._clientauth = clientauth
        except Exception as e:
            raise e

    @property
    def clientcert(self) :
        """Insert the entire client certificate into the HTTP header of the request being sent to the web server. The certificate is inserted in ASCII (PEM) format.<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._clientcert
        except Exception as e:
            raise e

    @clientcert.setter
    def clientcert(self, clientcert) :
        """Insert the entire client certificate into the HTTP header of the request being sent to the web server. The certificate is inserted in ASCII (PEM) format.<br/>Possible values = ENABLED, DISABLED

        :param clientcert: 

        """
        try :
            self._clientcert = clientcert
        except Exception as e:
            raise e

    @property
    def certheader(self) :
        """Name of the header into which to insert the client certificate."""
        try :
            return self._certheader
        except Exception as e:
            raise e

    @certheader.setter
    def certheader(self, certheader) :
        """Name of the header into which to insert the client certificate.

        :param certheader: 

        """
        try :
            self._certheader = certheader
        except Exception as e:
            raise e

    @property
    def clientcertserialnumber(self) :
        """Insert the entire client serial number into the HTTP header of the request being sent to the web server.<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._clientcertserialnumber
        except Exception as e:
            raise e

    @clientcertserialnumber.setter
    def clientcertserialnumber(self, clientcertserialnumber) :
        """Insert the entire client serial number into the HTTP header of the request being sent to the web server.<br/>Possible values = ENABLED, DISABLED

        :param clientcertserialnumber: 

        """
        try :
            self._clientcertserialnumber = clientcertserialnumber
        except Exception as e:
            raise e

    @property
    def certserialheader(self) :
        """Name of the header into which to insert the client serial number."""
        try :
            return self._certserialheader
        except Exception as e:
            raise e

    @certserialheader.setter
    def certserialheader(self, certserialheader) :
        """Name of the header into which to insert the client serial number.

        :param certserialheader: 

        """
        try :
            self._certserialheader = certserialheader
        except Exception as e:
            raise e

    @property
    def clientcertsubject(self) :
        """Insert the client certificate subject, also known as the distinguished name (DN), into the HTTP header of the request being sent to the web server.<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._clientcertsubject
        except Exception as e:
            raise e

    @clientcertsubject.setter
    def clientcertsubject(self, clientcertsubject) :
        """Insert the client certificate subject, also known as the distinguished name (DN), into the HTTP header of the request being sent to the web server.<br/>Possible values = ENABLED, DISABLED

        :param clientcertsubject: 

        """
        try :
            self._clientcertsubject = clientcertsubject
        except Exception as e:
            raise e

    @property
    def certsubjectheader(self) :
        """Name of the header into which to insert the client certificate subject."""
        try :
            return self._certsubjectheader
        except Exception as e:
            raise e

    @certsubjectheader.setter
    def certsubjectheader(self, certsubjectheader) :
        """Name of the header into which to insert the client certificate subject.

        :param certsubjectheader: 

        """
        try :
            self._certsubjectheader = certsubjectheader
        except Exception as e:
            raise e

    @property
    def clientcerthash(self) :
        """Insert the certificate signature (hash) into the HTTP header of the request being sent to the web server.<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._clientcerthash
        except Exception as e:
            raise e

    @clientcerthash.setter
    def clientcerthash(self, clientcerthash) :
        """Insert the certificate signature (hash) into the HTTP header of the request being sent to the web server.<br/>Possible values = ENABLED, DISABLED

        :param clientcerthash: 

        """
        try :
            self._clientcerthash = clientcerthash
        except Exception as e:
            raise e

    @property
    def certhashheader(self) :
        """Name of the header into which to insert the client certificate signature (hash)."""
        try :
            return self._certhashheader
        except Exception as e:
            raise e

    @certhashheader.setter
    def certhashheader(self, certhashheader) :
        """Name of the header into which to insert the client certificate signature (hash).

        :param certhashheader: 

        """
        try :
            self._certhashheader = certhashheader
        except Exception as e:
            raise e

    @property
    def clientcertissuer(self) :
        """Insert the certificate issuer details into the HTTP header of the request being sent to the web server.<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._clientcertissuer
        except Exception as e:
            raise e

    @clientcertissuer.setter
    def clientcertissuer(self, clientcertissuer) :
        """Insert the certificate issuer details into the HTTP header of the request being sent to the web server.<br/>Possible values = ENABLED, DISABLED

        :param clientcertissuer: 

        """
        try :
            self._clientcertissuer = clientcertissuer
        except Exception as e:
            raise e

    @property
    def certissuerheader(self) :
        """Name of the header into which to insert the client certificate issuer details."""
        try :
            return self._certissuerheader
        except Exception as e:
            raise e

    @certissuerheader.setter
    def certissuerheader(self, certissuerheader) :
        """Name of the header into which to insert the client certificate issuer details.

        :param certissuerheader: 

        """
        try :
            self._certissuerheader = certissuerheader
        except Exception as e:
            raise e

    @property
    def sessionid(self) :
        """Insert the SSL session ID into the HTTP header of the request being sent to the web server. Every SSL connection that the client and the NetScaler share has a unique ID that identifies the specific connection.<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._sessionid
        except Exception as e:
            raise e

    @sessionid.setter
    def sessionid(self, sessionid) :
        """Insert the SSL session ID into the HTTP header of the request being sent to the web server. Every SSL connection that the client and the NetScaler share has a unique ID that identifies the specific connection.<br/>Possible values = ENABLED, DISABLED

        :param sessionid: 

        """
        try :
            self._sessionid = sessionid
        except Exception as e:
            raise e

    @property
    def sessionidheader(self) :
        """Name of the header into which to insert the Session ID."""
        try :
            return self._sessionidheader
        except Exception as e:
            raise e

    @sessionidheader.setter
    def sessionidheader(self, sessionidheader) :
        """Name of the header into which to insert the Session ID.

        :param sessionidheader: 

        """
        try :
            self._sessionidheader = sessionidheader
        except Exception as e:
            raise e

    @property
    def cipher(self) :
        """Insert the cipher suite that the client and the NetScaler appliance negotiated for the SSL session into the HTTP header of the request being sent to the web server. The appliance inserts the cipher-suite name, SSL protocol, export or non-export string, and cipher strength bit, depending on the type of browser connecting to the SSL virtual server or service (for example, Cipher-Suite: RC4- MD5 SSLv3 Non-Export 128-bit).<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._cipher
        except Exception as e:
            raise e

    @cipher.setter
    def cipher(self, cipher) :
        """Insert the cipher suite that the client and the NetScaler appliance negotiated for the SSL session into the HTTP header of the request being sent to the web server. The appliance inserts the cipher-suite name, SSL protocol, export or non-export string, and cipher strength bit, depending on the type of browser connecting to the SSL virtual server or service (for example, Cipher-Suite: RC4- MD5 SSLv3 Non-Export 128-bit).<br/>Possible values = ENABLED, DISABLED

        :param cipher: 

        """
        try :
            self._cipher = cipher
        except Exception as e:
            raise e

    @property
    def cipherheader(self) :
        """Name of the header into which to insert the name of the cipher suite."""
        try :
            return self._cipherheader
        except Exception as e:
            raise e

    @cipherheader.setter
    def cipherheader(self, cipherheader) :
        """Name of the header into which to insert the name of the cipher suite.

        :param cipherheader: 

        """
        try :
            self._cipherheader = cipherheader
        except Exception as e:
            raise e

    @property
    def clientcertnotbefore(self) :
        """Insert the date from which the certificate is valid into the HTTP header of the request being sent to the web server. Every certificate is configured with the date and time from which it is valid.<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._clientcertnotbefore
        except Exception as e:
            raise e

    @clientcertnotbefore.setter
    def clientcertnotbefore(self, clientcertnotbefore) :
        """Insert the date from which the certificate is valid into the HTTP header of the request being sent to the web server. Every certificate is configured with the date and time from which it is valid.<br/>Possible values = ENABLED, DISABLED

        :param clientcertnotbefore: 

        """
        try :
            self._clientcertnotbefore = clientcertnotbefore
        except Exception as e:
            raise e

    @property
    def certnotbeforeheader(self) :
        """Name of the header into which to insert the date and time from which the certificate is valid."""
        try :
            return self._certnotbeforeheader
        except Exception as e:
            raise e

    @certnotbeforeheader.setter
    def certnotbeforeheader(self, certnotbeforeheader) :
        """Name of the header into which to insert the date and time from which the certificate is valid.

        :param certnotbeforeheader: 

        """
        try :
            self._certnotbeforeheader = certnotbeforeheader
        except Exception as e:
            raise e

    @property
    def clientcertnotafter(self) :
        """Insert the date of expiry of the certificate into the HTTP header of the request being sent to the web server. Every certificate is configured with the date and time at which the certificate expires.<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._clientcertnotafter
        except Exception as e:
            raise e

    @clientcertnotafter.setter
    def clientcertnotafter(self, clientcertnotafter) :
        """Insert the date of expiry of the certificate into the HTTP header of the request being sent to the web server. Every certificate is configured with the date and time at which the certificate expires.<br/>Possible values = ENABLED, DISABLED

        :param clientcertnotafter: 

        """
        try :
            self._clientcertnotafter = clientcertnotafter
        except Exception as e:
            raise e

    @property
    def certnotafterheader(self) :
        """Name of the header into which to insert the certificate's expiry date."""
        try :
            return self._certnotafterheader
        except Exception as e:
            raise e

    @certnotafterheader.setter
    def certnotafterheader(self, certnotafterheader) :
        """Name of the header into which to insert the certificate's expiry date.

        :param certnotafterheader: 

        """
        try :
            self._certnotafterheader = certnotafterheader
        except Exception as e:
            raise e

    @property
    def owasupport(self) :
        """If the appliance is in front of an Outlook Web Access (OWA) server, insert a special header field, FRONT-END-HTTPS: ON, into the HTTP requests going to the OWA server. This header communicates to the server that the transaction is HTTPS and not HTTP.<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._owasupport
        except Exception as e:
            raise e

    @owasupport.setter
    def owasupport(self, owasupport) :
        """If the appliance is in front of an Outlook Web Access (OWA) server, insert a special header field, FRONT-END-HTTPS: ON, into the HTTP requests going to the OWA server. This header communicates to the server that the transaction is HTTPS and not HTTP.<br/>Possible values = ENABLED, DISABLED

        :param owasupport: 

        """
        try :
            self._owasupport = owasupport
        except Exception as e:
            raise e

    @property
    def hits(self) :
        """The number of times the action has been taken."""
        try :
            return self._hits
        except Exception as e:
            raise e

    @property
    def undefhits(self) :
        """The number of times the action resulted in UNDEF."""
        try :
            return self._undefhits
        except Exception as e:
            raise e

    @property
    def referencecount(self) :
        """The number of references to the action."""
        try :
            return self._referencecount
        except Exception as e:
            raise e

    @property
    def description(self) :
        """Description of the action."""
        try :
            return self._description
        except Exception as e:
            raise e

    @property
    def builtin(self) :
        """Flag to determine whether ssl action is built-in or not.<br/>Possible values = MODIFIABLE, DELETABLE, IMMUTABLE, PARTITION_ALL."""
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
            result = service.payload_formatter.string_to_resource(sslaction_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.sslaction
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
        """Use this API to add sslaction.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                addresource = sslaction()
                addresource.name = resource.name
                addresource.clientauth = resource.clientauth
                addresource.clientcert = resource.clientcert
                addresource.certheader = resource.certheader
                addresource.clientcertserialnumber = resource.clientcertserialnumber
                addresource.certserialheader = resource.certserialheader
                addresource.clientcertsubject = resource.clientcertsubject
                addresource.certsubjectheader = resource.certsubjectheader
                addresource.clientcerthash = resource.clientcerthash
                addresource.certhashheader = resource.certhashheader
                addresource.clientcertissuer = resource.clientcertissuer
                addresource.certissuerheader = resource.certissuerheader
                addresource.sessionid = resource.sessionid
                addresource.sessionidheader = resource.sessionidheader
                addresource.cipher = resource.cipher
                addresource.cipherheader = resource.cipherheader
                addresource.clientcertnotbefore = resource.clientcertnotbefore
                addresource.certnotbeforeheader = resource.certnotbeforeheader
                addresource.clientcertnotafter = resource.clientcertnotafter
                addresource.certnotafterheader = resource.certnotafterheader
                addresource.owasupport = resource.owasupport
                return addresource.add_resource(client)
            else :
                if (resource and len(resource) > 0) :
                    addresources = [ sslaction() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        addresources[i].name = resource[i].name
                        addresources[i].clientauth = resource[i].clientauth
                        addresources[i].clientcert = resource[i].clientcert
                        addresources[i].certheader = resource[i].certheader
                        addresources[i].clientcertserialnumber = resource[i].clientcertserialnumber
                        addresources[i].certserialheader = resource[i].certserialheader
                        addresources[i].clientcertsubject = resource[i].clientcertsubject
                        addresources[i].certsubjectheader = resource[i].certsubjectheader
                        addresources[i].clientcerthash = resource[i].clientcerthash
                        addresources[i].certhashheader = resource[i].certhashheader
                        addresources[i].clientcertissuer = resource[i].clientcertissuer
                        addresources[i].certissuerheader = resource[i].certissuerheader
                        addresources[i].sessionid = resource[i].sessionid
                        addresources[i].sessionidheader = resource[i].sessionidheader
                        addresources[i].cipher = resource[i].cipher
                        addresources[i].cipherheader = resource[i].cipherheader
                        addresources[i].clientcertnotbefore = resource[i].clientcertnotbefore
                        addresources[i].certnotbeforeheader = resource[i].certnotbeforeheader
                        addresources[i].clientcertnotafter = resource[i].clientcertnotafter
                        addresources[i].certnotafterheader = resource[i].certnotafterheader
                        addresources[i].owasupport = resource[i].owasupport
                result = cls.add_bulk_request(client, addresources)
            return result
        except Exception as e :
            raise e

    @classmethod
    def delete(cls, client, resource) :
        """Use this API to delete sslaction.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                deleteresource = sslaction()
                if type(resource) !=  type(deleteresource):
                    deleteresource.name = resource
                else :
                    deleteresource.name = resource.name
                return deleteresource.delete_resource(client)
            else :
                if type(resource[0]) != cls :
                    if (resource and len(resource) > 0) :
                        deleteresources = [ sslaction() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            deleteresources[i].name = resource[i]
                else :
                    if (resource and len(resource) > 0) :
                        deleteresources = [ sslaction() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            deleteresources[i].name = resource[i].name
                result = cls.delete_bulk_request(client, deleteresources)
            return result
        except Exception as e :
            raise e

    @classmethod
    def get(cls, client, name="", option_="") :
        """Use this API to fetch all the sslaction resources that are configured on netscaler.

        :param client: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            if not name :
                obj = sslaction()
                response = obj.get_resources(client, option_)
            else :
                if type(name) != cls :
                    if type(name) is not list :
                        obj = sslaction()
                        obj.name = name
                        response = obj.get_resource(client, option_)
                    else :
                        if name and len(name) > 0 :
                            response = [sslaction() for _ in range(len(name))]
                            obj = [sslaction() for _ in range(len(name))]
                            for i in range(len(name)) :
                                obj[i] = sslaction()
                                obj[i].name = name[i]
                                response[i] = obj[i].get_resource(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def get_filtered(cls, client, filter_) :
        """Use this API to fetch filtered set of sslaction resources.
        filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = sslaction()
            option_ = options()
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def count(cls, client) :
        """Use this API to count the sslaction resources configured on NetScaler.

        :param client: 

        """
        try :
            obj = sslaction()
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
        """Use this API to count filtered the set of sslaction resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = sslaction()
            option_ = options()
            option_.count = True
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            if response :
                return response[0].__dict__['___count']
            return 0
        except Exception as e :
            raise e


    class Clientcertnotafter:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Builtin:
        """ """
        MODIFIABLE = "MODIFIABLE"
        DELETABLE = "DELETABLE"
        IMMUTABLE = "IMMUTABLE"
        PARTITION_ALL = "PARTITION_ALL"

    class Owasupport:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Clientcertsubject:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Clientcertissuer:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Clientcertnotbefore:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Clientcertserialnumber:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Cipher:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Clientcert:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Clientcerthash:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Clientauth:
        """ """
        DOCLIENTAUTH = "DOCLIENTAUTH"
        NOCLIENTAUTH = "NOCLIENTAUTH"

    class Sessionid:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

class sslaction_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.sslaction = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.sslaction = [sslaction() for _ in range(length)]

