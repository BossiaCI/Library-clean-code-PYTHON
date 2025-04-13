from domain.models.audit_trail import AuditTrail


class AuditTrailService:
    def __init__(self, audit_trail_repo):
        self.audit_trail_repo = audit_trail_repo

    def log_action(self, action, entity):
        audit_trail = AuditTrail(action, entity)
        self.audit_trail_repo.log(audit_trail)
