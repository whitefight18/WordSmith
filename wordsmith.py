import itertools, sys, time

def banner() -> str:
    '''Prints the banner'''
    print(f'''
      ,
     /(
    |  >:00000000000000]
     )(     _    _               _   _____           _ _   _      
     ""    | |  | |             | | /  ___|         (_) | | |     
           | |  | | ___  _ __ __| | \ `--. _ __ ___  _| |_| |__   
           | |/\| |/ _ \| '__/ _` |  `--. \ '_ ` _ \| | __| '_ \  
           \  /\  / (_) | | | (_| | /\__/ / | | | | | | |_| | | |   
            \/  \/ \___/|_|  \__,_| \____/|_| |_| |_|_|\__|_| |_|    --
                                                                     )(
                                                    [00000000000000:<  |
            v1.0.0                                                   )/
            Github : https://github.com/whitefight18                 ´
    ''')

def info_driver():
    '''Main driver to gather and process information'''
    length = input('[+] Provide the range of length of the passwords to generate [eg: "4 to 6" = 4-6]: ')

    if int(length.split('-')[0]) <= int(length.split('-')[1]):
        try:
            min_length = int(length.split('-')[0])
            max_length = int(length.split('-')[1])
        except:
            print('[x] Invalid input format! Length format: [min-max] Exiting program.')
            sys.exit()
            
    print('\n[!] Please provide the details you want to include (press Enter/n for defaults or to skip any).')

    time.sleep(0.6)
  
    if str.lower((input('\n[?] Do you want to enter personal information ? [y/N]: '))) == 'y':
        first_name = str(input('\n[+] First Name: '))
        last_name = str(input('[+] Last Name: '))
        birthday = str(input('[+] Birthday (Date): '))
        month = str(input('[+] (Month): '))
        year = str(input('[+] (Year): '))
        phone_number = str(input('[+] Phone Number: '))
        special_keyword = str(input('[+] Any special keyword if you want to include: '))
        chars = first_name + last_name + birthday + month + year + phone_number + special_keyword
    else:
        chars = 'abcdefghijklmnopqrstuvwxyz'
        pass
    
    L337_transform = str.maketrans('aAaAeEgGiIoOtTsSzZ','@@4433661100775522')
    leet_chars = chars.translate(L337_transform)
    chars_up = chars.upper()
    chars_cap = chars.capitalize()
    special_chars = '!\][/?.,~-=";:><@#^$%&*()_+\''
    numbers = '1234567890'
    
    time.sleep(0.5)

    if str.lower((input('\n[?] Do you want to use additional features ? [y/N]: '))) == 'y':
        if str.lower((input('\n[?] Do you want to use uppercase characters? (y/N): '))) == 'y':
            chars = ''.join([chars, chars_up])
        if str.lower((input('[?] Do you want to use capitalized characters? (y/N): '))) == 'y':
            chars = ''.join([chars, chars_cap])
        if str.lower((input('[?] Do you want to use 1337 characters? (y/N): '))) == 'y':
            chars = ''.join([chars, leet_chars])
        if str.lower((input('[?] Do you want to use special characters? (y/N): '))) == 'y':
            chars = ''.join([chars, special_chars])
        if str.lower((input('[?] Do you want to use numbers? (y/N): '))) == 'y':
            chars = ''.join([chars, numbers])

    file_name = str(input('\n[!] Insert a name for your wordlist file (or press Enter for default, Format: Wordlist.txt): '))
    if not file_name:
        try:
            if first_name:
                file_name = f'{first_name.capitalize()}_Wordlist.txt'
        except:
            file_name = 'Wordlist.txt'
    
    print (f'\n[+] Creating wordlist "{file_name}"...')
    print (f'\n[i] Start time: {time.strftime("%H:%M:%S")}\n')
    
    with open(file_name, 'w') as output:
        generator(min_length, max_length, chars, output)

    print (f'\n[i] End time: {time.strftime("%H:%M:%S")}')

def generator(minLen, maxLen, chars, out):
    for n in range(minLen, maxLen + 1):
        for iterables in itertools.product(chars, repeat=n):
            generated = ''.join(iterables)
            sys.stdout.write(f'\r[+] Saving characters "{generated}"')
            out.write(f'{generated}\n')
            sys.stdout.flush()

def main():
    try:
        banner(); time.sleep(0.6); info_driver()        

    except (IndexError, ValueError):
        print('\n[x] Invalid input format! Length format: [min-max] Exiting program.')
        time.sleep(0.5) , sys.exit()

    except KeyboardInterrupt:
        print('\n\n[x] Keyboard Interrupt received. Exiting program.')
        time.sleep(0.5) , sys.exit()
    
    except Exception as e:
        print(f'\n{e}'), time.sleep(0.5) , sys.exit()

if __name__ == '__main__':
    main()