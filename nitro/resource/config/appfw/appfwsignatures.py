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

class appfwsignatures(base_resource) :
    """Configuration for application firewall signatures XML configuration resource."""
    def __init__(self) :
        self._name = ""
        self._src = ""
        self._xslt = ""
        self._comment = ""
        self._overwrite = False
        self._merge = False
        self._sha1 = ""
        self._mergedefault = False
        self._response = ""

    @property
    def name(self) :
        """Name of the signature object.<br/>Minimum length =  1<br/>Maximum length =  31."""
        try :
            return self._name
        except Exception as e:
            raise e

    @name.setter
    def name(self, name) :
        """Name of the signature object.<br/>Minimum length =  1<br/>Maximum length =  31

        :param name: 

        """
        try :
            self._name = name
        except Exception as e:
            raise e

    @property
    def src(self) :
        """URL (protocol, host, path, and file name) for the location at which to store the imported signatures object.
        NOTE: The import fails if the object to be imported is on an HTTPS server that requires client certificate authentication for access.<br/>Minimum length =  1<br/>Maximum length =  2047.


        """
        try :
            return self._src
        except Exception as e:
            raise e

    @src.setter
    def src(self, src) :
        """URL (protocol, host, path, and file name) for the location at which to store the imported signatures object.
        NOTE: The import fails if the object to be imported is on an HTTPS server that requires client certificate authentication for access.<br/>Minimum length =  1<br/>Maximum length =  2047

        :param src: 

        """
        try :
            self._src = src
        except Exception as e:
            raise e

    @property
    def xslt(self) :
        """XSLT file source.<br/>Maximum length =  2047."""
        try :
            return self._xslt
        except Exception as e:
            raise e

    @xslt.setter
    def xslt(self, xslt) :
        """XSLT file source.<br/>Maximum length =  2047

        :param xslt: 

        """
        try :
            self._xslt = xslt
        except Exception as e:
            raise e

    @property
    def comment(self) :
        """Any comments to preserve information about the signatures object.<br/>Maximum length =  128."""
        try :
            return self._comment
        except Exception as e:
            raise e

    @comment.setter
    def comment(self, comment) :
        """Any comments to preserve information about the signatures object.<br/>Maximum length =  128

        :param comment: 

        """
        try :
            self._comment = comment
        except Exception as e:
            raise e

    @property
    def overwrite(self) :
        """Overwrite any existing signatures object of the same name."""
        try :
            return self._overwrite
        except Exception as e:
            raise e

    @overwrite.setter
    def overwrite(self, overwrite) :
        """Overwrite any existing signatures object of the same name.

        :param overwrite: 

        """
        try :
            self._overwrite = overwrite
        except Exception as e:
            raise e

    @property
    def merge(self) :
        """Merges the existing Signature with new signature rules."""
        try :
            return self._merge
        except Exception as e:
            raise e

    @merge.setter
    def merge(self, merge) :
        """Merges the existing Signature with new signature rules.

        :param merge: 

        """
        try :
            self._merge = merge
        except Exception as e:
            raise e

    @property
    def sha1(self) :
        """File path for sha1 file to validate signature file.<br/>Minimum length =  1<br/>Maximum length =  2047."""
        try :
            return self._sha1
        except Exception as e:
            raise e

    @sha1.setter
    def sha1(self, sha1) :
        """File path for sha1 file to validate signature file.<br/>Minimum length =  1<br/>Maximum length =  2047

        :param sha1: 

        """
        try :
            self._sha1 = sha1
        except Exception as e:
            raise e

    @property
    def mergedefault(self) :
        """Merges signature file with default signature file."""
        try :
            return self._mergedefault
        except Exception as e:
            raise e

    @mergedefault.setter
    def mergedefault(self, mergedefault) :
        """Merges signature file with default signature file.

        :param mergedefault: 

        """
        try :
            self._mergedefault = mergedefault
        except Exception as e:
            raise e

    @property
    def response(self) :
        """ """
        try :
            return self._response
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(appfwsignatures_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.appfwsignatures
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
    def delete(cls, client, resource) :
        """Use this API to delete appfwsignatures.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                deleteresource = appfwsignatures()
                if type(resource) !=  type(deleteresource):
                    deleteresource.name = resource
                else :
                    deleteresource.name = resource.name
                return deleteresource.delete_resource(client)
        except Exception as e :
            raise e

    @classmethod
    def Import(cls, client, resource) :
        """Use this API to Import appfwsignatures.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                Importresource = appfwsignatures()
                Importresource.src = resource.src
                Importresource.name = resource.name
                Importresource.xslt = resource.xslt
                Importresource.comment = resource.comment
                Importresource.overwrite = resource.overwrite
                Importresource.merge = resource.merge
                Importresource.sha1 = resource.sha1
                return Importresource.perform_operation(client,"Import")
        except Exception as e :
            raise e

    @classmethod
    def change(cls, client, resource) :
        """Use this API to change appfwsignatures.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                changeresource = appfwsignatures()
                changeresource.name = resource.name
                changeresource.mergedefault = resource.mergedefault
                return changeresource.perform_operation(client,"update")
        except Exception as e :
            raise e

    @classmethod
    def get(cls, client, name="", option_="") :
        """Use this API to fetch all the appfwsignatures resources that are configured on netscaler.

        :param client: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            if not name :
                obj = appfwsignatures()
                response = obj.get_resources(client, option_)
                if type(name) != cls :
                    if type(name) is not list :
                        obj = appfwsignatures()
                        obj.name = name
                        response = obj.get_resource(client, option_)
            return response
        except Exception as e :
            raise e


class appfwsignatures_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.appfwsignatures = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.appfwsignatures = [appfwsignatures() for _ in range(length)]

