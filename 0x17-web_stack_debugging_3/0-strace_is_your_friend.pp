# replace occurrences of 'phpp' with 'php'

exec { 'replace-phpp-with-php':
  command => '/bin/sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
}
