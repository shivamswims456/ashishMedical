import tornado.ioloop, tornado.web, os, json, time
from uuid import uuid4



class MainHandler( tornado.web.RequestHandler ):

    def get(self):

        self.render("index.html")

class AboutUs( tornado.web.RequestHandler ):

    def get(self):

        self.render("about.html")



class ContactUs( tornado.web.RequestHandler ):

    def get(self):

        self.render("contact.html")



class scanningDevices( tornado.web.RequestHandler ):

    def get(self):

        self.render("scanningDevices.html")


class anasthesia( tornado.web.RequestHandler ):

    def get(self):

        self.render("anasthesia.html")




class dental( tornado.web.RequestHandler ):

    def get(self):

        self.render("dental.html")


class ultra( tornado.web.RequestHandler ):

    def get(self):

        self.render("ultra.html")


class hospitalBeds( tornado.web.RequestHandler ):

    def get(self):

        self.render("hospitalBeds.html")


class OTLights( tornado.web.RequestHandler ):

    def get(self):

        self.render("OTLights.html")

class equipments( tornado.web.RequestHandler ):

    def get(self):

        self.render("equipments.html")

                                 

def make_app():

    settings = {"template_path": os.path.join(os.getcwd(), "templates"), "debug":True, "autoreload":True, "cookie_secret":"__TODO:_GENERATE_YOUR_OWN_RANDOM_VALUE_HERE__"}

    return tornado.web.Application([

                  

            
        (r"/", MainHandler),
        (r"/scanningDevices", scanningDevices),
        (r"/anesthesiaWorkstations", anasthesia),
        (r"/dentalEquipments", dental),
        (r"/ultra", ultra),
        (r"/hospitalBeds", hospitalBeds),
        (r"/OTLights", OTLights),
        (r"/equipments", equipments),
        (r"/about", AboutUs),
        (r"/contact", ContactUs),
        ("/assets/(.*)", tornado.web.StaticFileHandler, {"path":os.path.join(os.getcwd(), "assets")}),
        
        
    ], **settings)

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
