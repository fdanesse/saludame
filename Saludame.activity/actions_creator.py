# -*- coding: utf-8 -*-

import effects
import actions
import os

BARS_DECREASE_RATE = -0.1

#ANIMATIONS
BLIP_PATH = os.path.normpath("assets/sound/blip.ogg")
APPLE_PATH = os.path.normpath("assets/food/apple")
STEW_PATH = os.path.normpath("assets/food/stew")
CHEW_PATH = os.path.normpath("assets/kid/actions/eat")
JUMP_ROPE_PATH = os.path.normpath("assets/kid/actions/ropejump")

#EFFECTS
##BACKGROUND EFFECTS
#BAR DECREASE

bar_dec_effect = effects.Effect(None, [("nutrition", BARS_DECREASE_RATE), ("spare_time", BARS_DECREASE_RATE), ("physica", BARS_DECREASE_RATE), ("hygiene", BARS_DECREASE_RATE)])



#actions list tuple format:
#[("action's id","icon_path","picture_path", appereance_probability, time_span, 
#    kid_animation_frame_rate,kid_animation_loop_times, kid_animation_path, window_animation_frame_rate,
#    window_animation_loop_times, window_animation_path, sound_loop_times, sound_path, action's effect)]

### ACTIONS THAT AFFECT STATUS BARS

