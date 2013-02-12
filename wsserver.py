from tornado import websocket
from tornado import httpclient
import tornado.ioloop
import tornado.web
import pygame
import threading

value = 0.0

pygame.init()
myfont = pygame.font.SysFont("monospace", 100)


class EchoWebSocket(websocket.WebSocketHandler):
    def open(self):
        print "Websocket Opened"

    def on_message(self, message):
        global value

        print message
        scrollAmount = int(message)
        
        value += scrollAmount/10.0

        text = myfont.render("{0:g}".format(value), 1, (255,255,255))
        screen.fill((0,0,0))        
        screen.blit(text,(320 - text.get_width() // 2, 240 - text.get_height() // 2))
        pygame.display.flip()

        #self.write_message(u"You said: %s" % message)

    def on_close(self):
        print "Websocket closed"

static_path = "static/"
application = tornado.web.Application([(r"/", EchoWebSocket),(r'/jogdial/(.*)', tornado.web.StaticFileHandler, {'path': static_path})])

if __name__ == "__main__":
    screen = pygame.display.set_mode((640, 480))

    text = myfont.render("{:.2}".format(value), 1, (255,255,255))
    screen.blit(text,(320 - text.get_width() // 2, 240 - text.get_height() // 2))
    pygame.display.flip()
    
    application.listen(9000)
    tornado.ioloop.IOLoop.instance().start()
    

        



