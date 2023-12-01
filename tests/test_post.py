from lib.post import Post

# Test that class constructs with id, title and conent
def test_construct():
    test_post =  Post(1, "Title", "Content")
    assert test_post.id == 1
    assert test_post.title == "Title"
    assert test_post.content == "Content"

    # We can compare two identical artists
# And have them be equal

def test_posts_are_equal():
    test_post1 =  Post(1, "Title", "Content")
    test_post2 =  Post(1, "Title", "Content")
    assert test_post1 == test_post2

# We can format posts to strings nicely
def test_posts_format_nicely():
    test_post =  Post(1, "Title", "Content")
    assert str(test_post) == "Post(1, Title, Content)"



