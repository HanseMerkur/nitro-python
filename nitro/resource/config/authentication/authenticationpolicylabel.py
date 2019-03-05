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

class authenticationpolicylabel(base_resource) :
    """Configuration for authentication policy label resource."""
    def __init__(self) :
        self._labelname = ""
        self._comment = ""
        self._loginschema = ""
        self._newname = ""
        self._numpol = 0
        self._hits = 0
        self._policyname = ""
        self._priority = 0
        self._gotopriorityexpression = ""
        self._flowtype = 0
        self._description = ""
        self.___count = 0

    @property
    def labelname(self) :
        """Name for the new authentication policy label.
        Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon (:), and underscore characters.
        The following requirement applies only to the NetScaler CLI:
        If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my authentication policy label" or 'authentication policy label').


        """
        try :
            return self._labelname
        except Exception as e:
            raise e

    @labelname.setter
    def labelname(self, labelname) :
        """Name for the new authentication policy label.
        Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) pound (#), space ( ), at (@), equals (=), colon (:), and underscore characters.
        The following requirement applies only to the NetScaler CLI:
        If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my authentication policy label" or 'authentication policy label').

        :param labelname: 

        """
        try :
            self._labelname = labelname
        except Exception as e:
            raise e

    @property
    def comment(self) :
        """Any comments to preserve information about this authentication policy label."""
        try :
            return self._comment
        except Exception as e:
            raise e

    @comment.setter
    def comment(self, comment) :
        """Any comments to preserve information about this authentication policy label.

        :param comment: 

        """
        try :
            self._comment = comment
        except Exception as e:
            raise e

    @property
    def loginschema(self) :
        """Login schema associated with authentication policy label."""
        try :
            return self._loginschema
        except Exception as e:
            raise e

    @loginschema.setter
    def loginschema(self, loginschema) :
        """Login schema associated with authentication policy label.

        :param loginschema: 

        """
        try :
            self._loginschema = loginschema
        except Exception as e:
            raise e

    @property
    def newname(self) :
        """The new name of the auth policy label.<br/>Minimum length =  1."""
        try :
            return self._newname
        except Exception as e:
            raise e

    @newname.setter
    def newname(self, newname) :
        """The new name of the auth policy label.<br/>Minimum length =  1

        :param newname: 

        """
        try :
            self._newname = newname
        except Exception as e:
            raise e

    @property
    def numpol(self) :
        """Number of polices bound to label."""
        try :
            return self._numpol
        except Exception as e:
            raise e

    @property
    def hits(self) :
        """Number of times policy label was invoked."""
        try :
            return self._hits
        except Exception as e:
            raise e

    @property
    def policyname(self) :
        """Name of the authentication policy to bind to the policy label."""
        try :
            return self._policyname
        except Exception as e:
            raise e

    @property
    def priority(self) :
        """Specifies the priority of the policy."""
        try :
            return self._priority
        except Exception as e:
            raise e

    @property
    def gotopriorityexpression(self) :
        """Expression specifying the priority of the next policy which will get evaluated if the current policy rule evaluates to TRUE."""
        try :
            return self._gotopriorityexpression
        except Exception as e:
            raise e

    @property
    def flowtype(self) :
        """Flowtype of the bound authentication policy."""
        try :
            return self._flowtype
        except Exception as e:
            raise e

    @property
    def description(self) :
        """Description of the policylabel."""
        try :
            return self._description
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(authenticationpolicylabel_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.authenticationpolicylabel
        except Exception as e :
            raise e

    def _get_object_name(self) :
        """Returns the value of object identifier argument"""
        try :
            if self.labelname is not None :
                return str(self.labelname)
            return None
        except Exception as e :
            raise e



    @classmethod
    def add(cls, client, resource) :
        """Use this API to add authenticationpolicylabel.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                addresource = authenticationpolicylabel()
                addresource.labelname = resource.labelname
                addresource.comment = resource.comment
                addresource.loginschema = resource.loginschema
                return addresource.add_resource(client)
            else :
                if (resource and len(resource) > 0) :
                    addresources = [ authenticationpolicylabel() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        addresources[i].labelname = resource[i].labelname
                        addresources[i].comment = resource[i].comment
                        addresources[i].loginschema = resource[i].loginschema
                result = cls.add_bulk_request(client, addresources)
            return result
        except Exception as e :
            raise e

    @classmethod
    def delete(cls, client, resource) :
        """Use this API to delete authenticationpolicylabel.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                deleteresource = authenticationpolicylabel()
                if type(resource) !=  type(deleteresource):
                    deleteresource.labelname = resource
                else :
                    deleteresource.labelname = resource.labelname
                return deleteresource.delete_resource(client)
            else :
                if type(resource[0]) != cls :
                    if (resource and len(resource) > 0) :
                        deleteresources = [ authenticationpolicylabel() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            deleteresources[i].labelname = resource[i]
                else :
                    if (resource and len(resource) > 0) :
                        deleteresources = [ authenticationpolicylabel() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            deleteresources[i].labelname = resource[i].labelname
                result = cls.delete_bulk_request(client, deleteresources)
            return result
        except Exception as e :
            raise e

    @classmethod
    def rename(cls, client, resource, new_labelname) :
        """Use this API to rename a authenticationpolicylabel resource.

        :param client: 
        :param resource: 
        :param new_labelname: 

        """
        try :
            renameresource = authenticationpolicylabel()
            if type(resource) == cls :
                renameresource.labelname = resource.labelname
            else :
                renameresource.labelname = resource
            return renameresource.rename_resource(client,new_labelname)
        except Exception as e :
            raise e

    @classmethod
    def get(cls, client, name="", option_="") :
        """Use this API to fetch all the authenticationpolicylabel resources that are configured on netscaler.

        :param client: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            if not name :
                obj = authenticationpolicylabel()
                response = obj.get_resources(client, option_)
            else :
                if type(name) != cls :
                    if type(name) is not list :
                        obj = authenticationpolicylabel()
                        obj.labelname = name
                        response = obj.get_resource(client, option_)
                    else :
                        if name and len(name) > 0 :
                            response = [authenticationpolicylabel() for _ in range(len(name))]
                            obj = [authenticationpolicylabel() for _ in range(len(name))]
                            for i in range(len(name)) :
                                obj[i] = authenticationpolicylabel()
                                obj[i].labelname = name[i]
                                response[i] = obj[i].get_resource(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def get_filtered(cls, client, filter_) :
        """Use this API to fetch filtered set of authenticationpolicylabel resources.
        filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = authenticationpolicylabel()
            option_ = options()
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def count(cls, client) :
        """Use this API to count the authenticationpolicylabel resources configured on NetScaler.

        :param client: 

        """
        try :
            obj = authenticationpolicylabel()
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
        """Use this API to count filtered the set of authenticationpolicylabel resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = authenticationpolicylabel()
            option_ = options()
            option_.count = True
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            if response :
                return response[0].__dict__['___count']
            return 0
        except Exception as e :
            raise e


class authenticationpolicylabel_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.authenticationpolicylabel = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.authenticationpolicylabel = [authenticationpolicylabel() for _ in range(length)]

