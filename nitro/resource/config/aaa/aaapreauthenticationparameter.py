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

class aaapreauthenticationparameter(base_resource) :
    """Configuration for pre authentication parameter resource."""
    def __init__(self) :
        self._preauthenticationaction = ""
        self._rule = ""
        self._killprocess = ""
        self._deletefiles = ""
        self._builtin = []

    @property
    def preauthenticationaction(self) :
        """Deny or allow login on the basis of end point analysis results.<br/>Possible values = ALLOW, DENY."""
        try :
            return self._preauthenticationaction
        except Exception as e:
            raise e

    @preauthenticationaction.setter
    def preauthenticationaction(self, preauthenticationaction) :
        """Deny or allow login on the basis of end point analysis results.<br/>Possible values = ALLOW, DENY

        :param preauthenticationaction: 

        """
        try :
            self._preauthenticationaction = preauthenticationaction
        except Exception as e:
            raise e

    @property
    def rule(self) :
        """Name of the NetScaler named rule, or a default syntax expression, to be evaluated by the EPA tool."""
        try :
            return self._rule
        except Exception as e:
            raise e

    @rule.setter
    def rule(self, rule) :
        """Name of the NetScaler named rule, or a default syntax expression, to be evaluated by the EPA tool.

        :param rule: 

        """
        try :
            self._rule = rule
        except Exception as e:
            raise e

    @property
    def killprocess(self) :
        """String specifying the name of a process to be terminated by the EPA tool."""
        try :
            return self._killprocess
        except Exception as e:
            raise e

    @killprocess.setter
    def killprocess(self, killprocess) :
        """String specifying the name of a process to be terminated by the EPA tool.

        :param killprocess: 

        """
        try :
            self._killprocess = killprocess
        except Exception as e:
            raise e

    @property
    def deletefiles(self) :
        """String specifying the path(s) to and name(s) of the files to be deleted by the EPA tool, as a string of between 1 and 1023 characters."""
        try :
            return self._deletefiles
        except Exception as e:
            raise e

    @deletefiles.setter
    def deletefiles(self, deletefiles) :
        """String specifying the path(s) to and name(s) of the files to be deleted by the EPA tool, as a string of between 1 and 1023 characters.

        :param deletefiles: 

        """
        try :
            self._deletefiles = deletefiles
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
            result = service.payload_formatter.string_to_resource(aaapreauthenticationparameter_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.aaapreauthenticationparameter
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
        """Use this API to update aaapreauthenticationparameter.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                updateresource = aaapreauthenticationparameter()
                updateresource.preauthenticationaction = resource.preauthenticationaction
                updateresource.rule = resource.rule
                updateresource.killprocess = resource.killprocess
                updateresource.deletefiles = resource.deletefiles
                return updateresource.update_resource(client)
        except Exception as e :
            raise e

    @classmethod
    def unset(cls, client, resource, args) :
        """Use this API to unset the properties of aaapreauthenticationparameter resource.
        Properties that need to be unset are specified in args array.

        :param client: 
        :param resource: 
        :param args: 

        """
        try :
            if type(resource) is not list :
                unsetresource = aaapreauthenticationparameter()
                return unsetresource.unset_resource(client, args)
        except Exception as e :
            raise e

    @classmethod
    def get(cls, client, name="", option_="") :
        """Use this API to fetch all the aaapreauthenticationparameter resources that are configured on netscaler.

        :param client: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            if not name :
                obj = aaapreauthenticationparameter()
                response = obj.get_resources(client, option_)
            return response
        except Exception as e :
            raise e


    class Builtin:
        """ """
        MODIFIABLE = "MODIFIABLE"
        DELETABLE = "DELETABLE"
        IMMUTABLE = "IMMUTABLE"
        PARTITION_ALL = "PARTITION_ALL"

    class Preauthenticationaction:
        """ """
        ALLOW = "ALLOW"
        DENY = "DENY"

class aaapreauthenticationparameter_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.aaapreauthenticationparameter = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.aaapreauthenticationparameter = [aaapreauthenticationparameter() for _ in range(length)]