actions_list = [
    #id, icon, picture, appereance_probability, time_span, kid_animation_frame_rate, kid_animation_loop_times, kid_animation_path, window_animation_frame_rate, window_animation_loop_times, window_animation_path, sound_loop_times, sound_path, effect
    
    # Fruit
    ("eat_apple", 0.3, 8, 3, 3, CHEW_PATH, 3, 1, APPLE_PATH, 4, BLIP_PATH,
        effects.Effect(None, [("v_frutas", 3.0), ("weight", 0.5)])
    ),
    
    ("eat_orange", 0.3, 8, 3, 3, CHEW_PATH, 3, 1, APPLE_PATH, 4, BLIP_PATH,
        effects.Effect(None, [("v_frutas", 3.0), ("weight", 0.5)])
    ),

    ("eat_banana", 0.3, 8, 3, 3, CHEW_PATH, 3, 1, APPLE_PATH, 4, BLIP_PATH,
        effects.Effect(None, [("v_frutas", 3.0), ("weight", 0.5)])
    ),

    ("eat_kiwi", 0.3, 8, 3, 3, CHEW_PATH, 3, 1, APPLE_PATH, 4, BLIP_PATH,
        effects.Effect(None, [("v_frutas", 3.0), ("weight", 0.5)])
    ),

    # Meals
    ("eat_stew", 0.3, 8, 3, 3, CHEW_PATH, 3, 1, STEW_PATH, 4, BLIP_PATH,
        effects.Effect(None, [("c_leguminosas", 2.0), ("v_frutas", 1.0), ("c_huevos", 0.5), ("g_aceites", 1.0), ("agua", 1.0), ("weight", 1.0)])
    ),
    ("eat_churrasco", 0.3, 8, 3, 3, CHEW_PATH, 3, 1, STEW_PATH, 4, BLIP_PATH,
        effects.Effect(None, [("c_leguminosas", 2.0), ("v_frutas", 1.0), ("c_huevos", 0.5), ("g_aceites", 1.0), ("agua", 1.0), ("weight", 1.0)])
    ),
    ("eat_beaver", 0.3, 8, 3, 3, CHEW_PATH, 3, 1, STEW_PATH, 4, BLIP_PATH,
        effects.Effect(None, [("c_huevos", 3.0), ("g_aceites", 2.0), ("weight", 1.0)])
    ),
    ("eat_milanesa", 0.3, 8, 3, 3, CHEW_PATH, 3, 1, STEW_PATH, 4, BLIP_PATH,
        effects.Effect(None, [("c_huevos", 3.0), ("g_aceites", 2.0), ("weight", 2.0)])
    ),
    ("eat_torta_frita", 0.3, 8, 3, 3, CHEW_PATH, 3, 1, STEW_PATH, 4, BLIP_PATH,
        effects.Effect(None, [("c_huevos", 3.0), ("weight", 1.0)])
    ),
    ("salad", 0.3, 8, 3, 3, CHEW_PATH, 3, 1, STEW_PATH, 4, BLIP_PATH,
        effects.Effect(None, [("v_frutas", 2.0), ("weight", 0.5)])
    ),
    ("pascualina", 0.3, 8, 3, 3, CHEW_PATH, 3, 1, STEW_PATH, 4, BLIP_PATH,
        effects.Effect(None, [("v_frutas", 2.0), ("c_leguminosas", 1.0), ("weight", 1.0)])
    ),
    ("tortilla_verdura", 0.3, 8, 3, 3, CHEW_PATH, 3, 1, STEW_PATH, 4, BLIP_PATH,
        effects.Effect(None, [("v_frutas", 2.0), ("g_aceites", 1.0), ("weight", 1.0)])
    ),
    
    # Breakfast
    ("tostadas_membrillo", 0.3, 8, 3, 3, CHEW_PATH, 3, 1, STEW_PATH, 4, BLIP_PATH,
        effects.Effect(None, [("c_leguminosas", 1.5), ("dulces", 1.5), ("weight", 1.0)])
    ),
    
    ("tostadas_queso", 0.3, 8, 3, 3, CHEW_PATH, 3, 1, STEW_PATH, 4, BLIP_PATH,
        effects.Effect(None, [("c_leguminosas", 1.5), ("l_quesos", 1.5), ("weight", 1.0)])
    ),
    
    ("galletitas_saladas", 0.3, 8, 3, 3, CHEW_PATH, 3, 1, STEW_PATH, 4, BLIP_PATH,
        effects.Effect(None, [("c_leguminosas", 2.0), ("weight", 1.0)])
    ),
    
    ("galletitas_dulces", 0.3, 8, 3, 3, CHEW_PATH, 3, 1, STEW_PATH, 4, BLIP_PATH,
        effects.Effect(None, [("c_leguminosas", 2.0), ("weight", 1.0)])
    ),
    
    ("galletitas_dulce_leche", 0.3, 8, 3, 3, CHEW_PATH, 3, 1, STEW_PATH, 4, BLIP_PATH,
        effects.Effect(None, [("c_leguminosas", 2.0), ("dulces", 2.0), ("weight", 1.0)])
    ),
    
    ("leche_chocolatada", 0.3, 8, 3, 3, CHEW_PATH, 3, 1, STEW_PATH, 4, BLIP_PATH,
        effects.Effect(None, [("l_quesos", 2.0), ("dulces", 2.0), ("agua", 1.0), ("weight", 2.0)])
    ),
    
    ("leche_cafe", 0.3, 8, 3, 3, CHEW_PATH, 3, 1, STEW_PATH, 4, BLIP_PATH,
        effects.Effect(None, [("l_quesos", 2.0), ("agua", 1.0), ("weight", 2.0)])
    ),
    
    ("leche", 0.3, 8, 3, 3, CHEW_PATH, 3, 1, STEW_PATH, 4, BLIP_PATH,
        effects.Effect(None, [("l_quesos", 2.0), ("agua", 1.0), ("weight", 2.0)])
    ),
    
    ("leche_cereales", 0.3, 8, 3, 3, CHEW_PATH, 3, 1, STEW_PATH, 4, BLIP_PATH,
        effects.Effect(None, [("l_quesos", 2.0), ("c_leguminosas", 1.0), ("agua", 1.0), ("weight", 2.0)])
    ),
    
    # Líquidos
    ("agua", 0.3, 8, 3, 3, CHEW_PATH, 3, 1, None, 4, BLIP_PATH,
        effects.Effect(None, [("agua", 1.0)])
    ),
    ("limonada", 0.3, 8, 3, 3, CHEW_PATH, 3, 1, None, 4, BLIP_PATH,
        effects.Effect(None, [("agua", 1.0)])
    ),
    ("jugo_naranja", 0.3, 8, 3, 3, CHEW_PATH, 3, 1, None, 4, BLIP_PATH,
        effects.Effect(None, [("agua", 1.0)])
    ),
    ("jugo_peras", 0.3, 8, 3, 3, CHEW_PATH, 3, 1, None, 4, BLIP_PATH,
        effects.Effect(None, [("agua", 1.0)])
    ),
    ("jugo_zanahorias", 0.3, 8, 3, 3, CHEW_PATH, 3, 1, None, 4, BLIP_PATH,
        effects.Effect(None, [("agua", 1.0)])
    ),
    
    # Sports
    ("sport_football", 0.3, 8, 0, 0, None, 3, 1, None, 4, "sound_path",
        effects.Effect(None, [("energy", 0.5), ("sports", 2.0), ("shower", -0.5), ("fun", 2.0)])
    ),

    ("sport_run", 0.3, 8, 0, 0, None, 3, 1, None, 4, "sound_path",
        effects.Effect(None, [("energy", 0.5), ("sports", 2.0), ("shower", -0.5), ("fun", 2.0)])
    ),
    
    ("sport_hide_seek", 0.3, 8, 0, 0, None, 3, 1, None, 4, "sound_path",
        effects.Effect(None, [("energy", 0.5), ("sports", 2.0), ("shower", -0.5), ("fun", 2.0)])
    ),
    
    ("sport_jump", 0.3, 8, 0, 0, JUMP_ROPE_PATH, 3, 1, None, 4, "sound_path",
        effects.Effect(None, [("energy", 0.5), ("sports", 2.0), ("shower", -0.5), ("fun", 2.0)])
    ),
    
    # Tiempo Libre
    ("sp_sleep", 0.3, 8, 0, 0, None, 3, 1, None, 4, "sound_path",
        effects.Effect(None, [("energy", 1.0), ("relaxing", 2.0)])
    ),

    ("sp_talk", 0.3, 8, 0, 0, None, 3, 1, None, 4, "sound_path",
        effects.Effect(None, [("fun", 0.5)])
    ),
    
    ("sp_study", 0.3, 8, 0, 0, None, 3, 1, None, 4, "sound_path",
        effects.Effect(None, [("energy", -0.5), ("responsability", 2.0)])
    ),
    
    ("sp_clean", 0.3, 8, 0, 0, None, 3, 1, None, 4, "sound_path",
        effects.Effect(None, [("energy", -0.5), ("responsability", 2.0)])
    ),
    
    # Higiene
    ("shower", 0.3, 8, 0, 0, None, 3, 1, None, 4, "sound_path",
        effects.Effect(None, [("shower", 5.0)])
    ),

    ("brush_teeth", 0.3, 8, 0, 0, None, 3, 1, None, 4, "sound_path",
        effects.Effect(None, [("b_teeth", 0.5)])
    ),
    
    ("wash_hands", 0.3, 8, 0, 0, None, 3, 1, None, 4, "sound_path",
        effects.Effect(None, [("w_hands", 3.0)])
    ),
    
    ("toilet", 0.3, 1.9, 0, 1, "assets/kid/actions/toilet", 3, 1, None, 4, "sound_path",
        effects.Effect(None, [("toilet", 4.0)])
    ),
    
    # Default action - affects the bars continuously
    ("BARS_DEC", 1.0, -1, 0, 0, None, 0, 0, None, 0, None, bar_dec_effect)
]

