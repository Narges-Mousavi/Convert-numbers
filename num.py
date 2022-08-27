try:
    n = int(input('PLEASE ENTER A NUMBER : '))

    numbers0_10 = ['', 'یک', 'دو', 'سه', 'چهار', 'پنج', 'شش', 'هفت', 'هشت', 'نه', 'ده']
    numbers11_20 = ['ده و ', 'یازده', 'دوازده', 'سیزده', 'چهارده', 'پانزده', 'شانزده', 'هفده', 'هجده', 'نوزده']
    numbers10 = ['', '', 'بیست و ', 'سی و ', 'چهل و ', 'پنجاه و ', 'شصت و ', 'هفتاد و ', 'هشتاد و ', 'نود و ', 'صد و ']
    numbers100 = ['', 'صد و ', 'دویست و ', 'سیصد و ', 'چهارصد و ', 'پونصد و ', 'ششصد و ', 'هفتصد و ', 'هشتصد و ', 'نهصد و ']
    classes = [' ', ' هزار و ', ' میلیون و ', ' بیلیون و ', ' تریلیون و ', ' کوآدریلیون و ', ' کوینتیلیون و ', ' سیکستیلیون و ', ' سپتیلیون و ', ' اکتیلیون و ', ' نانیلیون و ', ' دسیلیون و ', ' آندسیلیون و ', ' دیودسیلیون و ', ' تریدسیلیون و ', ' کواتیوردسیلیون و ', ' کویندسیلیون و ', ' سیکسدسیلیون و ', ' سپتدسیلیون و ', ' اُکتودسیلیون و ', ' نومدسیلیون و ']


    def one_to_hundreds(n):
        yekan = n % 10
        dahgan = ((n % 100) // 10)
        sadgan = n // 100
        if dahgan == 1:
            text = numbers100[sadgan] + numbers11_20[yekan]
        else:
            text = numbers100[sadgan] + numbers10[dahgan] + numbers0_10[yekan]

        if yekan == 0:
            return text[:-2]
        else:
            return text


    def split(n):
        a = '{:,}'.format(n)
        x = a.split(',')
        return x


    print(f'The splitted number is : {split(n)}')


    def read(n):
        text = ''
        a = len(split(n))
        for i in split(n):
            if i == '000':
                a -= 1
            else:
                text += one_to_hundreds(int(i)) + classes[a - 1]
                a -= 1
        print(text[:-2]) if str(n).endswith('000') else print(text)


    def show(n):
        if n > 0:
            read(n)
        elif n == 0:
            print('صفر')
        else:
            n = abs(n)
            print('منفی ', end='')
            read(n)

    show(n)

except:
    print('The number you have entered is not valid')