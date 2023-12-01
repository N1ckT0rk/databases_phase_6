class Post:
    
    def __init__(self, id, title, content, comments = None):
        self.id = id
        self.title = title
        self.content = content
        self.comments = comments or []

    def __eq__(self, other):
        if isinstance(other, list):
            # Compare only the comments part
            return self.comments == other
        elif isinstance(other, Post):
            # Compare the entire Post object
            return self.__dict__ == other.__dict__
        return False
    
    # def __eq__(self, other):
    #     return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Post({self.id}, {self.title}, {self.content})"