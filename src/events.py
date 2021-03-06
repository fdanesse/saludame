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

MAX_BAR_VALUE = 100.0 #maximo valor que puede alcanzar una barra
                      #necesario para el calculo de probabilidades

from gi.repository import GObject


class Event(GObject.Object):
    
    def __init__(self, event_type, directory_path, name, description, impact, trigger, time_span, conditioned_bars, effect, library_link, level, preferred_mood):
        
        GObject.Object.__init__(self)

        if not time_span:
            time_span = 999
        
        self.event_type = event_type
        self.directory_path = directory_path
        self.name = name
        self.description = description
        
        self.impact = impact
        self.preferred_mood = preferred_mood
        
        self.trigger = trigger          # "random" - it's selected at random by it's probability,
                                        # "triggered" - it should appear only when it's triggered as a consequence of an action and it's probability is higher than zero
                                        # "environment" - it's triggered every time there's a change in {place, time, weather}
        self.time_span = time_span
        self.time_left = time_span

        self.effect = effect
        
        self.operator = conditioned_bars[0]
        self.condicioned_bars = conditioned_bars[1]
        self.probability = 0.0 # starts in 0.0
        self.level = level      # Starting level, in levels prior to this one, the event is not triggered

        self.library_link = library_link
        
        self.restrictions = {}
    
    def check_restrictions(self, restrictions):
        for restriction_id, values in self.restrictions.items():
            value = restrictions[restriction_id]
            if not value in values:
                return False
        return True
        
    def update_probability(self, bars_value_dic, restrictions, triggered = False):
        """
        Updates event probability
        """
        
        self.probability = 0.0
        
        if not self.check_restrictions(restrictions):
            return 0.0
            
        probs = []
        
        if self.condicioned_bars:
            
            for bar_con in self.condicioned_bars:
                bar_id, probability_type, threshold, max_prob = bar_con
                
                bar_value = bars_value_dic[bar_id]
                
                prob = 0.0
                if probability_type == "direct":
                    if bar_value >= threshold:
                        prob = max_prob * ((bar_value - threshold) / (MAX_BAR_VALUE - threshold))
                    
                elif probability_type == "indirect":
                    if bar_value <= threshold:
                        prob = max_prob * ((threshold - bar_value) / threshold)
                    
                elif probability_type == "constant+":
                    if bar_value >= threshold :
                        prob = float(max_prob)
                
                elif probability_type == "constant-":
                    if bar_value <= threshold :
                        prob = float(max_prob)

                elif probability_type == "range":
                    rMin, rMax = threshold
                    pMin, pMax = max_prob
                    if rMin <= bar_value and bar_value <= rMax:
                        prob = pMin + (bar_value-rMin)*(pMax-pMin)/(rMax-rMin)
                
                if self.operator == "all" and prob == 0.0:
                    return 0.0
                    
                probs.append(prob)
        
        if probs:
            self.probability = sum(probs) / len(probs)
        
        return self.probability
    
    def get_probability(self):
        #eventually we just take the conditioned
        #probability
        return int(self.probability)
        
    def perform(self):
        if self.time_left is None or self.time_left:
            if self.effect:
                self.effect.activate(1)
                
            if not self.time_left is None:
                self.time_left -= 1
    
    def reset(self):
        self.time_left = self.time_span
    
    def add_restriction(self, restriction_id, values):
        """ Adds a restriction for this event to be triggered
            place: []
            weather: []
            time: []
            clothes: []
        """
        self.restrictions[restriction_id] = values
        
        
class PersonalEvent(Event):
    def __init__(self, picture, kid_animation_path, name, description, impact, trigger, time_span, conditioned_bars, effect, kid_message, library_link, level=1, preferred_mood=9):
        Event.__init__(self, "personal", picture, name, description, impact, trigger, time_span, conditioned_bars, effect, library_link, level, preferred_mood)
        
        self.kid_animation_path = kid_animation_path
    
        # Messages at ballon
        self.kid_message = kid_message
        self.message_time_span = 250
    
    
class SocialEvent(Event):
    
    def __init__(self, picture, person_path, name, description, impact, trigger, time_span, conditioned_bars, effect, message, library_link, level=1, preferred_mood=9):
        Event.__init__(self, "social", picture, name, description, impact, trigger, time_span, conditioned_bars, effect, library_link, level, preferred_mood)
        
        self.time_left = time_span
        
        self.person_path = person_path
        self.person_message = message
        self.message_time_span = 250
