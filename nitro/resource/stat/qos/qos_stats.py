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

class qos_stats(base_resource) :
	def __init__(self) :
		self._clearstats = ""
		self._ipcmessagessent = 0
		self._ipcmessagessentrate = 0
		self._ipcmessagesfailed = 0
		self._ipcmessagesfailedrate = 0
		self._ipcmessagesreceived = 0
		self._ipcmessagesreceivedrate = 0
		self._ipcpe2qossent = 0
		self._ipcpe2qossentrate = 0
		self._ipcpe2qosfailed = 0
		self._ipcpe2qosfailedrate = 0
		self._ipcpe2qosreceived = 0
		self._ipcpe2qosreceivedrate = 0
		self._qosbytesdropped = 0
		self._qosbytesdroppedrate = 0
		self._qosbytessentnotclassified = 0
		self._qosbytessentnotclassifiedrate = 0
		self._qosbytesdroppednoconnection = 0
		self._qosbytesdroppednoconnectionrate = 0
		self._qosinputpackets = 0
		self._qosinputpacketsrate = 0
		self._qosoutputpackets = 0
		self._qosoutputpacketsrate = 0
		self._qosdroppackets = 0
		self._qosdroppacketsrate = 0
		self._qosrewritemacs = 0
		self._qosrewritemacsrate = 0
		self._qospacketsunclassified = 0
		self._qospacketsunclassifiedrate = 0
		self._qospacketsclassified = 0
		self._qospacketsclassifiedrate = 0
		self._qoslearnedmac = 0
		self._qoslearnedmacrate = 0
		self._qosinputbytes = 0
		self._qosinputbytesrate = 0
		self._qosoutputbytes = 0
		self._qosoutputbytesrate = 0
		self._qosfreeheldlist = 0
		self._qoslink00sent = 0
		self._qoslink00sentrate = 0
		self._qoslink00drop = 0
		self._qoslink00droprate = 0
		self._qoslink01sent = 0
		self._qoslink01sentrate = 0
		self._qoslink01drop = 0
		self._qoslink01droprate = 0
		self._qoslink02sent = 0
		self._qoslink02sentrate = 0
		self._qoslink02drop = 0
		self._qoslink02droprate = 0
		self._qoslink03sent = 0
		self._qoslink03sentrate = 0
		self._qoslink03drop = 0
		self._qoslink03droprate = 0
		self._qoslink04sent = 0
		self._qoslink04sentrate = 0
		self._qoslink04drop = 0
		self._qoslink04droprate = 0
		self._qoslink05sent = 0
		self._qoslink05sentrate = 0
		self._qoslink05drop = 0
		self._qoslink05droprate = 0
		self._qoslink06sent = 0
		self._qoslink06sentrate = 0
		self._qoslink06drop = 0
		self._qoslink06droprate = 0
		self._qoslink07sent = 0
		self._qoslink07sentrate = 0
		self._qoslink07drop = 0
		self._qoslink07droprate = 0
		self._qoslink08sent = 0
		self._qoslink08sentrate = 0
		self._qoslink08drop = 0
		self._qoslink08droprate = 0
		self._qoslink09sent = 0
		self._qoslink09sentrate = 0
		self._qoslink09drop = 0
		self._qoslink09droprate = 0
		self._qoslink10sent = 0
		self._qoslink10sentrate = 0
		self._qoslink10drop = 0
		self._qoslink10droprate = 0

	@property
	def clearstats(self) :
		r"""Clear the statsistics / counters.<br/>Possible values = basic, full.
		"""
		try :
			return self._clearstats
		except Exception as e:
			raise e

	@clearstats.setter
	def clearstats(self, clearstats) :
		r"""Clear the statsistics / counters
		"""
		try :
			self._clearstats = clearstats
		except Exception as e:
			raise e

	@property
	def qoslink06droprate(self) :
		r"""Rate (/s) counter for qoslink06drop.
		"""
		try :
			return self._qoslink06droprate
		except Exception as e:
			raise e

	@property
	def ipcpe2qosfailed(self) :
		r"""IPC messages failed to send to qos system.
		"""
		try :
			return self._ipcpe2qosfailed
		except Exception as e:
			raise e

	@property
	def qoslink02sent(self) :
		r"""QoS bytes sent on Link 02.
		"""
		try :
			return self._qoslink02sent
		except Exception as e:
			raise e

	@property
	def qoslink10sent(self) :
		r"""QoS bytes sent on Link 10.
		"""
		try :
			return self._qoslink10sent
		except Exception as e:
			raise e

	@property
	def ipcmessagessentrate(self) :
		r"""Rate (/s) counter for ipcmessagessent.
		"""
		try :
			return self._ipcmessagessentrate
		except Exception as e:
			raise e

	@property
	def qoslink02sentrate(self) :
		r"""Rate (/s) counter for qoslink02sent.
		"""
		try :
			return self._qoslink02sentrate
		except Exception as e:
			raise e

	@property
	def qosrewritemacsrate(self) :
		r"""Rate (/s) counter for qosrewritemacs.
		"""
		try :
			return self._qosrewritemacsrate
		except Exception as e:
			raise e

	@property
	def qoslink08sentrate(self) :
		r"""Rate (/s) counter for qoslink08sent.
		"""
		try :
			return self._qoslink08sentrate
		except Exception as e:
			raise e

	@property
	def qoslink04drop(self) :
		r"""QoS bytes dropped on Link 04.
		"""
		try :
			return self._qoslink04drop
		except Exception as e:
			raise e

	@property
	def qoslink01droprate(self) :
		r"""Rate (/s) counter for qoslink01drop.
		"""
		try :
			return self._qoslink01droprate
		except Exception as e:
			raise e

	@property
	def qosoutputbytesrate(self) :
		r"""Rate (/s) counter for qosoutputbytes.
		"""
		try :
			return self._qosoutputbytesrate
		except Exception as e:
			raise e

	@property
	def qoslink08drop(self) :
		r"""QoS bytes dropped on Link 08.
		"""
		try :
			return self._qoslink08drop
		except Exception as e:
			raise e

	@property
	def qoslink05sent(self) :
		r"""QoS bytes sent on Link 05.
		"""
		try :
			return self._qoslink05sent
		except Exception as e:
			raise e

	@property
	def qoslink10droprate(self) :
		r"""Rate (/s) counter for qoslink10drop.
		"""
		try :
			return self._qoslink10droprate
		except Exception as e:
			raise e

	@property
	def qoslink00drop(self) :
		r"""QoS bytes dropped on Link 00.
		"""
		try :
			return self._qoslink00drop
		except Exception as e:
			raise e

	@property
	def ipcmessagesfailedrate(self) :
		r"""Rate (/s) counter for ipcmessagesfailed.
		"""
		try :
			return self._ipcmessagesfailedrate
		except Exception as e:
			raise e

	@property
	def qoslink05droprate(self) :
		r"""Rate (/s) counter for qoslink05drop.
		"""
		try :
			return self._qoslink05droprate
		except Exception as e:
			raise e

	@property
	def qoslink08droprate(self) :
		r"""Rate (/s) counter for qoslink08drop.
		"""
		try :
			return self._qoslink08droprate
		except Exception as e:
			raise e

	@property
	def qosbytessentnotclassifiedrate(self) :
		r"""Rate (/s) counter for qosbytessentnotclassified.
		"""
		try :
			return self._qosbytessentnotclassifiedrate
		except Exception as e:
			raise e

	@property
	def qoslink03droprate(self) :
		r"""Rate (/s) counter for qoslink03drop.
		"""
		try :
			return self._qoslink03droprate
		except Exception as e:
			raise e

	@property
	def qoslink09sent(self) :
		r"""QoS bytes sent on Link 09.
		"""
		try :
			return self._qoslink09sent
		except Exception as e:
			raise e

	@property
	def qospacketsunclassifiedrate(self) :
		r"""Rate (/s) counter for qospacketsunclassified.
		"""
		try :
			return self._qospacketsunclassifiedrate
		except Exception as e:
			raise e

	@property
	def qosfreeheldlist(self) :
		r"""No. more packets QoS can hold onto.
		"""
		try :
			return self._qosfreeheldlist
		except Exception as e:
			raise e

	@property
	def qospacketsclassified(self) :
		r"""Number of packets with classification.
		"""
		try :
			return self._qospacketsclassified
		except Exception as e:
			raise e

	@property
	def qosbytesdroppednoconnectionrate(self) :
		r"""Rate (/s) counter for qosbytesdroppednoconnection.
		"""
		try :
			return self._qosbytesdroppednoconnectionrate
		except Exception as e:
			raise e

	@property
	def qoslink01sentrate(self) :
		r"""Rate (/s) counter for qoslink01sent.
		"""
		try :
			return self._qoslink01sentrate
		except Exception as e:
			raise e

	@property
	def qoslink09sentrate(self) :
		r"""Rate (/s) counter for qoslink09sent.
		"""
		try :
			return self._qoslink09sentrate
		except Exception as e:
			raise e

	@property
	def qoslink03drop(self) :
		r"""QoS bytes dropped on Link 03.
		"""
		try :
			return self._qoslink03drop
		except Exception as e:
			raise e

	@property
	def qoslink03sentrate(self) :
		r"""Rate (/s) counter for qoslink03sent.
		"""
		try :
			return self._qoslink03sentrate
		except Exception as e:
			raise e

	@property
	def qoslink02drop(self) :
		r"""QoS bytes dropped on Link 02.
		"""
		try :
			return self._qoslink02drop
		except Exception as e:
			raise e

	@property
	def qosinputbytes(self) :
		r"""Bytes sent to QoS for scheduling.
		"""
		try :
			return self._qosinputbytes
		except Exception as e:
			raise e

	@property
	def qosinputpacketsrate(self) :
		r"""Rate (/s) counter for qosinputpackets.
		"""
		try :
			return self._qosinputpacketsrate
		except Exception as e:
			raise e

	@property
	def qosoutputbytes(self) :
		r"""Bytes received from QoS to be sent.
		"""
		try :
			return self._qosoutputbytes
		except Exception as e:
			raise e

	@property
	def ipcmessagesfailed(self) :
		r"""IPC messages failed to send from qos system.
		"""
		try :
			return self._ipcmessagesfailed
		except Exception as e:
			raise e

	@property
	def qoslink07sentrate(self) :
		r"""Rate (/s) counter for qoslink07sent.
		"""
		try :
			return self._qoslink07sentrate
		except Exception as e:
			raise e

	@property
	def qosinputbytesrate(self) :
		r"""Rate (/s) counter for qosinputbytes.
		"""
		try :
			return self._qosinputbytesrate
		except Exception as e:
			raise e

	@property
	def qoslink04droprate(self) :
		r"""Rate (/s) counter for qoslink04drop.
		"""
		try :
			return self._qoslink04droprate
		except Exception as e:
			raise e

	@property
	def ipcpe2qosfailedrate(self) :
		r"""Rate (/s) counter for ipcpe2qosfailed.
		"""
		try :
			return self._ipcpe2qosfailedrate
		except Exception as e:
			raise e

	@property
	def qosoutputpackets(self) :
		r"""Packets from QoS to be sent.
		"""
		try :
			return self._qosoutputpackets
		except Exception as e:
			raise e

	@property
	def qosbytesdroppedrate(self) :
		r"""Rate (/s) counter for qosbytesdropped.
		"""
		try :
			return self._qosbytesdroppedrate
		except Exception as e:
			raise e

	@property
	def qoslink06sent(self) :
		r"""QoS bytes sent on Link 06.
		"""
		try :
			return self._qoslink06sent
		except Exception as e:
			raise e

	@property
	def qoslink04sent(self) :
		r"""QoS bytes sent on Link 04.
		"""
		try :
			return self._qoslink04sent
		except Exception as e:
			raise e

	@property
	def qoslink00sent(self) :
		r"""QoS bytes sent on Link 00.
		"""
		try :
			return self._qoslink00sent
		except Exception as e:
			raise e

	@property
	def qoslink07sent(self) :
		r"""QoS bytes sent on Link 07.
		"""
		try :
			return self._qoslink07sent
		except Exception as e:
			raise e

	@property
	def qoslink09droprate(self) :
		r"""Rate (/s) counter for qoslink09drop.
		"""
		try :
			return self._qoslink09droprate
		except Exception as e:
			raise e

	@property
	def qoslink10drop(self) :
		r"""QoS bytes dropped on Link 10.
		"""
		try :
			return self._qoslink10drop
		except Exception as e:
			raise e

	@property
	def qospacketsunclassified(self) :
		r"""Number of packets without classification.
		"""
		try :
			return self._qospacketsunclassified
		except Exception as e:
			raise e

	@property
	def qosoutputpacketsrate(self) :
		r"""Rate (/s) counter for qosoutputpackets.
		"""
		try :
			return self._qosoutputpacketsrate
		except Exception as e:
			raise e

	@property
	def qoslink03sent(self) :
		r"""QoS bytes sent on Link 03.
		"""
		try :
			return self._qoslink03sent
		except Exception as e:
			raise e

	@property
	def qoslink05sentrate(self) :
		r"""Rate (/s) counter for qoslink05sent.
		"""
		try :
			return self._qoslink05sentrate
		except Exception as e:
			raise e

	@property
	def qoslink04sentrate(self) :
		r"""Rate (/s) counter for qoslink04sent.
		"""
		try :
			return self._qoslink04sentrate
		except Exception as e:
			raise e

	@property
	def qosbytesdropped(self) :
		r"""Bytes QoS marked for drop.
		"""
		try :
			return self._qosbytesdropped
		except Exception as e:
			raise e

	@property
	def qosdroppackets(self) :
		r"""Packets Dropped by QoS.
		"""
		try :
			return self._qosdroppackets
		except Exception as e:
			raise e

	@property
	def qoslink06drop(self) :
		r"""QoS bytes dropped on Link 06.
		"""
		try :
			return self._qoslink06drop
		except Exception as e:
			raise e

	@property
	def qosinputpackets(self) :
		r"""Packets sent to QoS for scheduling.
		"""
		try :
			return self._qosinputpackets
		except Exception as e:
			raise e

	@property
	def qoslink07droprate(self) :
		r"""Rate (/s) counter for qoslink07drop.
		"""
		try :
			return self._qoslink07droprate
		except Exception as e:
			raise e

	@property
	def ipcmessagesreceived(self) :
		r"""IPC messages received by qos.
		"""
		try :
			return self._ipcmessagesreceived
		except Exception as e:
			raise e

	@property
	def qoslink09drop(self) :
		r"""QoS bytes dropped on Link 09.
		"""
		try :
			return self._qoslink09drop
		except Exception as e:
			raise e

	@property
	def qoslink02droprate(self) :
		r"""Rate (/s) counter for qoslink02drop.
		"""
		try :
			return self._qoslink02droprate
		except Exception as e:
			raise e

	@property
	def qoslink07drop(self) :
		r"""QoS bytes dropped on Link 07.
		"""
		try :
			return self._qoslink07drop
		except Exception as e:
			raise e

	@property
	def qoslink05drop(self) :
		r"""QoS bytes dropped on Link 05.
		"""
		try :
			return self._qoslink05drop
		except Exception as e:
			raise e

	@property
	def ipcpe2qosreceivedrate(self) :
		r"""Rate (/s) counter for ipcpe2qosreceived.
		"""
		try :
			return self._ipcpe2qosreceivedrate
		except Exception as e:
			raise e

	@property
	def qoslink00sentrate(self) :
		r"""Rate (/s) counter for qoslink00sent.
		"""
		try :
			return self._qoslink00sentrate
		except Exception as e:
			raise e

	@property
	def ipcpe2qossent(self) :
		r"""IPC messages sent to qos system.
		"""
		try :
			return self._ipcpe2qossent
		except Exception as e:
			raise e

	@property
	def qoslink01sent(self) :
		r"""QoS bytes sent on Link 01.
		"""
		try :
			return self._qoslink01sent
		except Exception as e:
			raise e

	@property
	def qoslearnedmacrate(self) :
		r"""Rate (/s) counter for qoslearnedmac.
		"""
		try :
			return self._qoslearnedmacrate
		except Exception as e:
			raise e

	@property
	def qoslink08sent(self) :
		r"""QoS bytes sent on Link 08.
		"""
		try :
			return self._qoslink08sent
		except Exception as e:
			raise e

	@property
	def qoslink06sentrate(self) :
		r"""Rate (/s) counter for qoslink06sent.
		"""
		try :
			return self._qoslink06sentrate
		except Exception as e:
			raise e

	@property
	def qoslink01drop(self) :
		r"""QoS bytes dropped on Link 01.
		"""
		try :
			return self._qoslink01drop
		except Exception as e:
			raise e

	@property
	def ipcmessagesreceivedrate(self) :
		r"""Rate (/s) counter for ipcmessagesreceived.
		"""
		try :
			return self._ipcmessagesreceivedrate
		except Exception as e:
			raise e

	@property
	def ipcpe2qossentrate(self) :
		r"""Rate (/s) counter for ipcpe2qossent.
		"""
		try :
			return self._ipcpe2qossentrate
		except Exception as e:
			raise e

	@property
	def qosbytessentnotclassified(self) :
		r"""Bytes scheduled by QoS that were not classified.
		"""
		try :
			return self._qosbytessentnotclassified
		except Exception as e:
			raise e

	@property
	def qoslearnedmac(self) :
		r"""QoS learned true MAC.
		"""
		try :
			return self._qoslearnedmac
		except Exception as e:
			raise e

	@property
	def ipcmessagessent(self) :
		r"""IPC messages sent from qos system.
		"""
		try :
			return self._ipcmessagessent
		except Exception as e:
			raise e

	@property
	def qoslink00droprate(self) :
		r"""Rate (/s) counter for qoslink00drop.
		"""
		try :
			return self._qoslink00droprate
		except Exception as e:
			raise e

	@property
	def qoslink10sentrate(self) :
		r"""Rate (/s) counter for qoslink10sent.
		"""
		try :
			return self._qoslink10sentrate
		except Exception as e:
			raise e

	@property
	def ipcpe2qosreceived(self) :
		r"""IPC messages received from qos system.
		"""
		try :
			return self._ipcpe2qosreceived
		except Exception as e:
			raise e

	@property
	def qosdroppacketsrate(self) :
		r"""Rate (/s) counter for qosdroppackets.
		"""
		try :
			return self._qosdroppacketsrate
		except Exception as e:
			raise e

	@property
	def qosbytesdroppednoconnection(self) :
		r"""Bytes dropped by QoS when no connection was found.
		"""
		try :
			return self._qosbytesdroppednoconnection
		except Exception as e:
			raise e

	@property
	def qospacketsclassifiedrate(self) :
		r"""Rate (/s) counter for qospacketsclassified.
		"""
		try :
			return self._qospacketsclassifiedrate
		except Exception as e:
			raise e

	@property
	def qosrewritemacs(self) :
		r"""Number of packets with inband classification in source MAC.
		"""
		try :
			return self._qosrewritemacs
		except Exception as e:
			raise e

	def _get_nitro_response(self, service, response) :
		r""" converts nitro response into object and returns the object array in case of get request.
		"""
		try :
			result = service.payload_formatter.string_to_resource(qos_response, response, self.__class__.__name__.replace('_stats',''))
			if(result.errorcode != 0) :
				if (result.errorcode == 444) :
					service.clear_session(self)
				if result.severity :
					if (result.severity == "ERROR") :
						raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
				else :
					raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
			return result.qos
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
	def  get(cls, service, name="", option_="") :
		r""" Use this API to fetch the statistics of all qos_stats resources that are configured on netscaler.
		"""
		try :
			obj = qos_stats()
			if not name :
				response = obj.stat_resources(service, option_)
			return response
		except Exception as e:
			raise e

	class Clearstats:
		basic = "basic"
		full = "full"

class qos_response(base_response) :
	def __init__(self, length=1) :
		self.qos = []
		self.errorcode = 0
		self.message = ""
		self.severity = ""
		self.sessionid = ""
		self.qos = [qos_stats() for _ in range(length)]

