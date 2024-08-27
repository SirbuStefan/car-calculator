import calculator

if __name__ == '__main__':
    calc = calculator.Calculator()
    calc.add_car(calculator.Car("Toyota Corolla", 7000, 1.70, 450, 500))
    calc.add_car(calculator.Car("Mazda CX-7", 7000, 1.70, 300, 500))
    calc.add_car(calculator.Car("Volvo v40", 7000, 1.70, 250, 500))
    calc.add_car(calculator.Car("Ford Focus", 7000, 1.70, 240, 500))

    calc.print_cars()