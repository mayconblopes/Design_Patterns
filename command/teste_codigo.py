"""
Simula código cliente.
"""

from command.light_intensity_command import LightIntensityCommand
from command.light_power_command import LightPowerCommand
from command.smart_house_app import SmartHouseApp
from command.smart_house_light import SmartHouseLight

# receiver
bedroom_light = SmartHouseLight('Luz Quarto')
bathroom_light = SmartHouseLight('Luz Banheiro')

# command
bedroom_light_power_command = LightPowerCommand(bedroom_light)
bathroom_light_power_command = LightPowerCommand(bathroom_light)
bedroom_intensity_command = LightIntensityCommand(bedroom_light)

print("Executando comando sem invoker")
bedroom_light_power_command.execute()
bedroom_light_power_command.undo()
bathroom_light_power_command.execute()
bathroom_light_power_command.undo()

# nesses exemplos acima, o cliente está chamando os comandos diretamente,
# sem passar pelo invoke, mas pode ser assim:

# Controle / Invoker
invoker = SmartHouseApp()
invoker.add_command('botao1', bedroom_light_power_command)
invoker.add_command('botao2', bathroom_light_power_command)
invoker.add_command('botao3', bedroom_intensity_command)

print("\nExecutando comando com invoker")
invoker.execute_command('botao1')
invoker.undo_command('botao1')
invoker.execute_command('botao2')
invoker.undo_command('botao2')

invoker.execute_command('botao3')
invoker.execute_command('botao3')
invoker.execute_command('botao3')

for i in range(60):
    invoker.execute_command('botao3')

invoker.undo_command('botao3')
invoker.undo_command('botao3')

for i in range(160):
    invoker.undo_command('botao3')

