## MEMBUAT APLIKASI ECOMMERCE MENGGUNAKAN DJANGO V3.2

https://github.com/gurnitha/django-ecom-ytbravindrakanitkar

### 1. BASICS SETUP 

#### 1.1. Inisialisasi proyek django bernama CONFIG

        new file:   .gitignore
        new file:   config/__init__.py
        new file:   config/asgi.py
        new file:   config/settings.py
        new file:   config/urls.py
        new file:   config/wsgi.py
        new file:   manage.py
        new file:   readme.md

#### 1.2. Membuat remote repository di Github 

		gurnitha/django-ecom-ytbravindrakanitkar
        modified:   readme.md

#### 1.3. Membuat app 'apps/core' dan meregistrasinya pada proyek/settings.py


        new file:   apps/core/__init__.py
        new file:   apps/core/admin.py
        new file:   apps/core/apps.py
        new file:   apps/core/models.py
        new file:   apps/core/tests.py
        new file:   apps/core/views.py
        modified:   config/settings.py
        new file:   db.sqlite3
        modified:   readme.md

#### 1.4. Membuat database menggunakan PostgreSQL dan menghubungkannya dengan proyek 

        modified:   config/settings.py
        modified:   readme.md


#### 1.5. Membuat dan menggunakan Environment Variable untuk db 

        modified:   .gitignore
        modified:   config/settings.py
        modified:   readme.md


#### 1.6. Membuat superuser

        modified:   readme.md

#### 1.7. Menggunakan django Views, Templates, dan Urls untuk menampilkan 'Halo dunia django' 


        new file:   apps/core/urls.py
        modified:   apps/core/views.py
        modified:   config/settings.py
        modified:   config/urls.py
        modified:   readme.md
        new file:   templates/core/index.html

#### 1.8. Mensetup static files 

        modified:   config/settings.py
        modified:   readme.md
        new file:   static/assets/css/style.css
        ...
        new file:   static/assets/img/clients/client-1.png
        new file:   static/assets/img/clients/client-2.png

#### 1.9. Menambahkan home template dan load static file 

        modified:   readme.md
        modified:   templates/core/index.html


#### 1.10. Modifikasi file readme.md

        modified:   readme.md

### 2. USER AUTHENTICATION AND AUTORIZATION

#### 2.1 Membuat app 'apps/accounts' dan registrasi ia pada settings.py

        new file:   apps/accounts/__init__.py
        new file:   apps/accounts/admin.py
        new file:   apps/accounts/apps.py
        new file:   apps/accounts/models.py
        new file:   apps/accounts/tests.py
        new file:   apps/accounts/views.py
        modified:   config/settings.py
        modified:   readme.md


#### 2.2 Menggunakan User models dengan menanmbahkan ekstra fields padanya dan meregistrasinya pada admin.py 

        modified:   apps/core/admin.py
        new file:   apps/core/migrations/0001_initial.py
        modified:   apps/core/models.py
        modified:   readme.md






































































































































