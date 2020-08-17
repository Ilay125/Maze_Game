class Console:
    ABC = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ.,><'1234567890-*/+=_)(&#!%^$[]{}`~; "

    def __init__(self, active=True):
        '''
        Initiate the object.
        :param active: bool
        '''
        self.txt = "_"
        self.active = active
        self.visible = True
        self.animation_clock = 0

    def enter(self):
        '''
        Enters the text from the console
        :return: str
        '''
        if self.active:
            if self.txt != "":
                return self.txt

    def reset(self):
        '''
        Resets the console.
        :return: None
        '''
        self.txt = "_"

    def delete(self):
        '''
        Deletes the last char form the text in the console.
        :return: None
        '''
        if self.active:
            self.txt = self.txt[:-1]

    def write(self, char):
        '''
        Writes new char in the console.
        :param char: char
        :return: None
        '''
        if self.active:
            if self.txt == "_":
                self.txt = ""
            if char in self.ABC:
                self.txt += char

    def animation(self):
        '''
        Animate the console when nothing is written in there.
        :return: None
        '''
        if self.active:
            self.animation_clock += 1

            if (self.txt == "_" or self.txt == "") and self.animation_clock % 13 == 0:
                self.visible = not self.visible
                self.Visible()
        else:
            if self.txt == "_" or self.txt == "":
                self.txt = "_"

    def Visible(self):
        '''
        Changes the visibility of an empty console.
        :return: None
        '''

        if self.visible:
            self.txt = "_"
        else:
            self.txt = ""