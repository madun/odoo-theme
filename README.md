## Katharos (mean "Clean" in Greece)

### how to start

create env
```
python3 -m venv env-name
```
mengaktifkan env yang akan digunakan
```
source env-name/bin/activate
```

install requirement dependencies (pastikan posisi active env di dalam (env-name)) 
```
pip3 install setuptools wheel
pip3 install -r requirements.txt
```

(optional) di dalam env env-name jalankan
```
npm install -g rtlcss
```

buatkan file odoo.conf di root project, lalu sesuaikan dgn kebutuhan config berikut
```
[options]
admin_passwd = $admin-db
db_host = localhost
db_port = 5432
db_user = odoo_user
db_password = odoo_user
dbfilter =
db_list = True
addons_path = /Users/ilmanqori/Playground/odoo-18.0/addons, /Users/ilmanqori/Playground/odoo-18.0/odoo/addons, /Users/ilmanqori/Playground/odoo-18.0/odoo,
http_port = 8069
```

setelahnya jalankan perintah berikut untuk menjalankan server odoo di port yg telah di pasang di odoo.conf
```
python3 odoo-bin -c odoo.conf dbbaru
```

### how to listen or build tailwindcss

on the path dir env-name/katharos-theme
```
npm run build:css
npm run watch:css
```


[![Build Status](https://runbot.odoo.com/runbot/badge/flat/1/master.svg)](https://runbot.odoo.com/runbot)
[![Tech Doc](https://img.shields.io/badge/master-docs-875A7B.svg?style=flat&colorA=8F8F8F)](https://www.odoo.com/documentation/master)
[![Help](https://img.shields.io/badge/master-help-875A7B.svg?style=flat&colorA=8F8F8F)](https://www.odoo.com/forum/help-1)
[![Nightly Builds](https://img.shields.io/badge/master-nightly-875A7B.svg?style=flat&colorA=8F8F8F)](https://nightly.odoo.com/)

Odoo
----

Odoo is a suite of web based open source business apps.

The main Odoo Apps include an <a href="https://www.odoo.com/page/crm">Open Source CRM</a>,
<a href="https://www.odoo.com/app/website">Website Builder</a>,
<a href="https://www.odoo.com/app/ecommerce">eCommerce</a>,
<a href="https://www.odoo.com/app/inventory">Warehouse Management</a>,
<a href="https://www.odoo.com/app/project">Project Management</a>,
<a href="https://www.odoo.com/app/accounting">Billing &amp; Accounting</a>,
<a href="https://www.odoo.com/app/point-of-sale-shop">Point of Sale</a>,
<a href="https://www.odoo.com/app/employees">Human Resources</a>,
<a href="https://www.odoo.com/app/social-marketing">Marketing</a>,
<a href="https://www.odoo.com/app/manufacturing">Manufacturing</a>,
<a href="https://www.odoo.com/">...</a>

Odoo Apps can be used as stand-alone applications, but they also integrate seamlessly so you get
a full-featured <a href="https://www.odoo.com">Open Source ERP</a> when you install several Apps.

Getting started with Odoo
-------------------------

For a standard installation please follow the <a href="https://www.odoo.com/documentation/master/administration/install/install.html">Setup instructions</a>
from the documentation.

To learn the software, we recommend the <a href="https://www.odoo.com/slides">Odoo eLearning</a>, or <a href="https://www.odoo.com/page/scale-up-business-game">Scale-up</a>, the <a href="https://www.odoo.com/page/scale-up-business-game">business game</a>. Developers can start with <a href="https://www.odoo.com/documentation/master/developer/howtos.html">the developer tutorials</a>
