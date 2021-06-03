from datetime import datetime, timedelta
from once import db


class Secret(db.Model):
    id = db.Column(db.String(32), primary_key=True)
    data = db.Column(db.String(32 * 1024), nullable=False)
    created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    created_by = db.Column(db.String(128))
    created_email = db.Column(db.String(128))
    max_views = db.Column(db.Integer, default=1)
    delete_after = db.Column(
        db.DateTime, default=(datetime.utcnow() + timedelta(days=7))
    )

    def __repr__(self):
        return f"<Secret {id}>"
