class Employee:
    def __init__(self, name, age, base_salary):
        self.name = name
        self.age = age
        self.base_salary = base_salary
    
    def calculate_salary(self, months):
        """Calculate base salary over a specified number of months."""
        return months * self.base_salary
    
class Manager(Employee):
    role = "Manager"
    __HOUSE_RENT_PERCENT = 0.30
    __BONUS_PERCENT = 0.10

    def calculate_salary(self, months):
        """Calculate salary with house rent allowance and bonus for managers."""
        base_salary = super().calculate_salary(months)
        house_rent = self.base_salary * self.__HOUSE_RENT_PERCENT * months
        bonus = self.base_salary * self.__BONUS_PERCENT * months
        return base_salary + house_rent + bonus
    
class Developer(Employee):
    role = "Developer"
    __HOUSE_RENT_PERCENT = 0.30
    __BONUS_PERCENT = 0.10
    __UTILITY_PERCENT = 0.10

    def calculate_salary(self, months):
        """Calculate salary with house rent allowance, bonus, and utility allowance for developers."""
        base_salary = super().calculate_salary(months)
        house_rent = self.base_salary * self.__HOUSE_RENT_PERCENT * months
        bonus = self.base_salary * self.__BONUS_PERCENT * months
        utility = self.base_salary * self.__UTILITY_PERCENT * months
        return base_salary + house_rent + bonus + utility

# Example usage
m1 = Manager('Sifa', 27, 2000)
d1 = Developer('Farad', 28, 2000)
print(f"{m1.name}'s Salary for 6 months as {m1.role}:", m1.calculate_salary(6))
print(f"{d1.name}'s Salary for 6 months as {d1.role}:", d1.calculate_salary(6))
