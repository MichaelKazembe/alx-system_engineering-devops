# Fix 500 Internal Server Error when a GET HTTP method is requested to Apache web server

# Ensure 'wp-settings.php' file is correctly configured for GET requests

exec {'configure_wp_settings_for_get':
  provider => shell,
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php',
}
