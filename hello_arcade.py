import arcade

SCREEN_WIDTH = 600
SCREEN_HIGHT = 800
SCREEN_TITLE = "Hola arcade"

def primera_forma():
    arcade.draw_rectangle_filled(180,400,80,50,arcade.color.YELLOW_ORANGE)
    arcade.draw_rectangle_filled(360,400,280,50,arcade.color.WHITE_SMOKE)

if __name__ == "__main__":
    #Crear ventana
    arcade.open_window(SCREEN_WIDTH,SCREEN_HIGHT, SCREEN_TITLE)
    #Cambiar color de fondo
    arcade.set_background_color(arcade.color.GREEN)

    #Iniciar render
    arcade.start_render()
    #Funciones para dibujar
    primera_forma()
    #finalizar render
    arcade.finish_render()

    #correr el programa
    arcade.run()
