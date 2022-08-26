

class default_args(object):
    
    map_name = "3m"
    add_local_obs = False
    add_move_state = False
    add_visible_state = False
    add_distance_state = False
    add_xy_state = False
    add_enemy_action_state = False
    add_agent_id = False
    use_state_agent = True
    use_mustalive = True
    add_center_xy = True
    use_stacked_frames = False
    stacked_frames = False
    
    def __init__(self, **kwargs):
        __dict__.update(kwargs)
        
    