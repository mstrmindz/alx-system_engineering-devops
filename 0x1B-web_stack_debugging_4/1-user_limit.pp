# changes to allow user's limits.
exec { 'change_user_limit':
command => "sed -i 's/5/6000/g; s/4/8000/g' /etc/security/limits.conf",
path    => [ '/bin/', '/sbin/', '/usr/bin', '/usr/sbin/' ]
}
