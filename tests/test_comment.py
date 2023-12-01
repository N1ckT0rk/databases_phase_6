from lib.comment import Comment

# Test that class constructs with id, content, author_name 
# and post_id
def test_construct():
    test_comment =  Comment(1, "Content", "Author", 1)
    assert test_comment.id == 1
    assert test_comment.content == "Content"
    assert test_comment.author_name == "Author"
    assert test_comment.post_id == 1

    # We can compare two identical artists
# And have them be equal
def test_comments_are_equal():
    test_comment1 =  Comment(1, "Content", "Author", 1)
    test_comment2 =  Comment(1, "Content", "Author", 1)
    assert test_comment1 == test_comment2

# # We can format posts to strings nicely
def test_comments_format_nicely():
    test_comment =  Comment(1, "Content", "Author", 1)
    assert str(test_comment) == "Comment(1, Content, Author, 1)"


