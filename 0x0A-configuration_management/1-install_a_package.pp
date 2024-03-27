# Install Flask version 2.1.0 and compatible version of Werkzeug using pip3
package { 'python3-pip':
  ensure => 'installed',
}

exec { 'install_werkzeug':
  command     => '/usr/bin/pip3 install Werkzeug==2.0.3',
  path        => ['/usr/local/bin', '/usr/bin'],
  environment => ['PATH=/usr/local/bin:/usr/bin'],
  unless      => '/usr/bin/pip3 show Werkzeug | grep -q "Version: 2.0.3"',
}

exec { 'install_flask':
  command     => '/usr/bin/pip3 install flask==2.1.0',
  path        => ['/usr/local/bin', '/usr/bin'],
  environment => ['PATH=/usr/local/bin:/usr/bin'],
  unless      => '/usr/bin/pip3 show flask | grep -q "Version: 2.1.0"',
}
