# This manifest kills the process of killmenow
exec { 'killmenow':
  command => '/usr/bin/pkill -f killmenow',
}
