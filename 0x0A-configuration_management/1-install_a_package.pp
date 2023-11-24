# install flask from pip3
class flask {
  package { 'flask':
    ensure   => 'installed',
    provider => 'pip3',
    version  => '2.1.0',
  }
}
