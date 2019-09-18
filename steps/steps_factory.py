from .size import Size
from .position import Position
from .price import Price
from .temperature import Temperature
from .suggest import Suggest
from .hardness import Hardness

class StepsFactory:
    def getStep(self, classname) :
        return {
            'size': Size(),
            'hardness': Hardness(),
            'position': Position(),
            'price': Price(),
            'temperature': Temperature(),
            'suggest': Suggest()
        }[classname]
    