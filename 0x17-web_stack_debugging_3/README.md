0x17. Web stack debugging #3

# Puppet Script to Fix PHP Typo Errors

## Overview

This project contains a Puppet script designed to automatically correct a specific typo in PHP files within a WordPress installation. The typo involves incorrectly typed PHP file extensions (`.phpp` instead of `.php`). The script identifies and replaces the typo to ensure proper functionality of the WordPress site.

## Requirements

- **Operating System**: Ubuntu 14.04 LTS
- **Puppet Version**: v3.4 or later
- **Ruby Version**: Ensure Ruby is installed as it is required for Puppet.

## Installation

1. **Install Puppet**:
    ```bash
    apt-get update
    apt-get install -y puppet
    ```

2. **Install puppet-lint** (optional for linting):
    ```bash
    apt-get install -y ruby
    gem install puppet-lint -v 2.1.1
    ```

## Usage

1. **Create the Puppet Manifest**:
    - Save the following Puppet script to a file named `fix-php-typo.pp`:

    ```puppet
    # Puppet script to fix typo errors in PHP files

    exec { 'fix-php-typo':
      command => "sed -i 's/.phpp/.php/g' /var/www/html/wp-settings.php",
      path    => ['/usr/local/sbin', '/usr/local/bin', '/usr/sbin', '/usr/bin', '/sbin', '/bin'],
      onlyif  => "grep -q '.phpp' /var/www/html/wp-settings.php",
    }
    ```

2. **Run the Puppet Manifest**:
    - Apply the Puppet manifest to correct the typo:
    
    ```bash
    puppet apply fix-php-typo.pp
    ```

3. **Verify**:
    - Confirm that the typo has been corrected and that your WordPress site is functioning properly.

## Troubleshooting

- **Check Logs**: If the script does not work as expected, check the logs for any errors.
- **Permissions**: Ensure that the script has the appropriate permissions to modify the PHP file.

## License

This project is open-source.
