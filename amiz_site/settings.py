"""
Django settings for amiz_site project.
"""

import os
from pathlib import Path

# ---------------------------
# BASE DIRECTORY
# ---------------------------
BASE_DIR = Path(__file__).resolve().parent.parent


# ---------------------------
# SECURITY SETTINGS
# ---------------------------
SECRET_KEY = 'django-insecure-=&m-*x9lgz=j&b=k930x!2g)h=5wdbaihk9tvw_^q)-@b&uyi&'
DEBUG = True
ALLOWED_HOSTS = ['127.0.0.1', 'localhost']


# ---------------------------
# APPLICATIONS
# ---------------------------
INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'shop',  # your main app
]


# =======================
# Jazzmin Configuration
# =======================
JAZZMIN_SETTINGS = {
    "site_title": "AmizClothz Admin",
    "site_header": "AmizClothz Dashboard",
    "site_brand": "AmizClothz",
    "welcome_sign": "Welcome to AmizClothz Admin",
    "copyright": "© 2025 AmizClothz",
    #"site_logo": "images/logo.png",
    #"site_logo_classes": "img-circle",   # optional style
    #"site_logo_width": "120px",          # 👈 change size here

    "login_logo": "images/logo.png",
    "login_logo_dark": "images/logo.png",
    "show_ui_builder": True,
    "navigation_expanded": True,

    "topmenu_links": [
        {"name": "Home", "url": "admin:index", "permissions": ["auth.view_user"]},
        {"name": "View Site", "url": "/", "new_window": True},
    ],

    "icons": {
        "auth": "fas fa-users",
        "shop.Product": "fas fa-tshirt",
        "shop.Order": "fas fa-box",
        "shop.Cart": "fas fa-shopping-cart",
        "shop.Wishlist": "fas fa-heart",
        "shop.Category": "fas fa-tags",
    },

    "order_with_respect_to": ["shop", "auth"],
}

# =======================
# Jazzmin UI Theme Tweaks
# =======================
JAZZMIN_UI_TWEAKS = {
    "theme": "minty",             # alternative: "pulse", "flatly", "cosmo"
    "navbar": "navbar-light",
    "navbar_fixed": True,
    "layout": "side-nav",
    "dark_mode_theme": "cyborg",
    "brand_colour": "navbar-pink",
    "accent": "accent-info",
    "button_classes": {
        "primary": "btn-primary",
        "secondary": "btn-outline-secondary",
        "success": "btn-success",
        "info": "btn-info",
        "warning": "btn-warning",
        "danger": "btn-danger",
    },
}


# ---------------------------
# MIDDLEWARE
# ---------------------------
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# ---------------------------
# URLS AND WSGI
# ---------------------------
ROOT_URLCONF = 'amiz_site.urls'
WSGI_APPLICATION = 'amiz_site.wsgi.application'


# ---------------------------
# TEMPLATES
# ---------------------------
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR /'templates'],  # global templates folder
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# ---------------------------
# DATABASE
# ---------------------------
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# ---------------------------
# PASSWORD VALIDATION
# ---------------------------
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# ---------------------------
# INTERNATIONALIZATION
# ---------------------------
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True


# ---------------------------
# STATIC FILES
# ---------------------------
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'shop' / 'static',
]
STATIC_ROOT = BASE_DIR / 'staticfiles'


# ---------------------------
# MEDIA FILES
# ---------------------------
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'


# ---------------------------
# LOGIN & REDIRECT SETTINGS
# ---------------------------
LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/account/'
LOGOUT_REDIRECT_URL = '/'


# ---------------------------
# DEFAULT AUTO FIELD
# ---------------------------
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
