import cowsay

cowsay.cheese('Cheese goes well with any wine!')
cowsay.pig('Pinot and Pork are best friends')
cowsay.cow('You cant go wrong with Beef and Cabernet')
cowsay.turkey('Poultry and Rose')

wine_food_logo = ("""
██╗    ██╗██╗███╗   ██╗███████╗       ██╗       ███████╗ ██████╗  ██████╗ ██████╗ 
██║    ██║██║████╗  ██║██╔════╝       ██║       ██╔════╝██╔═══██╗██╔═══██╗██╔══██╗
██║ █╗ ██║██║██╔██╗ ██║█████╗      ████████╗    █████╗  ██║   ██║██║   ██║██║  ██║
██║███╗██║██║██║╚██╗██║██╔══╝      ██╔═██╔═╝    ██╔══╝  ██║   ██║██║   ██║██║  ██║
╚███╔███╔╝██║██║ ╚████║███████╗    ██████║      ██║     ╚██████╔╝╚██████╔╝██████╔╝
 ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝╚══════╝    ╚═════╝      ╚═╝      ╚═════╝  ╚═════╝ ╚═════╝ 
                    WELCOME TO THE WINE AND FOOD PAIRING APP!
""")

wine_and_glass = ("""
                           __
                          [__]
                          |  |
                          |  |
                          |  |
                          |  |
                          |  |
             ,----.      /`-. |
            (      )    /-._|  |
            |`----'|   |        |
            \      /   |`-...   |
             `.  ,'    |'` . |  |
               ||      |`,'- |  |
             ,-||-.    |`-...|  |
            (  ''  )   |        |
             `----'     `-....-'
                THANK YOU!
""")

class Image:
  def __init__(self, cheese):
    self.cheese = cowsay.cheese('Cheese goes well with any wine!')