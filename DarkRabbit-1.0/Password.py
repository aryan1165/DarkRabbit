import pygame
import random
import os
import sys
import string

used_dots = []

outlines = []

WIDTH, HEIGHT = 245, 245

WIN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Pattern")

WHITE = (255,255,255)

FPS = 60

DOT_HEIGHT, DOT_WIDTH = 35, 35

DOT_IMAGE = pygame.image.load(r"dot.png")
DOT = pygame.transform.scale(DOT_IMAGE, (DOT_WIDTH, DOT_HEIGHT))

DOT_OUTLINE_IMAGE = pygame.image.load(r"dot outline.png")
DOT_OUTLINE = pygame.transform.scale(DOT_OUTLINE_IMAGE, (DOT_WIDTH, DOT_HEIGHT))

def findfile(name, path):
        for dirpath, dirname, filename in os.walk(path):
            if name in filename:
                return os.path.join(dirpath,name)

def draw_window():
    WIN.fill(WHITE)
   
    WIN.blit(DOT, (000,000))
    WIN.blit(DOT, (105,000))
    WIN.blit(DOT, (210,000))
   
    WIN.blit(DOT, (000,105))
    WIN.blit(DOT, (105,105))
    WIN.blit(DOT, (210,105))
   
    WIN.blit(DOT, (000,210))
    WIN.blit(DOT, (105,210))
    WIN.blit(DOT, (210,210))
   
   
   

