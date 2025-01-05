from typing import Dict

from .base_states import State, StateCollection

class WindowState(State):
    def __init__(self, name, permissions:Dict[str, bool]):
        super().__init__(name)
        self.__permissions=permissions
    
    @property
    def permissions(self):
        return self.__permissions.copy()
        


class WindowStateCollection(StateCollection):
    START=WindowState('START', permissions={})
