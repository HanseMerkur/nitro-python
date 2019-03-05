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

class lbmonitor_metric_binding(base_resource) :
    """Binding class showing the metric that can be bound to lbmonitor."""
    def __init__(self) :
        self._metric = ""
        self._metrictable = ""
        self._metric_unit = ""
        self._metricweight = 0
        self._metricthreshold = 0
        self._monitorname = ""
        self.___count = 0

    @property
    def metric(self) :
        """Metric name in the metric table, whose setting is changed. A value zero disables the metric and it will not be used for load calculation.<br/>Minimum length =  1<br/>Maximum length =  37."""
        try :
            return self._metric
        except Exception as e:
            raise e

    @metric.setter
    def metric(self, metric) :
        """Metric name in the metric table, whose setting is changed. A value zero disables the metric and it will not be used for load calculation.<br/>Minimum length =  1<br/>Maximum length =  37

        :param metric: 

        """
        try :
            self._metric = metric
        except Exception as e:
            raise e

    @property
    def metricthreshold(self) :
        """Threshold to be used for that metric."""
        try :
            return self._metricthreshold
        except Exception as e:
            raise e

    @metricthreshold.setter
    def metricthreshold(self, metricthreshold) :
        """Threshold to be used for that metric.

        :param metricthreshold: 

        """
        try :
            self._metricthreshold = metricthreshold
        except Exception as e:
            raise e

    @property
    def metricweight(self) :
        """The weight for the specified service metric with respect to others.<br/>Minimum value =  1<br/>Maximum value =  100."""
        try :
            return self._metricweight
        except Exception as e:
            raise e

    @metricweight.setter
    def metricweight(self, metricweight) :
        """The weight for the specified service metric with respect to others.<br/>Minimum value =  1<br/>Maximum value =  100

        :param metricweight: 

        """
        try :
            self._metricweight = metricweight
        except Exception as e:
            raise e

    @property
    def monitorname(self) :
        """Name of the monitor.<br/>Minimum length =  1."""
        try :
            return self._monitorname
        except Exception as e:
            raise e

    @monitorname.setter
    def monitorname(self, monitorname) :
        """Name of the monitor.<br/>Minimum length =  1

        :param monitorname: 

        """
        try :
            self._monitorname = monitorname
        except Exception as e:
            raise e

    @property
    def metric_unit(self) :
        """Giving the unit of the metric.<br/>Possible values = Bytes/s, ms, pkts/s, users."""
        try :
            return self._metric_unit
        except Exception as e:
            raise e

    @property
    def metrictable(self) :
        """Metric table to which to bind metrics.<br/>Minimum length =  1<br/>Maximum length =  99."""
        try :
            return self._metrictable
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(lbmonitor_metric_binding_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.lbmonitor_metric_binding
        except Exception as e :
            raise e

    def _get_object_name(self) :
        """Returns the value of object identifier argument"""
        try :
            if self.monitorname is not None :
                return str(self.monitorname)
            return None
        except Exception as e :
            raise e



    @classmethod
    def add(cls, client, resource) :
        """

        :param client: 
        :param resource: 

        """
        try :
            if resource and type(resource) is not list :
                updateresource = lbmonitor_metric_binding()
                updateresource.monitorname = resource.monitorname
                updateresource.metric = resource.metric
                updateresource.metricthreshold = resource.metricthreshold
                updateresource.metricweight = resource.metricweight
                return updateresource.update_resource(client)
            else :
                if resource and len(resource) > 0 :
                    updateresources = [lbmonitor_metric_binding() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        updateresources[i].monitorname = resource[i].monitorname
                        updateresources[i].metric = resource[i].metric
                        updateresources[i].metricthreshold = resource[i].metricthreshold
                        updateresources[i].metricweight = resource[i].metricweight
                return cls.update_bulk_request(client, updateresources)
        except Exception as e :
            raise e

    @classmethod
    def delete(cls, client, resource) :
        """

        :param client: 
        :param resource: 

        """
        try :
            if resource and type(resource) is not list :
                deleteresource = lbmonitor_metric_binding()
                deleteresource.monitorname = resource.monitorname
                deleteresource.metric = resource.metric
                return deleteresource.delete_resource(client)
            else :
                if resource and len(resource) > 0 :
                    deleteresources = [lbmonitor_metric_binding() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        deleteresources[i].monitorname = resource[i].monitorname
                        deleteresources[i].metric = resource[i].metric
                return cls.delete_bulk_request(client, deleteresources)
        except Exception as e :
            raise e

    @classmethod
    def get(cls, service, monitorname) :
        """Use this API to fetch lbmonitor_metric_binding resources.

        :param service: 
        :param monitorname: 

        """
        try :
            obj = lbmonitor_metric_binding()
            obj.monitorname = monitorname
            response = obj.get_resources(service)
            return response
        except Exception as e:
            raise e

    @classmethod
    def get_filtered(cls, service, monitorname, filter_) :
        """Use this API to fetch filtered set of lbmonitor_metric_binding resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param service: 
        :param monitorname: 
        :param filter_: 

        """
        try :
            obj = lbmonitor_metric_binding()
            obj.monitorname = monitorname
            option_ = options()
            option_.filter = filter_
            response = obj.getfiltered(service, option_)
            return response
        except Exception as e:
            raise e

    @classmethod
    def count(cls, service, monitorname) :
        """Use this API to count lbmonitor_metric_binding resources configued on NetScaler.

        :param service: 
        :param monitorname: 

        """
        try :
            obj = lbmonitor_metric_binding()
            obj.monitorname = monitorname
            option_ = options()
            option_.count = True
            response = obj.get_resources(service, option_)
            if response :
                return response[0].__dict__['___count']
            return 0
        except Exception as e:
            raise e

    @classmethod
    def count_filtered(cls, service, monitorname, filter_) :
        """Use this API to count the filtered set of lbmonitor_metric_binding resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param service: 
        :param monitorname: 
        :param filter_: 

        """
        try :
            obj = lbmonitor_metric_binding()
            obj.monitorname = monitorname
            option_ = options()
            option_.count = True
            option_.filter = filter_
            response = obj.getfiltered(service, option_)
            if response :
                return response[0].__dict__['___count']
            return 0
        except Exception as e:
            raise e

    class Dup_state:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class State:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Metric_unit:
        """ """
        Bytes_s = "Bytes/s"
        ms = "ms"
        pkts_s = "pkts/s"
        users = "users"

class lbmonitor_metric_binding_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.lbmonitor_metric_binding = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.lbmonitor_metric_binding = [lbmonitor_metric_binding() for _ in range(length)]

