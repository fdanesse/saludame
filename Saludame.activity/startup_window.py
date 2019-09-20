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

import gi
gi.require_version('Gtk', '3.0')
gi.require_version('Gdk', '3.0')
from gi.repository import Gtk
from gi.repository import Gdk
from gi.repository import Pango
from gi.repository import GdkPixbuf

from gettext import gettext as _
    

def get_button(path):
    img = Gtk.Image()
    img.set_from_file(path)
    btn = Gtk.Button()
    btn.set_image(img)
    return btn


story = [
    {
        "image": "assets/slides/history1.jpg"
    },
    {
        "image": "assets/slides/history2.jpg"
    },
    {
        "image": "assets/slides/help.png"
    },
]


class StartupWindow(Gtk.EventBox):
    
    def __init__(self, start_cb, load_last_game_cb):
        
        Gtk.EventBox.__init__(self)
        
        self.start_cb = start_cb
        self.load_last_game_cb = load_last_game_cb
        self.size = (800, 600)
        self.show_all()

    def set_welcome(self, size=False):
        if size: self.size = size
        for child in self.get_children():
            child.destroy()
        self.add(Welcome(self.size, self._new_game, self.load_last_game_cb))
        self.show_all()
        
    def _new_game(self, button):
        for child in self.get_children():
            child.destroy()
        self.add(SelectGenderAndName(self.size, self._gender_selected))
    
    def _gender_selected(self, name, gender):
        for child in self.get_children():
            child.destroy()
        callback = lambda: self.start_cb(gender, name)
        self.add(Introduction(self.size, callback))


class Welcome(Gtk.Fixed):
    
    def __init__(self, size, new_game_cb, load_last_game_cb):
        
        Gtk.Fixed.__init__(self)
        
        image = Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("assets/slides/screen_mainmenu.jpg", size[0], size[1], True)
        image.set_from_pixbuf(pixbuf)
        self.put(image, 0, 0)
        
        h = pixbuf.get_width()/2-114
        v = pixbuf.get_height()/2
        # Tamaño original de las imágenes de los botones => 229, 82
        btn_new = get_button("assets/layout/btn_new_game.png")
        if new_game_cb: btn_new.connect("clicked", new_game_cb)
        self.put(btn_new, h, v)
        
        btn_last_game = get_button("assets/layout/btn_load_last.png")
        if load_last_game_cb: btn_last_game.connect("clicked", load_last_game_cb)
        self.put(btn_last_game, h, v+95)
        
        self.show_all()


class SelectGenderAndName(Gtk.Fixed):
    
    def __init__(self, size, callback):
        
        Gtk.Fixed.__init__(self)
        
        self.callback = callback
        
        image = Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale("assets/slides/screen_name_and_gender.jpg", size[0], size[1], True)
        image.set_from_pixbuf(pixbuf)
        self.put(image, 0, 0)

        self.kid_name = PlaceholderEntry(_('Escribe un nombre'))
        font = 'dejavu 24'
        font_desc = Pango.FontDescription(font)
        self.kid_name.modify_font(font_desc)
        self.kid_name.set_has_frame(False)
        self.kid_name.set_size_request(666, 98)
        self.put(self.kid_name, 172, 100)
                
        btn_boy = get_button("assets/layout/btn_boy.png")
        btn_boy.connect("clicked", self._boy)
        self.put(btn_boy, 169, 233)
        
        btn_girl = get_button("assets/layout/btn_girl.png")
        btn_girl.connect("clicked", self._girl)
        self.put(btn_girl, 602, 233)
        
        self.show_all()
        
    def _boy(self, button):
        self.callback(self.kid_name.get_text(), "boy")

    def _girl(self, button):
        self.callback(self.kid_name.get_text(), "girl")


class PlaceholderEntry(Gtk.Entry):

    _default = True

    def __init__(self, placeholder):
    
        Gtk.Entry.__init__(self)
    
        self.placeholder = placeholder
        self._focus_out_event(self, None)
        self.connect('focus-in-event', self._focus_in_event)
        self.connect('focus-out-event', self._focus_out_event)

    def _focus_in_event(self, widget, event):
        if self._default:
            self.set_text('')
            self.modify_text(Gtk.StateType.NORMAL, Gdk.color_parse('black'))

    def _focus_out_event(self, widget, event):
        if self.get_text() == '':
            self.set_text(self.placeholder)
            self.modify_text(Gtk.StateType.NORMAL, Gdk.color_parse('gray'))
            self._default = True
        else:
            self._default = False

    def get_text(self):
        if self._default:
            return ''
        return self.get_text()


class Introduction(Gtk.Fixed):
    
    def __init__(self, size, callback):
    
        Gtk.Fixed.__init__(self)
        
        self.size = size
        self.callback = callback
        self.index = 0    
        self.show_slide()
        
    def show_slide(self):
        for child in self.get_children():
            child.destroy()
            
        slide = story[self.index]
        
        image = Gtk.Image()
        pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(slide["image"], self.size[0], self.size[1], True)
        image.set_from_pixbuf(pixbuf)
        self.put(image, 0, 0)
        
        btn_back = get_button("assets/layout/btn_back.png")
        btn_back.connect("clicked", self._back)
        self.put(btn_back, 5, pixbuf.get_height()-180)
        if self.index == 0:
            btn_back.set_sensitive(False)
        
        btn_next = get_button("assets/layout/btn_next.png")
        btn_next.connect("clicked", self._next)
        self.put(btn_next, pixbuf.get_width()-105, pixbuf.get_height()-180)
        
        self.show_all()
        
    def _next(self, button):
        if self.index + 1 < len(story):
            self.index += 1
            self.show_slide()
        else:
            self.callback()
        
    def _back(self, button):
        if self.index > 0:
            self.index -= 1
            self.show_slide()
        

if __name__ == "__main__":
    sw = StartupWindow(None, None)
    main_window = Gtk.Window(Gtk.WindowType.TOPLEVEL)
    main_window.maximize()
    main_window.add(sw)
    main_window.show_all()
    main_window.connect("delete-event", Gtk.main_quit)
    Gtk.main()
