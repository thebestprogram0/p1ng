import json
import re
import pygame
import webbrowser
import pygame.font

print("Welcome to P1nG 1.3v")
print("Xander, all rights reserved")
print("-------------------------------")

variables = {}

while True:
    command = input("</> ")
    if "=" in command:
        variable, value = command.split("=")
        if value.startswith("ask{") and value.endswith("}"):
            query = value[4:-1]
            variables[variable] = input(query)
            print('')
        elif value.startswith("math{") and value.endswith("}"):
            math_expression = value[5:-1]
            try:
                result = eval(math_expression)
                variables[variable] = result
                print('')
            except:
                print("Invalid mathematical expression")
                print('')
        elif value.startswith("read{") and value.endswith("}"):
            file_path = variable
            try:
                with open(file_path, 'r') as file:
                    data = json.load(file)
                    variables[variable] = data
                    print('DATA:')
                    print('')
                    print(data)
                    print('')
            except:
                print(f"Failed to read {file_path}.")
                print('')
        elif value.startswith("write{") and value.endswith("}"):
            data = value[6:-1]
            file_path = variable
            try:
                with open(file_path, 'w') as file:
                    json.dump(data, file)
                    print(f"{file_path} written successfully.")
                    print('')
            except:
                print(f"Failed to write to {file_path}.")
                print('')
        else:
            print("Invalid Syntax")
            print('')

    elif command.startswith("win{") and command.endswith("}"):
        try:
            pygame.init()
            size = command[4:-1]
            width, height = size.split("-")
            width = int(width)
            height = int(height)
            window = pygame.display.set_mode((width, height))
            running = True
            print(f"Pygame window of size {width}x{height} created.")
            print('')
            while running:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        running = False
        except:
            print("Failed to create Pygame window.")
            print('')
    elif command.startswith("int{") and command.endswith("}"):
        url = command[4:-1]
        webbrowser.open(url)
        print(f"Opening {url} in your default browser.")
        print('')
    elif command.startswith("wint{") and command.endswith("}"):
        text = command[5:-1]
        try:
            font = pygame.font.SysFont("arial", 30)
            text_surface = font.render(text, True, (255, 255, 255))
            window.blit(text_surface, (10, 10))
            pygame.display.update()
            print(f"The Text: '{text}' was added to the window.")
            print('')
        except:
            print("Failed to add text to window.")
            print('')
    elif command.startswith("paste{") and command.endswith("}"):
        paste_text = command[6:-1]
        for key, value in variables.items():
            paste_text = paste_text.replace("{" + key + "}", str(value))
        print(paste_text)
        print('')
    elif command == "end{!}":
        exit()
    else:
        print("Invalid Syntax")
        print('')
