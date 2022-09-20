#Client configuration file
include stdlib
file_line { 'Declare identify file':
  path    => '/etc/ssh/sshd_config',
  line    => '    IdentifyFile ~/.ssh/school',
  replace => true,
}

file_line { 'Passwd authentication':
  path    => '/etc/ssh/ssh_config',
  line    => '    PasswordAuthentication no',
  replace => true,
}