def main():
     
    clock = pygame.time.Clock()
   
    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
               
        draw_window()
       
        x, y = pygame.mouse.get_pos()
       
        mouse_buttons = pygame.mouse.get_pressed()
       

        if mouse_buttons[0] == True:
            if 0 < x < 35 and 0 < y < 35:
                if 1 not in used_dots:
                    outlines.append(1)
                    used_dots.append(1)
                   
               
            if 105 < x < 140 and 0 < y < 35:
                if 2 not in used_dots:
                    outlines.append(2)
                    used_dots.append(2)
               
            if 210 < x < 245 and 0 < y < 35:
                if 3 not in used_dots:
                    outlines.append(3)
                    used_dots.append(3)
               
            if 0 < x < 35 and 105 < y < 140:
                if 4 not in used_dots:
                    outlines.append(4)
                    used_dots.append(4)
               
            if 105 < x < 140 and 105 < y < 140:
                if 5 not in used_dots:
                    outlines.append(5)
                    used_dots.append(5)
               
            if 210 < x < 245 and 105 < y < 140:
                if 6 not in used_dots:
                    outlines.append(6)
                    used_dots.append(6)
               
            if 0 < x < 35 and 210 < y < 245:
                if 7 not in used_dots:
                    outlines.append(7)
                    used_dots.append(7)
               
            if 105 < x < 140 and 210 < y < 245:
                if 8 not in used_dots:
                    outlines.append(8)
                    used_dots.append(8)
                   
            if 210 < x < 245 and 210 < y < 245:
                if 9 not in used_dots:
                    outlines.append(9)
                    used_dots.append(9)
       
        if 1 in outlines:
            WIN.blit(DOT_OUTLINE, (000,000))
       
        if 2 in outlines:
            WIN.blit(DOT_OUTLINE, (105,000))
       
       
        if 3 in outlines:
            WIN.blit(DOT_OUTLINE, (210,000))
       
        if 4 in outlines:
            WIN.blit(DOT_OUTLINE, (000,105))
       
        if 5 in outlines:
            WIN.blit(DOT_OUTLINE, (105,105))
       
        if 6 in outlines:
            WIN.blit(DOT_OUTLINE, (210,105))
       
        if 7 in outlines:
            WIN.blit(DOT_OUTLINE, (000,210))
       
        if 8 in outlines:
            WIN.blit(DOT_OUTLINE, (105,210))
       
        if 9 in outlines:
            WIN.blit(DOT_OUTLINE, (210,210))
       
        pygame.display.update()
    pygame.quit()

    # print(used_dots)
    #Let points be 1,2,3,4,5,6,7,8,9
    i=0
    #Enter 0 to quit
    str_1 = ""
    while(i<len(used_dots)):
        # point = int(input("Enter Point: "))
        
        if used_dots[i] ==1:
            str_1 = str_1 + chr(random.randint(33,132)) +chr(random.randint(33,132)) + chr(random.randint(33,132))
            i=i+1
        elif used_dots[i] ==2:  
            str_1 = str_1 + chr(random.randint(33,132)) +chr(random.randint(33,132)) + chr(random.randint(33,132))
            i=i+1
        elif used_dots[i] ==3:  
            str_1 = str_1 + chr(random.randint(33,132)) +chr(random.randint(33,132)) + chr(random.randint(33,132))
            i=i+1
        elif used_dots[i] ==4:  
            str_1 = str_1 + chr(random.randint(33,132)) +chr(random.randint(33,132)) + chr(random.randint(33,132))
            i=i+1
        elif used_dots[i] ==5:  
            str_1 = str_1 + chr(random.randint(33,132)) +chr(random.randint(33,132)) + chr(random.randint(33,132))
            i=i+1
        elif used_dots[i] ==6:  
            str_1 = str_1 + chr(random.randint(33,132)) +chr(random.randint(33,132)) + chr(random.randint(33,132))
            i=i+1
        elif used_dots[i] ==7:  
            str_1 = str_1 + chr(random.randint(33,132)) +chr(random.randint(33,132)) + chr(random.randint(33,132))
            i=i+1
        elif used_dots[i] ==8:  
            str_1 = str_1 + chr(random.randint(33,132)) +chr(random.randint(33,132)) + chr(random.randint(33,132))
            i=i+1
        elif used_dots[i] ==9:  
            str_1 = str_1 + chr(random.randint(33,132)) +chr(random.randint(33,132)) + chr(random.randint(33,132))
            i=i+1

        # print(used_dots)
        # print(str_1)

    with open("text.txt","w") as file:
        file.write(str_1)
    
    # sys.path.insert(0,findfile('AffineEncryption.py','/users'))
    # sys.path.insert(0,findfile("HillEncryption.py",'/users'))
    # sys.path.insert(0,findfile("Permutationencryption.py",'/users'))
    # sys.path.insert(0,findfile("ShiftEncryption.py",'/users'))
    # sys.path.insert(0,findfile("VignereEncryption.py",'/users'))
    # sys.path.insert(0,findfile("SubstitutionEncryption.py",'/users'))

    from AffineCipher import AffineEncryption
    from ShiftCipher import ShiftEncryption
    from SubstitutionCipher import SubstitutionEncryption
    from VignereCipher import VignereEncryption
    from HillCipher import HillEncryption
    from PermutationCipher import Permutationencryption


    with open('text.txt','r') as file:
        message = file.read()
        
    randomNumList =[]
    for i in range(10000):
        randnum = random.randint(1,6)
        if randnum not in randomNumList:
            randomNumList.append(randnum)
            if len(randomNumList)==6:
                break
    
    # print(randomNumList)

    with open("Keys/randomList.txt","w")as file:
        for i in range(len(randomNumList)):
            file.write((f"{str(randomNumList[i])}\n"))
    file.close()    

    def encryption(argument):
        match argument:
            case 1:
                return AffineEncryption.encryption(message)
            case 2:
                return HillEncryption.encryption(message)
            case 3:
                return ShiftEncryption.encryption(message)
            case 4:
                return SubstitutionEncryption.encryption(message)
            case 5:
                return VignereEncryption.encryption(message) 
            case 6:
                return Permutationencryption.encryption(message) 


    message = encryption(randomNumList[0])  #message ko overwrite kar diya
    # print(message)
    message=encryption(randomNumList[1])
    # print(message)
    message=encryption(randomNumList[2])
    # print(message)
    message=encryption(randomNumList[3])
    # print(message)
    message=encryption(randomNumList[4])
    # print(message)
    message=encryption(randomNumList[5])

    with open('Encrypted.txt',"w") as file:
        file.write(message)

    # import random


    with open("Encrypted.txt", "r") as file:
        message = file.read()
    length = len(message)

    x = 10
    diff_length = 0


    if length > 10:
        diff_length = length-10


    messageList = []


    for i in range(length):
        messageList.append(message[i])

    # print(messageList)
    index_list = []
    for i in range(diff_length):
        index = random.randint(0, len(messageList)-1)
        del messageList[index]
        
    # print(messageList)

    new_password = ""

    for i in messageList:
        new_password += str(i)+ "" 

    # print(new_password)


    new_password=new_password+random.choice(string.ascii_lowercase)+random.choice(string.ascii_uppercase)+random.choice(string.punctuation)+random.choice(string.ascii_letters)

    from PermutationCipher import Permutationencryption

    # print(new_password)
    Final_password= Permutationencryption.encryption(new_password)
    print(Final_password)

    with open("FINALLY.bin","wb") as file:
        file.write(str.encode((Final_password)))



if __name__ == "__main__":
    main()
   
   


