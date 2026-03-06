from fastapi import FastAPI

app = FastAPI()

# Product list
products = [
    {"id": 1, "name": "Notebook", "price": 120, "category": "Stationery", "in_stock": True},
    {"id": 2, "name": "Pen Set", "price": 49, "category": "Stationery", "in_stock": True},
    {"id": 3, "name": "Wireless Mouse", "price": 799, "category": "Electronics", "in_stock": True},
    {"id": 4, "name": "USB Cable", "price": 199, "category": "Electronics", "in_stock": False},

    # Added products (Q1)
    {"id": 5, "name": "Laptop Stand", "price": 1299, "category": "Electronics", "in_stock": True},
    {"id": 6, "name": "Mechanical Keyboard", "price": 2499, "category": "Electronics", "in_stock": True},
    {"id": 7, "name": "Webcam", "price": 1899, "category": "Electronics", "in_stock": False},
]


# Home route
@app.get("/")
def home():
    return {"message": "FastAPI Assignment Running"}


# Q1 – Show all products
@app.get("/products")
def get_products():

    total_products = len(products)

    return {
        "products": products,
        "total": total_products
    }


# Q2 – Filter products by category
@app.get("/products/category/{category_name}")
def get_category(category_name: str):

    filtered_products = []

    for p in products:
        if p["category"].lower() == category_name.lower():
            filtered_products.append(p)

    if len(filtered_products) == 0:
        return {"error": "No products found in this category"}

    return {
        "category": category_name,
        "products": filtered_products,
        "total": len(filtered_products)
    }


# Q3 – Show only in-stock products
@app.get("/products/instock")
def get_instock():

    in_stock_products = []

    for p in products:
        if p["in_stock"] == True:
            in_stock_products.append(p)

    return {
        "in_stock_products": in_stock_products,
        "count": len(in_stock_products)
    }


# Q4 – Store summary
@app.get("/store/summary")
def store_summary():

    total_products = len(products)
    in_stock_count = 0
    out_stock_count = 0
    categories = []

    for p in products:

        if p["in_stock"] == True:
            in_stock_count += 1
        else:
            out_stock_count += 1

        if p["category"] not in categories:
            categories.append(p["category"])

    return {
        "store_name": "My E-commerce Store",
        "total_products": total_products,
        "in_stock": in_stock_count,
        "out_of_stock": out_stock_count,
        "categories": categories
    }


# Q5 – Search products by keyword
@app.get("/products/search/{keyword}")
def search_products(keyword: str):

    results = []

    for p in products:
        if keyword.lower() in p["name"].lower():
            results.append(p)

    if len(results) == 0:
        return {"message": "No products matched your search"}

    return {
        "keyword": keyword,
        "results": results,
        "total_matches": len(results)
    }


# Bonus – Cheapest and most expensive product
@app.get("/products/deals")
def product_deals():

    cheapest = products[0]
    expensive = products[0]

    for p in products:

        if p["price"] < cheapest["price"]:
            cheapest = p

        if p["price"] > expensive["price"]:
            expensive = p

    return {
        "best_deal": cheapest,
        "premium_pick": expensive
    }