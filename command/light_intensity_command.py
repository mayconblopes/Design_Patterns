"""
Comando concreto que lida com a intensidade da luz.
"""

from command.smart_house_command_interface import SmartHouseCommandInterface
from command.smart_house_light import SmartHouseLight


class LightIntensityCommand(SmartHouseCommandInterface):

    def __init__(self, light: SmartHouseLight):
        self.light = light

    def execute(self) -> None:
        self.light.increase_intensity()

    def undo(self) -> None:
        self.light.decrease_intensity()

