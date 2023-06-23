# a script that increases the limit of requests.
exec { 'limit_request_increase':
  command => "sed -i 's/15/25000/g' /etc/default/nginx; service nginx restart",
    path    => ['/bin/', '/sbin/', '/usr/bin/', '/usr/sbin/']
    }
