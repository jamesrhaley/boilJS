class InputMap(object):
    """create a map of answers"""
    def __init__(self):
        self.inputs = {}

    def set_inputs(self, key, value):
        self.inputs[key] = value

    def get_inputs(self, key):
        return self.inputs[key]

    def catch_phrase(self, key, phrase):
        """key_phrase is a dictionary of a variable and a phrase.
        that phrase will be handled by raw input"""
        variable = key
        answers = raw_input(phrase)

        print('len',len(answers))
        self.inputs[variable] = answers
