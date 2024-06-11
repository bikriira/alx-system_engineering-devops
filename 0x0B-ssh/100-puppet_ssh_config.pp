# ASKED: Puppet to make changes to our configuration file.
# Just as in the previous configuration file task, we’d like you to set up your
# client SSH configuration file so that you can connect to a server without typing a password

file_line { 'Declare_identity_file':
  path => '/etc/ssh/ssh_config',
  line => 'IdentityFile ~/.ssh/holberton',
}

file_line { 'Turn_off_passwd_auth':
  path => '/etc/ssh/ssh_config',
  line => 'PasswordAuthentication no',
}
