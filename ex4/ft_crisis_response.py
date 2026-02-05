#! python3


def ft_crisis_response() -> None:
    print('=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===\n')
    filename = 'lost_archive.txt'
    try:
        print(f'CRISIS ALERT: Attempting access to \'{filename}\'...')
        with open(filename, 'r') as f:
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

    filename = 'classified_vault.txt'
    try:
        print(f'CRISIS ALERT: Attempting access to \'{filename}\'...')
        with open(filename, 'r') as f:
            print(f'SUCCESS: Archive recovered - \'\'{f.read()}\'\'')
    except FileNotFoundError:
        print('RESPONSE: Archive not found in storage matrix')
    except PermissionError:
        print('RESPONSE: Security protocols deny access')
    except OSError:
        print('RESPONSE: Could not open/read file!')
    finally:
        print('STATUS: Crisis handled, ecurity maintained')

    filename = 'standard_archive.txt'
    print('')
    try:
        print(f'ROUTINE ACCES: Attempting access to \'{filename}\''
              '...')
        with open(filename, 'r') as f:
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
