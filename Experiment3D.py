#      +--------+     _____                            _    ___ _         _ 
#     /        /|    |   __|___ ___ ___ ___ ___    ___| |  |  _|_|___ ___| |
#    /        / |    |   __|_ -| . | -_|  _| .'|  | .'| |  |  _| |   | .'| |
#   +--------+  |    |_____|___|  _|___|_| |__,|  |__,|_|  |_| |_|_|_|__,|_|                                                     
#   |        |  |              |_|                                          
#   |        |  +   APP i TCC
#   |        | /
#   |        |/
#   +--------+

import turtle#Fase de importación
import math
import time
t2 = turtle.Turtle()#Tortugas y sus diferentes comandos aparte de la pantalla y sus requeridas características
t2.hideturtle()
t3 = turtle.Turtle()
t5 = turtle.Turtle()
fw = t3.forward
ra = t3.right
la = t3.left
t4 = turtle.Turtle()
t4.screen.screensize(800,600)
t4.color("blue")
t4.shape("turtle")
t4.screen.bgcolor("black")



def A(j,k):
    t4.hideturtle()#Letra A con sistema de coordenadas
    t4.penup()
    t4.goto(j,k+40)
    t4.pendown()
    t4.goto(j+10,k+40)
    t4.goto(j+20,k+20)
#     Sección de las patas
    t4.goto(j+20,k-5)
    t4.goto(j+10,k-5)
    t4.goto(j+10,k+10)
    t4.goto(j,k+10)
    t4.penup()
    #Parte del lado izquierdo
    t4.goto(j,k+40)
    t4.pendown()
    t4.goto(j-10,k+40)
    t4.goto(j-20,k+20)
    t4.goto(j-20,k-5)
    t4.goto(j-10,k-5)
    t4.goto(j-10,k+10)
    t4.goto(j,k+10)
    t4.penup()
    #Sección centro
    t4.goto(j,k+30)
    t4.pendown()
    t4.goto(j+10,k+20)
    t4.goto(j-10,k+20)
    t4.goto(j,k+30)
    
def B(j,k):
    t4.hideturtle()#Letra B con sistema de coordenadas
    t4.penup()
    t4.goto(j-10,k-5)
    t4.pendown()
    t4.goto(j+20,k-5)#exterior
    t4.goto(j+20,k+20)
    t4.goto(j+20,k+20)
    t4.goto(j+10,k+25)
    t4.goto(j+20,k+30)
    t4.goto(j+20,k+40)
    t4.goto(j-10,k+40)
    t4.goto(j-10,k-5)
    #interior
    t4.penup()#osa menor
    t4.goto(j,k+35)
    t4.pendown()
    t4.goto(j,k+25)
    t4.goto(j+10,k+35)
    t4.goto(j,k+35)
   
    t4.penup()#Osa mayor
    t4.goto(j,k+20)
    t4.pendown()
    t4.goto(j,k+5)
    t4.goto(j+15,k+17.5)
    t4.goto(j,k+20)
def U(j,k):
    t4.penup()
    t4.goto(j,k-5)
    t4.pendown()
    t4.goto(j,k+40)
    t4.goto(j-10,k+40)
    t4.goto(j-10,k+15)
    t4.goto(j-20,k+15)
    t4.goto(j-20,k+40)
    t4.goto(j-30,k+40)
    t4.goto(j-30,k-5)
    t4.goto(j,k-5)

def Y(j,k):
    t4.hideturtle()
    t4.penup()
    t4.goto(j+5,k-5)
    t4.pendown()
    t4.goto(j+5,k+15)
    t4.goto(j+20,k+40)
    t4.goto(j+10,k+40)
    t4.goto(j-5,k+20)
    t4.goto(j-20,k+40)
    t4.goto(j-30,k+40)
    t4.goto(j-15,k+15)
    t4.goto(j-15,k-5)
    t4.goto(j,k-5)
    t4.goto(j+5,k-5)
    
