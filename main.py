import numpy as np
import pandas as pd
import pygame

pygame.init()
WIDTH, HEIGHT = 450, 650
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sensor Fusion Iphone 11")
clock = pygame.time.Clock()
FPS = 100

filename_1 = "accel_8.csv"
#filename_2 = "gyro_2.csv"

df_1 = pd.read_csv(filename_1, delimiter=";")
#df_2 = pd.read_csv(filename_2, delimiter=";")

data_1 = df_1[['AccelerationX', 'AccelerationY', 'AccelerationZ']].values #Reads the Acceleration values
#data_2 = df_2[['GyroscopeX', 'GyroscopeY', 'GyroscopeZ']].values #Reads the Gysocopic values


def render_path(phone, points):
    points.append([phone.x+25,phone.y+50])
    for point in points:
        rect = pygame.Rect(point[0]-1,point[1]-1,2,2)
        
        pygame.draw.rect(screen, (194,24,7), rect)
    return points

def main():
    running = True
    points = []
    index = 1
    x,y,z=0,0,0 #Initialize starting values of vector
    x_off,y_off,z_off = (-data_1[0][0], -data_1[0][1], -data_1[0][2]) #Values of offsets
    mult = 500
    phone = pygame.Rect((mult*x)-25+(WIDTH//2),(mult*y)-50+(HEIGHT//2),50,100)

    while running:
        if index+5 > len(data_1):
            pygame.image.save(screen, "final.png")
            running = False

        screen.fill((0,0,0))
        ac = data_1[index]
        x,y,z = x+ac[0]+x_off,y+ac[1]+y_off,z+ac[2]+z_off
        phone = pygame.Rect((mult*x)-25+(WIDTH//2),(mult*y)-50+(HEIGHT//2),50,100)
        points = render_path(phone,points)
        #pygame.draw.rect(screen, (255,255,255), phone)

        index += 1

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
	main()
	pygame.quit()