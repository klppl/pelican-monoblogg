# Monoblogg

A minimalist Pelican theme with a focus on typography and readability. Built with a clean dark mode design using Monaspace fonts.

## Features

- Clean dark mode design
- Beautiful typography using Monaspace font family
- Responsive layout that works on all devices
- Social media integration with Font Awesome icons
- OpenGraph meta tags support
- Customizable avatar and footer text
- Pagination support
- Tag and category pages

## Installation

1. Clone this repository to your Pelican themes directory:
```bash
git clone https://github.com/yourusername/monoblogg.git
```

2. Add the theme to your `pelicanconf.py`:
```python
THEME = 'path/to/monoblogg'
```

## Configuration

Add these settings to your `pelicanconf.py`:

```python
# Required settings
AUTHOR = 'Your Name'
SITENAME = 'Your Site Name'
SITETITLE = 'Your Site Title'
SITESUBTITLE = 'Your Site Subtitle'

# Theme configuration
FOOTER_TEXT = 'Your footer text'
AVATAR_URL = '/images/avatar.png'  # Path to your avatar image

# Social media links
SOCIAL = (
    ('GitHub', 'https://github.com/username'),
    ('LinkedIn', 'https://linkedin.com/in/username'),
    # Add more social media platforms as needed
)

# Navigation
MENUITEMS = (
    ('about', '/pages/about.html'),
    ('tags', '/tags.html'),
    ('categories', '/categories.html'),
)
```

## License

MIT License

## Credits

- Uses [Monaspace](https://monaspace.githubnext.com/) font family
- Icons by [Font Awesome](https://fontawesome.com/) 