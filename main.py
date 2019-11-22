#Importar módulo OS que roda o script no Terminal
import os
import PySimpleGUIWeb as sg

#Declarar variáveis de configuração da câmera
inverter_v = 0
inverter_h = 0
opacidade = '255'
nitidez = '0'
contraste = '0'
brilho = '50'
saturacao = '0'
iso = '800'
exposicao = '0'
abertura = '1000'

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
