# This manifest kills the process of killmenow
exec { 'killmenow':
  command => 'pkill -f killmenow',
}
