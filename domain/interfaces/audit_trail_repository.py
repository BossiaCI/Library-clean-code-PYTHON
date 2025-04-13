from abc import ABC, abstractmethod

class AuditTrailRepository(ABC):
    @abstractmethod
    def log(self, audit_trail):
        pass
