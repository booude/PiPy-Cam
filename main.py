#Importar módulo OS que roda o script no Terminal
import os
import PySimpleGUIWeb as sg

#Declarar variável do script que será montado no código
pipycamera = 'raspistill -vf -hf -o /home/pi/camera/$DATE.jpg'

#Inserindo valor de data ao nome da foto
os.system('DATE=$(date +"%Y-%m-%d_%H%M")')

#Utilizando o método system
os.system(pipycamera)

#Interface em PySimpleGUI para configurar a câmera
window = sg.Window('hello world').Layout([
  [sg.Text('hello world')],
  [sg.InputText('enter name')],
  [sg.Submit(), sg.Cancel()]
])

[button, [name]] = window.Read()

if button == 'Submit':
  print('Hello ' + name)
