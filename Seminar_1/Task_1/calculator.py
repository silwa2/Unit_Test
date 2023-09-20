
def calculate(first_operand: int, second_operand: int, operator: str) -> int | float:
    match operator:
        case '+':
            result = first_operand + second_operand
        case '-':
            result = first_operand - second_operand
        case '*':
            result = first_operand * second_operand
        case '/':
            if second_operand != 0:
                result = first_operand / second_operand
            else:
                raise ArithmeticError("Деление на ноль невозможно")
        case _:
            raise ValueError("Оператор с неправильным значением: " + operator)
    return result


def calculate_discount(purchase_amount: float, discount_amount: int) -> float:
    if discount_amount < 0:
        raise ArithmeticError("Скидка не может быть меньше нуля")
    elif discount_amount > 100:
        raise ArithmeticError("Скидка не может быть больше 100")

    return purchase_amount - discount_amount / 100 * purchase_amount