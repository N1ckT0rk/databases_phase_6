from lib.database_connection import DatabaseConnection
from lib.post_repository import PostRepository


# Connect to the database
connection = DatabaseConnection()
connection.connect()

# Seed with some seed data
connection.seed("seeds/blog_posts.sql")


repository = PostRepository(connection)
post = repository.find_with_comments(1)

print(post)
# List out comments
for comment in post.comments:
    print(comment)
