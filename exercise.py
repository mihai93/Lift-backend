class Exercise:
    id = 0 # global exercise id

    # bare min init b/c user may add new exercises
    def __init__(self, name):
        self.name = name
        Exercise.id += 1

    # def set_rating(self, rating)
    #     self.rating = rating

    def set_type(self, type):
        self.type = type

    def set_url(self,url):
        self.url = url

    def set_muscle(self, muscle):
        self.muscle = muscle

    def set_other_muscles(self, other_muscles):
        self.other_muscles = other_muscles

    def set_equipment(self, equipment):
        self.equipment = equipment

    def set_mechanics(self, mechanics):
        self.mechanics = mechanics

    def set_rating(self, rating):
        self.rating = rating

    def set_level(self, level):
        self.level = level

    def set_sport(self, sport):
        self.sport = sport

    def set_force(self, force):
        self.force = force

    def set_guide_items(self, guide_items):
        self.guide_items = guide_items

    def set_note_title(self, note_title):
        self.note_title = note_title

    def set_notes(self, notes):
        self.notes = notes
