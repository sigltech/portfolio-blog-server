from portfolio_blog_server import db
from portfolio_blog_server.models import users, posts

# Clear it all out

db.drop_all()

# Set it back up

db.create_all()
