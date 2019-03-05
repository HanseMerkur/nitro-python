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

class nsextension(base_resource) :
    """Configuration for Extension resource."""
    def __init__(self) :
        self._src = ""
        self._name = ""
        self._comment = ""
        self._overwrite = False
        self._trace = ""
        self._tracefunctions = ""
        self._tracevariables = ""
        self._detail = ""
        self._type = ""
        self._functionhits = 0
        self._functionundefhits = 0
        self._functionhaltcount = 0
        self.___count = 0

    @property
    def src(self) :
        """Local path to and name of, or URL (protocol, host, path, and file name) for, the file in which to store the imported extension.
        NOTE: The import fails if the object to be imported is on an HTTPS server that requires client certificate authentication for access.<br/>Minimum length =  1<br/>Maximum length =  2047.


        """
        try :
            return self._src
        except Exception as e:
            raise e

    @src.setter
    def src(self, src) :
        """Local path to and name of, or URL (protocol, host, path, and file name) for, the file in which to store the imported extension.
        NOTE: The import fails if the object to be imported is on an HTTPS server that requires client certificate authentication for access.<br/>Minimum length =  1<br/>Maximum length =  2047

        :param src: 

        """
        try :
            self._src = src
        except Exception as e:
            raise e

    @property
    def name(self) :
        """Name to assign to the extension object on the NetScaler appliance.<br/>Minimum length =  1<br/>Maximum length =  31."""
        try :
            return self._name
        except Exception as e:
            raise e

    @name.setter
    def name(self, name) :
        """Name to assign to the extension object on the NetScaler appliance.<br/>Minimum length =  1<br/>Maximum length =  31

        :param name: 

        """
        try :
            self._name = name
        except Exception as e:
            raise e

    @property
    def comment(self) :
        """Any comments to preserve information about the extension object.<br/>Maximum length =  128."""
        try :
            return self._comment
        except Exception as e:
            raise e

    @comment.setter
    def comment(self, comment) :
        """Any comments to preserve information about the extension object.<br/>Maximum length =  128

        :param comment: 

        """
        try :
            self._comment = comment
        except Exception as e:
            raise e

    @property
    def overwrite(self) :
        """Overwrites the existing file."""
        try :
            return self._overwrite
        except Exception as e:
            raise e

    @overwrite.setter
    def overwrite(self, overwrite) :
        """Overwrites the existing file.

        :param overwrite: 

        """
        try :
            self._overwrite = overwrite
        except Exception as e:
            raise e

    @property
    def trace(self) :
        """Enables tracing to the NS log file of extension execution:
        off   - turns off tracing (equivalent to unset ns extension <extension-name> -trace)
        calls - traces extension function calls with arguments and function returns with the first return value
        lines - traces the above plus line numbers for executed extension lines
        all   - traces the above plus local variables changed by executed extension lines
        Note that the DEBUG log level must be enabled to see extension tracing.
        This can be done by set audit syslogParams -loglevel ALL or -loglevel DEBUG.<br/>Default value: off<br/>Possible values = off, calls, lines, all.


        """
        try :
            return self._trace
        except Exception as e:
            raise e

    @trace.setter
    def trace(self, trace) :
        """Enables tracing to the NS log file of extension execution:
        off   - turns off tracing (equivalent to unset ns extension <extension-name> -trace)
        calls - traces extension function calls with arguments and function returns with the first return value
        lines - traces the above plus line numbers for executed extension lines
        all   - traces the above plus local variables changed by executed extension lines
        Note that the DEBUG log level must be enabled to see extension tracing.
        This can be done by set audit syslogParams -loglevel ALL or -loglevel DEBUG.<br/>Default value: off<br/>Possible values = off, calls, lines, all

        :param trace: 

        """
        try :
            self._trace = trace
        except Exception as e:
            raise e

    @property
    def tracefunctions(self) :
        """Comma-separated list of extension functions to trace. By default, all extension functions are traced.<br/>Maximum length =  256."""
        try :
            return self._tracefunctions
        except Exception as e:
            raise e

    @tracefunctions.setter
    def tracefunctions(self, tracefunctions) :
        """Comma-separated list of extension functions to trace. By default, all extension functions are traced.<br/>Maximum length =  256

        :param tracefunctions: 

        """
        try :
            self._tracefunctions = tracefunctions
        except Exception as e:
            raise e

    @property
    def tracevariables(self) :
        """Comma-separated list of variables (in traced extension functions) to trace. By default, all variables are traced.<br/>Maximum length =  256."""
        try :
            return self._tracevariables
        except Exception as e:
            raise e

    @tracevariables.setter
    def tracevariables(self, tracevariables) :
        """Comma-separated list of variables (in traced extension functions) to trace. By default, all variables are traced.<br/>Maximum length =  256

        :param tracevariables: 

        """
        try :
            self._tracevariables = tracevariables
        except Exception as e:
            raise e

    @property
    def detail(self) :
        """Show detail for extension function.<br/>Possible values = brief, all."""
        try :
            return self._detail
        except Exception as e:
            raise e

    @detail.setter
    def detail(self, detail) :
        """Show detail for extension function.<br/>Possible values = brief, all

        :param detail: 

        """
        try :
            self._detail = detail
        except Exception as e:
            raise e

    @property
    def type(self) :
        """.<br/>Possible values = WSDL, CustomSettings, XMLSchema, XMLErrorPage, htmlpage, CustomResp, Extension."""
        try :
            return self._type
        except Exception as e:
            raise e

    @property
    def functionhits(self) :
        """Number of time function evaluates successfully."""
        try :
            return self._functionhits
        except Exception as e:
            raise e

    @property
    def functionundefhits(self) :
        """Number of times error occured in evaluating extension function."""
        try :
            return self._functionundefhits
        except Exception as e:
            raise e

    @property
    def functionhaltcount(self) :
        """Number of time function evaluation is halted."""
        try :
            return self._functionhaltcount
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(nsextension_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.nsextension
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
    def Import(cls, client, resource) :
        """Use this API to Import nsextension.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                Importresource = nsextension()
                Importresource.src = resource.src
                Importresource.name = resource.name
                Importresource.comment = resource.comment
                Importresource.overwrite = resource.overwrite
                return Importresource.perform_operation(client,"Import")
            else :
                if (resource and len(resource) > 0) :
                    Importresources = [ nsextension() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        Importresources[i].src = resource[i].src
                        Importresources[i].name = resource[i].name
                        Importresources[i].comment = resource[i].comment
                        Importresources[i].overwrite = resource[i].overwrite
                result = cls.perform_operation_bulk_request(client, Importresources,"Import")
            return result
        except Exception as e :
            raise e

    @classmethod
    def delete(cls, client, resource) :
        """Use this API to delete nsextension.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                deleteresource = nsextension()
                if type(resource) !=  type(deleteresource):
                    deleteresource.name = resource
                else :
                    deleteresource.name = resource.name
                return deleteresource.delete_resource(client)
            else :
                if type(resource[0]) != cls :
                    if (resource and len(resource) > 0) :
                        deleteresources = [ nsextension() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            deleteresources[i].name = resource[i]
                else :
                    if (resource and len(resource) > 0) :
                        deleteresources = [ nsextension() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            deleteresources[i].name = resource[i].name
                result = cls.delete_bulk_request(client, deleteresources)
            return result
        except Exception as e :
            raise e

    @classmethod
    def add(cls, client, resource) :
        """Use this API to add nsextension.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                addresource = nsextension()
                addresource.name = resource.name
                addresource.comment = resource.comment
                return addresource.add_resource(client)
            else :
                if (resource and len(resource) > 0) :
                    addresources = [ nsextension() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        addresources[i].name = resource[i].name
                        addresources[i].comment = resource[i].comment
                result = cls.add_bulk_request(client, addresources)
            return result
        except Exception as e :
            raise e

    @classmethod
    def change(cls, client, resource) :
        """Use this API to change nsextension.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                changeresource = nsextension()
                changeresource.name = resource.name
                return changeresource.perform_operation(client,"update")
            else :
                if (resource and len(resource) > 0) :
                    changeresources = [ nsextension() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        changeresources[i].name = resource[i].name
                result = cls.perform_operation_bulk_request(client, changeresources,"update")
            return result
        except Exception as e :
            raise e

    @classmethod
    def update(cls, client, resource) :
        """Use this API to update nsextension.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                updateresource = nsextension()
                updateresource.name = resource.name
                updateresource.trace = resource.trace
                updateresource.tracefunctions = resource.tracefunctions
                updateresource.tracevariables = resource.tracevariables
                updateresource.comment = resource.comment
                return updateresource.update_resource(client)
            else :
                if (resource and len(resource) > 0) :
                    updateresources = [ nsextension() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        updateresources[i].name = resource[i].name
                        updateresources[i].trace = resource[i].trace
                        updateresources[i].tracefunctions = resource[i].tracefunctions
                        updateresources[i].tracevariables = resource[i].tracevariables
                        updateresources[i].comment = resource[i].comment
                result = cls.update_bulk_request(client, updateresources)
            return result
        except Exception as e :
            raise e

    @classmethod
    def unset(cls, client, resource, args) :
        """Use this API to unset the properties of nsextension resource.
        Properties that need to be unset are specified in args array.

        :param client: 
        :param resource: 
        :param args: 

        """
        try :
            if type(resource) is not list :
                unsetresource = nsextension()
                if type(resource) !=  type(unsetresource):
                    unsetresource.name = resource
                else :
                    unsetresource.name = resource.name
                return unsetresource.unset_resource(client, args)
            else :
                if type(resource[0]) != cls :
                    if (resource and len(resource) > 0) :
                        unsetresources = [ nsextension() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            unsetresources[i].name = resource[i]
                else :
                    if (resource and len(resource) > 0) :
                        unsetresources = [ nsextension() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            unsetresources[i].name = resource[i].name
                result = cls.unset_bulk_request(client, unsetresources, args)
            return result
        except Exception as e :
            raise e

    @classmethod
    def get(cls, client, name="", option_="") :
        """Use this API to fetch all the nsextension resources that are configured on netscaler.

        :param client: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            if not name :
                obj = nsextension()
                response = obj.get_resources(client, option_)
            else :
                if type(name) != cls :
                    if type(name) is not list :
                        obj = nsextension()
                        obj.name = name
                        response = obj.get_resource(client, option_)
                    else :
                        if name and len(name) > 0 :
                            response = [nsextension() for _ in range(len(name))]
                            obj = [nsextension() for _ in range(len(name))]
                            for i in range(len(name)) :
                                obj[i] = nsextension()
                                obj[i].name = name[i]
                                response[i] = obj[i].get_resource(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def get_args(cls, client, args) :
        """Use this API to fetch all the nsextension resources that are configured on netscaler.
            # This uses nsextension_args which is a way to provide additional arguments while fetching the resources.

        :param client: 
        :param args: 

        """
        try :
            obj = nsextension()
            option_ = options()
            option_.args = nitro_util.object_to_string_withoutquotes(args)
            response = obj.get_resources(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def get_filtered(cls, client, filter_) :
        """Use this API to fetch filtered set of nsextension resources.
        filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = nsextension()
            option_ = options()
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def count(cls, client) :
        """Use this API to count the nsextension resources configured on NetScaler.

        :param client: 

        """
        try :
            obj = nsextension()
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
        """Use this API to count filtered the set of nsextension resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = nsextension()
            option_ = options()
            option_.count = True
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            if response :
                return response[0].__dict__['___count']
            return 0
        except Exception as e :
            raise e


    class Trace:
        """ """
        off = "off"
        calls = "calls"
        lines = "lines"
        all = "all"

    class Type:
        """ """
        WSDL = "WSDL"
        CustomSettings = "CustomSettings"
        XMLSchema = "XMLSchema"
        XMLErrorPage = "XMLErrorPage"
        htmlpage = "htmlpage"
        CustomResp = "CustomResp"
        Extension = "Extension"

    class Detail:
        """ """
        brief = "brief"
        all = "all"

class nsextension_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.nsextension = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.nsextension = [nsextension() for _ in range(length)]

