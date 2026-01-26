#! python3

import sys


def standard(message: str) -> None:
    print(f'[STANDARD] {message}', file=sys.stdout)


def alert(message: str) -> None:
    print(f'[ALERT] {message}', file=sys.stderr)


def ft_stream_management() -> None:
    print('=== CYBER ARCHIVES - COMMUNICATION SYSTEM ===\n')
    archive_id = input('Input Stream active. Enter archivist ID: ')
    status_report = input('Input Stream active. Enter status report: ')
    print('')

    try:
        standard(f'Archive status from {archive_id}: {status_report}')
        alert('System diagnostic: Communication channels verified')
        standard('Data transmission complete')
        print('\nThree-channel communication test successful')
    except Exception:
        print('\nThree-channel communication test not successful !')


if __name__ == '__main__':
    ft_stream_management()
