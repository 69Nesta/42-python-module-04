#! python3

def ft_vault_security() -> None:
    print('=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n')
    filename = 'classified_data.txt'
    try:
        print('Initiating secure vault access...')
        with open(filename, 'r+') as f:
            print('Vault connection established with failsafe protocols')
            print('SECURE EXTRACTION:')
            print(f.read())

            print('\nSECURE PRESERVATION:')
            new_content = '[CLASSIFIED] New security protocols archived'
            f.write(f'\n{new_content}')
            print(new_content)
        print('Vault automatically sealed upon completion\n')

    except (FileNotFoundError, PermissionError, IOError) as e:
        print(f'{type(e).__name__}: {e}')
    finally:
        print('All vault operations completed with maximum security.')


if __name__ == '__main__':
    ft_vault_security()
