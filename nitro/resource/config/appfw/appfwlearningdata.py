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

class appfwlearningdata(base_resource) :
    """Configuration for learning data resource."""
    def __init__(self) :
        self._profilename = ""
        self._starturl = ""
        self._cookieconsistency = ""
        self._fieldconsistency = ""
        self._formactionurl_ffc = ""
        self._contenttype = ""
        self._crosssitescripting = ""
        self._formactionurl_xss = ""
        self._as_scan_location_xss = ""
        self._as_value_type_xss = ""
        self._as_value_expr_xss = ""
        self._sqlinjection = ""
        self._formactionurl_sql = ""
        self._as_scan_location_sql = ""
        self._as_value_type_sql = ""
        self._as_value_expr_sql = ""
        self._fieldformat = ""
        self._formactionurl_ff = ""
        self._csrftag = ""
        self._csrfformoriginurl = ""
        self._creditcardnumber = ""
        self._creditcardnumberurl = ""
        self._xmldoscheck = ""
        self._xmlwsicheck = ""
        self._xmlattachmentcheck = ""
        self._totalxmlrequests = False
        self._securitycheck = ""
        self._target = ""
        self._url = ""
        self._name = ""
        self._fieldtype = ""
        self._fieldformatminlength = 0
        self._fieldformatmaxlength = 0
        self._fieldformatcharmappcre = ""
        self._value_type = ""
        self._value = ""
        self._hits = 0
        self._data = ""
        self.___count = 0

    @property
    def profilename(self) :
        """Name of the profile."""
        try :
            return self._profilename
        except Exception as e:
            raise e

    @profilename.setter
    def profilename(self, profilename) :
        """Name of the profile.

        :param profilename: 

        """
        try :
            self._profilename = profilename
        except Exception as e:
            raise e

    @property
    def starturl(self) :
        """Start URL configuration.<br/>Minimum length =  1."""
        try :
            return self._starturl
        except Exception as e:
            raise e

    @starturl.setter
    def starturl(self, starturl) :
        """Start URL configuration.<br/>Minimum length =  1

        :param starturl: 

        """
        try :
            self._starturl = starturl
        except Exception as e:
            raise e

    @property
    def cookieconsistency(self) :
        """Cookie Name.<br/>Minimum length =  1."""
        try :
            return self._cookieconsistency
        except Exception as e:
            raise e

    @cookieconsistency.setter
    def cookieconsistency(self, cookieconsistency) :
        """Cookie Name.<br/>Minimum length =  1

        :param cookieconsistency: 

        """
        try :
            self._cookieconsistency = cookieconsistency
        except Exception as e:
            raise e

    @property
    def fieldconsistency(self) :
        """Form field name.<br/>Minimum length =  1."""
        try :
            return self._fieldconsistency
        except Exception as e:
            raise e

    @fieldconsistency.setter
    def fieldconsistency(self, fieldconsistency) :
        """Form field name.<br/>Minimum length =  1

        :param fieldconsistency: 

        """
        try :
            self._fieldconsistency = fieldconsistency
        except Exception as e:
            raise e

    @property
    def formactionurl_ffc(self) :
        """Form action URL."""
        try :
            return self._formactionurl_ffc
        except Exception as e:
            raise e

    @formactionurl_ffc.setter
    def formactionurl_ffc(self, formactionurl_ffc) :
        """Form action URL.

        :param formactionurl_ffc: 

        """
        try :
            self._formactionurl_ffc = formactionurl_ffc
        except Exception as e:
            raise e

    @property
    def contenttype(self) :
        """Content Type Name.<br/>Minimum length =  1."""
        try :
            return self._contenttype
        except Exception as e:
            raise e

    @contenttype.setter
    def contenttype(self, contenttype) :
        """Content Type Name.<br/>Minimum length =  1

        :param contenttype: 

        """
        try :
            self._contenttype = contenttype
        except Exception as e:
            raise e

    @property
    def crosssitescripting(self) :
        """Cross-site scripting.<br/>Minimum length =  1."""
        try :
            return self._crosssitescripting
        except Exception as e:
            raise e

    @crosssitescripting.setter
    def crosssitescripting(self, crosssitescripting) :
        """Cross-site scripting.<br/>Minimum length =  1

        :param crosssitescripting: 

        """
        try :
            self._crosssitescripting = crosssitescripting
        except Exception as e:
            raise e

    @property
    def formactionurl_xss(self) :
        """Form action URL.<br/>Minimum length =  1."""
        try :
            return self._formactionurl_xss
        except Exception as e:
            raise e

    @formactionurl_xss.setter
    def formactionurl_xss(self, formactionurl_xss) :
        """Form action URL.<br/>Minimum length =  1

        :param formactionurl_xss: 

        """
        try :
            self._formactionurl_xss = formactionurl_xss
        except Exception as e:
            raise e

    @property
    def as_scan_location_xss(self) :
        """Location of cross-site scripting exception - form field, header or cookie.<br/>Possible values = FORMFIELD, HEADER, COOKIE."""
        try :
            return self._as_scan_location_xss
        except Exception as e:
            raise e

    @as_scan_location_xss.setter
    def as_scan_location_xss(self, as_scan_location_xss) :
        """Location of cross-site scripting exception - form field, header or cookie.<br/>Possible values = FORMFIELD, HEADER, COOKIE

        :param as_scan_location_xss: 

        """
        try :
            self._as_scan_location_xss = as_scan_location_xss
        except Exception as e:
            raise e

    @property
    def as_value_type_xss(self) :
        """XSS value type. (Tag | Attribute | Pattern).<br/>Possible values = Tag, Attribute, Pattern."""
        try :
            return self._as_value_type_xss
        except Exception as e:
            raise e

    @as_value_type_xss.setter
    def as_value_type_xss(self, as_value_type_xss) :
        """XSS value type. (Tag | Attribute | Pattern).<br/>Possible values = Tag, Attribute, Pattern

        :param as_value_type_xss: 

        """
        try :
            self._as_value_type_xss = as_value_type_xss
        except Exception as e:
            raise e

    @property
    def as_value_expr_xss(self) :
        """XSS value expressions consistituting expressions for Tag, Attribute or Pattern."""
        try :
            return self._as_value_expr_xss
        except Exception as e:
            raise e

    @as_value_expr_xss.setter
    def as_value_expr_xss(self, as_value_expr_xss) :
        """XSS value expressions consistituting expressions for Tag, Attribute or Pattern.

        :param as_value_expr_xss: 

        """
        try :
            self._as_value_expr_xss = as_value_expr_xss
        except Exception as e:
            raise e

    @property
    def sqlinjection(self) :
        """Form field name.<br/>Minimum length =  1."""
        try :
            return self._sqlinjection
        except Exception as e:
            raise e

    @sqlinjection.setter
    def sqlinjection(self, sqlinjection) :
        """Form field name.<br/>Minimum length =  1

        :param sqlinjection: 

        """
        try :
            self._sqlinjection = sqlinjection
        except Exception as e:
            raise e

    @property
    def formactionurl_sql(self) :
        """Form action URL.<br/>Minimum length =  1."""
        try :
            return self._formactionurl_sql
        except Exception as e:
            raise e

    @formactionurl_sql.setter
    def formactionurl_sql(self, formactionurl_sql) :
        """Form action URL.<br/>Minimum length =  1

        :param formactionurl_sql: 

        """
        try :
            self._formactionurl_sql = formactionurl_sql
        except Exception as e:
            raise e

    @property
    def as_scan_location_sql(self) :
        """Location of sql injection exception - form field, header or cookie.<br/>Possible values = FORMFIELD, HEADER, COOKIE."""
        try :
            return self._as_scan_location_sql
        except Exception as e:
            raise e

    @as_scan_location_sql.setter
    def as_scan_location_sql(self, as_scan_location_sql) :
        """Location of sql injection exception - form field, header or cookie.<br/>Possible values = FORMFIELD, HEADER, COOKIE

        :param as_scan_location_sql: 

        """
        try :
            self._as_scan_location_sql = as_scan_location_sql
        except Exception as e:
            raise e

    @property
    def as_value_type_sql(self) :
        """SQL value type. Keyword, SpecialString or Wildchar.<br/>Possible values = Keyword, SpecialString, Wildchar."""
        try :
            return self._as_value_type_sql
        except Exception as e:
            raise e

    @as_value_type_sql.setter
    def as_value_type_sql(self, as_value_type_sql) :
        """SQL value type. Keyword, SpecialString or Wildchar.<br/>Possible values = Keyword, SpecialString, Wildchar

        :param as_value_type_sql: 

        """
        try :
            self._as_value_type_sql = as_value_type_sql
        except Exception as e:
            raise e

    @property
    def as_value_expr_sql(self) :
        """SQL value expressions consistituting expressions for Keyword, SpecialString or Wildchar."""
        try :
            return self._as_value_expr_sql
        except Exception as e:
            raise e

    @as_value_expr_sql.setter
    def as_value_expr_sql(self, as_value_expr_sql) :
        """SQL value expressions consistituting expressions for Keyword, SpecialString or Wildchar.

        :param as_value_expr_sql: 

        """
        try :
            self._as_value_expr_sql = as_value_expr_sql
        except Exception as e:
            raise e

    @property
    def fieldformat(self) :
        """Field format name.<br/>Minimum length =  1."""
        try :
            return self._fieldformat
        except Exception as e:
            raise e

    @fieldformat.setter
    def fieldformat(self, fieldformat) :
        """Field format name.<br/>Minimum length =  1

        :param fieldformat: 

        """
        try :
            self._fieldformat = fieldformat
        except Exception as e:
            raise e

    @property
    def formactionurl_ff(self) :
        """Form action URL.<br/>Minimum length =  1."""
        try :
            return self._formactionurl_ff
        except Exception as e:
            raise e

    @formactionurl_ff.setter
    def formactionurl_ff(self, formactionurl_ff) :
        """Form action URL.<br/>Minimum length =  1

        :param formactionurl_ff: 

        """
        try :
            self._formactionurl_ff = formactionurl_ff
        except Exception as e:
            raise e

    @property
    def csrftag(self) :
        """CSRF Form Action URL.<br/>Minimum length =  1."""
        try :
            return self._csrftag
        except Exception as e:
            raise e

    @csrftag.setter
    def csrftag(self, csrftag) :
        """CSRF Form Action URL.<br/>Minimum length =  1

        :param csrftag: 

        """
        try :
            self._csrftag = csrftag
        except Exception as e:
            raise e

    @property
    def csrfformoriginurl(self) :
        """CSRF Form Origin URL.<br/>Minimum length =  1."""
        try :
            return self._csrfformoriginurl
        except Exception as e:
            raise e

    @csrfformoriginurl.setter
    def csrfformoriginurl(self, csrfformoriginurl) :
        """CSRF Form Origin URL.<br/>Minimum length =  1

        :param csrfformoriginurl: 

        """
        try :
            self._csrfformoriginurl = csrfformoriginurl
        except Exception as e:
            raise e

    @property
    def creditcardnumber(self) :
        """The object expression that is to be excluded from safe commerce check.<br/>Minimum length =  1."""
        try :
            return self._creditcardnumber
        except Exception as e:
            raise e

    @creditcardnumber.setter
    def creditcardnumber(self, creditcardnumber) :
        """The object expression that is to be excluded from safe commerce check.<br/>Minimum length =  1

        :param creditcardnumber: 

        """
        try :
            self._creditcardnumber = creditcardnumber
        except Exception as e:
            raise e

    @property
    def creditcardnumberurl(self) :
        """The url for which the list of credit card numbers are needed to be bypassed from inspection.<br/>Minimum length =  1."""
        try :
            return self._creditcardnumberurl
        except Exception as e:
            raise e

    @creditcardnumberurl.setter
    def creditcardnumberurl(self, creditcardnumberurl) :
        """The url for which the list of credit card numbers are needed to be bypassed from inspection.<br/>Minimum length =  1

        :param creditcardnumberurl: 

        """
        try :
            self._creditcardnumberurl = creditcardnumberurl
        except Exception as e:
            raise e

    @property
    def xmldoscheck(self) :
        """XML Denial of Service check, one of
        MaxAttributes
        MaxAttributeNameLength
        MaxAttributeValueLength
        MaxElementNameLength
        MaxFileSize
        MinFileSize
        MaxCDATALength
        MaxElements
        MaxElementDepth
        MaxElementChildren
        NumDTDs
        NumProcessingInstructions
        NumExternalEntities
        MaxEntityExpansions
        MaxEntityExpansionDepth
        MaxNamespaces
        MaxNamespaceUriLength
        MaxSOAPArraySize
        MaxSOAPArrayRank
        .<br/>Minimum length =  1.


        """
        try :
            return self._xmldoscheck
        except Exception as e:
            raise e

    @xmldoscheck.setter
    def xmldoscheck(self, xmldoscheck) :
        """XML Denial of Service check, one of
        MaxAttributes
        MaxAttributeNameLength
        MaxAttributeValueLength
        MaxElementNameLength
        MaxFileSize
        MinFileSize
        MaxCDATALength
        MaxElements
        MaxElementDepth
        MaxElementChildren
        NumDTDs
        NumProcessingInstructions
        NumExternalEntities
        MaxEntityExpansions
        MaxEntityExpansionDepth
        MaxNamespaces
        MaxNamespaceUriLength
        MaxSOAPArraySize
        MaxSOAPArrayRank
        .<br/>Minimum length =  1

        :param xmldoscheck: 

        """
        try :
            self._xmldoscheck = xmldoscheck
        except Exception as e:
            raise e

    @property
    def xmlwsicheck(self) :
        """Web Services Interoperability Rule ID.<br/>Minimum length =  1."""
        try :
            return self._xmlwsicheck
        except Exception as e:
            raise e

    @xmlwsicheck.setter
    def xmlwsicheck(self, xmlwsicheck) :
        """Web Services Interoperability Rule ID.<br/>Minimum length =  1

        :param xmlwsicheck: 

        """
        try :
            self._xmlwsicheck = xmlwsicheck
        except Exception as e:
            raise e

    @property
    def xmlattachmentcheck(self) :
        """XML Attachment Content-Type.<br/>Minimum length =  1."""
        try :
            return self._xmlattachmentcheck
        except Exception as e:
            raise e

    @xmlattachmentcheck.setter
    def xmlattachmentcheck(self, xmlattachmentcheck) :
        """XML Attachment Content-Type.<br/>Minimum length =  1

        :param xmlattachmentcheck: 

        """
        try :
            self._xmlattachmentcheck = xmlattachmentcheck
        except Exception as e:
            raise e

    @property
    def totalxmlrequests(self) :
        """Total XML requests."""
        try :
            return self._totalxmlrequests
        except Exception as e:
            raise e

    @totalxmlrequests.setter
    def totalxmlrequests(self, totalxmlrequests) :
        """Total XML requests.

        :param totalxmlrequests: 

        """
        try :
            self._totalxmlrequests = totalxmlrequests
        except Exception as e:
            raise e

    @property
    def securitycheck(self) :
        """Name of the security check.<br/>Possible values = startURL, cookieConsistency, fieldConsistency, crossSiteScripting, SQLInjection, fieldFormat, CSRFtag, XMLDoSCheck, XMLWSICheck, XMLAttachmentCheck, TotalXMLRequests, creditCardNumber, ContentType."""
        try :
            return self._securitycheck
        except Exception as e:
            raise e

    @securitycheck.setter
    def securitycheck(self, securitycheck) :
        """Name of the security check.<br/>Possible values = startURL, cookieConsistency, fieldConsistency, crossSiteScripting, SQLInjection, fieldFormat, CSRFtag, XMLDoSCheck, XMLWSICheck, XMLAttachmentCheck, TotalXMLRequests, creditCardNumber, ContentType

        :param securitycheck: 

        """
        try :
            self._securitycheck = securitycheck
        except Exception as e:
            raise e

    @property
    def target(self) :
        """Target filename for data to be exported.<br/>Minimum length =  1<br/>Maximum length =  127."""
        try :
            return self._target
        except Exception as e:
            raise e

    @target.setter
    def target(self, target) :
        """Target filename for data to be exported.<br/>Minimum length =  1<br/>Maximum length =  127

        :param target: 

        """
        try :
            self._target = target
        except Exception as e:
            raise e

    @property
    def url(self) :
        """Learnt url."""
        try :
            return self._url
        except Exception as e:
            raise e

    @property
    def name(self) :
        """Learnt field name."""
        try :
            return self._name
        except Exception as e:
            raise e

    @property
    def fieldtype(self) :
        """Learnt field type."""
        try :
            return self._fieldtype
        except Exception as e:
            raise e

    @property
    def fieldformatminlength(self) :
        """The minimum allowed length for data in this form field."""
        try :
            return self._fieldformatminlength
        except Exception as e:
            raise e

    @property
    def fieldformatmaxlength(self) :
        """The maximum allowed length for data in this form field."""
        try :
            return self._fieldformatmaxlength
        except Exception as e:
            raise e

    @property
    def fieldformatcharmappcre(self) :
        """Form field value allowed character map."""
        try :
            return self._fieldformatcharmappcre
        except Exception as e:
            raise e

    @property
    def value_type(self) :
        """Learnt field value type."""
        try :
            return self._value_type
        except Exception as e:
            raise e

    @property
    def value(self) :
        """Learnt field value."""
        try :
            return self._value
        except Exception as e:
            raise e

    @property
    def hits(self) :
        """Learnt entity hit count."""
        try :
            return self._hits
        except Exception as e:
            raise e

    @property
    def data(self) :
        """Learned data."""
        try :
            return self._data
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(appfwlearningdata_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.appfwlearningdata
        except Exception as e :
            raise e

    def _get_object_name(self) :
        """Returns the value of object identifier argument"""
        try :
            return 0
        except Exception as e :
            raise e



    @classmethod
    def delete(cls, client, resource) :
        """Use this API to delete appfwlearningdata.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                deleteresource = appfwlearningdata()
                deleteresource.profilename = resource.profilename
                deleteresource.starturl = resource.starturl
                deleteresource.cookieconsistency = resource.cookieconsistency
                deleteresource.fieldconsistency = resource.fieldconsistency
                deleteresource.formactionurl_ffc = resource.formactionurl_ffc
                deleteresource.contenttype = resource.contenttype
                deleteresource.crosssitescripting = resource.crosssitescripting
                deleteresource.formactionurl_xss = resource.formactionurl_xss
                deleteresource.as_scan_location_xss = resource.as_scan_location_xss
                deleteresource.as_value_type_xss = resource.as_value_type_xss
                deleteresource.as_value_expr_xss = resource.as_value_expr_xss
                deleteresource.sqlinjection = resource.sqlinjection
                deleteresource.formactionurl_sql = resource.formactionurl_sql
                deleteresource.as_scan_location_sql = resource.as_scan_location_sql
                deleteresource.as_value_type_sql = resource.as_value_type_sql
                deleteresource.as_value_expr_sql = resource.as_value_expr_sql
                deleteresource.fieldformat = resource.fieldformat
                deleteresource.formactionurl_ff = resource.formactionurl_ff
                deleteresource.csrftag = resource.csrftag
                deleteresource.csrfformoriginurl = resource.csrfformoriginurl
                deleteresource.creditcardnumber = resource.creditcardnumber
                deleteresource.creditcardnumberurl = resource.creditcardnumberurl
                deleteresource.xmldoscheck = resource.xmldoscheck
                deleteresource.xmlwsicheck = resource.xmlwsicheck
                deleteresource.xmlattachmentcheck = resource.xmlattachmentcheck
                deleteresource.totalxmlrequests = resource.totalxmlrequests
                return deleteresource.delete_resource(client)
            else :
                if (resource and len(resource) > 0) :
                    deleteresources = [ appfwlearningdata() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        deleteresources[i].profilename = resource[i].profilename
                        deleteresources[i].starturl = resource[i].starturl
                        deleteresources[i].cookieconsistency = resource[i].cookieconsistency
                        deleteresources[i].fieldconsistency = resource[i].fieldconsistency
                        deleteresources[i].formactionurl_ffc = resource[i].formactionurl_ffc
                        deleteresources[i].contenttype = resource[i].contenttype
                        deleteresources[i].crosssitescripting = resource[i].crosssitescripting
                        deleteresources[i].formactionurl_xss = resource[i].formactionurl_xss
                        deleteresources[i].as_scan_location_xss = resource[i].as_scan_location_xss
                        deleteresources[i].as_value_type_xss = resource[i].as_value_type_xss
                        deleteresources[i].as_value_expr_xss = resource[i].as_value_expr_xss
                        deleteresources[i].sqlinjection = resource[i].sqlinjection
                        deleteresources[i].formactionurl_sql = resource[i].formactionurl_sql
                        deleteresources[i].as_scan_location_sql = resource[i].as_scan_location_sql
                        deleteresources[i].as_value_type_sql = resource[i].as_value_type_sql
                        deleteresources[i].as_value_expr_sql = resource[i].as_value_expr_sql
                        deleteresources[i].fieldformat = resource[i].fieldformat
                        deleteresources[i].formactionurl_ff = resource[i].formactionurl_ff
                        deleteresources[i].csrftag = resource[i].csrftag
                        deleteresources[i].csrfformoriginurl = resource[i].csrfformoriginurl
                        deleteresources[i].creditcardnumber = resource[i].creditcardnumber
                        deleteresources[i].creditcardnumberurl = resource[i].creditcardnumberurl
                        deleteresources[i].xmldoscheck = resource[i].xmldoscheck
                        deleteresources[i].xmlwsicheck = resource[i].xmlwsicheck
                        deleteresources[i].xmlattachmentcheck = resource[i].xmlattachmentcheck
                        deleteresources[i].totalxmlrequests = resource[i].totalxmlrequests
                result = cls.delete_bulk_request(client, deleteresources)
            return result
        except Exception as e :
            raise e

    @classmethod
    def reset(cls, client, resource="") :
        """Use this API to reset appfwlearningdata.

        :param client: 
        :param resource:  (Default value = "")

        """
        try :
            if type(resource) is not list :
                resetresource = appfwlearningdata()
                return resetresource.perform_operation(client,"reset")
            else :
                if (resource and len(resource) > 0) :
                    resetresources = [ appfwlearningdata() for _ in range(len(resource))]
                result = cls.perform_operation_bulk_request(client, resetresources,"reset")
            return result
        except Exception as e :
            raise e

    @classmethod
    def export(cls, client, resource) :
        """Use this API to export appfwlearningdata.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                exportresource = appfwlearningdata()
                exportresource.profilename = resource.profilename
                exportresource.securitycheck = resource.securitycheck
                exportresource.target = resource.target
                return exportresource.perform_operation(client,"export")
            else :
                if (resource and len(resource) > 0) :
                    exportresources = [ appfwlearningdata() for _ in range(len(resource))]
                    for i in range(len(resource)) :
                        exportresources[i].profilename = resource[i].profilename
                        exportresources[i].securitycheck = resource[i].securitycheck
                        exportresources[i].target = resource[i].target
                result = cls.perform_operation_bulk_request(client, exportresources,"export")
            return result
        except Exception as e :
            raise e

    @classmethod
    def get(cls, client, name="", option_="") :
        """Use this API to fetch all the appfwlearningdata resources that are configured on netscaler.

        :param client: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            if type(name) == cls :
                if type(name) is not list :
                    option_ = options()
                    option_.args = nitro_util.object_to_string_withoutquotes(name)
                    response = name.get_resource(client, option_)
                else :
                    if name and len(name) > 0 :
                        response = [appfwlearningdata() for _ in range(len(name))]
                        for i in range(len(name)) :
                            option_ = options()
                            option_.args = nitro_util.object_to_string_withoutquotes(name[i])
                            response[i] = name[i].get_resource(client, option_)
                return response
        except Exception as e :
            raise e


    @classmethod
    def get_args(cls, client, args) :
        """Use this API to fetch all the appfwlearningdata resources that are configured on netscaler.
            # This uses appfwlearningdata_args which is a way to provide additional arguments while fetching the resources.

        :param client: 
        :param args: 

        """
        try :
            obj = appfwlearningdata()
            option_ = options()
            option_.args = nitro_util.object_to_string_withoutquotes(args)
            response = obj.get_resources(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def get_filtered(cls, client, filter_, obj) :
        """Use this API to fetch filtered set of appfwlearningdata resources.
        filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 
        :param obj: 

        """
        try :
            option_ = options()
            option_.filter = filter_
            option_.args = nitro_util.object_to_string_withoutquotes(obj)
            response = obj.getfiltered(client, option_)
            return response
        except Exception as e :
            raise e


    @classmethod
    def count(cls, client, obj) :
        """Use this API to count the appfwlearningdata resources configured on NetScaler.

        :param client: 
        :param obj: 

        """
        try :
            option_ = options()
            option_.count = True
            option_.args = nitro_util.object_to_string_withoutquotes(obj)
            response = obj.get_resources(client, option_)
            if response :
                return response[0].__dict__['___count']
            return 0
        except Exception as e :
            raise e

    @classmethod
    def count_filtered(cls, client, filter_, obj) :
        """Use this API to count filtered the set of appfwlearningdata resources.
        Filter string should be in JSON format.eg: "port:80,servicetype:HTTP".

        :param client: 
        :param filter_: 
        :param obj: 

        """
        try :
            option_ = options()
            option_.count = True
            option_.filter = filter_
            option_.args = nitro_util.object_to_string_withoutquotes(obj)
            response = obj.getfiltered(client, option_)
            if response :
                return response[0].__dict__['___count']
            return 0
        except Exception as e :
            raise e


    class As_scan_location_xss:
        """ """
        FORMFIELD = "FORMFIELD"
        HEADER = "HEADER"
        COOKIE = "COOKIE"

    class As_scan_location_sql:
        """ """
        FORMFIELD = "FORMFIELD"
        HEADER = "HEADER"
        COOKIE = "COOKIE"

    class Securitycheck:
        """ """
        startURL = "startURL"
        cookieConsistency = "cookieConsistency"
        fieldConsistency = "fieldConsistency"
        crossSiteScripting = "crossSiteScripting"
        SQLInjection = "SQLInjection"
        fieldFormat = "fieldFormat"
        CSRFtag = "CSRFtag"
        XMLDoSCheck = "XMLDoSCheck"
        XMLWSICheck = "XMLWSICheck"
        XMLAttachmentCheck = "XMLAttachmentCheck"
        TotalXMLRequests = "TotalXMLRequests"
        creditCardNumber = "creditCardNumber"
        ContentType = "ContentType"

    class As_value_type_sql:
        """ """
        Keyword = "Keyword"
        SpecialString = "SpecialString"
        Wildchar = "Wildchar"

    class As_value_type_xss:
        """ """
        Tag = "Tag"
        Attribute = "Attribute"
        Pattern = "Pattern"

class appfwlearningdata_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.appfwlearningdata = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.appfwlearningdata = [appfwlearningdata() for _ in range(length)]

