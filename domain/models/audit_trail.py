from datetime import datetime

class AuditTrail:
    def __init__(self, action: str, entity: str):
        self.action = action
        self.entity = entity
        self.timestamp = datetime.now()

    def __str__(self):
        return f"{self.timestamp} - {self.action} - {self.entity}"
