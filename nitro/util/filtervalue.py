
# Copyright (c) 2008-2015 Citrix Systems, Inc.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use self file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.




class filtervalue:
    """Filtervalue class provides a way to specify the filter parameter name and value for performing filtered get operation."""
    _name=""
    _value=""
    
    def __init__(self, name="", value=""):
        self._name = name
        self._value = value
        
    def filtervalue(self, name, value):
        """

        :param name: 
        :param value: 

        """
        self._name = name
        self._value = value
    
    
    @property
    def name(self):
        """


        :returns: gets the name of the filter parameter.

        """
        return self._name
    

    @property
    def value(self):
        """


        :returns: gets the value of the filter parameter.

        """
        return self._value
