from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-%3_pe(z01qs*z0uh5odln3q)8@4ii&1fhecdzaoc#ma0)4d@ce'

DEBUG = True

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'axes',
    'core',  # Include the 'core' app
    'members',
]

# Security processes

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'core.middleware.RestrictedAccessMiddleware',
    'axes.middleware.AxesMiddleware',
    'django.middleware.security.SecurityMiddleware',  # Add SecurityMiddleware here
]

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.SHA1PasswordHasher',
]

AUTHENTICATION_BACKENDS = [
    'axes.backends.AxesBackend',  # Add AxesBackend
]

ROOT_URLCONF = 'TestDjango.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'core'],  # Include core templates
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

WSGI_APPLICATION = 'TestDjango.wsgi.application'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'MasterBikesDb',
        'USER': 'root',
        'PASSWORD': 'ikeasusig2228',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'sql_mode': 'traditional',
        }
    }
}

ALLOWED_HOSTS = ['MasterBikesDemo.herokuapp.com']

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

STATICFILES_DIRS = [
    BASE_DIR / 'core' / 'static',  # Adjust the path to the 'static' folder inside the 'core' app
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'

# Axes configuration
AXES_FAILURE_LIMIT = 3  # Number of allowed login attempts
AXES_LOCK_OUT_AT_FAILURE = True  # Lock out the user after failure limit
AXES_COOLOFF_TIME = 1  # Lockout period in hours

# Security settings
SECURE_BROWSER_XSS_FILTER = True  # Enable XSS protection

# Content Security Policy
CSP_HEADER = {
    'default-src': "'self'",
    'script-src': ["'self'", "'unsafe-inline'", 'https://cdn.jsdelivr.net'],
    'style-src': ["'self'", "'unsafe-inline'", 'https://cdn.jsdelivr.net'],
    'img-src': "'self'",
    'font-src': "'self' https://fonts.gstatic.com",
    'connect-src': "'self'",
    'media-src': "'self'",
}

# Secure your cookies
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Prevent framing of your site to avoid clickjacking
X_FRAME_OPTIONS = 'DENY'

# Enable HSTS (HTTP Strict Transport Security) to force HTTPS
SECURE_HSTS_SECONDS = 31536000  # One year
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# Security headers
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_REFERRER_POLICY = 'same-origin'

# Disable the browsable API renderer for production
if not DEBUG:
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = (
        'rest_framework.renderers.JSONRenderer',
    )

#security procesess

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'core.middleware.RestrictedAccessMiddleware',
    'axes.middleware.AxesMiddleware',
    'django.middleware.security.SecurityMiddleware',
]

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
    'django.contrib.auth.hashers.SHA1PasswordHasher',
]

AUTHENTICATION_BACKENDS = [
    'axes.backends.AxesBackend',  # Add AxesBackend
]

ROOT_URLCONF = 'TestDjango.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'core'],  # Include core templates
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

WSGI_APPLICATION = 'TestDjango.wsgi.application'

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'MasterBikesDb',
        'USER': 'root',
        'PASSWORD': 'ikeasusig2228',
        'HOST': 'localhost',
        'PORT': '3306',
        'OPTIONS': {
            'sql_mode': 'traditional',
        }
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

STATICFILES_DIRS = [
    BASE_DIR / 'core' / 'static',  # Adjust the path to the 'static' folder inside the 'core' app
]

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

STATIC_URL = '/static/'

# Axes configuration
AXES_FAILURE_LIMIT = 3  # Number of allowed login attempts
AXES_LOCK_OUT_AT_FAILURE = True  # Lock out the user after failure limit
AXES_COOLOFF_TIME = 1  # Lockout period in hours
