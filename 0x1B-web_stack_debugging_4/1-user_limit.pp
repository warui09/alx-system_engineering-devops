# increase the number of files user can open

class increase_open_file_limits {
  # Set soft and hard limits for the user
  file { '/etc/security/limits.conf':
    ensure  => file,
    content => "holberton soft nofile 4096\nholberton hard nofile 8192\n",
  }

  # Reload the system limits
  exec { 'sysctl-reload':
    command     => 'sysctl -p',
    refreshonly => true,
  }
}

class { 'increase_open_file_limits': }