### ACTIONS THAT SET CHARACTER LOCATION

locations_ac_list = [("goto_schoolyard", None, 1, None, None, None, None, None, None, None, None, effects.LocationEffect(None, "schoolyard")),
                     ("goto_country", None, 1, None, None, None, None, None, None, None, None, effects.LocationEffect(None, "country")),
                     ("goto_classroom", None, 1, None, None, None, None, None, None, None, None, effects.LocationEffect(None, "classroom")),
                     ("goto_square", None, 1, None, None, None, None, None, None, None, None, effects.LocationEffect(None, "square")),
                     ("goto_living", None, 1, None, None, None, None, None, None, None, None, effects.LocationEffect(None, "home")),
                     ("goto_bedroom", None, 1, None, None, None, None, None, None, None, None, effects.LocationEffect(None, "home")),
                     ("goto_kitchen", None, 1, None, None, None, None, None, None, None, None, effects.LocationEffect(None, "home")),
                     ("goto_bathroom", None, 1, None, None, None, None, None, None, None, None, effects.LocationEffect(None, "home"))
                    ]

class ActionsLoader:
    """
    Crea las acciones (Action) y sus efectos (Effect y EffectStatus) asociados.
    """
    
    def __init__(self, bar_controller, game_manager):
        self.bar_controller = bar_controller
        self.game_manager = game_manager
        self.actions_list = self.__load_actions()
        
        
    def get_actions_list(self): 
        return self.actions_list
    
    def __load_actions(self):
        status_actions = [actions.Action(action[0], action[1], action[2], action[3], action[4], action[5], action[6], action[7], action[8], action[9], action[10], self.__set_bar_controller(action[11])) for action in actions_list]
        
        location_actions = [actions.Action(action[0], action[1], action[2], action[3], action[4], action[5], action[6], action[7], action[8], action[9], action[10], self.__set_game_manager(action[11])) for action in locations_ac_list]
        
        return status_actions + location_actions
        
    def __set_bar_controller(self, effect):
        effect.set_bar_controller(self.bar_controller)
        return effect
    
    def __set_game_manager(self, location_effect):
        location_effect.set_game_manager(self.game_manager)
        return location_effect


