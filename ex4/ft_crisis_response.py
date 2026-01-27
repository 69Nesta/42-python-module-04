#! python3


def ft_crisis_response() -> None:
    print('=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n')
    try:
        print('CRISIS ALERT: Attempting access to \'lost_archive.txt\'...')
        with open('lost_archive.txt', 'r') as f:
            print(f'SUCCESS: Archive recovered - \'\'{f.read()}\'\'')
    except FileNotFoundError:
        print('RESPONSE: Archive not found in storage matrix')
    except PermissionError:
        print('RESPONSE: Security protocols deny access')
    except OSError:
        print('RESPONSE: Could not open/read file!')
    finally:
        print('STATUS: Crisis handled, system stable')
    print('')

    try:
        print('CRISIS ALERT: Attempting access to \'classified_vault.txt\'...')
        with open('classified_vault.txt', 'r') as f:
            print(f'SUCCESS: Archive recovered - \'\'{f.read()}\'\'')
    except FileNotFoundError:
        print('RESPONSE: Archive not found in storage matrix')
    except PermissionError:
        print('RESPONSE: Security protocols deny access')
    except OSError:
        print('RESPONSE: Could not open/read file!')
    finally:
        print('STATUS: Crisis handled, ecurity maintained')

    print('')
    try:
        print('ROUTINE ACCES: Attempting access to \'standard_archive.txt\''
              '...')
        with open('standard_archive.txt', 'r') as f:
            print(f'SUCCESS: Archive recovered - \'\'{f.read()}\'\'')
    except FileNotFoundError:
        print('RESPONSE: Archive not found in storage matrix')
    except PermissionError:
        print('RESPONSE: Security protocols deny access')
    except OSError:
        print('RESPONSE: Could not open/read file!')
    finally:
        print('STATUS: Crisis handled, system stable')

    print('\nAll crisis scenarios handled successfully. Archives secure.')


if __name__ == '__main__':
    ft_crisis_response()
