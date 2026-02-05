#! python3

def ft_archive_creation() -> None:
    print('=== CYBER ARCHIVES - PRESERVATION SYSTEM ===\n')

    filename = 'new_discovery.txt'
    entrys = [
        'New quantum algorithm discovered',
        'Efficiency increased by 347%',
        'Archived by Data Archivist trainee'
    ]

    try:
        print(f'Initializing new storage unit: {filename}')
        with open(filename, 'a') as file:
            print('Storage unit created successfully...')
            print('\nInscribing preservation data...')
            for idx, entry in enumerate(entrys):
                content = f'[ENTRY {idx}] {entry}'
                file.write(content)
                if (idx != len(entrys) - 1):
                    file.write('\n')
                print(content)
            print('')
        print('Data inscription complete. Storage unit sealed.')
        print(f'Archive \'{filename}\' ready for long-term preservation.')

    except PermissionError:
        print('Error: Failaid to inscribing preservation data '
              '(no permission)...')
    except OSError as e:
        print(f'Error: {e}')


if __name__ == '__main__':
    ft_archive_creation()
