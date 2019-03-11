import requests


def main():
    zipcode = input('郵便番号(7桁)?: ')
    length = len(zipcode)
    if length == 7:
        url = f'http://zipcloud.ibsnet.co.jp/api/search?zipcode={zipcode}'
        r = requests.get(url)
        address_dict = r.json()

        result = address_dict['results']

        if result is not None:
            address1 = address_dict['results'][0]['address1']
            address2 = address_dict['results'][0]['address2']
            address3 = address_dict['results'][0]['address3']

            print(f'{address1}{address2}{address3}')
        else:
            print('該当するデータは見つかりませんでした。検索キーワードを変えて再検索してください。')
    elif length == 0:
        print('必須パラメータが指定されていません。')
    else:
        print('パラメータ「郵便番号」の桁数が不正です。')


if __name__ == '__main__':
    main()
