fromserviceable

class Car(Serviceable):
    def __init__(self, last_service_date, engine, battery):
        self.battery = battery
        self.engine = engine

    @abstractmethod
    def needs_service(self):
        return self.battery.needs_service() or self.engine.needs_service()
