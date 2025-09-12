# Magic Methods (Dunder Methods) - automatically invokes by Python interpreter for certain operations.

# __str__() - invoked by print() or str() method.
# __repr__() - invoked by repr() method.
# __len__() - invoked by len() method.
# __add__() - invoked by + operator.
# __eq__() - invoked by == operator.

class BlogPost:
    def __init__(self, title, content):
        self._title = title
        self._content = content

    def __str__(self):
        return f'\nBlog: {self._title}'
    
    def __repr__(self):
        return f'BlogPost(title = {self._title}, content = {self._content})'
    
    def __len__(self):
        '''Returns the number of words in the content.'''
        return len(self._content.split())
    
    def __add__(self, blog):
        '''Returns the new blog post concatenating title and content of two blogposts.'''
        if isinstance(blog, BlogPost):
            new_title = self._title + blog._title
            new_content = self._content + blog._content
            return BlogPost(new_title, new_content)
        else:
            raise('ERROR: Not able to add object other than BlogPost type.')
        
    def __eq__(self, blog):
        '''Check title and content of two blogposts are same.'''
        if isinstance(blog, BlogPost):
            return self._title == blog._title and self._content == blog._content
        else:
            raise('ERROR: Not able to compare object other than BlogPost type.')
        
    
def main():
    blog1 = BlogPost('Functions in Python', 'Functions are used for code reusibility.')
    blog2 = BlogPost('Generators in Python', 'Generators in Python uses for memory efficiency.')
    blog3 = BlogPost('Generators in Python', 'Generators in Python uses for memory efficiency.')

    print(blog1)
    print(repr(blog1))
    print(f'Number of words in content - {len(blog1)}')
    print(blog2)
    print(repr(blog2))
    print(f'Number of words in content - {len(blog2)}')

    print('-' * 20)

    print(f'blog1 == blog2: {blog1 == blog2}')
    print(f'blog2 == blog3: {blog2 == blog3}')

    new_blog = blog1 + blog2
    print(new_blog)
    print(repr(new_blog))

    
if __name__ == '__main__':
    main()