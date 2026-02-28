import asyncio
from collections import defaultdict
from datetime import datetime


class Event:
    def __init__(self, name: str, payload: dict = None):
        self.name = name
        self.payload = payload or {}
        self.timestamp = datetime.utcnow()

    def __repr__(self):
        return f"<Event {self.name} at {self.timestamp}>"


class EventBus:
    def __init__(self):
        self._subscribers = defaultdict(list)

    def subscribe(self, event_name: str, handler):
        self._subscribers[event_name].append(handler)

    async def publish(self, event: Event):
        handlers = self._subscribers.get(event.name, [])
        for handler in handlers:
            try:
                await handler(event)
            except Exception as e:
                print(f"⚠ Error in handler for {event.name}: {e}")