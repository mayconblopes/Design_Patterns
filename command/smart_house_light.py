"""
SmartHouseLight é o receiver, isto é, o objeto que vai receber o comando.
"""


class SmartHouseLight:

    def __init__(self, name: str):
        self._name = name
        self._is_on = True
        self._intensity = 50


    """    
    @property
    def is_on(self):
        return self._is_on

    @property
    def intensity(self):
        return self._intensity
    """

    def get_power_status(self) -> str:
        return 'ON' if self._is_on else 'OFF'

    def on(self) -> bool:
        self._is_on = True
        print(f'{self._name} agora está {self.get_power_status()}')
        return self._is_on

    def off(self) -> bool:
        self._is_on = False
        print(f'{self._name} agora está {self.get_power_status()}')
        return self._is_on

    def increase_intensity(self) -> int:
        self._intensity += 1 if self._intensity < 100 else 0
        print(f'Intensidade da {self._name} é {self._intensity}')
        return self._intensity

    def decrease_intensity(self) -> int:
        self._intensity -= 1 if self._intensity > 0 else 0
        print(f'Intensidade da {self._name} é {self._intensity}')
        return self._intensity

