# Define a class to manage SSH client configuration
class ssh_config {
  # Install the SSH client configuration file
  file { '/etc/ssh/ssh_config':
    ensure  => file,
    content => "
Host *
  IdentityFile ~/.ssh/school
  PasswordAuthentication no
",
    mode    => '0644',
  }
}
# Include the class to apply the SSH client configuration
include ssh_config
