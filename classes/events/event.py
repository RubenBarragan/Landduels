import pygame
from events.dispatch import EventDispatcher

class Event(object):
    def __init__(self, event):
        self.data= event

class QuitEvent(Event):
    pass

class MouseMoveEvent(Event):
    pass

class MouseEnteredButtonEvent(Event):
    def __init__(self, button_id):
        self.id = button_id

class MouseLeftButtonEvent(Event):
    def __init__(self, button_id):
        self.id = button_id

class MouseButtonDownEvent(Event):
    pass

class MouseButtonUpEvent(Event):
    pass

class GameStartedEvent(Event):
    pass

_event_lookup = {
    pygame.QUIT : QuitEvent,
    pygame.MOUSEMOTION : MouseMoveEvent,
    pygame.MOUSEBUTTONDOWN : MouseButtonDownEvent,
    pygame.MOUSEBUTTONUP : MouseButtonUpEvent
}

class EventProcessor(object):
    def __init__(self):
        self._event_queue= []
        self._dispatcher= EventDispatcher()

    def get_dispatcher(self):
        return self._dispatcher

    def process_events(self):
        pass

class PyGameEventProcessor(EventProcessor):
    def __init__(self):
        super(PyGameEventProcessor, self).__init__()

    def process_events(self):
        for pygame_event in pygame.event.get():
            if _event_lookup.has_key(pygame_event.type):
                self._event_queue.append(_event_lookup[pygame_event.type](pygame_event))
        for event in self._event_queue:
            self._dispatcher.dispatch_event(event)
        self._event_queue= []