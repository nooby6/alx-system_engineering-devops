# Manifest to kill a process named "killmenow" using pkill
exec { 'kill_killmenow_process':
  command => 'pkill -f killmenow',
  onlyif  => 'pgrep -f killmenow',
}
