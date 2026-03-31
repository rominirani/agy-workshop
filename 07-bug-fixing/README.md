# Project 07: Bug-Fixing (Inventory API)

This project is a back-end service for a coffee shop that calculates order totals, loyalty discounts, and item statistics. It is written entirely in **Python and Flask**.

## 🎯 Phased Troubleshooting

This project contains **3 intentional logic bugs**. Follow this order to fix them:

### **Phase 1: The Zero-Item Crash**

* **The Issue**: If an empty order is submitted, the server crashes with a `ZeroDivisionError`.
* **Reproduce**: Send a POST request to `/order` with `{"items": []}`.
* **Goal**: Ensure the "average price per item" calculation handles empty lists safely.

### **Phase 2: The Order Bleeding Bug**

* **The Issue**: If you make multiple requests, items from previous orders start appearing in new ones!
* **Reproduce**: Send an order with "Espresso". Then send a second order with "Latte". Notice that the second response mistakenly includes the Espresso price.
* **Goal**: Fix the mutable default argument in the `process_order` function.

### **Phase 3: The Discount Math Error**

* **The Issue**: The 10% loyalty discount is calculated incorrectly. Instead of taking 10% off the total, it just subtracts $0.10.
* **Reproduce**: Send an order for $10.00 with `is_loyal: true`. The total will be $9.90 instead of $9.00.
* **Goal**: Fix the math logic in the discount application.

---

## 🛠️ Setup

1. **Enter the directory**:

   ```bash
   cd 07-bug-fixing
   ```

2. **Set up venv**:

   ```bash
   python3 -m venv venv && source venv/bin/activate
   pip install -r requirements.txt
   ```

3. **Run the server**:

   ```bash
   python app.py
   ```

---

## ⚡ Recommended Prompts

"I'm working on Project 07. The Inventory API has three bugs: it crashes on empty orders, orders are 'bleeding' into each other, and the loyalty discount math is wrong. Can you help me fix `app.py`?"

