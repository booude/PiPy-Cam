#Importar módulo OS que roda o script no Terminal
import os
import PySimpleGUIWeb as sg

#Declarar variáveis de configuração da câmera
inverter_v = 1
inverter_h = 1
opacidade = '255'
nitidez = '0'
contraste = '0'
brilho = '50'
saturacao = '0'
iso = '800'
exposicao = '0'
abertura = '8000000'

#Condicionais para ativar e desativar espelhamento
if inverter_v == 1:
  inverter_v = '-vf'
elif inverter_v == 0:
  inverter_v = ''
else:
  inverter_v = ''

if inverter_h == 1:
  inverter_h = '-hf'
elif inverter_h == 0:
  inverter_h = ''
else:
  inverter_h = ''

#Declarar variável do script que será montado no código
pipycamera = f'raspistill {inverter_v} {inverter_h} -op {opacidade} -sh {nitidez} -co {contraste} -br {brilho} -sa {saturacao} -ISO {iso} -ev {exposicao} -ss {abertura} -o /home/pi/camera/$DATE.jpg'

#Inserindo valor de data ao nome da foto
os.system('DATE=$(date +"%Y-%m-%d_%H%M")')

#Utilizando o método system
"""os.system(pipycamera)"""
print(pipycamera)

#Interface em PySimpleGUI para configurar a câmera
layout = [
  [sg.Text('Opacidade (255)'),sg.InputText('(0-255)')],  [sg.Text('Nitidez (0)'),sg.InputText('(-100-100)')],
  [sg.Text('Contraste (0)'),sg.InputText('(-100-100)')],
  [sg.Text('Brilho (50)'),sg.InputText('(0-100)')],
  [sg.Text('Saturação (0)'),sg.InputText('(-100-100)')],
  [sg.Text('ISO (8)'),sg.InputText('(100-800)')],
  [sg.Text('Exposição (0)'),sg.InputText('(-10-10)')],
  [sg.Text('Abertura (1/125)'),sg.InputText('(~-6000000)')],
  [sg.Submit(), sg.Cancel()]
]

window = sg.Window('PiPy Camera Manager').Layout(layout)
button, values = window.Read()
print(button, values[0], values[1], values[2])
