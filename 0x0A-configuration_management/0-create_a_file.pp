#creating a file with specific permission and owners
file { '/tmp/school':
    ensure  => present,
    mode    => '0744',
    owner   => 'www-data',
    group   => 'www-data',
    content => 'I love Puppet'
}
