#!/usr/bin/env bash
# use Puppet to make changes to ssh configuration file

file {'etc/ssh/ssh_config':
  ensure  => file,
}

file_line {'IdentityFile':
  path      => 'etc/ssh/ssh_config',
  file_line => 'IdentityFile ~/.ssh/school',
}

file_line {'NoPassword':
  path      => 'etc/ssh/ssh_config',
  file_line => 'PasswordAuthentication no',
}

