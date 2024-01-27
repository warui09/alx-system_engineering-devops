# increase the maximum number of files nginx can start

class { 'nginx_open_file_limits':
  file_max_limit     => 70000,
  nofile_soft_limit  => 10000,
  nofile_hard_limit  => 30000,
}

class nginx_open_file_limits (
  Int $file_max_limit,
  Int $nofile_soft_limit,
  Int $nofile_hard_limit,
) {
  file { '/etc/sysctl.conf':
    ensure  => file,
    content => "fs.file-max = ${file_max_limit}\n",
    notify  => Exec['sysctl-reload'],
  }

  file { '/etc/security/limits.conf':
    ensure  => file,
    content => "nginx soft nofile ${nofile_soft_limit}\nnginx hard nofile ${nofile_hard_limit}\n",
  }

  exec { 'sysctl-reload':
    command => 'sysctl -p',
    refreshonly => true,
  }
}
