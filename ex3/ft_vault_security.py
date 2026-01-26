#! python3

def ft_vault_security() -> None:
    print('=== CYBER ARCHIVES - VAULT SECURITY SYSTEM ===\n')
    try:
        print('Initiating secure vault access...')
        with open('classified_data.txt', 'a+') as f:
            print('Vault connection established with failsafe protocols')
            print('SECURE EXTRACTION:')
            f.seek(0)
            print(f.read())
            start = f.tell() + 1

            print('\nSECURE PRESERVATION:')
            f.write('\n[CLASSIFIED] New security protocols archived')
            f.seek(start)
            print(f.read())
        print('Vault automatically sealed upon completion\n')
        print('All vault operations completed with maximum security.')

    except Exception as e:
        print(f'{type(e)}: {e}')


if __name__ == '__main__':
    ft_vault_security()
