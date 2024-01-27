# Moroccan Traditional Food Restaurant Order Calculator

**Note:** As of the latest update, the prices for Moroccan traditional dishes have been refreshed!

## Overview

Moroccan Traditional Food Restaurant Order Calculator is a Python program, implemented in the `moroccan_order.py` file, designed for streamlined ordering at a Moroccan traditional food restaurant. Users can input dishes one at a time until the order is complete, and the program displays the total cost after each item. The order can be finalized by inputting control-d. User input is case-insensitive, and any non-menu input is disregarded.

## Menu

```python
{
    "Couscous": 4.25,
    "Rfissa": 7.50,
    "Tajin Kefta": 8.50,
    "Tajin Djjaj": 11.00,
    "Pastilla": 8.50,
    "Mrouzia": 8.50,
    "Harira": 9.50,
    "Merguez": 3.00,
    "Maaqouda": 8.00
}
```

## How to Use

1. Run the program by executing `python moroccan_order.py`.
2. Input Moroccan traditional dishes one at a time, and the program will display the total cost after each item.
3. Continue adding items until you input control-d to signal the end of your order.

## How to Test

Manually test your code using the following steps:

1. Run your program with `python moroccan_order.py`.
2. Input Moroccan traditional dishes and verify that the program correctly displays the total cost after each item.
3. Test different food items and casing variations, ensuring that the program behaves as expected in a case-insensitive manner.

Example:

```bash
$ python moroccan_order.py
Mrouzia
Total Cost: $8.50
Harira
Total Cost: $18.00
^D
```

```bash
$ python moroccan_order.py
Couscous
Total Cost: $4.25
Tajin Kefta
Total Cost: $12.75
^D
```

```bash
$ python moroccan_order.py
Pizza
(Pizza is not on the menu, program reprompts)
```

Ensure to test the program using the provided check50 command for additional verification.

Enjoy your Moroccan culinary experience with the Moroccan Traditional Food Restaurant Order Calculator!
