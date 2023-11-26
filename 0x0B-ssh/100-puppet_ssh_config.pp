#!/usr/bin/env bash
# use Puppet to make changes to ssh configuration file

file {'etc/ssh/ssh_config':
  ensure  => file,
  content => "
Host *
  IdentityFile ~/.ssh/school
  PasswordAuthentication no
",
  mode    => '0644',
}