def T(j,k):
    t4.hideturtle()
    t4.penup()
    t4.goto(j,k)
    t4.pendown()
    t4.goto(j+5,k-5)
    t4.goto(j+5,k+30)
    t4.goto(j+15,k+30)
    t4.goto(j+15,k+40)
    t4.goto(j-5,k+40)
    t4.goto(j,k+40)
    t4.goto(j-15,k+40)
    t4.goto(j-15,k+30)
    t4.goto(j-5,k+30)
    t4.goto(j-5,k-5)
    t4.goto(j+5,k-5)
    
def Sobre(h,b,j,k):#Función sobre
    t4.penup()
    goto = t4.goto
    goto(j,k)
    goto(j,k-(h/2))
    t4.pendown()
    goto(j-(b/2),k-(h/2))#Coordenadas para el sobre
    goto(j-(b/2),k+(h/2))
    goto(j,k-(h/2))
    goto(j+(b/2),k-(h/2))
    goto(j+(b/2),k+(h/2))
    goto(j,k-(h/2))
    goto(j+(b/2),k+(h/2))
    goto(j-(b/2),k+(h/2))
    t4.penup()
color = ["cyan","green","red","yellow","purple","blue","orange","dark green","pink"]#Lista con los colores para los diferenters fors y decoraciones
def Confetti (DistanciaCentro,AlturaCentro,color):
    t3.penup()#Definición de todo lo necesario para luego
    t3.speed(0)
    j = DistanciaCentro
    k = AlturaCentro
    t3.goto(j,k)
    t3.color(color)
    for i in range (4):#Loop para hacer la espira mediante coordenadas
        t3.pendown()
        t3.goto(j+10,k-20-i*10)
        t3.goto(j-10,k-30-i*10)
        t3.goto(j+10,k-40-i*10)
        ra(.24)
def Glovo(x,y):
    t5.penup()#Lo hago prácticamente desaparecer
    t5.hideturtle
    goto = t5.goto
    goto(x-15,y)#Glovo parte superior
    t5.pendown()
    goto(x,y+25)
    goto(x+15,y)
    goto(x,y-30)
    goto(x-15,y)
    #Glovo parte inferior/lanita
    goto(x,y-30)
    goto(x+1,y-50)
    goto(x-1,y-60)
    goto(x+1,y-70)
    goto(x-1,y-80)
    t5.penup()
def Tarta(x,y):
    goto = t3.goto
    t3.penup()
    def sqr (h,b,j,k):#Función local de cuadrado
        goto(j+(h/2),k+(b/2))#DerArb
        t3.pendown()
        goto(j-(h/2),k+(b/2))#IzqArb
        goto(j-(h/2),k-(b/2))#IzqAbj
        goto(j+(h/2),k-(b/2))#DerAbj
        goto(j+(h/2),k+(b/2))#DerArb
        t3.penup()
    def trl (h,b,j,k):#Función local de triangulp
        goto(j-(h/2),k+(b/2))#IzqArb
        t3.pendown()
        goto(j+(h/2),k+(b/2))#DerArb
        goto(j,k-(b/2))#CentAbj
        goto(j-(h/2),k+(b/2))#IzqArb
        t3.penup()
       
    sqr(50,25,x,y-29)#base
    sqr(35,30,x,y)#intermedio
    sqr(15,25,x,y+30)#alto
    sqr(3,9,x-5,y+49)#vela
    sqr(3,9,x+5,y+49)#vela
    trl(5,10,x-5,y+60)#llama
    trl(5,10,x+5,y+60)#llama
    t3.hideturtle()
def rotate_y(point, angle):#Función mediante trigonometria para la rotación del cubo/regalo
    x, y, z = point
    rad = math.radians(angle)
    x2 = x * math.cos(rad) + z * math.sin(rad)
    z2 = -x * math.sin(rad) + z * math.cos(rad)
    return x2, y, z2

def project_point(x, y, z):#matematica para representar los puntos que sirven como origen de los vectores representados
    factor = 500 / (500 + z)
    x2 = x * factor
    y2 = y * factor
    return x2, y2

