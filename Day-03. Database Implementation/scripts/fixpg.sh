#!/bin/bash
sed -i 's\ident\md5\g' /var/lib/pgsql/data/pg_hba.conf
systemctl restart postgresql