from datetime import datetime, timedelta
from once import db


class Secret(db.Model):
    id = db.Column(db.String(32), primary_key=True)
    data = db.Column(db.String(32 * 1024), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    created_by = db.Column(db.String(128))
    created_email = db.Column(db.String(128))
    max_views = db.Column(db.Integer, nullable=False, default=1)
    delete_after = db.Column(
        db.DateTime, default=(datetime.utcnow() + timedelta(days=7))
    )

    def __repr__(self):
        return f"<Secret {id}>"

    def as_dict(self):
        d = {}
        d["id"] = self.id
        d["data"] = self.data
        d["created_at"] = str(self.created_at)
        d["created_by"] = str(self.created_by) if self.created_by else "Anonymous"
        d["created_email"] = str(self.created_email) if self.created_email else "none"
        d["max_views"] = self.max_views
        d["delete_after"] = str(self.delete_after) if self.delete_after else ""
        return d