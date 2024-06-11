# ASKED: Puppet to make changes to our configuration file.
# Just as in the previous configuration file task, we’d like you to set up your
# client SSH configuration file so that you can connect to a server without typing a password

file{'client configuration':
  ensure  => 'present',
  path    => '/etc/ssh/ssh_config',
  content => 'host 100.24.244.146\n\tIdentityFile ~/.ssh/school\tPasswordAuthentication No',
}
