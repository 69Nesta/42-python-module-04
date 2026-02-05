#! python3

def ft_ancient_text() -> None:
    print('=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n')
    filename = 'ancient_fragment.txt'
    try:
        print(f'Accessing Storage Vault: {filename}')
        with open(filename, 'r') as file:
            print('Connection established...')
            print('\nRECOVERED DATA:')
            for line in file:
                print(line, end='')
            print('\n\nData recovery complete.', end=' ')
        print('Storage unit disconnected.')

    except FileNotFoundError:
        print('Error: Storage vault not found.')
    except PermissionError:
        print('Error: You don\'t have permission to open the vault!')
    except OSError as e:
        print(f'Error: {e}')


if __name__ == '__main__':
    ft_ancient_text()
