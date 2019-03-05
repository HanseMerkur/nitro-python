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

class techsupport(base_resource) :
    """Configuration for tech support resource."""
    def __init__(self) :
        self._scope = ""
        self._partitionname = ""
        self._upload = False
        self._proxy = ""
        self._casenumber = ""
        self._file = ""
        self._description = ""
        self._username = ""
        self._password = ""
        self._response = ""
        self._servername = ""

    @property
    def scope(self) :
        """Use this option to gather data on the present node, all cluster nodes, or for the specified partitions. The CLUSTER scope generates smaller abbreviated archives for all nodes. The PARTITION scope collects the admin partition in addition to those specified. The partitionName option is only required for the PARTITION scope.<br/>Default value: NODE<br/>Possible values = NODE, CLUSTER, PARTITION."""
        try :
            return self._scope
        except Exception as e:
            raise e

    @scope.setter
    def scope(self, scope) :
        """Use this option to gather data on the present node, all cluster nodes, or for the specified partitions. The CLUSTER scope generates smaller abbreviated archives for all nodes. The PARTITION scope collects the admin partition in addition to those specified. The partitionName option is only required for the PARTITION scope.<br/>Default value: NODE<br/>Possible values = NODE, CLUSTER, PARTITION

        :param scope: 

        """
        try :
            self._scope = scope
        except Exception as e:
            raise e

    @property
    def partitionname(self) :
        """Name of the partition.<br/>Minimum length =  1."""
        try :
            return self._partitionname
        except Exception as e:
            raise e

    @partitionname.setter
    def partitionname(self, partitionname) :
        """Name of the partition.<br/>Minimum length =  1

        :param partitionname: 

        """
        try :
            self._partitionname = partitionname
        except Exception as e:
            raise e

    @property
    def upload(self) :
        """Securely upload the collector archive to Citrix Technical Support using SSL. MyCitrix credentials will be required. If used with the -file option, no new collector archive is generated. Instead, the specified archive is uploaded. Note that the upload operation time depends on the size of the archive file, and the connection bandwidth."""
        try :
            return self._upload
        except Exception as e:
            raise e

    @upload.setter
    def upload(self, upload) :
        """Securely upload the collector archive to Citrix Technical Support using SSL. MyCitrix credentials will be required. If used with the -file option, no new collector archive is generated. Instead, the specified archive is uploaded. Note that the upload operation time depends on the size of the archive file, and the connection bandwidth.

        :param upload: 

        """
        try :
            self._upload = upload
        except Exception as e:
            raise e

    @property
    def proxy(self) :
        """Specifies the proxy server to be used when uploading a collector archive. Use this parameter if the NetScaler appliance does not have direct internet connectivity. The basic format of the proxy string is: "proxy_IP:<proxy_port>" (without quotes). If the proxy requires authentication the format is: "username:password@proxy_IP:<proxy_port>"."""
        try :
            return self._proxy
        except Exception as e:
            raise e

    @proxy.setter
    def proxy(self, proxy) :
        """Specifies the proxy server to be used when uploading a collector archive. Use this parameter if the NetScaler appliance does not have direct internet connectivity. The basic format of the proxy string is: "proxy_IP:<proxy_port>" (without quotes). If the proxy requires authentication the format is: "username:password@proxy_IP:<proxy_port>".

        :param proxy: 

        """
        try :
            self._proxy = proxy
        except Exception as e:
            raise e

    @property
    def casenumber(self) :
        """Specifies the associated case or service request number if it has already been opened with Citrix Technical Support."""
        try :
            return self._casenumber
        except Exception as e:
            raise e

    @casenumber.setter
    def casenumber(self, casenumber) :
        """Specifies the associated case or service request number if it has already been opened with Citrix Technical Support.

        :param casenumber: 

        """
        try :
            self._casenumber = casenumber
        except Exception as e:
            raise e

    @property
    def file(self) :
        """Specifies the name (with full path) of the collector archive file to be uploaded. If this is specified, no new collector archive is generated."""
        try :
            return self._file
        except Exception as e:
            raise e

    @file.setter
    def file(self, file) :
        """Specifies the name (with full path) of the collector archive file to be uploaded. If this is specified, no new collector archive is generated.

        :param file: 

        """
        try :
            self._file = file
        except Exception as e:
            raise e

    @property
    def description(self) :
        """Provides a text description for the the upload, and can be used for logging purposes."""
        try :
            return self._description
        except Exception as e:
            raise e

    @description.setter
    def description(self, description) :
        """Provides a text description for the the upload, and can be used for logging purposes.

        :param description: 

        """
        try :
            self._description = description
        except Exception as e:
            raise e

    @property
    def username(self) :
        """Specifies My Citrix user name, which is used to login to Citrix upload server."""
        try :
            return self._username
        except Exception as e:
            raise e

    @username.setter
    def username(self, username) :
        """Specifies My Citrix user name, which is used to login to Citrix upload server.

        :param username: 

        """
        try :
            self._username = username
        except Exception as e:
            raise e

    @property
    def password(self) :
        """Specifies My Citrix password, which is used to login to Citrix upload server."""
        try :
            return self._password
        except Exception as e:
            raise e

    @password.setter
    def password(self, password) :
        """Specifies My Citrix password, which is used to login to Citrix upload server.

        :param password: 

        """
        try :
            self._password = password
        except Exception as e:
            raise e

    @property
    def response(self) :
        """Output as text printed to console and syslog at NOTICE level."""
        try :
            return self._response
        except Exception as e:
            raise e

    @property
    def servername(self) :
        """ """
        try :
            return self._servername
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(techsupport_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.techsupport
        except Exception as e :
            raise e

    def _get_object_name(self) :
        """Returns the value of object identifier argument"""
        try :
            return 0
        except Exception as e :
            raise e



    @classmethod
    def get(cls, client, name="", option_="") :
        """Use this API to fetch all the techsupport resources that are configured on netscaler.

        :param client: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            if not name :
                obj = techsupport()
                response = obj.get_resources(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def get_args(cls, client, args) :
        """Use this API to fetch all the techsupport resources that are configured on netscaler.
            # This uses techsupport_args which is a way to provide additional arguments while fetching the resources.

        :param client: 
        :param args: 

        """
        try :
            obj = techsupport()
            option_ = options()
            option_.args = nitro_util.object_to_string_withoutquotes(args)
            response = obj.get_resources(client, option_)
            return response
        except Exception as e :
            raise e


    class Scope:
        """ """
        NODE = "NODE"
        CLUSTER = "CLUSTER"
        PARTITION = "PARTITION"

class techsupport_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.techsupport = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.techsupport = [techsupport() for _ in range(length)]

