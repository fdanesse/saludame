# -*- coding: utf-8 -*-

# Copyright (C) 2011 ceibalJAM! - ceibaljam.org
# This file is part of Saludame.
#
# Saludame is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Saludame is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with Saludame. If not, see <http://www.gnu.org/licenses/>.

import os
import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import GLib

import gettext
gettextold = gettext.gettext

from sugargame.canvas import PygameCanvas

def _(string):
    string = gettextold(string)
    if isinstance(string, unicode):
        return string.upper()
    else:
        return unicode(string.decode("utf-8")).upper()
gettext.gettext = _

from gettext import gettext as _

from startup_window import StartupWindow
from game import Main
from credits import Credits
from content_window import ContentWindow
from guides_window import GuidesWindow

import logging

BASEPATH = os.path.dirname(__file__)


class SaludameActivity(Gtk.Window):
    
    def __init__(self):
    
        Gtk.Window.__init__(self)

        self.set_title("Saludame")
        self.set_icon_from_file(os.path.join(BASEPATH, "assets/saludame.svg"))
        self.set_resizable(True)
        self.set_position(Gtk.WindowPosition.CENTER)

        self.game_init = False
        
        self.maximize()
        
        self.startup_window = StartupWindow(self._start_cb, self._load_last_cb)
        self.pygame_canvas = PygameCanvas()
        self.health_library = ContentWindow()
        self.guides = GuidesWindow()
        self.credits = Credits()
        
        self.items = Gtk.Notebook()
        
        self.items.append_page(self.startup_window, Gtk.Label(_("Activity")))
        self.items.append_page(self.pygame_canvas, Gtk.Label(_("Game")))
        self.items.append_page(self.health_library, Gtk.Label(_("Health Library")))
        self.items.append_page(self.guides, Gtk.Label(_("Guides")))
        self.items.append_page(self.credits, Gtk.Label(_("Credits")))

        self.add(self.items)

        logging.debug("Create main")

        self.game = Main()
        self.game.set_game_over_callback(self.game_over_callback)
        self.game.set_library_function = self.set_library    # Sets the callback to put links in the library
        
        self.show_all()

        self.items.connect('switch_page', self.__switch_page)
        self.connect("delete-event", Gtk.main_quit)
    
        self.items.get_children()[1].hide()

        self.items.set_current_page(0)

    def __switch_page(self, widget, widget_child, indice):
        item = self.items.get_tab_label(self.items.get_children()[indice]).get_text()
        self.game.pause = True    
        if item == _("Game"):
            self.game.pause = False
            if self.game.started:
                self.game.windows_controller.reload_main = True       # Repaints the whole screen
            if self.game_init:
                self.pygame_canvas.translator.hook_pygame()
            else:
                self.game_init = True
                r = self.pygame_canvas.get_allocation()
                GLib.timeout_add(500, self.game.main, True, (r.width, r.height))
            
    def _start_cb(self, gender, name):
        #self.metadata['title'] = _("Saludame") + " " + name
        # FIXME: no debiera funcionar sin genero y nombre.
        # FIXME: Debiera reiniciarse el juego aquí oen __switch_page
        self.game.gender = gender
        self.game.name = name
        self.startup_window.set_welcome()
        self.items.get_children()[1].show()
        self.items.set_current_page(1)

    def set_library(self, link, anchor=None):
        self.items.set_current_page(2)
        self.health_library.set_url(link, anchor)
    
    def _load_last_cb(self, button):
        print "FIXME: Debiera cargar el ultimo juego guardado", self._load_last_cb
        '''
        metadata = self.get_last_game()
        if metadata:
            self.metadata['title'] = metadata['title']
            self.make_toolbox(True)
            self.toolbox.set_current_toolbar(1)
        '''
    
    def game_over_callback(self):
        # FIXME: No parece ejecutarse nunca
        print self.game_over_callback
        #self.make_toolbox(False)
        #self.toolbox.set_current_toolbar(0)             # Move to game tab

    '''
    def get_game_toolbar(self):        
        toolbar = gtk.Toolbar()
        
        # Music Volume scale
        min = 0
        max = 10
        step = 1
        default = 3
        
        image = gtk.Image()
        image.set_from_file("assets/music/music_icon.png")
        image.show()
        
        tool_item = gtk.ToolItem()
        tool_item.set_expand(False)
        tool_item.add(image)
        tool_item.show()
        toolbar.insert(tool_item, -1)
        
        adj = gtk.Adjustment(default, min, max, step)
        scale = gtk.HScale(adj)
        scale.set_update_policy(gtk.UPDATE_DISCONTINUOUS)
        scale.set_size_request(240,15)
        scale.set_draw_value(False)
        scale.connect("value-changed", self.game.volume_changed)
        scale.show()
                
        tool_item = gtk.ToolItem()
        tool_item.set_expand(False)
        tool_item.add(scale)
        tool_item.show()
        toolbar.insert(tool_item, -1)
        
        toolbar.show()
        return toolbar
    '''

if __name__=="__main__":
    SaludameActivity()
    Gtk.main()
