# Tuples are used for the status choices for the Post model
# to enable staff to moderate posts and allow users to save drafts
STATUS = (
    (0, 'Draft'),
    (1, 'Sent for moderation'),
    (2, 'Published'),
    )

# Categories for model Post
POST_CATEGORIES = (
        ('adventure', 'Adventure'),
        ('travel', 'Travel'),
        ('nature', 'Nature'),
        ('landscape', 'Landscape'),
        ('aerial', 'Aerial'),
        ('wildlife', 'Wildlife'),
        ('street', 'Street'),
        ('architecture', 'Architecture'),
    )

# Pagination for post list and tag list views
PAGINATION = 5  # posts per page

# Template names
ABOUT = 'about.html'
ADD_POST = 'add_post.html'
BLOG = 'blog.html'
CONTACT = 'contact.html'
DELETE_POST = 'delete_post.html'
EDIT_POST = 'edit_post.html'
FULL_POST = 'full_post.html'
INDEX = 'index.html'
USER_ACCOUNT = 'user_account.html'
