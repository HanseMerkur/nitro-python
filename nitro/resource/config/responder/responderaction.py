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

class responderaction(base_resource) :
    """Configuration for responder action resource."""
    def __init__(self) :
        self._name = ""
        self._type = ""
        self._target = ""
        self._htmlpage = ""
        self._bypasssafetycheck = ""
        self._comment = ""
        self._responsestatuscode = 0
        self._reasonphrase = ""
        self._newname = ""
        self._hits = 0
        self._referencecount = 0
        self._undefhits = 0
        self._builtin = []
        self.___count = 0

    @property
    def name(self) :
        """Name for the responder action. Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) hash (#), space ( ), at (@), equals (=), colon (:), and underscore characters. Can be changed after the responder policy is added.
        The following requirement applies only to the NetScaler CLI:
        If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my responder action" or 'my responder action').


        """
        try :
            return self._name
        except Exception as e:
            raise e

    @name.setter
    def name(self, name) :
        """Name for the responder action. Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) hash (#), space ( ), at (@), equals (=), colon (:), and underscore characters. Can be changed after the responder policy is added.
        The following requirement applies only to the NetScaler CLI:
        If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my responder action" or 'my responder action').

        :param name: 

        """
        try :
            self._name = name
        except Exception as e:
            raise e

    @property
    def type(self) :
        """Type of responder action. Available settings function as follows:
        * respondwith <target> - Respond to the request with the expression specified as the target.
        * respondwithhtmlpage - Respond to the request with the uploaded HTML page object specified as the target.
        * redirect - Redirect the request to the URL specified as the target.
        * sqlresponse_ok - Send an SQL OK response.
        * sqlresponse_error - Send an SQL ERROR response.<br/>Possible values = noop, respondwith, redirect, respondwithhtmlpage, sqlresponse_ok, sqlresponse_error.


        """
        try :
            return self._type
        except Exception as e:
            raise e

    @type.setter
    def type(self, type) :
        """Type of responder action. Available settings function as follows:
        * respondwith <target> - Respond to the request with the expression specified as the target.
        * respondwithhtmlpage - Respond to the request with the uploaded HTML page object specified as the target.
        * redirect - Redirect the request to the URL specified as the target.
        * sqlresponse_ok - Send an SQL OK response.
        * sqlresponse_error - Send an SQL ERROR response.<br/>Possible values = noop, respondwith, redirect, respondwithhtmlpage, sqlresponse_ok, sqlresponse_error

        :param type: 

        """
        try :
            self._type = type
        except Exception as e:
            raise e

    @property
    def target(self) :
        """Expression specifying what to respond with. Typically a URL for redirect policies or a default-syntax expression.  In addition to NetScaler default-syntax expressions that refer to information in the request, a stringbuilder expression can contain text and HTML, and simple escape codes that define new lines and paragraphs. Enclose each stringbuilder expression element (either a NetScaler default-syntax expression or a string) in double quotation marks. Use the plus (+) character to join the elements.
        Examples:
        1) Respondwith expression that sends an HTTP 1.1 200 OK response:
        "HTTP/1.1 200 OK\r\n\r\n"
        2) Redirect expression that redirects user to the specified web host and appends the request URL to the redirect.
        "http://backupsite2.com" + HTTP.REQ.URL
        3) Respondwith expression that sends an HTTP 1.1 404 Not Found response with the request URL included in the response:
        "HTTP/1.1 404 Not Found\r\n\r\n"+ "HTTP.REQ.URL.HTTP_URL_SAFE" + "does not exist on the web server."
        The following requirement applies only to the NetScaler CLI:
        Enclose the entire expression in single quotation marks. (NetScaler default expression elements should be included inside the single quotation marks for the entire expression, but do not need to be enclosed in double quotation marks.).


        """
        try :
            return self._target
        except Exception as e:
            raise e

    @target.setter
    def target(self, target) :
        """Expression specifying what to respond with. Typically a URL for redirect policies or a default-syntax expression.  In addition to NetScaler default-syntax expressions that refer to information in the request, a stringbuilder expression can contain text and HTML, and simple escape codes that define new lines and paragraphs. Enclose each stringbuilder expression element (either a NetScaler default-syntax expression or a string) in double quotation marks. Use the plus (+) character to join the elements.
        Examples:
        1) Respondwith expression that sends an HTTP 1.1 200 OK response:
        "HTTP/1.1 200 OK\r\n\r\n"
        2) Redirect expression that redirects user to the specified web host and appends the request URL to the redirect.
        "http://backupsite2.com" + HTTP.REQ.URL
        3) Respondwith expression that sends an HTTP 1.1 404 Not Found response with the request URL included in the response:
        "HTTP/1.1 404 Not Found\r\n\r\n"+ "HTTP.REQ.URL.HTTP_URL_SAFE" + "does not exist on the web server."
        The following requirement applies only to the NetScaler CLI:
        Enclose the entire expression in single quotation marks. (NetScaler default expression elements should be included inside the single quotation marks for the entire expression, but do not need to be enclosed in double quotation marks.).

        :param target: 

        """
        try :
            self._target = target
        except Exception as e:
            raise e

    @property
    def htmlpage(self) :
        """For respondwithhtmlpage policies, name of the HTML page object to use as the response. You must first import the page object.<br/>Minimum length =  1."""
        try :
            return self._htmlpage
        except Exception as e:
            raise e

    @htmlpage.setter
    def htmlpage(self, htmlpage) :
        """For respondwithhtmlpage policies, name of the HTML page object to use as the response. You must first import the page object.<br/>Minimum length =  1

        :param htmlpage: 

        """
        try :
            self._htmlpage = htmlpage
        except Exception as e:
            raise e

    @property
    def bypasssafetycheck(self) :
        """Bypass the safety check, allowing potentially unsafe expressions. An unsafe expression in a response is one that contains references to request elements that might not be present in all requests. If a response refers to a missing request element, an empty string is used instead.<br/>Default value: NO<br/>Possible values = YES, NO."""
        try :
            return self._bypasssafetycheck
        except Exception as e:
            raise e

    @bypasssafetycheck.setter
    def bypasssafetycheck(self, bypasssafetycheck) :
        """Bypass the safety check, allowing potentially unsafe expressions. An unsafe expression in a response is one that contains references to request elements that might not be present in all requests. If a response refers to a missing request element, an empty string is used instead.<br/>Default value: NO<br/>Possible values = YES, NO

        :param bypasssafetycheck: 

        """
        try :
            self._bypasssafetycheck = bypasssafetycheck
        except Exception as e:
            raise e

    @property
    def comment(self) :
        """Comment. Any type of information about this responder action."""
        try :
            return self._comment
        except Exception as e:
            raise e

    @comment.setter
    def comment(self, comment) :
        """Comment. Any type of information about this responder action.

        :param comment: 

        """
        try :
            self._comment = comment
        except Exception as e:
            raise e

    @property
    def responsestatuscode(self) :
        """HTTP response status code, for example 200, 302, 404, etc. The default value for the redirect action type is 302 and for respondwithhtmlpage is 200.<br/>Minimum length =  100<br/>Maximum length =  599."""
        try :
            return self._responsestatuscode
        except Exception as e:
            raise e

    @responsestatuscode.setter
    def responsestatuscode(self, responsestatuscode) :
        """HTTP response status code, for example 200, 302, 404, etc. The default value for the redirect action type is 302 and for respondwithhtmlpage is 200.<br/>Minimum length =  100<br/>Maximum length =  599

        :param responsestatuscode: 

        """
        try :
            self._responsestatuscode = responsestatuscode
        except Exception as e:
            raise e

    @property
    def reasonphrase(self) :
        """Expression specifying the reason phrase of the HTTP response. The reason phrase may be a string literal with quotes or a PI expression. For example: "Invalid URL: " + HTTP.REQ.URL."""
        try :
            return self._reasonphrase
        except Exception as e:
            raise e

    @reasonphrase.setter
    def reasonphrase(self, reasonphrase) :
        """Expression specifying the reason phrase of the HTTP response. The reason phrase may be a string literal with quotes or a PI expression. For example: "Invalid URL: " + HTTP.REQ.URL.

        :param reasonphrase: 

        """
        try :
            self._reasonphrase = reasonphrase
        except Exception as e:
            raise e

    @property
    def newname(self) :
        """New name for the responder action.
        Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) hash (#), space ( ), at (@), equals (=), colon (:), and underscore characters.
        The following requirement applies only to the NetScaler CLI:
        If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my responder action" or my responder action').<br/>Minimum length =  1.


        """
        try :
            return self._newname
        except Exception as e:
            raise e

    @newname.setter
    def newname(self, newname) :
        """New name for the responder action.
        Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) hash (#), space ( ), at (@), equals (=), colon (:), and underscore characters.
        The following requirement applies only to the NetScaler CLI:
        If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my responder action" or my responder action').<br/>Minimum length =  1

        :param newname: 

        """
        try :
            self._newname = newname
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
    def referencecount(self) :
        """The number of references to the action."""
        try :
            return self._referencecount
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
    def builtin(self) :
        """Flag to determine whether responder action is built-in or not.<br/>Possible values = MODIFIABLE, DELETABLE, IMMUTABLE, PARTITION_ALL."""
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
            result = service.payload_formatter.string_to_resource(responderaction_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.responderaction
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
        """Use this API to add responderaction.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                addresource = responderaction()
                addresource.name = resource.name
                addresource.type = resource.type
                addresource.target = resource.target
                addresource.htmlpage = resource.htmlpage
                addresource.bypasssafetycheck = resource.bypasssafetycheck
                addresource.comment = resource.comment
                addresource.responsestatuscode = resource.responsestatuscode
                addresource.reasonphrase = resource.reasonphrase
                return addresource.add_resource(client)
            else :
                if (resource and len(resource) > 0) :
                    addresources = [ responderaction() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        addresources[i].name = resource[i].name
                        addresources[i].type = resource[i].type
                        addresources[i].target = resource[i].target
                        addresources[i].htmlpage = resource[i].htmlpage
                        addresources[i].bypasssafetycheck = resource[i].bypasssafetycheck
                        addresources[i].comment = resource[i].comment
                        addresources[i].responsestatuscode = resource[i].responsestatuscode
                        addresources[i].reasonphrase = resource[i].reasonphrase
                result = cls.add_bulk_request(client, addresources)
            return result
        except Exception as e :
            raise e

    @classmethod
    def delete(cls, client, resource) :
        """Use this API to delete responderaction.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                deleteresource = responderaction()
                if type(resource) !=  type(deleteresource):
                    deleteresource.name = resource
                else :
                    deleteresource.name = resource.name
                return deleteresource.delete_resource(client)
            else :
                if type(resource[0]) != cls :
                    if (resource and len(resource) > 0) :
                        deleteresources = [ responderaction() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            deleteresources[i].name = resource[i]
                else :
                    if (resource and len(resource) > 0) :
                        deleteresources = [ responderaction() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            deleteresources[i].name = resource[i].name
                result = cls.delete_bulk_request(client, deleteresources)
            return result
        except Exception as e :
            raise e

    @classmethod
    def update(cls, client, resource) :
        """Use this API to update responderaction.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                updateresource = responderaction()
                updateresource.name = resource.name
                updateresource.target = resource.target
                updateresource.bypasssafetycheck = resource.bypasssafetycheck
                updateresource.htmlpage = resource.htmlpage
                updateresource.responsestatuscode = resource.responsestatuscode
                updateresource.reasonphrase = resource.reasonphrase
                updateresource.comment = resource.comment
                return updateresource.update_resource(client)
            else :
                if (resource and len(resource) > 0) :
                    updateresources = [ responderaction() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        updateresources[i].name = resource[i].name
                        updateresources[i].target = resource[i].target
                        updateresources[i].bypasssafetycheck = resource[i].bypasssafetycheck
                        updateresources[i].htmlpage = resource[i].htmlpage
                        updateresources[i].responsestatuscode = resource[i].responsestatuscode
                        updateresources[i].reasonphrase = resource[i].reasonphrase
                        updateresources[i].comment = resource[i].comment
                result = cls.update_bulk_request(client, updateresources)
            return result
        except Exception as e :
            raise e

    @classmethod
    def unset(cls, client, resource, args) :
        """Use this API to unset the properties of responderaction resource.
        Properties that need to be unset are specified in args array.

        :param client: 
        :param resource: 
        :param args: 

        """
        try :
            if type(resource) is not list :
                unsetresource = responderaction()
                if type(resource) !=  type(unsetresource):
                    unsetresource.name = resource
                else :
                    unsetresource.name = resource.name
                return unsetresource.unset_resource(client, args)
            else :
                if type(resource[0]) != cls :
                    if (resource and len(resource) > 0) :
                        unsetresources = [ responderaction() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            unsetresources[i].name = resource[i]
                else :
                    if (resource and len(resource) > 0) :
                        unsetresources = [ responderaction() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            unsetresources[i].name = resource[i].name
                result = cls.unset_bulk_request(client, unsetresources, args)
            return result
        except Exception as e :
            raise e

    @classmethod
    def rename(cls, client, resource, new_name) :
        """Use this API to rename a responderaction resource.

        :param client: 
        :param resource: 
        :param new_name: 

        """
        try :
            renameresource = responderaction()
            if type(resource) == cls :
                renameresource.name = resource.name
            else :
                renameresource.name = resource
            return renameresource.rename_resource(client,new_name)
        except Exception as e :
            raise e

    @classmethod
    def get(cls, client, name="", option_="") :
        """Use this API to fetch all the responderaction resources that are configured on netscaler.

        :param client: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            if not name :
                obj = responderaction()
                response = obj.get_resources(client, option_)
            else :
                if type(name) != cls :
                    if type(name) is not list :
                        obj = responderaction()
                        obj.name = name
                        response = obj.get_resource(client, option_)
                    else :
                        if name and len(name) > 0 :
                            response = [responderaction() for _ in range(len(name))]
                            obj = [responderaction() for _ in range(len(name))]
                            for i in range(len(name)) :
                                obj[i] = responderaction()
                                obj[i].name = name[i]
                                response[i] = obj[i].get_resource(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def get_filtered(cls, client, filter_) :
        """Use this API to fetch filtered set of responderaction resources.
        filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = responderaction()
            option_ = options()
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def count(cls, client) :
        """Use this API to count the responderaction resources configured on NetScaler.

        :param client: 

        """
        try :
            obj = responderaction()
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
        """Use this API to count filtered the set of responderaction resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = responderaction()
            option_ = options()
            option_.count = True
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            if response :
                return response[0].__dict__['___count']
            return 0
        except Exception as e :
            raise e


    class Builtin:
        """ """
        MODIFIABLE = "MODIFIABLE"
        DELETABLE = "DELETABLE"
        IMMUTABLE = "IMMUTABLE"
        PARTITION_ALL = "PARTITION_ALL"

    class Type:
        """ """
        noop = "noop"
        respondwith = "respondwith"
        redirect = "redirect"
        respondwithhtmlpage = "respondwithhtmlpage"
        sqlresponse_ok = "sqlresponse_ok"
        sqlresponse_error = "sqlresponse_error"

    class Bypasssafetycheck:
        """ """
        YES = "YES"
        NO = "NO"

class responderaction_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.responderaction = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.responderaction = [responderaction() for _ in range(length)]

