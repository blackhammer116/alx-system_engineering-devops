# Automating previous tasks with puppet
file { ~/.ssh/config:
  ensure => present,
  content => 'User ubuntu',
}
file { ~/.ssh/config:
  ensure => present,
  content => 'IdentityFile ~/.ssh/school',
}
