import pygame as pg
import moderngl as mgl

class GraphicsEngine:
    def __init__(self, win_size = ( 1600, 900 )):
        #init pygame modules
        pg.init()
        # window size
        self.WIN_SIZE = win_size
        #set opengl attributes
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3) 
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        #create opengl context
        pg.display.set_mode(self.WIN_SIZE, flags=pg.OPENGL | pg.DOUBLEBUF)
        #detect and use existing opengl context
        self.ctx = mgl.create_context()
        #create an object to help track time
        self.clock = pg.time.Clock()