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

class mediaclassification_stats(base_resource) :
    """ """
    def __init__(self) :
        self._clearstats = ""
        self._mcencvideo = 0
        self._mcencvideorate = 0
        self._mctotother = 0
        self._mctoherrate = 0
        self._mctotvideo = 0
        self._mcvideorate = 0
        self._mctotaudio = 0
        self._mcaudiorate = 0
        self._mcmssmthstrmvid = 0
        self._mcmssmthstrmvidrate = 0
        self._mcmssmthstrvidpl = 0
        self._mcmssmthstrvidplrate = 0
        self._mccaplelivestrmngvid = 0
        self._mccaplelivestrmngvidrate = 0
        self._mccapplelivestrmngvidpl = 0
        self._mccapplelivestrmngvidplrate = 0
        self._mcadtsaudio = 0
        self._mcadtsaudiorate = 0
        self._mcaacaudio = 0
        self._mcaacaudiorate = 0
        self._mcflvvid = 0
        self._mcflvvidrate = 0
        self._mcmp4vid = 0
        self._mcmp4vidrate = 0
        self._mc3pvid = 0
        self._mc3pvidrate = 0
        self._mcyoutubedash = 0
        self._mcyoutubedashrate = 0
        self._mcmssmthstrmvidbytes = 0
        self._mcmssmthstrmvidbytesrate = 0
        self._mcmssmthstrmplvidbytespl = 0
        self._mcmssmthstrmplvidbytesplrate = 0
        self._mcapplelivestreamingvidbytes = 0
        self._mcapplelivestreamingvidbytesrate = 0
        self._mcapplelivestreamingplaylistvidbytespl = 0
        self._mcapplelivestreamingplaylistvidbytesplrate = 0
        self._mcadtsaudiobytes = 0
        self._mcadtsaudiobytesrate = 0
        self._mcaacaudiobytes = 0
        self._mcaacaudiobytesrate = 0
        self._mcflvvidbytes = 0
        self._mcflvvidbytesrate = 0
        self._mcmp4vidbytes = 0
        self._mcmp4vidbytesrate = 0
        self._mc3gpvidbytes = 0
        self._mc3gpvidbytesrate = 0
        self._mcyoutubedashbytes = 0
        self._mcyoutubedashbytesrate = 0
        self._mcandroid = 0
        self._mcandroidrate = 0
        self._mclaptopdesktp = 0
        self._mclaptopdesktprate = 0
        self._mcios = 0
        self._mciosrate = 0
        self._mcother = 0
        self._mcotherrate = 0
        self._mcunidentified = 0
        self._mcunidentifiedrate = 0
        self._mcenchls = 0
        self._mcenchlsrate = 0
        self._mcencdash = 0
        self._mcencdashrate = 0
        self._mcencandroid = 0
        self._mcencandroidrate = 0
        self._mcencios = 0
        self._mcenciosrate = 0
        self._mcencother = 0
        self._mcencotherrate = 0

    @property
    def clearstats(self) :
        """Clear the statsistics / counters.<br/>Possible values = basic, full."""
        try :
            return self._clearstats
        except Exception as e:
            raise e

    @clearstats.setter
    def clearstats(self, clearstats) :
        """Clear the statsistics / counters

        :param clearstats: 

        """
        try :
            self._clearstats = clearstats
        except Exception as e:
            raise e

    @property
    def mcmp4vid(self) :
        """This tells the total number of MP4 videos served by NS."""
        try :
            return self._mcmp4vid
        except Exception as e:
            raise e

    @property
    def mcvideorate(self) :
        """Rate (/s) counter for mctotvideo."""
        try :
            return self._mcvideorate
        except Exception as e:
            raise e

    @property
    def mc3pvid(self) :
        """This tells the total number of 3GP videos served by NS."""
        try :
            return self._mc3pvid
        except Exception as e:
            raise e

    @property
    def mcencandroid(self) :
        """Total number of encrypted video streams requested by Android devices."""
        try :
            return self._mcencandroid
        except Exception as e:
            raise e

    @property
    def mcflvvid(self) :
        """This tells the total number of FLV videos served by NS."""
        try :
            return self._mcflvvid
        except Exception as e:
            raise e

    @property
    def mcunidentifiedrate(self) :
        """Rate (/s) counter for mcunidentified."""
        try :
            return self._mcunidentifiedrate
        except Exception as e:
            raise e

    @property
    def mcencvideo(self) :
        """Total number of encrypted video streams."""
        try :
            return self._mcencvideo
        except Exception as e:
            raise e

    @property
    def mclaptopdesktprate(self) :
        """Rate (/s) counter for mclaptopdesktp."""
        try :
            return self._mclaptopdesktprate
        except Exception as e:
            raise e

    @property
    def mcyoutubedash(self) :
        """This tells the total number of YouTube DASH served by NS."""
        try :
            return self._mcyoutubedash
        except Exception as e:
            raise e

    @property
    def mccaplelivestrmngvidrate(self) :
        """Rate (/s) counter for mccaplelivestrmngvid."""
        try :
            return self._mccaplelivestrmngvidrate
        except Exception as e:
            raise e

    @property
    def mcaacaudiobytes(self) :
        """This tells the total number of AAC bytes served by NS ."""
        try :
            return self._mcaacaudiobytes
        except Exception as e:
            raise e

    @property
    def mcenchls(self) :
        """Total number of encrypted AppleLive video streams."""
        try :
            return self._mcenchls
        except Exception as e:
            raise e

    @property
    def mcother(self) :
        """Total number of other mobile device requests to netscaler."""
        try :
            return self._mcother
        except Exception as e:
            raise e

    @property
    def mcflvvidbytesrate(self) :
        """Rate (/s) counter for mcflvvidbytes."""
        try :
            return self._mcflvvidbytesrate
        except Exception as e:
            raise e

    @property
    def mc3gpvidbytes(self) :
        """This tells the total number of 3GP bytes served by NS ."""
        try :
            return self._mc3gpvidbytes
        except Exception as e:
            raise e

    @property
    def mcencvideorate(self) :
        """Rate (/s) counter for mcencvideo."""
        try :
            return self._mcencvideorate
        except Exception as e:
            raise e

    @property
    def mctotaudio(self) :
        """ """
        try :
            return self._mctotaudio
        except Exception as e:
            raise e

    @property
    def mcenciosrate(self) :
        """Rate (/s) counter for mcencios."""
        try :
            return self._mcenciosrate
        except Exception as e:
            raise e

    @property
    def mcadtsaudiobytes(self) :
        """This tells the total number of ADTS audio bytes served by NS ."""
        try :
            return self._mcadtsaudiobytes
        except Exception as e:
            raise e

    @property
    def mcaacaudiobytesrate(self) :
        """Rate (/s) counter for mcaacaudiobytes."""
        try :
            return self._mcaacaudiobytesrate
        except Exception as e:
            raise e

    @property
    def mcandroid(self) :
        """Total number of android requests to netscaler."""
        try :
            return self._mcandroid
        except Exception as e:
            raise e

    @property
    def mccaplelivestrmngvid(self) :
        """This tells the total number of AppleLive videos served by NS."""
        try :
            return self._mccaplelivestrmngvid
        except Exception as e:
            raise e

    @property
    def mciosrate(self) :
        """Rate (/s) counter for mcios."""
        try :
            return self._mciosrate
        except Exception as e:
            raise e

    @property
    def mctotvideo(self) :
        """ """
        try :
            return self._mctotvideo
        except Exception as e:
            raise e

    @property
    def mcmssmthstrvidplrate(self) :
        """Rate (/s) counter for mcmssmthstrvidpl."""
        try :
            return self._mcmssmthstrvidplrate
        except Exception as e:
            raise e

    @property
    def mcapplelivestreamingvidbytesrate(self) :
        """Rate (/s) counter for mcapplelivestreamingvidbytes."""
        try :
            return self._mcapplelivestreamingvidbytesrate
        except Exception as e:
            raise e

    @property
    def mcyoutubedashbytesrate(self) :
        """Rate (/s) counter for mcyoutubedashbytes."""
        try :
            return self._mcyoutubedashbytesrate
        except Exception as e:
            raise e

    @property
    def mcapplelivestreamingplaylistvidbytespl(self) :
        """This tells the total number of AppleLive Playlist bytes served by NS ."""
        try :
            return self._mcapplelivestreamingplaylistvidbytespl
        except Exception as e:
            raise e

    @property
    def mcmp4vidbytes(self) :
        """This tells the total number of MP4 video bytes served by NS ."""
        try :
            return self._mcmp4vidbytes
        except Exception as e:
            raise e

    @property
    def mcmssmthstrmvidbytesrate(self) :
        """Rate (/s) counter for mcmssmthstrmvidbytes."""
        try :
            return self._mcmssmthstrmvidbytesrate
        except Exception as e:
            raise e

    @property
    def mc3gpvidbytesrate(self) :
        """Rate (/s) counter for mc3gpvidbytes."""
        try :
            return self._mc3gpvidbytesrate
        except Exception as e:
            raise e

    @property
    def mcaudiorate(self) :
        """Rate (/s) counter for mctotaudio."""
        try :
            return self._mcaudiorate
        except Exception as e:
            raise e

    @property
    def mcyoutubedashbytes(self) :
        """This tells the total number of YouTube DASH bytes served by NS ."""
        try :
            return self._mcyoutubedashbytes
        except Exception as e:
            raise e

    @property
    def mcmp4vidrate(self) :
        """Rate (/s) counter for mcmp4vid."""
        try :
            return self._mcmp4vidrate
        except Exception as e:
            raise e

    @property
    def mcmp4vidbytesrate(self) :
        """Rate (/s) counter for mcmp4vidbytes."""
        try :
            return self._mcmp4vidbytesrate
        except Exception as e:
            raise e

    @property
    def mcunidentified(self) :
        """Total number of unidentified requests to netscaler."""
        try :
            return self._mcunidentified
        except Exception as e:
            raise e

    @property
    def mcios(self) :
        """Total number of IOS requests to netscaler."""
        try :
            return self._mcios
        except Exception as e:
            raise e

    @property
    def mc3pvidrate(self) :
        """Rate (/s) counter for mc3pvid."""
        try :
            return self._mc3pvidrate
        except Exception as e:
            raise e

    @property
    def mccapplelivestrmngvidplrate(self) :
        """Rate (/s) counter for mccapplelivestrmngvidpl."""
        try :
            return self._mccapplelivestrmngvidplrate
        except Exception as e:
            raise e

    @property
    def mctoherrate(self) :
        """Rate (/s) counter for mctotother."""
        try :
            return self._mctoherrate
        except Exception as e:
            raise e

    @property
    def mcotherrate(self) :
        """Rate (/s) counter for mcother."""
        try :
            return self._mcotherrate
        except Exception as e:
            raise e

    @property
    def mcenchlsrate(self) :
        """Rate (/s) counter for mcenchls."""
        try :
            return self._mcenchlsrate
        except Exception as e:
            raise e

    @property
    def mcmssmthstrmplvidbytesplrate(self) :
        """Rate (/s) counter for mcmssmthstrmplvidbytespl."""
        try :
            return self._mcmssmthstrmplvidbytesplrate
        except Exception as e:
            raise e

    @property
    def mccapplelivestrmngvidpl(self) :
        """This tells the total number of AppleLive Playlist served by NS."""
        try :
            return self._mccapplelivestrmngvidpl
        except Exception as e:
            raise e

    @property
    def mcencandroidrate(self) :
        """Rate (/s) counter for mcencandroid."""
        try :
            return self._mcencandroidrate
        except Exception as e:
            raise e

    @property
    def mcmssmthstrmvid(self) :
        """This tells the total number of Microsoft SmoothStreaming videos served by NS."""
        try :
            return self._mcmssmthstrmvid
        except Exception as e:
            raise e

    @property
    def mcencdash(self) :
        """Total number of encrypted Youtube DASH video streams."""
        try :
            return self._mcencdash
        except Exception as e:
            raise e

    @property
    def mcandroidrate(self) :
        """Rate (/s) counter for mcandroid."""
        try :
            return self._mcandroidrate
        except Exception as e:
            raise e

    @property
    def mcaacaudiorate(self) :
        """Rate (/s) counter for mcaacaudio."""
        try :
            return self._mcaacaudiorate
        except Exception as e:
            raise e

    @property
    def mctotother(self) :
        """ """
        try :
            return self._mctotother
        except Exception as e:
            raise e

    @property
    def mcencdashrate(self) :
        """Rate (/s) counter for mcencdash."""
        try :
            return self._mcencdashrate
        except Exception as e:
            raise e

    @property
    def mcmssmthstrmvidbytes(self) :
        """This tells the total number of Microsoft SmoothStreaming video bytes served by NS ."""
        try :
            return self._mcmssmthstrmvidbytes
        except Exception as e:
            raise e

    @property
    def mcencios(self) :
        """Total number of encrypted video streams requested by IOS devices."""
        try :
            return self._mcencios
        except Exception as e:
            raise e

    @property
    def mcadtsaudiorate(self) :
        """Rate (/s) counter for mcadtsaudio."""
        try :
            return self._mcadtsaudiorate
        except Exception as e:
            raise e

    @property
    def mcaacaudio(self) :
        """This tells the total number of AAC audios served by NS."""
        try :
            return self._mcaacaudio
        except Exception as e:
            raise e

    @property
    def mcflvvidrate(self) :
        """Rate (/s) counter for mcflvvid."""
        try :
            return self._mcflvvidrate
        except Exception as e:
            raise e

    @property
    def mcencotherrate(self) :
        """Rate (/s) counter for mcencother."""
        try :
            return self._mcencotherrate
        except Exception as e:
            raise e

    @property
    def mcapplelivestreamingplaylistvidbytesplrate(self) :
        """Rate (/s) counter for mcapplelivestreamingplaylistvidbytespl."""
        try :
            return self._mcapplelivestreamingplaylistvidbytesplrate
        except Exception as e:
            raise e

    @property
    def mcmssmthstrvidpl(self) :
        """This tells the total number of Microsoft SmoothStreaming playlist served by NS."""
        try :
            return self._mcmssmthstrvidpl
        except Exception as e:
            raise e

    @property
    def mcflvvidbytes(self) :
        """This tells the total number of FLV bytes served by NS ."""
        try :
            return self._mcflvvidbytes
        except Exception as e:
            raise e

    @property
    def mcmssmthstrmvidrate(self) :
        """Rate (/s) counter for mcmssmthstrmvid."""
        try :
            return self._mcmssmthstrmvidrate
        except Exception as e:
            raise e

    @property
    def mcyoutubedashrate(self) :
        """Rate (/s) counter for mcyoutubedash."""
        try :
            return self._mcyoutubedashrate
        except Exception as e:
            raise e

    @property
    def mcapplelivestreamingvidbytes(self) :
        """This tells the total number of AppleLive video bytes served by NS ."""
        try :
            return self._mcapplelivestreamingvidbytes
        except Exception as e:
            raise e

    @property
    def mcadtsaudiobytesrate(self) :
        """Rate (/s) counter for mcadtsaudiobytes."""
        try :
            return self._mcadtsaudiobytesrate
        except Exception as e:
            raise e

    @property
    def mcmssmthstrmplvidbytespl(self) :
        """This tells the total number of Microsoft SmoothStreaming playlist bytes served by NS ."""
        try :
            return self._mcmssmthstrmplvidbytespl
        except Exception as e:
            raise e

    @property
    def mcadtsaudio(self) :
        """This tells the total number of ADTS audios served by NS."""
        try :
            return self._mcadtsaudio
        except Exception as e:
            raise e

    @property
    def mclaptopdesktp(self) :
        """Total number of laptop/desktop requests to netscaler."""
        try :
            return self._mclaptopdesktp
        except Exception as e:
            raise e

    @property
    def mcencother(self) :
        """Total number of encrypted video streams requested by non-Android and non-IOS devices."""
        try :
            return self._mcencother
        except Exception as e:
            raise e

    def _get_nitro_response(self, service, response) :
        """converts nitro response into object and returns the object array in case of get request.

        :param service: 
        :param response: 

        """
        try :
            result = service.payload_formatter.string_to_resource(mediaclassification_response, response, self.__class__.__name__.replace('_stats',''))
            if(result.errorcode != 0) :
                if (result.errorcode == 444) :
                    service.clear_session(self)
                if result.severity :
                    if (result.severity == "ERROR") :
                        raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
                else :
                    raise nitro_exception(result.errorcode, str(result.message), str(result.severity))
            return result.mediaclassification
        except Exception as e :
            raise e

    def _get_object_name(self) :
        """Returns the value of object identifier argument"""
        try :
            return 0
        except Exception as e :
            raise e



    @classmethod
    def  get(cls, service, name="", option_="") :
        """Use this API to fetch the statistics of all mediaclassification_stats resources that are configured on netscaler.

        :param service: 
        :param name:  (Default value = "")
        :param option_:  (Default value = "")

        """
        try :
            obj = mediaclassification_stats()
            if not name :
                response = obj.stat_resources(service, option_)
            return response
        except Exception as e:
            raise e

    class Clearstats:
        """ """
        basic = "basic"
        full = "full"

class mediaclassification_response(base_response) :
    """ """
    def __init__(self, length=1) :
        self.mediaclassification = []
        self.errorcode = 0
        self.message = ""
        self.severity = ""
        self.sessionid = ""
        self.mediaclassification = [mediaclassification_stats() for _ in range(length)]

