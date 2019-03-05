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

class responderpolicylabel(base_resource) :
    """Configuration for responder policy label resource."""
    def __init__(self) :
        self._labelname = ""
        self._policylabeltype = ""
        self._comment = ""
        self._newname = ""
        self._numpol = 0
        self._hits = 0
        self._priority = 0
        self._gotopriorityexpression = ""
        self._labeltype = ""
        self._invoke_labelname = ""
        self.___count = 0

    @property
    def labelname(self) :
        """Name for the responder policy label. Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) hash (#), space ( ), at (@), equals (=), colon (:), and underscore characters. Cannot be changed after the responder policy label is added.
        The following requirement applies only to the NetScaler CLI:
        If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my responder policy label" or my responder policy label').


        """
        try :
            return self._labelname
        except Exception as e:
            raise e

    @labelname.setter
    def labelname(self, labelname) :
        """Name for the responder policy label. Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) hash (#), space ( ), at (@), equals (=), colon (:), and underscore characters. Cannot be changed after the responder policy label is added.
        The following requirement applies only to the NetScaler CLI:
        If the name includes one or more spaces, enclose the name in double or single quotation marks (for example, "my responder policy label" or my responder policy label').

        :param labelname: 

        """
        try :
            self._labelname = labelname
        except Exception as e:
            raise e

    @property
    def policylabeltype(self) :
        """Type of responses sent by the policies bound to this policy label. Types are:
        * HTTP - HTTP responses.
        * OTHERTCP - NON-HTTP TCP responses.
        * SIP_UDP - SIP responses.
        * RADIUS - RADIUS responses.
        * MYSQL - SQL responses in MySQL format.
        * MSSQL - SQL responses in Microsoft SQL format.
        * NAT - NAT response.<br/>Default value: HTTP<br/>Possible values = HTTP, OTHERTCP, SIP_UDP, SIP_TCP, MYSQL, MSSQL, NAT, DIAMETER, RADIUS, DNS.


        """
        try :
            return self._policylabeltype
        except Exception as e:
            raise e

    @policylabeltype.setter
    def policylabeltype(self, policylabeltype) :
        """Type of responses sent by the policies bound to this policy label. Types are:
        * HTTP - HTTP responses.
        * OTHERTCP - NON-HTTP TCP responses.
        * SIP_UDP - SIP responses.
        * RADIUS - RADIUS responses.
        * MYSQL - SQL responses in MySQL format.
        * MSSQL - SQL responses in Microsoft SQL format.
        * NAT - NAT response.<br/>Default value: HTTP<br/>Possible values = HTTP, OTHERTCP, SIP_UDP, SIP_TCP, MYSQL, MSSQL, NAT, DIAMETER, RADIUS, DNS

        :param policylabeltype: 

        """
        try :
            self._policylabeltype = policylabeltype
        except Exception as e:
            raise e

    @property
    def comment(self) :
        """Any comments to preserve information about this responder policy label."""
        try :
            return self._comment
        except Exception as e:
            raise e

    @comment.setter
    def comment(self, comment) :
        """Any comments to preserve information about this responder policy label.

        :param comment: 

        """
        try :
            self._comment = comment
        except Exception as e:
            raise e

    @property
    def newname(self) :
        """New name for the responder policy label. Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) hash (#), space ( ), at (@), equals (=), colon (:), and underscore characters.<br/>Minimum length =  1."""
        try :
            return self._newname
        except Exception as e:
            raise e

    @newname.setter
    def newname(self, newname) :
        """New name for the responder policy label. Must begin with a letter, number, or the underscore character (_), and must contain only letters, numbers, and the hyphen (-), period (.) hash (#), space ( ), at (@), equals (=), colon (:), and underscore characters.<br/>Minimum length =  1

        :param newname: 

        """
        try :
            self._newname = newname
        except Exception as e:
            raise e

    @property
    def numpol(self) :
        """number of polices bound to label."""
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
    def labeltype(self) :
        """Type of policy label to invoke. Available settings function as follows:
        * vserver - Invoke an unnamed policy label associated with a virtual server.
        * policylabel - Invoke a user-defined policy label.<br/>Possible values = vserver, policylabel.


        """
        try :
            return self._labeltype
        except Exception as e:
            raise e

    @property
    def invoke_labelname(self) :
        """* If labelType is policylabel, name of the policy label to invoke.
        * If labelType is reqvserver or resvserver, name of the virtual server.


        """
        try :
            return self._invoke_labelname
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(responderpolicylabel_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.responderpolicylabel
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
        """Use this API to add responderpolicylabel.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                addresource = responderpolicylabel()
                addresource.labelname = resource.labelname
                addresource.policylabeltype = resource.policylabeltype
                addresource.comment = resource.comment
                return addresource.add_resource(client)
            else :
                if (resource and len(resource) > 0) :
                    addresources = [ responderpolicylabel() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        addresources[i].labelname = resource[i].labelname
                        addresources[i].policylabeltype = resource[i].policylabeltype
                        addresources[i].comment = resource[i].comment
                result = cls.add_bulk_request(client, addresources)
            return result
        except Exception as e :
            raise e

    @classmethod
    def delete(cls, client, resource) :
        """Use this API to delete responderpolicylabel.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                deleteresource = responderpolicylabel()
                if type(resource) !=  type(deleteresource):
                    deleteresource.labelname = resource
                else :
                    deleteresource.labelname = resource.labelname
                return deleteresource.delete_resource(client)
            else :
                if type(resource[0]) != cls :
                    if (resource and len(resource) > 0) :
                        deleteresources = [ responderpolicylabel() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            deleteresources[i].labelname = resource[i]
                else :
                    if (resource and len(resource) > 0) :
                        deleteresources = [ responderpolicylabel() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            deleteresources[i].labelname = resource[i].labelname
                result = cls.delete_bulk_request(client, deleteresources)
            return result
        except Exception as e :
            raise e

    @classmethod
    def rename(cls, client, resource, new_labelname) :
        """Use this API to rename a responderpolicylabel resource.

        :param client: 
        :param resource: 
        :param new_labelname: 

        """
        try :
            renameresource = responderpolicylabel()
            if type(resource) == cls :
                renameresource.labelname = resource.labelname
            else :
                renameresource.labelname = resource
            return renameresource.rename_resource(client,new_labelname)
        except Exception as e :
            raise e

    @classmethod
    def get(cls, client, name="", option_="") :
        """Use this API to fetch all the responderpolicylabel resources that are configured on netscaler.

        :param client: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            if not name :
                obj = responderpolicylabel()
                response = obj.get_resources(client, option_)
            else :
                if type(name) != cls :
                    if type(name) is not list :
                        obj = responderpolicylabel()
                        obj.labelname = name
                        response = obj.get_resource(client, option_)
                    else :
                        if name and len(name) > 0 :
                            response = [responderpolicylabel() for _ in range(len(name))]
                            obj = [responderpolicylabel() for _ in range(len(name))]
                            for i in range(len(name)) :
                                obj[i] = responderpolicylabel()
                                obj[i].labelname = name[i]
                                response[i] = obj[i].get_resource(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def get_filtered(cls, client, filter_) :
        """Use this API to fetch filtered set of responderpolicylabel resources.
        filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = responderpolicylabel()
            option_ = options()
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def count(cls, client) :
        """Use this API to count the responderpolicylabel resources configured on NetScaler.

        :param client: 

        """
        try :
            obj = responderpolicylabel()
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
        """Use this API to count filtered the set of responderpolicylabel resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = responderpolicylabel()
            option_ = options()
            option_.count = True
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            if response :
                return response[0].__dict__['___count']
            return 0
        except Exception as e :
            raise e


    class Policylabeltype:
        """ """
        HTTP = "HTTP"
        OTHERTCP = "OTHERTCP"
        SIP_UDP = "SIP_UDP"
        SIP_TCP = "SIP_TCP"
        MYSQL = "MYSQL"
        MSSQL = "MSSQL"
        NAT = "NAT"
        DIAMETER = "DIAMETER"
        RADIUS = "RADIUS"
        DNS = "DNS"

    class Labeltype:
        """ """
        vserver = "vserver"
        policylabel = "policylabel"

class responderpolicylabel_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.responderpolicylabel = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.responderpolicylabel = [responderpolicylabel() for _ in range(length)]

