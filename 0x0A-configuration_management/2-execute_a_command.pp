# kills a process named killmenow
exec { 'kill killmenow':
  command => 'pkill -f killmenow',
  onlyif  => 'pgrep -f killmenow',
  path    => ['/usr/bin', '/bin', '/usr/sbin', '/sbin'],
}
