# Install nginx
package {'nginx':
  ensure   => 'installed',
  provider => 'apt',
}

# Allow Nginx HTTP traffic through the firewall
exec {'allow nginx traffic':
  command => "sudo ufw allow 'Nginx HTTP'",
  unless  => "sudo ufw status | grep 'Nginx HTTP'",
  path    => ['/usr/bin', '/bin', '/usr/sbin', '/sbin'],
}

# Change the content of the default page
file {'/var/www/html/index.nginx-debian.html':
  ensure  => 'present',
  content => 'Hello World!',
  mode    => '0644'
}

# Setup custopm 404 error page
file {'/var/www/html/error_pages/404.html':
  ensure  => 'present',
  content => "Ceci n'est pas une page",
  mode    => '0644'
}

# Make /redirect_me is redirect to another page(and clean default host configuration).
exec {'configure nginix default':
command => "echo '\
server {
    listen 80 default_server;
    listen [::]:80 default_server;

    root /var/www/html;
    index index.html index.htm index.nginx-debian.html;

    server_name _;

    location / {
        try_files \$uri \$uri/ =404;
    }

    location /redirect_me/ {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }

    error_page 404 /404.html;
    location = /404.html{
        root /var/www/html/error_pages/;
        internal;
    }
}' | sudo tee /etc/nginx/sites-available/default >/dev/null",
path    => ['/usr/bin', '/bin', '/usr/sbin', '/sbin'],
notify  => Service['nginx']
}

# Start Nginx 
service { 'nginx':
  ensure    => running,   # Ensure the service is running
  enable    => true,      # Enable the service to start on boot
  subscribe => File['/etc/nginx/sites-available/default'],  # Restart when this file changes
}
