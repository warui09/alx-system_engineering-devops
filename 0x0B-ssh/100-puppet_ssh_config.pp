#!/usr/bin/env bash
# use Puppet to make changes to ssh configuration file

file {'/etc/ssh/ssh_config':
  ensure  => present,
}

file_line {'IdentityFile':
  path      => '/etc/ssh/ssh_config',
  file_line => 'IdentityFile ~/.ssh/school',
  match     => '^IdentityFile',
}

file_line {'NoPassword':
  path      => '/etc/ssh/ssh_config',
  file_line => 'PasswordAuthentication no',
  match     => '^PasswordAuthentication',
}

