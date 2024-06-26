from DatabaseManager import DatabaseManager
from datetime import datetime, timedelta

class ManagementFacade:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    def get_yesterdays_sales(self):
        return self.db_manager.get_yesterdays_sales()

    def get_menu(self):
        return self.db_manager.get_menu()

    def add_menu_item(self, name, allergy, cost):
        self.db_manager.add_menu_item(name, allergy, cost)

    def delete_menu_item(self, name):
        self.db_manager.delete_menu_item(name)

    def get_sales_records_by_date_range(self, start_date, end_date):
        return self.db_manager.get_sales_records_by_date_range(start_date, end_date)

if __name__ == "__main__":
    db_manager = DatabaseManager('root', 'password', '127.0.0.1', 'CafeDB')
    management_facade = ManagementFacade(db_manager)

    # Get yesterday's sales
    yesterdays_sales = management_facade.get_yesterdays_sales()
    print("Yesterday's Sales:", yesterdays_sales)

    # Get entire menu
    menu = management_facade.get_menu()
    print("Menu:", menu)

    # Add new menu item
    management_facade.add_menu_item('Bagel', 'Gluten', 2.00)
    print("Added Bagel to the menu.")

    # Delete menu item
    management_facade.delete_menu_item('Bagel')
    print("Deleted Bagel from the menu.")

    db_manager.close()
