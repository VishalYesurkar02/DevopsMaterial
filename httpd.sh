#!/bin/bash
yum install httpd -yum
echo "<h1> Web server installed "</h1>
service httpd start
chconfig httpd on