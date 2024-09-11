from abc import ABC, abstractmethod

# Antarmuka untuk diskon produk
class Discount(ABC):
    @abstractmethod
    def calculate_discount(self, price):
        pass

# Kelas untuk diskon elektronik
class ElectronicsDiscount(Discount):
    def calculate_discount(self, price):
        return price * 0.9  # 10% discount for electronics

# Kelas untuk diskon pakaian
class ClothingDiscount(Discount):
    def calculate_discount(self, price):
        return price * 0.8  # 20% discount for clothing

# Kelas untuk diskon default (tanpa diskon)
class NoDiscount(Discount):
    def calculate_discount(self, price):
        return price  # no discount

# Kelas utama untuk menghitung diskon
class DiscountCalculator:
    def get_discount_strategy(self, product_type):
        if product_type == 'electronics':
            return ElectronicsDiscount()
        elif product_type == 'clothing':
            return ClothingDiscount()
        else:
            return NoDiscount()

    def calculate_discount(self, product_type, price):
        discount_strategy = self.get_discount_strategy(product_type)
        return discount_strategy.calculate_discount(price)

# Contoh penggunaan
if __name__ == "__main__":
    calculator = DiscountCalculator()
    product_type = input("Masukkan jenis produk (electronics/clothing): ")
    price = float(input("Masukkan harga produk: "))
    discounted_price = calculator.calculate_discount(product_type, price)
    print(f"Harga setelah diskon: {discounted_price}")