def draw_frame(t, points, edges):#Funcion para el dibujo del cubo/regalo
    t.clear()
    projected = [project_point(*p) for p in points]
    for start, end in edges:
        t.penup()
        t.goto(projected[start])
        t.pendown()
        t.goto(projected[end])
    turtle.update()

def main():#Lo que acontece en la escena principal
    A(-150,35)
    U(-95,35)
    B(-80,35)
    A(-35,35)
    Y(35,35)
    T(85,35)
    for i in range (8):#Loop para la decoración repetida
        for x in range (2):
            Confetti(-240+i*70*x,300,color[i])#Usando los dos loops puedo usar la función que cree varias veces en diferentes posiciones y multiplicandolo obtengo un "offset"
            Confetti(-250+i*60*x,390,color[i])#Después la linea  de color es para que la lista sea recorrida  y en los dos siguientes cambia un poco al empezar el color
            Confetti(-230+i*45*2*x,350,color[i+1])
            Confetti(-250+3*55*2*x,400,color[i+1])
        Sobre(25,50,-250+i*100,-100)#Sobre con color alternante (siguiente linea de codigo) que cambia de posición según el loop
        t4.color(color[i])
    for i in range(8):
        t5.color(color[i])
        Glovo(-80+i*40,-200)
    Tarta(0,-120)#La tarta
        
    #****************************************************************
#     SEPARACIÓN CODIGO 3D Y 2D
    #****************************************************************
    screen = turtle.Screen()#Características de la tortuga del regalo
    screen.tracer(0)
   
    screen.bgcolor("black")
    t = turtle.Turtle()
    t.speed(0)
    t.color("green")#Cubo verde
    points = [#Definición de todos los puntos del cubo
        #(x , y , z )
        (-25, -25, -25),#0 Izquierda Abajo Detrás
        (25, -25, -25),#1 Derecha Abajo Detrás
        (25, 25, -25),#2 Derecha Arriba Detrás
        (-25, 25, -25),#3 Izquierda Arriba Detrás
        (-25, -25, 25),#4 Izquierda Abajo Delante
        (25, -25, 25),#5 Derecha Abajo Delante
        (25, 25, 25),#6 Derecha Abajo Delante
        (-25, 25, 25),#7 Derecha Arriba Delante
       
        #BarraDer
        (25 , -25 , 0),#8
        (25, 25, 0),#9
       
        #BarraIzq
        (-25 , -25 , 0),#10
        (-25, 25, 0),#11
       
       #Tapa: (12-15 abajo, 16-19 arriba)
        (-25,75,-25),#12
        (25,75,-25),
        (-25,75,25),
        (25,75,25),#15
       
        (-25,85,-25),#16
        (25,85,-25),
        (-25,85,25),
        (25,85,25),#19
       
        #Lazo centro
        (0,85,0),#20
       
        #Lazo Der
        (35,105,0),#21
        (10,105,0),#22
         #Lazo Izq
        (-35,105,0),#23
        (-10,105,0),#24

        (25 , 75 , 0),#25
        (25, 85, 0),#26
       
        #BarraIzq
        (-25 , 75 , 0),#27
        (-25, 85, 0),#28
]

    edges = [#Si bien pone edges, no son bordes si no más bien vectores
        (0,1), (1,2), (2,3), (3,0),
        (4,5), (5,6), (6,7), (7,4),
        (0,4), (1,5), (2,6), (3,7),
        (0,8), (1,8), (9,8), (10,11),
        (12,13),(14,15),(12,14),(13,15),
        (16,17),(18,19),(16,18),(17,19),
        (12,16),(13,17),(14,18),(15,19),
       
        (25,26), (27,28), (20,28), (20,26),
       
        (20,21),(20,22),(21,22),
       
        (20,23),(20,24),(23,24),
     
    ]
    angle = 0
    while True:#Para que siga girando

        rotated_points = [rotate_y(p, angle) for p in points]
        draw_frame(t, rotated_points, edges)
        angle += 2
        time.sleep(0.03)
        screen.screensize(800,600)
       

if __name__ == "__main__":
   

    main()




