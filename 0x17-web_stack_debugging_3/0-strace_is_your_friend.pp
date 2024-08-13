# 0-strace_is_your_friend.pp
# This Puppet manifest installs the missing php5-mysql module and restarts Apache

exec { 'install-php-mysql':
  command => '/usr/bin/apt-get install -y php5-mysql',
  path    => ['/bin', '/usr/bin'],
}

service { 'apache2':
  ensure    => 'running',
  enable    => true,
  require   => Exec['install-php-mysql'],
  subscribe => Exec['install-php-mysql'],
}
