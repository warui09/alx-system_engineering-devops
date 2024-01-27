# increase the number of files user can open

exec { 'increase_open_file_limits_for_holberton':
  command     => 'echo "holberton soft nofile 4096\nholberton hard nofile 8192" >> /etc/security/limits.conf && sysctl -p',
  onlyif      => 'grep -q "holberton" /etc/security/limits.conf',
  refreshonly => true,
}
