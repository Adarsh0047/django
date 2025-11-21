from blogs.models import Blog, BlogPost

# Get all blog objects
all_blogs = Blog.objects.all()

# Get the SQL query used for running the above cmd as django supports ORM language
print(all_blogs.query)

# Now Get Info from a single blog object
blog_obj = all_blogs[0]

# Get Title
blog_obj.title
blog_obj.date_added
blog_obj.date_added.isoformat()

# Get all the attributes of the blog object
blog_obj.__dict__

# Get the id of the blog object
blog_id = blog_obj.id

# Get the blog obj using id
blog_from_id = Blog.objects.get(id=blog_id)

# Get Blog Posts
all_posts = BlogPost.objects.all()


# Retrieve posts for a specific blog
all_related_blogposts = blog_obj.blogpost_set.all()

# Get the most recent blog post for a specific blog
most_recent_post = blog_obj.blogpost_set.order_by('-date_added')[0]
