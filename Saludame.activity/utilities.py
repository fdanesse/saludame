# -*- coding: utf-8 -*-

# Utilitarios: Text, Button (abstract), ImageButton, TextButton

from widget import *
import pygame

class Text(Widget):
    
    ALIGN_LEFT = 0
    ALIGN_RIGHT = 1
    
    def __init__(self, container_rect, x, y, frame_rate, text, size, color, alignment=ALIGN_LEFT, bold=False, italic=False):
        self.font = get_font(size, bold, italic)
        self.text = unicode(text)
        self.color = color
        
        # Render the text and calculate the size
        render = self.font.render(self.text, False, color)
        if alignment == Text.ALIGN_LEFT:
            rect = render.get_rect(topleft=(x, y))
        else:
            rect = render.get_rect(topright=(x, y))
        
        # Make it fit in the container
        if rect.right > container_rect.right:
            rect.right = container_rect.right
        if rect.bottom > container_rect.bottom:
            rect.bottom = container_rect.bottom
        
        Widget.__init__(self, container_rect, rect, frame_rate)
        
        self.refresh()
    
    def refresh(self):
        background = self.get_background_rect().copy()
        self.background = self.font.render(self.text, False, self.color)
    
    def switch_color_text(self, color):
        self.refresh()
        return (self)
    
class Image(Widget):
    def __init__(self, container, rect, frame_rate, image):
        
        if not isinstance(image, pygame.Surface):
            self.background = pygame.image.load(image).convert_alpha()
        else:
            self.background = image
        Widget.__init__(self, container, rect, frame_rate, self.background)        
        

class Button(Widget):
    
    # Clase abstracta que representa un boton
    
    def __init__(self, container, rect, frame_rate, surface, cb_click=None, cb_over=None, cb_out=None):
        
        Widget.__init__(self, container, rect, frame_rate, surface)
        
        self.function_on_mouse_click = cb_click
        self.function_on_mouse_over = cb_over
        self.function_on_mouse_out = cb_out
        
        self.over = False
        
    def contains_point(self, x, y):
        return self.rect_absolute.collidepoint(x, y)
    
    def set_tooltip(self, text):
        self.tooltip = text
    
    def on_mouse_click(self):
        if self.function_on_mouse_click: # if there's a callback setted makes the call
            self.function_on_mouse_click(self)
        
    def on_mouse_over(self):
        if self.function_on_mouse_over: # if there's a callback setted makes the call
            self.function_on_mouse_over(self)
    
    def on_mouse_out(self):
        if self.function_on_mouse_out: # if there's a callback setted makes the call
            self.function_on_mouse_out(self)
            
    def set_on_mouse_click(self, fn):
        self.function_on_mouse_click = fn
   
    def set_on_mouse_over(self, fn):
        self.function_on_mouse_over = fn

    def set_on_mouse_out(self, fn):
        self.function_on_mouse_out = fn   
    

class ImageButton(Button):
    
    def __init__(self, container, rect, frame_rate, image, cb_click=None, cb_over=None, cb_out=None):
        
        self.image = image       
        if not isinstance(image, pygame.Surface):
            self.image = pygame.image.load(image).convert_alpha()
        
        rect.size = self.image.get_rect().size
        Button.__init__(self, container, rect, frame_rate, self.image, cb_click, cb_over, cb_out)
    
    def switch_image_background(self, image):
        if not isinstance(image, pygame.Surface):
            image = pygame.image.load(image).convert_alpha()
        self.background = image
        
class TextButton(ImageButton):     
    def __init__(self, container, rect, frame_rate, text, size, color, cb_click=None, cb_over=None, cb_out=None):
        self.text = Text(container, rect.x, rect.y, frame_rate, text, size, color)
        ImageButton.__init__(self, container, self.text.rect_in_container, frame_rate, self.text.background, cb_click, cb_over, cb_out)
        
    def switch_color_text(self, color):
        self.background = self.text.switch_color_text(color).background        
        
def change_color(surface, old_color, new_color):
    # No funciona en pygame 1.8.0
    #image_pixel_array = pygame.PixelArray(self.sprite)
    #image_pixel_array.replace(old_color, new_color)
    
    #mapped_int = surface.map_rgb(old_color)
    #surface.set_palette_at(mapped_int, new_color[0:3])   
    
    i = 0
    indexes = []
    palette = surface.get_palette()
    for color in palette:
        if get_color_tuple(color) == get_color_tuple(old_color):
            indexes += [i]
        i += 1
    
    for i in indexes:
        surface.set_palette_at(i, get_color_tuple(new_color))

def get_color_tuple(color):
    if isinstance(color, tuple):
        return color[0:3]
    elif isinstance(color, pygame.Color):
        return (color.r, color.g, color.b, color.a)[0:3]
    else:
        color = pygame.Color(color)
        return get_color_tuple(color)
    
class TextBlock(Widget):
    def __init__(self, container, x, y, frame_rate, text, size, color):        
        Widget.__init__(self, container, pygame.Rect(x,y,0,0), frame_rate)
        
        self.lines = []
        self.font = get_font(size)
        self.color = color
        self.parse_lines(text)
        self.size = size
        
    def parse_lines(self, text):
        (b, _, a) = text.partition("\n")
        self.lines.append(b)
        while(a != ''):
            (b, _, a) = a.partition("\n")
            self.lines.append(b)
        
    def draw(self, screen):
        number_of_lines = 0
        for l in self.lines:
            number_of_lines += 1           
            r = self.font.render(l, False, self.color)
            screen.blit(r, (self.rect_absolute.left, self.rect_absolute.top + r.get_rect().height * number_of_lines)) 

font_dict = {}  # Chaches created font instances
def get_font(size, bold=False, italic=False):
    key = (size, bold, italic)
    if key in font_dict:
        return font_dict[key]
    
    if bold:
        font = pygame.font.Font("assets/fonts/DroidSans-Bold.ttf", size)
    else:
        font = pygame.font.Font("assets/fonts/DroidSans.ttf", size)
    
    if italic:
        font.set_italic(True)
    
    font_dict[key] = font
    
    return font
