class Converter:
    def __init__(self,screen):
        self.screen = screen

    def conv_x(self,n):
        return int(n/1920*self.screen.get_width())
    
    def conv_y(self,n):
        return int(n/1080*self.screen.get_height())
