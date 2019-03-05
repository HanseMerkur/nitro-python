
# Copyright (c) 2008-2015 Citrix Systems, Inc.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
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

import json
from nitro.util.nitro_util import nitro_util
from nitro.resource.base.ipayload_formatter import ipayload_formatter


class Json(ipayload_formatter): 
    """Json class implements the methods in ipayload_formatter interface."""
    
    def resource_to_string_convert(self, resrc):
        """Converts netscaler resource to Json string.

        :param resrc: nitro resource
        :param Returns: 

        """
        try:
            dict_valid_values = dict((k.replace('_',''), v) for k, v in resrc.__dict__.items() if v)
            return json.dumps(dict_valid_values) 
        except Exception as e:
            raise e
    
    def string_to_resource(self, responseClass, response_dict, resrc_type):
        """Converts Json string to netscaler resource.

        :param responseClass: Type of the class to which the string has to be converted to
        :param response: input string
        :param Returns: 
        :param response_dict: 
        :param resrc_type: 

        """
        try:
            underscore_dict = {}
            temp_dict = json.loads(response_dict)
            if resrc_type.lower() in temp_dict.keys() :
                if (type(json.loads(response_dict)[resrc_type.lower()]) is list) :
                    length = len(json.loads(response_dict)[resrc_type.lower()])
                else :
                    length = 1
                response = responseClass(length)
            elif resrc_type in temp_dict.keys() :
                if (type(json.loads(response_dict)[resrc_type]) is list) :
                    length = len(json.loads(response_dict)[resrc_type])
                else :
                    length = 1
                response = responseClass(length)            
            elif 'response' in temp_dict.keys() :                
                if (type(json.loads(response_dict)['response']) is list) :
                    length = len(json.loads(response_dict)['response'])
                else :
                    length = 1
                response = responseClass(length)
            else :
                response = responseClass()
            for key in temp_dict.keys() :
                if type(response.__dict__[key]) is list :
                    if type(temp_dict[key]) is list :
                        for i in range(length) :
                            for each_key in (temp_dict[key][i]).keys() :
                                underscore_dict['_'+each_key] = (temp_dict[key][i])[each_key]
                            # instead of references we are copying elements
                            (response.__dict__[key])[i].__dict__ = underscore_dict.copy()
                    else :
                        for item in temp_dict[key].keys() :
                            (response.__dict__[key])[0].__dict__['_'+item] = (temp_dict[key])[item] 
                else :
                    response.__dict__[key] = temp_dict[key]                     
            return response
        except Exception as e:
            raise e

    def resource_to_string(self, resrc):
        """Converts netscaler resource to Json string.

        :param resrc: nitro resource
        :param id: sessionId
        :param option: options class object
        :param Returns: 

        """
        try: 
            objtype = resrc.__class__.get_object_type()
            result = "{ "
            result = result + "\"" + objtype + "\":" + self.resource_to_string_convert(resrc) + "}"
            return result
        except Exception as e:
            raise e
    
    def resource_to_string_bulk(self, resources):
        """Converts netscaler resources to Json string.

        :param resources: nitro resources
        :param id: sessionId
        :param option: options class object
        :param Returns: 

        """
        try :
            objecttype = resources[0].__class__.get_object_type()
            request = "{"
            request = request + "\"" + objecttype + "\":["
            for i in range(len(resources)): 
                str_ = self.resource_to_string_convert(resources[i])
                request = request + str_
                if i!= (len(resources)-1):
                    request = request + ","
            request = request + "]}"
            return request
        except Exception as e:
            raise e
        
    
    def unset_string(self, resrc, args):
        """Converts nitro resource to Json string. This is exclusively for forming unset string.
        
        Parameters:
            resrc - nitro resource.
            id - sessionId.
            option - options class object.

        :param Returns: 
        :param resrc: 
        :param args: 

        """
        try:
            result = "{ "
            objstr = nitro_util.object_to_string(resrc)
            if objstr :
                result = result + objstr       
            if args :
                for i in range(len(args)): 
                    result = result + "\"" + args[i] + "\": true"
                    if i != (len(args)-1) :
                        result = result + ","
                    else :
                        result = result + "}"
            return result
        except Exception as e:
            raise e


    def unset_string_bulk(self, resources, args):
        """

        :param resources: 
        :param args: 

        """
        try:
            objecttype = resources[0].__class__.get_object_type()
            result = "{ "        
            result = result + "\"" + objecttype + "\": [" 
            for i in range(len(resources)): 
                objstr = self.unset_string(resources[i],args)
                if objstr :
                    result = result + objstr
                if i != (len(resources)-1) :
                    result = result + ","
            result = result + "]}"
            return result
        except Exception as e:
            raise e

