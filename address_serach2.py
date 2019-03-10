import requests


def main():
    zipcode = input('郵便番号(7桁)?: ')
    url = f'http://zipcloud.ibsnet.co.jp/api/search?zipcode={zipcode}'
    r = requests.get(url)
    address_dict = r.json()
    address1 = address_dict['results'][0]['address1']
    address2 = address_dict['results'][0]['address2']
    address3 = address_dict['results'][0]['address3']
    print(f'{address1}{address2}{address3}')


if __name__ == '__main__':
    main()
