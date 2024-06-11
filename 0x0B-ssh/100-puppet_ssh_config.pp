# ASKED: Puppet to make changes to our configuration file.
# Just as in the previous configuration file task, we’d like you to set up your
# client SSH configuration file so that you can connect to a server without typing a password

include stdlib
file_line { 'Declare identity file':
  path    => '/etc/ssh/ssh_config',
  line    => '    IdentityFile ~/.ssh/holberton',
  replace => true,
}

file_line { 'Turn off passwd auth':
  path    => '/etc/ssh/ssh_config',
  line    => '    PasswordAuthentication no',
  replace => true,
}
