# ──────────────── Site identity ────────────────
AUTHOR = 'John Doe'
SITENAME = 'My Blog'
SITETITLE = 'My Blog'
SITESUBTITLE = 'Thoughts, stories and ideas'
SITEURL = ''
RELATIVE_URLS = True
DEFAULT_LANG = 'en'
TIMEZONE = 'Europe/London'

# ──────────────── Content paths ────────────────
PATH = 'content'
STATIC_PATHS = ['images']
IGNORE_FILES = ['README.md', '.gitignore', '.gitattributes']

# ──────────────── Theme config ────────────────
THEME = 'monoblogg'
THEME_STATIC_DIR = 'static'

# ──────────────── Navigation ────────────────
MENUITEMS = (
    ('about', '/pages/about.html'),
    ('tags', '/tags.html'),
    ('categories', '/categories.html'),
)

SOCIAL = (
    ('GitHub', 'https://github.com/username'),
    ('LinkedIn', 'https://linkedin.com/in/username'),
    ('Twitter', 'https://twitter.com/username'),
    ('Instagram', 'https://instagram.com/in/username'),
)

# ──────────────── Appearance / Customization ────────────────
FOOTER_TEXT = 'Powered by Pelican and Monoblogg theme'
AVATAR_URL = '/images/avatar.png'

# ──────────────── Open Graph metadata ────────────────
OG_TITLE = SITENAME
OG_DESCRIPTION = SITESUBTITLE
OG_IMAGE = SITEURL + '/images/avatar.png'
OG_TYPE = 'website'

JINJA_GLOBALS = {
    'FOOTER_TEXT': FOOTER_TEXT,
    'OG_TITLE': OG_TITLE,
    'OG_DESCRIPTION': OG_DESCRIPTION,
    'OG_IMAGE': OG_IMAGE,
    'OG_TYPE': OG_TYPE,
    'AVATAR_URL': AVATAR_URL,
}

# ──────────────── Pagination ────────────────
DEFAULT_PAGINATION = 10

# ──────────────── Feeds (disabled) ────────────────
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None 