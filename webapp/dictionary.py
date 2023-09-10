import justpy as jp
import definition
from webapp import layout
from webapp import page


class Dictionary(page.Page):
    path = "/dictionary"

    @classmethod #decorator
    #request handler
    def serve(cls, req):
        wp = jp.QuasarPage(tailwind=True)

        lay = layout.DefaultLayout(a=wp)

        container = jp.QPageContainer(a=lay)

        div = jp.Div(a=container, classes="bg-gray-100 h-screen")
        jp.Div(a=div, text="Instant English Dictionary", classes="text-4xl m-2")
        jp.Div(a=div, text="Get the definition of any english word instantly", classes="text-lg")

        input_div = jp.Div(a=div, classes="grid grid-cols-2")
        
        
        output_div = jp.Div(a=div, classes="bg-white m-2 p-2 text-lg border-2 h-40")

        input_box = jp.Input(a=input_div, placeholder="Type a word here...", outputdiv=output_div, 
                 classes="m-2 bg-gray-100 border-2 border-gray-200 rounded w-64 focus:bg-white focus:outline-none focus:border-purple-500 "
                         "py-2 px-4")
        
        # using the typing event without a button
        input_box.on('input', cls.get_definition)

        # using the button and click event
        # created attributes - outputdiv and inputbox for the button widget
        # jp.Button(a=input_div, text="Get Definition", classes="border-2 text-gray-500", click=cls.get_definition, outputdiv=output_div, inputbox=input_box)

        #print(cls,req)
        return wp
    
    @staticmethod
    def get_definition(widget, msg):
        # using the button
        # defined = definition.Definition(widget.inputbox.value).get()
        defined = definition.Definition(widget.value).get()
        widget.outputdiv.text = " ".join(defined) # convert the tuple into string