# -*- coding: utf-8 -*-

"""
    AliveGR Add-on
    Author: Twilight0

        This program is free software: you can redistribute it and/or modify
        it under the terms of the GNU General Public License as published by
        the Free Software Foundation, either version 3 of the License, or
        (at your option) any later version.

        This program is distributed in the hope that it will be useful,
        but WITHOUT ANY WARRANTY; without even the implied warranty of
        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
        GNU General Public License for more details.

        You should have received a copy of the GNU General Public License
        along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import os
import sys
import urllib
import urlparse
import xbmc
import xbmcaddon
import xbmcgui
import xbmcplugin

# Global variables:
language = xbmcaddon.Addon().getLocalizedString
addonname = xbmcaddon.Addon().getAddonInfo("name")
addonpath = xbmcaddon.Addon().getAddonInfo("path")
addondesc = language(30000).encode("utf-8")
datapath = xbmc.translatePath(xbmcaddon.Addon().getAddonInfo("profile")).decode("utf-8")
addonicon = os.path.join(addonpath, 'icon.png')
addonart = os.path.join(addonpath, 'resources/art')
addonlogos = os.path.join(addonpath, 'resources/logos')
addonfanart = os.path.join(addonpath, 'fanart.jpg')
LiveTVimage = os.path.join(addonart, 'root_livetv.jpg')
RadioImage = os.path.join(addonart, 'radios_all.jpg')
channel_urls = 'https://raw.githubusercontent.com/Twilight0/Channel-Lists/master/alivegr-tv.m3u'
radio_urls = 'https://raw.githubusercontent.com/Twilight0/Channel-Lists/master/alivegr-radios.m3u'

# Handlers:
addon_url = sys.argv[0]
addon_handle = int(sys.argv[1])
args_handler = urlparse.parse_qs(sys.argv[2][1:])

# Set the content type:
xbmcplugin.setContent(addon_handle, 'movies')

# Function to build addon's url
def build_url(query):
    return addon_url + '?' + urllib.urlencode(query)


mode = args_handler.get('mode', None)
if mode is None:
    url = build_url({'mode': 'folder', 'foldername': 30001})
    LiveTV = xbmcgui.ListItem(language(30001), iconImage=LiveTVimage)
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=channel_urls, listitem=LiveTV)
    url = build_url({'mode': 'folder', 'foldername': 30002})
    Radio = xbmcgui.ListItem(language(30002), iconImage=RadioImage)
    xbmcplugin.addDirectoryItem(handle=addon_handle, url=radio_urls, listitem=Radio)
    xbmcplugin.endOfDirectory(addon_handle)
