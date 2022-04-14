"""
Comando concreto que cuida de ligar/desligar a luz
"""

from command.smart_house_command_interface import SmartHouseCommandInterface
from command.smart_house_light import SmartHouseLight


class LightPowerCommand(SmartHouseCommandInterface):

    def __init__(self, light: SmartHouseLight):
        self.light = light

    def execute(self) -> None:
        self.light.on()

    def undo(self) -> None:
        self.light.off()

