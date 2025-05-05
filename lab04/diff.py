def compare_bitwise(array1, array2):
    """Compare two lists element by element and calculate differing bits."""
    for i in range(min(len(array1), len(array2))):
        # Convert hex to binary (string)
        bin1 = bin(int(array1[i], 16))[2:].zfill(len(array1[i]) * 4)
        bin2 = bin(int(array2[i], 16))[2:].zfill(len(array2[i]) * 4)
        
        length = min(len(bin1), len(bin2))
        bin1, bin2 = bin1[:length], bin2[:length]
        
        # Count differing bits
        differing_bits = sum(1 for b1, b2 in zip(bin1, bin2) if b1 != b2)
        total_bits = length
        percentage = (differing_bits / total_bits) * 100
        
        print(f"Liczba różniących się bitów: {differing_bits} z {total_bits}, procentowo: {percentage:.0f}%.")

if __name__ == "__main__":
    array = [
        "4213820acf88ada306fd41ff0118bc08",
        "ef357a090766e1b32cb619442b6fd40670c14c82",
        "422295f91d7507927c70dcd04a5c6763ed0b43992c7698b4226fb261",
        "3fff3fed65c1af8b9436c04942fc4dbc51372fd9c9e9a82bc9adf2f0565ac777",
        "4cba7d8a73272152f975318955257ab6dfa8c8874c7c0972e0929c18dde45f3de079449417b6e83b9e7cbd074f1da99a",
        "c6bdb88eefd980a2719b8bc4ab59068ad5f9442284707ba3a52c94a8cebdb6e08497cf8ff84f1b5e3b020fd57178dce43b9d544c873d21a430591fa9be33cd87",
        "dfc2e0675527c65856ff16c2ef00db8fa75e171d2be82678ef4491fe4ac506a9068a47981167045607d8a99e728ca02e212dae5ded4a66d3ffb3eb3027dcf67a"
    ]

    array_ = [
        "83813fb6a1405383ee7efa924dd8dddc",
        "8acf788b33b837f018b0f53256d2d2f8aca64ca8",
        "11048559ff036854381c00a59ec0b007c77aa3317c51a428aa756ca9",
        "47b7872f68cbdf6ad39354dbac9b5f7f4a29ad0b425337e73f79961f8d615ba4",
        "1bffe309c1d97d89cca30cf434ec7dd7e9beed4251aa7782fc34845fba11c8a739dc77955fe9b9fa6d95edbbbf9d5469",
        "e2b0014639a2320af8c39d7af44a00d08423be3479c1e6b5f5a262b87a595470383e8a47e4a3f14b1a77158b0656945d3fa877437c0ae068fd39f4c7e6e588b2",
        "6cbf4c004206b49edd620e7c1d01249a19d51930e2c3ae81d626b3afdf9029a5264d2d099b2b1022abdf4a9049fdf2087a95cf29b1c872dc2ff93a9e265427e8"
    ]

    compare_bitwise(array, array_)

