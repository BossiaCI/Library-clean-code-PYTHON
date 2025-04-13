

from domain.interfaces.audit_trail_repository import AuditTrailRepository


class InMemoryAuditTrailRepository(AuditTrailRepository):
    def __init__(self):
        self.audit_trails = []

    def log(self, audit_trail):
        self.audit_trails.append(audit_trail)

    def get_all(self):
        return self.audit_trails
