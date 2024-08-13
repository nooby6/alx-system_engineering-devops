# Puppet script to fix typo errors in PHP files

exec { 'fix-php-typo':
  command => "sed -i 's/.phpp/.php/g' /var/www/html/wp-settings.php",
  path    => ['/usr/local/sbin', '/usr/local/bin', '/usr/sbin', '/usr/bin', '/sbin', '/bin'],
  onlyif  => "grep -q '.phpp' /var/www/html/wp-settings.php",
}
