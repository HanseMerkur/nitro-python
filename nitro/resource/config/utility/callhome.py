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

class callhome(base_resource) :
	""" Configuration for callhome resource. """
	def __init__(self) :
		self._emailaddress = ""
		self._proxymode = ""
		self._ipaddress = ""
		self._port = 0
		self._sslcardfirstfailure = ""
		self._sslcardlatestfailure = ""
		self._powfirstfail = ""
		self._powlatestfailure = ""
		self._hddfirstfail = ""
		self._hddlatestfailure = ""
		self._flashfirstfail = ""
		self._flashlatestfailure = ""
		self._restartlatestfail = ""
		self._callhomestatus = []

	@property
	def emailaddress(self) :
		r"""The contact person's E-mail address.<br/>Maximum length =  78.
		"""
		try :
			return self._emailaddress
		except Exception as e:
			raise e

	@emailaddress.setter
	def emailaddress(self, emailaddress) :
		r"""The contact person's E-mail address.<br/>Maximum length =  78
		"""
		try :
			self._emailaddress = emailaddress
		except Exception as e:
			raise e

	@property
	def proxymode(self) :
		r"""Deploy the callhome proxy mode.<br/>Default value: NO<br/>Possible values = YES, NO.
		"""
		try :
			return self._proxymode
		except Exception as e:
			raise e

	@proxymode.setter
	def proxymode(self, proxymode) :
		r"""Deploy the callhome proxy mode.<br/>Default value: NO<br/>Possible values = YES, NO
		"""
		try :
			self._proxymode = proxymode
		except Exception as e:
			raise e

	@property
	def ipaddress(self) :
		r"""Proxy Server IP address.<br/>Minimum length =  1.
		"""
		try :
			return self._ipaddress
		except Exception as e:
			raise e

	@ipaddress.setter
	def ipaddress(self, ipaddress) :
		r"""Proxy Server IP address.<br/>Minimum length =  1
		"""
		try :
			self._ipaddress = ipaddress
		except Exception as e:
			raise e

	@property
	def port(self) :
		r"""Proxy Server Port.<br/>Minimum length =  1<br/>Range 1 - 65535.
		"""
		try :
			return self._port
		except Exception as e:
			raise e

	@port.setter
	def port(self, port) :
		r"""Proxy Server Port.<br/>Minimum length =  1<br/>Range 1 - 65535
		"""
		try :
			self._port = port
		except Exception as e:
			raise e

	@property
	def sslcardfirstfailure(self) :
		r"""First occurrence SSL card failure.
		"""
		try :
			return self._sslcardfirstfailure
		except Exception as e:
			raise e

	@property
	def sslcardlatestfailure(self) :
		r"""Latest occurrence SSL card failure.
		"""
		try :
			return self._sslcardlatestfailure
		except Exception as e:
			raise e

	@property
	def powfirstfail(self) :
		r"""First occurrence power supply unit failure.
		"""
		try :
			return self._powfirstfail
		except Exception as e:
			raise e

	@property
	def powlatestfailure(self) :
		r"""Latest occurrence power supply unit failure.
		"""
		try :
			return self._powlatestfailure
		except Exception as e:
			raise e

	@property
	def hddfirstfail(self) :
		r"""First occurrence hard disk drive failure.
		"""
		try :
			return self._hddfirstfail
		except Exception as e:
			raise e

	@property
	def hddlatestfailure(self) :
		r"""Latest occurrence hard disk drive failure.
		"""
		try :
			return self._hddlatestfailure
		except Exception as e:
			raise e

	@property
	def flashfirstfail(self) :
		r"""First occurrence compact flash failure.
		"""
		try :
			return self._flashfirstfail
		except Exception as e:
			raise e

	@property
	def flashlatestfailure(self) :
		r"""Latest occurrence compact flush failure.
		"""
		try :
			return self._flashlatestfailure
		except Exception as e:
			raise e

	@property
	def restartlatestfail(self) :
		r"""Latest occurrence warm restart failure.
		"""
		try :
			return self._restartlatestfail
		except Exception as e:
			raise e

	@property
	def callhomestatus(self) :
		r"""Callhome feature enabled/disable, register with upload server successful/failed.<br/>Possible values = ENABLED, DISABLED, SUCCESSFUL, FAILED.
		"""
		try :
			return self._callhomestatus
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(callhome_response, response, self.__class__.__name__)
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.callhome
		except Exception as e :
			raise e

	def _get_object_name(self) :
		r""" Returns the value of object identifier argument
		"""
		try :
			return 0
		except Exception as e :
			raise e



	@classmethod
	def update(cls, client, resource) :
		r""" Use this API to update callhome.
		"""
		try :
			if type(resource) is not list :
				updateresource = callhome()
				updateresource.emailaddress = resource.emailaddress
				updateresource.proxymode = resource.proxymode
				updateresource.ipaddress = resource.ipaddress
				updateresource.port = resource.port
				return updateresource.update_resource(client)
		except Exception as e :
			raise e

	@classmethod
	def unset(cls, client, resource, args) :
		r""" Use this API to unset the properties of callhome resource.
		Properties that need to be unset are specified in args array.
		"""
		try :
			if type(resource) is not list :
				unsetresource = callhome()
				return unsetresource.unset_resource(client, args)
		except Exception as e :
			raise e

	@classmethod
	def get(cls, client, name="", option_="") :
		r""" Use this API to fetch all the callhome resources that are configured on netscaler.
		"""
		try :
			if not name :
				obj = callhome()
				response = obj.get_resources(client, option_)
			return response
		except Exception as e :
			raise e


	class Callhomestatus:
		ENABLED = "ENABLED"
		DISABLED = "DISABLED"
		SUCCESSFUL = "SUCCESSFUL"
		FAILED = "FAILED"

	class Proxymode:
		YES = "YES"
		NO = "NO"

class callhome_response(base_response) :
	def __init__(self, length=1) :
		self.callhome = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.callhome = [callhome() for _ in range(length)]

