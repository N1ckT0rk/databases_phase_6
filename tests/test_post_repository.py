from lib.post_repository import PostRepository
from lib.post import Post
from lib.comment import Comment

# When we call #find_with_comments function with a post_id
# as a paramenter, we return the post with all related 
# comments.
def test_find_with_comments(db_connection):
    db_connection.seed("seeds/blog_posts.sql")
    respository = PostRepository(db_connection)

    result = respository.find_with_comments(1)

    assert result == Post(1, 'Post1', "Content1", [
        Comment(1, 'Content1', 'Barry', 1),
        Comment(2, 'Content2', 'Gary', 1)
    ])


