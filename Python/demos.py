def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

print(bubble_sort([64, 34, 25, 12, 22, 11, 90]))



 import csv
from collections import defaultdict

class SalesAnalyzer:
    def __init__(self, file_path):
        self.file_path = file_path
        self.sales_data = []
        self.total_sales = 0
        self.sales_by_category = defaultdict(float)

    def load_data(self):
        """Reads the CSV file and loads sales data."""
        try:
            with open(self.file_path, mode="r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    try:
                        category = row["Category"]
                        amount = float(row["Amount"])
                        self.sales_data.append({"category": category, "amount": amount})
                    except ValueError:
                        print(f"Skipping invalid row: {row}")
        except FileNotFoundError:
            print(f"Error: File '{self.file_path}' not found.")

    def calculate_totals(self):
        """Calculates total sales and sales per category."""
        for record in self.sales_data:
            self.total_sales += record["amount"]
            self.sales_by_category[record["category"]] += record["amount"]

    def generate_report(self):
        """Generates a sales summary report."""
        print("\n🔹 Sales Summary Report 🔹")
        print(f"Total Sales: ${self.total_sales:.2f}\n")
        print("Sales by Category:")
        for category, amount in sorted(self.sales_by_category.items(), key=lambda x: x[1], reverse=True):
            print(f" - {category}: ${amount:.2f}")

if __name__ == "__main__":
    analyzer = SalesAnalyzer("sales_data.csv")
    analyzer.load_data()
    analyzer.calculate_totals()
    analyzer.generate_report()
