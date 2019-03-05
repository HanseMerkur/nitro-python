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

class nstcpparam(base_resource) :
    """Configuration for tcp parameters resource."""
    def __init__(self) :
        self._ws = ""
        self._wsval = 0
        self._sack = ""
        self._learnvsvrmss = ""
        self._maxburst = 0
        self._initialcwnd = 0
        self._recvbuffsize = 0
        self._delayedack = 0
        self._downstaterst = ""
        self._nagle = ""
        self._limitedpersist = ""
        self._oooqsize = 0
        self._ackonpush = ""
        self._maxpktpermss = 0
        self._pktperretx = 0
        self._minrto = 0
        self._slowstartincr = 0
        self._maxdynserverprobes = 0
        self._synholdfastgiveup = 0
        self._maxsynholdperprobe = 0
        self._maxsynhold = 0
        self._msslearninterval = 0
        self._msslearndelay = 0
        self._maxtimewaitconn = 0
        self._kaprobeupdatelastactivity = ""
        self._maxsynackretx = 0
        self._synattackdetection = ""
        self._connflushifnomem = ""
        self._connflushthres = 0
        self._mptcpconcloseonpassivesf = ""
        self._mptcpchecksum = ""
        self._mptcpsftimeout = 0
        self._mptcpsfreplacetimeout = 0
        self._mptcpmaxsf = 0
        self._mptcpmaxpendingsf = 0
        self._mptcppendingjointhreshold = 0
        self._mptcprtostoswitchsf = 0
        self._mptcpusebackupondss = ""
        self._tcpmaxretries = 0
        self._mptcpimmediatesfcloseonfin = ""
        self._mptcpclosemptcpsessiononlastsfclose = ""
        self._builtin = []

    @property
    def ws(self) :
        """Enable or disable window scaling.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._ws
        except Exception as e:
            raise e

    @ws.setter
    def ws(self, ws) :
        """Enable or disable window scaling.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED

        :param ws: 

        """
        try :
            self._ws = ws
        except Exception as e:
            raise e

    @property
    def wsval(self) :
        """Factor used to calculate the new window size.
        This argument is needed only when the window scaling is enabled.<br/>Default value: 4<br/>Maximum length =  14.


        """
        try :
            return self._wsval
        except Exception as e:
            raise e

    @wsval.setter
    def wsval(self, wsval) :
        """Factor used to calculate the new window size.
        This argument is needed only when the window scaling is enabled.<br/>Default value: 4<br/>Maximum length =  14

        :param wsval: 

        """
        try :
            self._wsval = wsval
        except Exception as e:
            raise e

    @property
    def sack(self) :
        """Enable or disable Selective ACKnowledgement (SACK).<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._sack
        except Exception as e:
            raise e

    @sack.setter
    def sack(self, sack) :
        """Enable or disable Selective ACKnowledgement (SACK).<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED

        :param sack: 

        """
        try :
            self._sack = sack
        except Exception as e:
            raise e

    @property
    def learnvsvrmss(self) :
        """Enable or disable maximum segment size (MSS) learning for virtual servers.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._learnvsvrmss
        except Exception as e:
            raise e

    @learnvsvrmss.setter
    def learnvsvrmss(self, learnvsvrmss) :
        """Enable or disable maximum segment size (MSS) learning for virtual servers.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED

        :param learnvsvrmss: 

        """
        try :
            self._learnvsvrmss = learnvsvrmss
        except Exception as e:
            raise e

    @property
    def maxburst(self) :
        """Maximum number of TCP segments allowed in a burst.<br/>Default value: 6<br/>Minimum length =  1<br/>Maximum length =  255."""
        try :
            return self._maxburst
        except Exception as e:
            raise e

    @maxburst.setter
    def maxburst(self, maxburst) :
        """Maximum number of TCP segments allowed in a burst.<br/>Default value: 6<br/>Minimum length =  1<br/>Maximum length =  255

        :param maxburst: 

        """
        try :
            self._maxburst = maxburst
        except Exception as e:
            raise e

    @property
    def initialcwnd(self) :
        """Initial maximum upper limit on the number of TCP packets that can be outstanding on the TCP link to the server.<br/>Default value: 4<br/>Minimum length =  1<br/>Maximum length =  44."""
        try :
            return self._initialcwnd
        except Exception as e:
            raise e

    @initialcwnd.setter
    def initialcwnd(self, initialcwnd) :
        """Initial maximum upper limit on the number of TCP packets that can be outstanding on the TCP link to the server.<br/>Default value: 4<br/>Minimum length =  1<br/>Maximum length =  44

        :param initialcwnd: 

        """
        try :
            self._initialcwnd = initialcwnd
        except Exception as e:
            raise e

    @property
    def recvbuffsize(self) :
        """TCP Receive buffer size.<br/>Default value: 8190<br/>Minimum length =  8190<br/>Maximum length =  20971520."""
        try :
            return self._recvbuffsize
        except Exception as e:
            raise e

    @recvbuffsize.setter
    def recvbuffsize(self, recvbuffsize) :
        """TCP Receive buffer size.<br/>Default value: 8190<br/>Minimum length =  8190<br/>Maximum length =  20971520

        :param recvbuffsize: 

        """
        try :
            self._recvbuffsize = recvbuffsize
        except Exception as e:
            raise e

    @property
    def delayedack(self) :
        """Timeout for TCP delayed ACK, in milliseconds.<br/>Default value: 100<br/>Minimum length =  10<br/>Maximum length =  300."""
        try :
            return self._delayedack
        except Exception as e:
            raise e

    @delayedack.setter
    def delayedack(self, delayedack) :
        """Timeout for TCP delayed ACK, in milliseconds.<br/>Default value: 100<br/>Minimum length =  10<br/>Maximum length =  300

        :param delayedack: 

        """
        try :
            self._delayedack = delayedack
        except Exception as e:
            raise e

    @property
    def downstaterst(self) :
        """Flag to switch on RST on down services.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._downstaterst
        except Exception as e:
            raise e

    @downstaterst.setter
    def downstaterst(self, downstaterst) :
        """Flag to switch on RST on down services.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED

        :param downstaterst: 

        """
        try :
            self._downstaterst = downstaterst
        except Exception as e:
            raise e

    @property
    def nagle(self) :
        """Enable or disable the Nagle algorithm on TCP connections.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._nagle
        except Exception as e:
            raise e

    @nagle.setter
    def nagle(self, nagle) :
        """Enable or disable the Nagle algorithm on TCP connections.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED

        :param nagle: 

        """
        try :
            self._nagle = nagle
        except Exception as e:
            raise e

    @property
    def limitedpersist(self) :
        """Limit the number of persist (zero window) probes.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._limitedpersist
        except Exception as e:
            raise e

    @limitedpersist.setter
    def limitedpersist(self, limitedpersist) :
        """Limit the number of persist (zero window) probes.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED

        :param limitedpersist: 

        """
        try :
            self._limitedpersist = limitedpersist
        except Exception as e:
            raise e

    @property
    def oooqsize(self) :
        """Maximum size of out-of-order packets queue. A value of 0 means no limit.<br/>Default value: 64<br/>Maximum length =  65535."""
        try :
            return self._oooqsize
        except Exception as e:
            raise e

    @oooqsize.setter
    def oooqsize(self, oooqsize) :
        """Maximum size of out-of-order packets queue. A value of 0 means no limit.<br/>Default value: 64<br/>Maximum length =  65535

        :param oooqsize: 

        """
        try :
            self._oooqsize = oooqsize
        except Exception as e:
            raise e

    @property
    def ackonpush(self) :
        """Send immediate positive acknowledgement (ACK) on receipt of TCP packets with PUSH flag.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._ackonpush
        except Exception as e:
            raise e

    @ackonpush.setter
    def ackonpush(self, ackonpush) :
        """Send immediate positive acknowledgement (ACK) on receipt of TCP packets with PUSH flag.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED

        :param ackonpush: 

        """
        try :
            self._ackonpush = ackonpush
        except Exception as e:
            raise e

    @property
    def maxpktpermss(self) :
        """Maximum number of TCP packets allowed per maximum segment size (MSS).<br/>Maximum length =  1460."""
        try :
            return self._maxpktpermss
        except Exception as e:
            raise e

    @maxpktpermss.setter
    def maxpktpermss(self, maxpktpermss) :
        """Maximum number of TCP packets allowed per maximum segment size (MSS).<br/>Maximum length =  1460

        :param maxpktpermss: 

        """
        try :
            self._maxpktpermss = maxpktpermss
        except Exception as e:
            raise e

    @property
    def pktperretx(self) :
        """Maximum limit on the number of packets that should be retransmitted on receiving a partial ACK.<br/>Default value: 1<br/>Minimum length =  1<br/>Maximum length =  100."""
        try :
            return self._pktperretx
        except Exception as e:
            raise e

    @pktperretx.setter
    def pktperretx(self, pktperretx) :
        """Maximum limit on the number of packets that should be retransmitted on receiving a partial ACK.<br/>Default value: 1<br/>Minimum length =  1<br/>Maximum length =  100

        :param pktperretx: 

        """
        try :
            self._pktperretx = pktperretx
        except Exception as e:
            raise e

    @property
    def minrto(self) :
        """Minimum retransmission timeout, in milliseconds, specified in 10-millisecond increments (value must yield a whole number if divided by 10).<br/>Default value: 1000<br/>Minimum length =  10<br/>Maximum length =  64000."""
        try :
            return self._minrto
        except Exception as e:
            raise e

    @minrto.setter
    def minrto(self, minrto) :
        """Minimum retransmission timeout, in milliseconds, specified in 10-millisecond increments (value must yield a whole number if divided by 10).<br/>Default value: 1000<br/>Minimum length =  10<br/>Maximum length =  64000

        :param minrto: 

        """
        try :
            self._minrto = minrto
        except Exception as e:
            raise e

    @property
    def slowstartincr(self) :
        """Multiplier that determines the rate at which slow start increases the size of the TCP transmission window after each acknowledgement of successful transmission.<br/>Default value: 2<br/>Minimum length =  1<br/>Maximum length =  100."""
        try :
            return self._slowstartincr
        except Exception as e:
            raise e

    @slowstartincr.setter
    def slowstartincr(self, slowstartincr) :
        """Multiplier that determines the rate at which slow start increases the size of the TCP transmission window after each acknowledgement of successful transmission.<br/>Default value: 2<br/>Minimum length =  1<br/>Maximum length =  100

        :param slowstartincr: 

        """
        try :
            self._slowstartincr = slowstartincr
        except Exception as e:
            raise e

    @property
    def maxdynserverprobes(self) :
        """Maximum number of probes that NetScaler can send out in 10 milliseconds, to dynamically learn a service. NetScaler probes for the existence of the origin in case of wildcard virtual server or services.<br/>Default value: 7<br/>Minimum length =  1<br/>Maximum length =  65535."""
        try :
            return self._maxdynserverprobes
        except Exception as e:
            raise e

    @maxdynserverprobes.setter
    def maxdynserverprobes(self, maxdynserverprobes) :
        """Maximum number of probes that NetScaler can send out in 10 milliseconds, to dynamically learn a service. NetScaler probes for the existence of the origin in case of wildcard virtual server or services.<br/>Default value: 7<br/>Minimum length =  1<br/>Maximum length =  65535

        :param maxdynserverprobes: 

        """
        try :
            self._maxdynserverprobes = maxdynserverprobes
        except Exception as e:
            raise e

    @property
    def synholdfastgiveup(self) :
        """Maximum threshold. After crossing this threshold number of outstanding probes for origin, the NetScaler reduces the number of connection retries for probe connections.<br/>Default value: 1024<br/>Minimum length =  256<br/>Maximum length =  65535."""
        try :
            return self._synholdfastgiveup
        except Exception as e:
            raise e

    @synholdfastgiveup.setter
    def synholdfastgiveup(self, synholdfastgiveup) :
        """Maximum threshold. After crossing this threshold number of outstanding probes for origin, the NetScaler reduces the number of connection retries for probe connections.<br/>Default value: 1024<br/>Minimum length =  256<br/>Maximum length =  65535

        :param synholdfastgiveup: 

        """
        try :
            self._synholdfastgiveup = synholdfastgiveup
        except Exception as e:
            raise e

    @property
    def maxsynholdperprobe(self) :
        """Limit the number of client connections (SYN) waiting for status of single probe. Any new SYN packets will be dropped.<br/>Default value: 128<br/>Minimum length =  1<br/>Maximum length =  255."""
        try :
            return self._maxsynholdperprobe
        except Exception as e:
            raise e

    @maxsynholdperprobe.setter
    def maxsynholdperprobe(self, maxsynholdperprobe) :
        """Limit the number of client connections (SYN) waiting for status of single probe. Any new SYN packets will be dropped.<br/>Default value: 128<br/>Minimum length =  1<br/>Maximum length =  255

        :param maxsynholdperprobe: 

        """
        try :
            self._maxsynholdperprobe = maxsynholdperprobe
        except Exception as e:
            raise e

    @property
    def maxsynhold(self) :
        """Limit the number of client connections (SYN) waiting for status of probe system wide. Any new SYN packets will be dropped.<br/>Default value: 16384<br/>Minimum length =  256<br/>Maximum length =  65535."""
        try :
            return self._maxsynhold
        except Exception as e:
            raise e

    @maxsynhold.setter
    def maxsynhold(self, maxsynhold) :
        """Limit the number of client connections (SYN) waiting for status of probe system wide. Any new SYN packets will be dropped.<br/>Default value: 16384<br/>Minimum length =  256<br/>Maximum length =  65535

        :param maxsynhold: 

        """
        try :
            self._maxsynhold = maxsynhold
        except Exception as e:
            raise e

    @property
    def msslearninterval(self) :
        """Duration, in seconds, to sample the Maximum Segment Size (MSS) of the services. The NetScaler appliance determines the best MSS to set for the virtual server based on this sampling. The argument to enable maximum segment size (MSS) for virtual servers must be enabled.<br/>Default value: 180<br/>Minimum length =  1<br/>Maximum length =  1048576."""
        try :
            return self._msslearninterval
        except Exception as e:
            raise e

    @msslearninterval.setter
    def msslearninterval(self, msslearninterval) :
        """Duration, in seconds, to sample the Maximum Segment Size (MSS) of the services. The NetScaler appliance determines the best MSS to set for the virtual server based on this sampling. The argument to enable maximum segment size (MSS) for virtual servers must be enabled.<br/>Default value: 180<br/>Minimum length =  1<br/>Maximum length =  1048576

        :param msslearninterval: 

        """
        try :
            self._msslearninterval = msslearninterval
        except Exception as e:
            raise e

    @property
    def msslearndelay(self) :
        """Frequency, in seconds, at which the virtual servers learn the Maximum segment size (MSS) from the services. The argument to enable maximum segment size (MSS) for virtual servers must be enabled.<br/>Default value: 3600<br/>Minimum length =  1<br/>Maximum length =  1048576."""
        try :
            return self._msslearndelay
        except Exception as e:
            raise e

    @msslearndelay.setter
    def msslearndelay(self, msslearndelay) :
        """Frequency, in seconds, at which the virtual servers learn the Maximum segment size (MSS) from the services. The argument to enable maximum segment size (MSS) for virtual servers must be enabled.<br/>Default value: 3600<br/>Minimum length =  1<br/>Maximum length =  1048576

        :param msslearndelay: 

        """
        try :
            self._msslearndelay = msslearndelay
        except Exception as e:
            raise e

    @property
    def maxtimewaitconn(self) :
        """Maximum number of connections to hold in the TCP TIME_WAIT state on a packet engine. New connections entering TIME_WAIT state are proactively cleaned up.<br/>Default value: 7000<br/>Minimum length =  1."""
        try :
            return self._maxtimewaitconn
        except Exception as e:
            raise e

    @maxtimewaitconn.setter
    def maxtimewaitconn(self, maxtimewaitconn) :
        """Maximum number of connections to hold in the TCP TIME_WAIT state on a packet engine. New connections entering TIME_WAIT state are proactively cleaned up.<br/>Default value: 7000<br/>Minimum length =  1

        :param maxtimewaitconn: 

        """
        try :
            self._maxtimewaitconn = maxtimewaitconn
        except Exception as e:
            raise e

    @property
    def kaprobeupdatelastactivity(self) :
        """Update last activity for KA probes.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._kaprobeupdatelastactivity
        except Exception as e:
            raise e

    @kaprobeupdatelastactivity.setter
    def kaprobeupdatelastactivity(self, kaprobeupdatelastactivity) :
        """Update last activity for KA probes.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED

        :param kaprobeupdatelastactivity: 

        """
        try :
            self._kaprobeupdatelastactivity = kaprobeupdatelastactivity
        except Exception as e:
            raise e

    @property
    def maxsynackretx(self) :
        """When 'syncookie' is disabled in the TCP profile that is bound to the virtual server or service, and the number of TCP SYN+ACK retransmission by NetScaler for that virtual server or service crosses this threshold, the NetScaler appliance responds by using the TCP SYN-Cookie mechanism.<br/>Default value: 100<br/>Minimum length =  100<br/>Maximum length =  1048576."""
        try :
            return self._maxsynackretx
        except Exception as e:
            raise e

    @maxsynackretx.setter
    def maxsynackretx(self, maxsynackretx) :
        """When 'syncookie' is disabled in the TCP profile that is bound to the virtual server or service, and the number of TCP SYN+ACK retransmission by NetScaler for that virtual server or service crosses this threshold, the NetScaler appliance responds by using the TCP SYN-Cookie mechanism.<br/>Default value: 100<br/>Minimum length =  100<br/>Maximum length =  1048576

        :param maxsynackretx: 

        """
        try :
            self._maxsynackretx = maxsynackretx
        except Exception as e:
            raise e

    @property
    def synattackdetection(self) :
        """Detect TCP SYN packet flood and send an SNMP trap.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._synattackdetection
        except Exception as e:
            raise e

    @synattackdetection.setter
    def synattackdetection(self, synattackdetection) :
        """Detect TCP SYN packet flood and send an SNMP trap.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED

        :param synattackdetection: 

        """
        try :
            self._synattackdetection = synattackdetection
        except Exception as e:
            raise e

    @property
    def connflushifnomem(self) :
        """Flush an existing connection if no memory can be obtained for new connection.
        HALF_CLOSED_AND_IDLE: Flush a connection that is closed by us but not by peer, or failing that, a connection that is past configured idle time.  New connection fails if no such connection can be found.
        FIFO: If no half-closed or idle connection can be found, flush the oldest non-management connection, even if it is active.  New connection fails if the oldest few connections are management connections.
        Note: If you enable this setting, you should also consider lowering the zombie timeout and half-close timeout, while setting the NetScaler timeout.
        See Also: connFlushThres argument below.
        <br/>Default value: 5<br/>Possible values = NONE, HALFCLOSED_AND_IDLE, FIFO.


        """
        try :
            return self._connflushifnomem
        except Exception as e:
            raise e

    @connflushifnomem.setter
    def connflushifnomem(self, connflushifnomem) :
        """Flush an existing connection if no memory can be obtained for new connection.
        HALF_CLOSED_AND_IDLE: Flush a connection that is closed by us but not by peer, or failing that, a connection that is past configured idle time.  New connection fails if no such connection can be found.
        FIFO: If no half-closed or idle connection can be found, flush the oldest non-management connection, even if it is active.  New connection fails if the oldest few connections are management connections.
        Note: If you enable this setting, you should also consider lowering the zombie timeout and half-close timeout, while setting the NetScaler timeout.
        See Also: connFlushThres argument below.
        <br/>Default value: 5<br/>Possible values = NONE, HALFCLOSED_AND_IDLE, FIFO

        :param connflushifnomem: 

        """
        try :
            self._connflushifnomem = connflushifnomem
        except Exception as e:
            raise e

    @property
    def connflushthres(self) :
        """Flush an existing connection (as configured through -connFlushIfNoMem FIFO) if the system has more than specified number of connections, and a new connection is to be established.  Note: This value may be rounded down to be a whole multiple of the number of packet engines running.<br/>Minimum length =  1."""
        try :
            return self._connflushthres
        except Exception as e:
            raise e

    @connflushthres.setter
    def connflushthres(self, connflushthres) :
        """Flush an existing connection (as configured through -connFlushIfNoMem FIFO) if the system has more than specified number of connections, and a new connection is to be established.  Note: This value may be rounded down to be a whole multiple of the number of packet engines running.<br/>Minimum length =  1

        :param connflushthres: 

        """
        try :
            self._connflushthres = connflushthres
        except Exception as e:
            raise e

    @property
    def mptcpconcloseonpassivesf(self) :
        """Accept DATA_FIN/FAST_CLOSE on passive subflow.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._mptcpconcloseonpassivesf
        except Exception as e:
            raise e

    @mptcpconcloseonpassivesf.setter
    def mptcpconcloseonpassivesf(self, mptcpconcloseonpassivesf) :
        """Accept DATA_FIN/FAST_CLOSE on passive subflow.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED

        :param mptcpconcloseonpassivesf: 

        """
        try :
            self._mptcpconcloseonpassivesf = mptcpconcloseonpassivesf
        except Exception as e:
            raise e

    @property
    def mptcpchecksum(self) :
        """Use MPTCP DSS checksum.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._mptcpchecksum
        except Exception as e:
            raise e

    @mptcpchecksum.setter
    def mptcpchecksum(self, mptcpchecksum) :
        """Use MPTCP DSS checksum.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED

        :param mptcpchecksum: 

        """
        try :
            self._mptcpchecksum = mptcpchecksum
        except Exception as e:
            raise e

    @property
    def mptcpsftimeout(self) :
        """The timeout value in seconds for idle mptcp subflows. If this timeout is not set, idle subflows are cleared after cltTimeout of vserver.<br/>Default value: 0<br/>Maximum length =  31536000."""
        try :
            return self._mptcpsftimeout
        except Exception as e:
            raise e

    @mptcpsftimeout.setter
    def mptcpsftimeout(self, mptcpsftimeout) :
        """The timeout value in seconds for idle mptcp subflows. If this timeout is not set, idle subflows are cleared after cltTimeout of vserver.<br/>Default value: 0<br/>Maximum length =  31536000

        :param mptcpsftimeout: 

        """
        try :
            self._mptcpsftimeout = mptcpsftimeout
        except Exception as e:
            raise e

    @property
    def mptcpsfreplacetimeout(self) :
        """The minimum idle time value in seconds for idle mptcp subflows after which the sublow is replaced by new incoming subflow if maximum subflow limit is reached. The priority for replacement is given to those subflow without any transaction.<br/>Default value: 10<br/>Maximum length =  31536000."""
        try :
            return self._mptcpsfreplacetimeout
        except Exception as e:
            raise e

    @mptcpsfreplacetimeout.setter
    def mptcpsfreplacetimeout(self, mptcpsfreplacetimeout) :
        """The minimum idle time value in seconds for idle mptcp subflows after which the sublow is replaced by new incoming subflow if maximum subflow limit is reached. The priority for replacement is given to those subflow without any transaction.<br/>Default value: 10<br/>Maximum length =  31536000

        :param mptcpsfreplacetimeout: 

        """
        try :
            self._mptcpsfreplacetimeout = mptcpsfreplacetimeout
        except Exception as e:
            raise e

    @property
    def mptcpmaxsf(self) :
        """Maximum number of subflow connections supported in established state per mptcp connection.<br/>Default value: 4<br/>Minimum length =  2<br/>Maximum length =  6."""
        try :
            return self._mptcpmaxsf
        except Exception as e:
            raise e

    @mptcpmaxsf.setter
    def mptcpmaxsf(self, mptcpmaxsf) :
        """Maximum number of subflow connections supported in established state per mptcp connection.<br/>Default value: 4<br/>Minimum length =  2<br/>Maximum length =  6

        :param mptcpmaxsf: 

        """
        try :
            self._mptcpmaxsf = mptcpmaxsf
        except Exception as e:
            raise e

    @property
    def mptcpmaxpendingsf(self) :
        """Maximum number of subflow connections supported in pending join state per mptcp connection.<br/>Default value: 4<br/>Maximum length =  4."""
        try :
            return self._mptcpmaxpendingsf
        except Exception as e:
            raise e

    @mptcpmaxpendingsf.setter
    def mptcpmaxpendingsf(self, mptcpmaxpendingsf) :
        """Maximum number of subflow connections supported in pending join state per mptcp connection.<br/>Default value: 4<br/>Maximum length =  4

        :param mptcpmaxpendingsf: 

        """
        try :
            self._mptcpmaxpendingsf = mptcpmaxpendingsf
        except Exception as e:
            raise e

    @property
    def mptcppendingjointhreshold(self) :
        """Maximum system level pending join connections allowed.<br/>Default value: 0<br/>Maximum length =  0xFFFFFFFE."""
        try :
            return self._mptcppendingjointhreshold
        except Exception as e:
            raise e

    @mptcppendingjointhreshold.setter
    def mptcppendingjointhreshold(self, mptcppendingjointhreshold) :
        """Maximum system level pending join connections allowed.<br/>Default value: 0<br/>Maximum length =  0xFFFFFFFE

        :param mptcppendingjointhreshold: 

        """
        try :
            self._mptcppendingjointhreshold = mptcppendingjointhreshold
        except Exception as e:
            raise e

    @property
    def mptcprtostoswitchsf(self) :
        """Number of RTO's at subflow level, after which MPCTP should start using other subflow.<br/>Default value: 2<br/>Minimum length =  1<br/>Maximum length =  6."""
        try :
            return self._mptcprtostoswitchsf
        except Exception as e:
            raise e

    @mptcprtostoswitchsf.setter
    def mptcprtostoswitchsf(self, mptcprtostoswitchsf) :
        """Number of RTO's at subflow level, after which MPCTP should start using other subflow.<br/>Default value: 2<br/>Minimum length =  1<br/>Maximum length =  6

        :param mptcprtostoswitchsf: 

        """
        try :
            self._mptcprtostoswitchsf = mptcprtostoswitchsf
        except Exception as e:
            raise e

    @property
    def mptcpusebackupondss(self) :
        """When enabled, if NS receives a DSS on a backup subflow, NS will start using that subflow to send data. And if disabled, NS will continue to transmit on current chosen subflow. In case there is some error on a subflow (like RTO's/RST etc.) then NS can choose a backup subflow irrespective of this tunable.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._mptcpusebackupondss
        except Exception as e:
            raise e

    @mptcpusebackupondss.setter
    def mptcpusebackupondss(self, mptcpusebackupondss) :
        """When enabled, if NS receives a DSS on a backup subflow, NS will start using that subflow to send data. And if disabled, NS will continue to transmit on current chosen subflow. In case there is some error on a subflow (like RTO's/RST etc.) then NS can choose a backup subflow irrespective of this tunable.<br/>Default value: ENABLED<br/>Possible values = ENABLED, DISABLED

        :param mptcpusebackupondss: 

        """
        try :
            self._mptcpusebackupondss = mptcpusebackupondss
        except Exception as e:
            raise e

    @property
    def tcpmaxretries(self) :
        """Number of RTO's after which a connection should be freed.<br/>Default value: 7<br/>Minimum length =  1<br/>Maximum length =  7."""
        try :
            return self._tcpmaxretries
        except Exception as e:
            raise e

    @tcpmaxretries.setter
    def tcpmaxretries(self, tcpmaxretries) :
        """Number of RTO's after which a connection should be freed.<br/>Default value: 7<br/>Minimum length =  1<br/>Maximum length =  7

        :param tcpmaxretries: 

        """
        try :
            self._tcpmaxretries = tcpmaxretries
        except Exception as e:
            raise e

    @property
    def mptcpimmediatesfcloseonfin(self) :
        """Allow subflows to close immediately on FIN before the DATA_FIN exchange is completed at mptcp level.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._mptcpimmediatesfcloseonfin
        except Exception as e:
            raise e

    @mptcpimmediatesfcloseonfin.setter
    def mptcpimmediatesfcloseonfin(self, mptcpimmediatesfcloseonfin) :
        """Allow subflows to close immediately on FIN before the DATA_FIN exchange is completed at mptcp level.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED

        :param mptcpimmediatesfcloseonfin: 

        """
        try :
            self._mptcpimmediatesfcloseonfin = mptcpimmediatesfcloseonfin
        except Exception as e:
            raise e

    @property
    def mptcpclosemptcpsessiononlastsfclose(self) :
        """Allow to send DATA FIN or FAST CLOSE on mptcp connection while sending FIN or RST on the last subflow.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED."""
        try :
            return self._mptcpclosemptcpsessiononlastsfclose
        except Exception as e:
            raise e

    @mptcpclosemptcpsessiononlastsfclose.setter
    def mptcpclosemptcpsessiononlastsfclose(self, mptcpclosemptcpsessiononlastsfclose) :
        """Allow to send DATA FIN or FAST CLOSE on mptcp connection while sending FIN or RST on the last subflow.<br/>Default value: DISABLED<br/>Possible values = ENABLED, DISABLED

        :param mptcpclosemptcpsessiononlastsfclose: 

        """
        try :
            self._mptcpclosemptcpsessiononlastsfclose = mptcpclosemptcpsessiononlastsfclose
        except Exception as e:
            raise e

    @property
    def builtin(self) :
        """Flag to determine if the tcp param is built-in or not.<br/>Possible values = MODIFIABLE, DELETABLE, IMMUTABLE, PARTITION_ALL."""
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
            result = service.payload_formatter.string_to_resource(nstcpparam_response, response, self.__class__.__name__)
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.nstcpparam
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
        """Use this API to update nstcpparam.

        :param client: 
        :param resource: 

        """
        try :
            if type(resource) is not list :
                updateresource = nstcpparam()
                updateresource.ws = resource.ws
                updateresource.wsval = resource.wsval
                updateresource.sack = resource.sack
                updateresource.learnvsvrmss = resource.learnvsvrmss
                updateresource.maxburst = resource.maxburst
                updateresource.initialcwnd = resource.initialcwnd
                updateresource.recvbuffsize = resource.recvbuffsize
                updateresource.delayedack = resource.delayedack
                updateresource.downstaterst = resource.downstaterst
                updateresource.nagle = resource.nagle
                updateresource.limitedpersist = resource.limitedpersist
                updateresource.oooqsize = resource.oooqsize
                updateresource.ackonpush = resource.ackonpush
                updateresource.maxpktpermss = resource.maxpktpermss
                updateresource.pktperretx = resource.pktperretx
                updateresource.minrto = resource.minrto
                updateresource.slowstartincr = resource.slowstartincr
                updateresource.maxdynserverprobes = resource.maxdynserverprobes
                updateresource.synholdfastgiveup = resource.synholdfastgiveup
                updateresource.maxsynholdperprobe = resource.maxsynholdperprobe
                updateresource.maxsynhold = resource.maxsynhold
                updateresource.msslearninterval = resource.msslearninterval
                updateresource.msslearndelay = resource.msslearndelay
                updateresource.maxtimewaitconn = resource.maxtimewaitconn
                updateresource.kaprobeupdatelastactivity = resource.kaprobeupdatelastactivity
                updateresource.maxsynackretx = resource.maxsynackretx
                updateresource.synattackdetection = resource.synattackdetection
                updateresource.connflushifnomem = resource.connflushifnomem
                updateresource.connflushthres = resource.connflushthres
                updateresource.mptcpconcloseonpassivesf = resource.mptcpconcloseonpassivesf
                updateresource.mptcpchecksum = resource.mptcpchecksum
                updateresource.mptcpsftimeout = resource.mptcpsftimeout
                updateresource.mptcpsfreplacetimeout = resource.mptcpsfreplacetimeout
                updateresource.mptcpmaxsf = resource.mptcpmaxsf
                updateresource.mptcpmaxpendingsf = resource.mptcpmaxpendingsf
                updateresource.mptcppendingjointhreshold = resource.mptcppendingjointhreshold
                updateresource.mptcprtostoswitchsf = resource.mptcprtostoswitchsf
                updateresource.mptcpusebackupondss = resource.mptcpusebackupondss
                updateresource.tcpmaxretries = resource.tcpmaxretries
                updateresource.mptcpimmediatesfcloseonfin = resource.mptcpimmediatesfcloseonfin
                updateresource.mptcpclosemptcpsessiononlastsfclose = resource.mptcpclosemptcpsessiononlastsfclose
                return updateresource.update_resource(client)
        except Exception as e :
            raise e

    @classmethod
    def unset(cls, client, resource, args) :
        """Use this API to unset the properties of nstcpparam resource.
        Properties that need to be unset are specified in args array.

        :param client: 
        :param resource: 
        :param args: 

        """
        try :
            if type(resource) is not list :
                unsetresource = nstcpparam()
                return unsetresource.unset_resource(client, args)
        except Exception as e :
            raise e

    @classmethod
    def get(cls, client, name="", option_="") :
        """Use this API to fetch all the nstcpparam resources that are configured on netscaler.

        :param client: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            if not name :
                obj = nstcpparam()
                response = obj.get_resources(client, option_)
            return response
        except Exception as e :
            raise e


    class Kaprobeupdatelastactivity:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Mptcpusebackupondss:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Mptcpclosemptcpsessiononlastsfclose:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Connflushifnomem:
        """ """
        NONE = "NONE"
        HALFCLOSED_AND_IDLE = "HALFCLOSED_AND_IDLE"
        FIFO = "FIFO"

    class Mptcpconcloseonpassivesf:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Builtin:
        """ """
        MODIFIABLE = "MODIFIABLE"
        DELETABLE = "DELETABLE"
        IMMUTABLE = "IMMUTABLE"
        PARTITION_ALL = "PARTITION_ALL"

    class Learnvsvrmss:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Synattackdetection:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Mptcpimmediatesfcloseonfin:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Sack:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Ws:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Ackonpush:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Downstaterst:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Nagle:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Limitedpersist:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

    class Mptcpchecksum:
        """ """
        ENABLED = "ENABLED"
        DISABLED = "DISABLED"

class nstcpparam_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.nstcpparam = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.nstcpparam = [nstcpparam() for _ in range(length)]

