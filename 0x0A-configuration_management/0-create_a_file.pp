# This puppet file creates a file in /tmp with contents
# I love Puppet
file { '/tmp/school':
  ensure  => 'present',
  owner   => 'www-data',
  group   => 'www-data',
  mode    => '0744',
  content => 'I love Puppet',
}
