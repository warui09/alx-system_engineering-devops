# increase the maximum number of files nginx can start

exec { 'adjust_nginx_file_limit':
  command     => 'sed -i "5s/[0-9]\+/$(`ulimit -n`)/" /etc/default/nginx && service nginx restart',
  refreshonly => true,
  onlyif      => 'test -e /etc/default/nginx',
  provider    => shell,
}
