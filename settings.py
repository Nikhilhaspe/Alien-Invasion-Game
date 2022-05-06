class settings():
    def __init__(self):
        self.screen_width = 1360
        self.screen_height = 768
        self.bg_color = (230,230,230)
        self.bullet_color = 30,30,30
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullets_allowed = 5
        self.ship_limit = 3
        self.fleet_drop_speed = 10
        self.speedup_scale = 1.1
        self.score_scale = 1.5
        self.initialize_dynamic_settings()
    def initialize_dynamic_settings(self):
        self.fleet_direction = 1
        self.bullet_speed_factor = 5
        self.alien_speed_factor = 1
        self.speed_factor = 4
        self.alien_points = 50
    def increase_speed(self):
        self.bullet_speed_factor *= self.speedup_scale
        self.alien_speed_factor *= self.speedup_scale
        self.speed_factor *= self.speedup_scale
        self.alien_points = int(self.alien_points * self.score_scale)