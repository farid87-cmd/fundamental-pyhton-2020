"""
TIPE DATA DICTIONARY SEKEDAR MENGGABUNGKAN ANTARA KEY DAN VALUE
KVP = Key Value Pair
dictionary = kamus

"""
print('data ini di berikan oleh server gojek,untuk memberikan info driver di sekitar pemakai aplikasi')
data_dari_server_gojek = {

    'tanggal': '2021-02-19',
    'driver_list': [
        {'nama': 'farid', 'jarak': 100},
        {'nama': 'jarwo', 'jarak': 200},
        {'nama': 'anang', 'jarak': 1000},
        {'nama': 'molen', 'jarak': 400}
    ]
}
print(data_dari_server_gojek)
print(f"\nDriver di daerah itu {data_dari_server_gojek['driver_list']}")
print(f"Driver # 1 {data_dari_server_gojek['driver_list'][0]}")
print(f"Driver # 1 {data_dari_server_gojek['driver_list'][2]}")
print(f"\nDriver terdekat berjarak {data_dari_server_gojek['driver_list'][0]} meter")
#print(f"\nDriver terdekat berjarak {data_dari_server_gojek['driver_list'][0]} meter", end="")
#print(f"dengan nama {data_dari_server_gojek['driver_list'][0]['nama']}")
