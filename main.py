#Importar módulo OS que roda o script no Terminal
import os
import PySimpleGUIWeb as sg

#Interface em PySimpleGUI para configurar a câmera
layout = [
  [sg.Text('Opacidade(255)'),sg.Slider(range=(0,255), default_value=255, size=(10,10), orientation='horizontal',font=('Helvetica', 12)), sg.Text('Nitidez(0)'),sg.Slider(range=(-100,100), default_value=0, size=(10,10), orientation='horizontal', font=('Helvetica', 12))],

  [sg.Text('Contraste(0)'),sg.Slider(range=(-100,100), default_value=0, size=(10,10), orientation='horizontal',font=('Helvetica', 12)), sg.Text('Brilho(50)'),sg.Slider(range=(0,100), default_value=50, size=(10,10), orientation='horizontal', font=('Helvetica', 12))],

  [sg.Text('Saturação(0)'),sg.Slider(range=(-100,100), default_value=0, size=(10,10), orientation='horizontal',font=('Helvetica', 12)), sg.Text('ISO(800)'),sg.Slider(range=(100,800), default_value=800, size=(10,10), orientation='horizontal', font=('Helvetica', 12))],

  [sg.Text('Exposição(0)'),sg.Slider(range=(-10,10), default_value=0, size=(10,10), orientation='horizontal',font=('Helvetica', 12)), sg.Text('Abertura(1/125)'),sg.Slider(range=(0,6000000), default_value=1000, size=(10,10), orientation='horizontal', font=('Helvetica', 12))],

  [sg.Checkbox('Inverter Vertical', default=True)],[sg.Checkbox('Inverter Horizontal', default=True)],
  
  [sg.Submit('Capturar'), sg.Cancel('Cancelar')]
]

window = sg.Window('PiPy Camera Manager').Layout(layout)
button, values = window.Read()

#Declarar variáveis de configuração da câmera
opacidade = values[0]
nitidez = values[1]
contraste = values[2]
brilho = values[3]
saturacao = values[4]
iso = values[5]
exposicao = values[6]
abertura = values[7]
inverter_v = values[8]
inverter_h = values[9]

#Condicionais para traduzir o botão de espelhamento de imagem
if inverter_v == True:
  inverter_v = '-vf'
else:
  inverter_v = ''

if inverter_h == True:
  inverter_h = '-hf'
else:
  inverter_h = ''

#Inserindo data à variável utilizada no nome da foto
os.system('DATE=$(date +"%Y-%m-%d_%H%M")')

#Montando o script para tirar foto de acordo com os parâmetros informados na interface
os.system("raspistill {} {} -op {} -sh {} -co {} -br {} -sa {} -ISO {} -ev {} -ss {} -o /home/pi/camera/$DATE.jpg" .format(inverter_v,inverter_h,opacidade,nitidez,contraste,brilho,saturacao,iso,exposicao,abertura))
