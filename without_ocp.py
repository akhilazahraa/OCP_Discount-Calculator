class DiscountCalculator:
    def calculate_discount(self, product_type, price):
        if product_type == 'electronics':
            return price * 0.9  # 10% discount for electronics
        elif product_type == 'clothing':
            return price * 0.8  # 20% discount for clothing
        else:
            return price  # no discount for other products

# Contoh penggunaan
if __name__ == "__main__":
    calculator = DiscountCalculator()
    product_type = input("Masukkan jenis produk (electronics/clothing): ")
    price = float(input("Masukkan harga produk: "))
    discounted_price = calculator.calculate_discount(product_type, price)
    print(f"Harga setelah diskon: {discounted_price}")
