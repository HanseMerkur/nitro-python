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

class streamidentifier(base_resource) :
    """Configuration for identifier resource."""
    def __init__(self) :
        self._name = ""
        self._selectorname = ""
        self._interval = 0
        self._samplecount = 0
        self._sort = ""
        self._snmptrap = ""
        self._appflowlog = ""
        self._tracktransactions = ""
        self._maxtransactionthreshold = 0
        self._mintransactionthreshold = 0
        self._acceptancethreshold = ""
        self._breachthreshold = 0
        self._rule = []
        self.___count = 0

    @property
    def name(self) :
        """The name of stream identifier."""
        try :
            return self._name
        except Exception as e:
            raise e

    @name.setter
    def name(self, name) :
        """The name of stream identifier.

        :param name: 

        """
        try :
            self._name = name
        except Exception as e:
            raise e

    @property
    def selectorname(self) :
        """Name of the selector to use with the stream identifier.<br/>Minimum length =  1."""
        try :
            return self._selectorname
        except Exception as e:
            raise e

    @selectorname.setter
    def selectorname(self, selectorname) :
        """Name of the selector to use with the stream identifier.<br/>Minimum length =  1

        :param selectorname: 

        """
        try :
            self._selectorname = selectorname
        except Exception as e:
            raise e

    @property
    def interval(self) :
        """Number of minutes of data to use when calculating session statistics (number of requests, bandwidth, and response times). The interval is a moving window that keeps the most recently collected data. Older data is discarded at regular intervals.<br/>Default value: 1<br/>Minimum length =  1."""
        try :
            return self._interval
        except Exception as e:
            raise e

    @interval.setter
    def interval(self, interval) :
        """Number of minutes of data to use when calculating session statistics (number of requests, bandwidth, and response times). The interval is a moving window that keeps the most recently collected data. Older data is discarded at regular intervals.<br/>Default value: 1<br/>Minimum length =  1

        :param interval: 

        """
        try :
            self._interval = interval
        except Exception as e:
            raise e

    @property
    def samplecount(self) :
        """Size of the sample from which to select a request for evaluation. The smaller the sample count, the more accurate is the statistical data. To evaluate all requests, set the sample count to 1. However, such a low setting can result in excessive consumption of memory and processing resources.<br/>Default value: 1<br/>Minimum length =  1<br/>Maximum length =  65535."""
        try :
            return self._samplecount
        except Exception as e:
            raise e

    @samplecount.setter
    def samplecount(self, samplecount) :
        """Size of the sample from which to select a request for evaluation. The smaller the sample count, the more accurate is the statistical data. To evaluate all requests, set the sample count to 1. However, such a low setting can result in excessive consumption of memory and processing resources.<br/>Default value: 1<br/>Minimum length =  1<br/>Maximum length =  65535

        :param samplecount: 

        """
        try :
            self._samplecount = samplecount
        except Exception as e:
            raise e

    @property
    def sort(self) :
        """Sort stored records by the specified statistics column, in descending order. Performed during data collection, the sorting enables real-time data evaluation through NetScaler policies (for example, compression and caching policies) that use functions such as IS_TOP(n).<br/>Default value: REQUESTS<br/>Possible values = REQUESTS, CONNECTIONS, RESPTIME, BANDWIDTH, RESPTIME_BREACHES, NONE."""
        try :
            return self._sort
        except Exception as e:
            raise e

    @sort.setter
    def sort(self, sort) :
        """Sort stored records by the specified statistics column, in descending order. Performed during data collection, the sorting enables real-time data evaluation through NetScaler policies (for example, compression and caching policies) that use functions such as IS_TOP(n).<br/>Default value: REQUESTS<br/>Possible values = REQUESTS, CONNECTIONS, RESPTIME, BANDWIDTH, RESPTIME_BREACHES, NONE

        :param sort: 

        """
        try :
            self._sort = sort
        except Exception as e:
            raise e

    @property
    def snmptrap(self) :
        """Enable/disable SNMP trap for stream identifier.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._snmptrap
        except Exception as e:
            raise e

    @snmptrap.setter
    def snmptrap(self, snmptrap) :
        """Enable/disable SNMP trap for stream identifier.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED

        :param snmptrap: 

        """
        try :
            self._snmptrap = snmptrap
        except Exception as e:
            raise e

    @property
    def appflowlog(self) :
        """Enable/disable Appflow logging for stream identifier.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._appflowlog
        except Exception as e:
            raise e

    @appflowlog.setter
    def appflowlog(self, appflowlog) :
        """Enable/disable Appflow logging for stream identifier.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED

        :param appflowlog: 

        """
        try :
            self._appflowlog = appflowlog
        except Exception as e:
            raise e

    @property
    def tracktransactions(self) :
        """Track transactions exceeding configured threshold. Transaction tracking can be enabled for following metric: ResponseTime.
        By default transaction tracking is disabled.<br/>Default value: NONE<br/>Possible values = RESPTIME, NONE.


        """
        try :
            return self._tracktransactions
        except Exception as e:
            raise e

    @tracktransactions.setter
    def tracktransactions(self, tracktransactions) :
        """Track transactions exceeding configured threshold. Transaction tracking can be enabled for following metric: ResponseTime.
        By default transaction tracking is disabled.<br/>Default value: NONE<br/>Possible values = RESPTIME, NONE

        :param tracktransactions: 

        """
        try :
            self._tracktransactions = tracktransactions
        except Exception as e:
            raise e

    @property
    def maxtransactionthreshold(self) :
        """Maximum per transcation value of metric. Metric to be tracked is specified by tracktransactions attribute.<br/>Default value: 0."""
        try :
            return self._maxtransactionthreshold
        except Exception as e:
            raise e

    @maxtransactionthreshold.setter
    def maxtransactionthreshold(self, maxtransactionthreshold) :
        """Maximum per transcation value of metric. Metric to be tracked is specified by tracktransactions attribute.<br/>Default value: 0

        :param maxtransactionthreshold: 

        """
        try :
            self._maxtransactionthreshold = maxtransactionthreshold
        except Exception as e:
            raise e

    @property
    def mintransactionthreshold(self) :
        """Minimum per transcation value of metric. Metric to be tracked is specified by tracktransactions attribute.<br/>Default value: 0."""
        try :
            return self._mintransactionthreshold
        except Exception as e:
            raise e

    @mintransactionthreshold.setter
    def mintransactionthreshold(self, mintransactionthreshold) :
        """Minimum per transcation value of metric. Metric to be tracked is specified by tracktransactions attribute.<br/>Default value: 0

        :param mintransactionthreshold: 

        """
        try :
            self._mintransactionthreshold = mintransactionthreshold
        except Exception as e:
            raise e

    @property
    def acceptancethreshold(self) :
        """Non-Breaching transactions to Total transactions threshold expressed in percent.
        Maximum of 6 decimal places is supported.<br/>Default value: 0.000000<br/>Maximum length =  10.


        """
        try :
            return self._acceptancethreshold
        except Exception as e:
            raise e

    @acceptancethreshold.setter
    def acceptancethreshold(self, acceptancethreshold) :
        """Non-Breaching transactions to Total transactions threshold expressed in percent.
        Maximum of 6 decimal places is supported.<br/>Default value: 0.000000<br/>Maximum length =  10

        :param acceptancethreshold: 

        """
        try :
            self._acceptancethreshold = acceptancethreshold
        except Exception as e:
            raise e

    @property
    def breachthreshold(self) :
        """Breaching transactions threshold calculated over interval.<br/>Default value: 0."""
        try :
            return self._breachthreshold
        except Exception as e:
            raise e

    @breachthreshold.setter
    def breachthreshold(self, breachthreshold) :
        """Breaching transactions threshold calculated over interval.<br/>Default value: 0

        :param breachthreshold: 

        """
        try :
            self._breachthreshold = breachthreshold
        except Exception as e:
            raise e

    @property
    def rule(self) :
        """Rule."""
        try :
            return self._rule
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(streamidentifier_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.streamidentifier
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
        """Use this API to add streamidentifier.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                addresource = streamidentifier()
                addresource.name = resource.name
                addresource.selectorname = resource.selectorname
                addresource.interval = resource.interval
                addresource.samplecount = resource.samplecount
                addresource.sort = resource.sort
                addresource.snmptrap = resource.snmptrap
                addresource.appflowlog = resource.appflowlog
                addresource.tracktransactions = resource.tracktransactions
                addresource.maxtransactionthreshold = resource.maxtransactionthreshold
                addresource.mintransactionthreshold = resource.mintransactionthreshold
                addresource.acceptancethreshold = resource.acceptancethreshold
                addresource.breachthreshold = resource.breachthreshold
                return addresource.add_resource(client)
            else :
                if (resource and len(resource) > 0) :
                    addresources = [ streamidentifier() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        addresources[i].name = resource[i].name
                        addresources[i].selectorname = resource[i].selectorname
                        addresources[i].interval = resource[i].interval
                        addresources[i].samplecount = resource[i].samplecount
                        addresources[i].sort = resource[i].sort
                        addresources[i].snmptrap = resource[i].snmptrap
                        addresources[i].appflowlog = resource[i].appflowlog
                        addresources[i].tracktransactions = resource[i].tracktransactions
                        addresources[i].maxtransactionthreshold = resource[i].maxtransactionthreshold
                        addresources[i].mintransactionthreshold = resource[i].mintransactionthreshold
                        addresources[i].acceptancethreshold = resource[i].acceptancethreshold
                        addresources[i].breachthreshold = resource[i].breachthreshold
                result = cls.add_bulk_request(client, addresources)
            return result
        except Exception as e :
            raise e

    @classmethod
    def update(cls, client, resource) :
        """Use this API to update streamidentifier.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                updateresource = streamidentifier()
                updateresource.name = resource.name
                updateresource.selectorname = resource.selectorname
                updateresource.interval = resource.interval
                updateresource.samplecount = resource.samplecount
                updateresource.sort = resource.sort
                updateresource.snmptrap = resource.snmptrap
                updateresource.appflowlog = resource.appflowlog
                updateresource.tracktransactions = resource.tracktransactions
                updateresource.maxtransactionthreshold = resource.maxtransactionthreshold
                updateresource.mintransactionthreshold = resource.mintransactionthreshold
                updateresource.acceptancethreshold = resource.acceptancethreshold
                updateresource.breachthreshold = resource.breachthreshold
                return updateresource.update_resource(client)
            else :
                if (resource and len(resource) > 0) :
                    updateresources = [ streamidentifier() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        updateresources[i].name = resource[i].name
                        updateresources[i].selectorname = resource[i].selectorname
                        updateresources[i].interval = resource[i].interval
                        updateresources[i].samplecount = resource[i].samplecount
                        updateresources[i].sort = resource[i].sort
                        updateresources[i].snmptrap = resource[i].snmptrap
                        updateresources[i].appflowlog = resource[i].appflowlog
                        updateresources[i].tracktransactions = resource[i].tracktransactions
                        updateresources[i].maxtransactionthreshold = resource[i].maxtransactionthreshold
                        updateresources[i].mintransactionthreshold = resource[i].mintransactionthreshold
                        updateresources[i].acceptancethreshold = resource[i].acceptancethreshold
                        updateresources[i].breachthreshold = resource[i].breachthreshold
                result = cls.update_bulk_request(client, updateresources)
            return result
        except Exception as e :
            raise e

    @classmethod
    def unset(cls, client, resource, args) :
        """Use this API to unset the properties of streamidentifier resource.
        Properties that need to be unset are specified in args array.

        :param client: 
        :param resource: 
        :param args: 

        """
        try :
            if type(resource) is not list :
                unsetresource = streamidentifier()
                if type(resource) !=  type(unsetresource):
                    unsetresource.name = resource
                else :
                    unsetresource.name = resource.name
                return unsetresource.unset_resource(client, args)
            else :
                if type(resource[0]) != cls :
                    if (resource and len(resource) > 0) :
                        unsetresources = [ streamidentifier() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            unsetresources[i].name = resource[i]
                else :
                    if (resource and len(resource) > 0) :
                        unsetresources = [ streamidentifier() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            unsetresources[i].name = resource[i].name
                result = cls.unset_bulk_request(client, unsetresources, args)
            return result
        except Exception as e :
            raise e

    @classmethod
    def delete(cls, client, resource) :
        """Use this API to delete streamidentifier.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                deleteresource = streamidentifier()
                if type(resource) !=  type(deleteresource):
                    deleteresource.name = resource
                else :
                    deleteresource.name = resource.name
                return deleteresource.delete_resource(client)
            else :
                if type(resource[0]) != cls :
                    if (resource and len(resource) > 0) :
                        deleteresources = [ streamidentifier() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            deleteresources[i].name = resource[i]
                else :
                    if (resource and len(resource) > 0) :
                        deleteresources = [ streamidentifier() for _ in range(len(resource))]
                        for i in range(len(resource)) :
                            deleteresources[i].name = resource[i].name
                result = cls.delete_bulk_request(client, deleteresources)
            return result
        except Exception as e :
            raise e

    @classmethod
    def get(cls, client, name="", option_="") :
        """Use this API to fetch all the streamidentifier resources that are configured on netscaler.

        :param client: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            if not name :
                obj = streamidentifier()
                response = obj.get_resources(client, option_)
            else :
                if type(name) != cls :
                    if type(name) is not list :
                        obj = streamidentifier()
                        obj.name = name
                        response = obj.get_resource(client, option_)
                    else :
                        if name and len(name) > 0 :
                            response = [streamidentifier() for _ in range(len(name))]
                            obj = [streamidentifier() for _ in range(len(name))]
                            for i in range(len(name)) :
                                obj[i] = streamidentifier()
                                obj[i].name = name[i]
                                response[i] = obj[i].get_resource(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def get_filtered(cls, client, filter_) :
        """Use this API to fetch filtered set of streamidentifier resources.
        filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = streamidentifier()
            option_ = options()
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def count(cls, client) :
        """Use this API to count the streamidentifier resources configured on NetScaler.

        :param client: 

        """
        try :
            obj = streamidentifier()
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
        """Use this API to count filtered the set of streamidentifier resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 

        """
        try :
            obj = streamidentifier()
            option_ = options()
            option_.count = True
            option_.filter = filter_
            response = obj.getfiltered(client, option_)
            if response :
                return response[0].__dict__['___count']
            return 0
        except Exception as e :
            raise e


    class Snmptrap:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Tracktransactions:
        """ """
        RESPTIME = "RESPTIME"
        NONE = "NONE"

    class Appflowlog:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Sort:
        """ """
        REQUESTS = "REQUESTS"
        CONNECTIONS = "CONNECTIONS"
        RESPTIME = "RESPTIME"
        BANDWIDTH = "BANDWIDTH"
        RESPTIME_BREACHES = "RESPTIME_BREACHES"
        NONE = "NONE"

class streamidentifier_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.streamidentifier = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.streamidentifier = [streamidentifier() for _ in range(length)]

