# from flask import Flask, render_template, request
# import pickle
# import numpy as np
# import sys, traceback

# app = Flask(__name__)
# try:
#     with open(r"D:\Appro_Project_1(image_classification)\prediction\house_Prediction\model\house.pickle","rb") as file:
#         model1 = pickle.load(file)
#     print("[INFO] Model loaded successfully.")
# except Exception as e:
#     print(f"[ERROR] Loading model failed: {e}")
#     model1 = None
# FEATURES = [
#     "area", "bedrooms", "bathrooms", "stories", "mainroad",
#     "guestroom", "basement", "hotwaterheating", "airconditioning", "parking",
#     "prefarea", "furnishingstatus"
# ]
# @app.route("/")
# def index():
#     return render_template("index.html")


# @app.route("/predict", methods=["POST"])
# def predict():
#     try:
#         print("\n====== /predict CALLED ======")
#         print("[RAW FORM] ->", request.form.to_dict())
#         d1 = int(request.form.get("area", 0))
#         d2 = int(request.form.get("bedrooms", 0))
#         d3 = int(request.form.get("bathrooms", 0))
#         d4 = int(request.form.get("stories", 0))
#         d5 = int(request.form.get("mainroad", 0))
#         d6 = int(request.form.get("guestroom", 0))              
#         d7 = int(request.form.get("basement", 0))
#         d8 = int(request.form.get("hotwaterheating", 0))
#         d9 = int(request.form.get("airconditioning", 0))
#         d10 = int(request.form.get("parking", 0))
#         d11 = int(request.form.get("prefarea", 0))
#         d12 = int(request.form.get("furnishingstatus", 0))
#         arr = np.array([[d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12]], dtype=float)

#         print("[ORDER ] ->", FEATURES)
#         print("[PARSED] ->", arr.tolist())
#         print("[SHAPE ] ->", arr.shape)
#         if model1:
#             # Check if model supports probability
#             proba, score = None, None
#             if hasattr(model1, "predict_proba"):
#                 proba = model1.predict_proba(arr)[0]
#                 print("[PROBA ] ->", proba)
#             if hasattr(model1, "decision_function"):
#                 score = model1.decision_function(arr)
#                 print("[DECISION] ->", score)

#             pred1 = model1.predict(arr)
#             risk = int(pred1[0])
#             print("[PRED  ] ->", risk)
#         else:
#             print("[WARN] Model not loaded, defaulting risk=0")
#             risk = 0
#         return render_template(
#             "result.html",
#             risk=risk,
#             features=FEATURES,
#             values=arr.tolist()[0],
#             proba=None if proba is None else [float(p) for p in proba],
#         )

#     except Exception as e:
#         print("[EXCEPTION]", e, file=sys.stderr)
#         traceback.print_exc()
#         return f"An error occurred: {e}", 500


# if __name__ == "__main__":
#     app.run(debug=True)


# from flask import Flask, render_template, request
# import pickle
# import numpy as np
# import sys, traceback

# # =========================================================
# # App Setup
# # =========================================================
# app = Flask(__name__)

# # Load model
# try:
#     with open(r"D:\Appro_Project_1(image_classification)\prediction\house_Prediction\model\house.pickle", "rb") as file:
#         model = pickle.load(file)
#         print("[INFO] Model loaded successfully.")
# except Exception as e:
#     print("[ERROR] Loading model failed:", e)
#     model = None

# # Features order
# FEATURES = [
#     "area", "bedrooms", "bathrooms", "stories", "mainroad",
#     "guestroom", "basement", "hotwaterheating", "airconditioning",
#     "parking", "prefarea", "furnishingstatus"
# ]

# # =========================================================
# # Helper Functions
# # =========================================================
# def yes_no(value):
#     """Convert yes/no to 1/0"""
#     return 1 if value and value.lower() == "yes" else 0

# def furnishing_status(value):
#     """Convert furnishingstatus string to numeric"""
#     if value == "furnished":
#         return 2
#     elif value == "semi-furnished":
#         return 1
#     return 0  # default = unfurnished

# # =========================================================
# # Routes
# # =========================================================
# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route("/predict", methods=["POST"])
# def predict():
#     try:
#         # Collect form data
#         d1 = int(request.form.get("area", 0))
#         d2 = int(request.form.get("bedrooms", 0))
#         d3 = int(request.form.get("bathrooms", 0))
#         d4 = int(request.form.get("stories", 0))
#         d5 = yes_no(request.form.get("mainroad"))
#         d6 = yes_no(request.form.get("guestroom"))
#         d7 = yes_no(request.form.get("basement"))
#         d8 = yes_no(request.form.get("hotwaterheating"))
#         d9 = yes_no(request.form.get("airconditioning"))
#         d10 = int(request.form.get("parking", 0))
#         d11 = yes_no(request.form.get("prefarea"))
#         d12 = furnishing_status(request.form.get("furnishingstatus"))

#         arr = np.array([[d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12]], dtype=float)

#         print("Order:", FEATURES)
#         print("Input:", arr)

#         if model:
#             prediction = model.predict(arr)[0]  # 1 = high price, 0 = low price
#         else:
#             prediction = 0  # fallback

#         return render_template("result.html", prediction=prediction)

#     except Exception as e:
#         print("[EXCEPTION]", e, file=sys.stderr)
#         traceback.print_exc()
#         return f"An error occurred: {e}", 500

# # =========================================================
# # Run App
# # =========================================================
# if __name__ == "__main__":
#     app.run(debug=True)


# from flask import Flask, render_template, request
# import pickle
# import numpy as np
# import sys, traceback

# # =========================================================
# # App Setup
# # =========================================================
# app = Flask(__name__)

# # Load trained regression model
# try:
#     with open(r"D:\Appro_Project_1(image_classification)\prediction\house_Prediction\model\house.pickle", "rb") as file:
#         model = pickle.load(file)
#         print("[INFO] Model loaded successfully.")
# except Exception as e:
#     print("[ERROR] Loading model failed:", e)
#     model = None

# # =========================================================
# # Helper Functions
# # =========================================================
# def yes_no(value):
#     """Convert yes/no to 1/0"""
#     return 1 if value and value.lower() == "yes" else 0

# def furnishing_status(value):
#     """Convert furnishingstatus string to numeric"""
#     if value == "furnished":
#         return 2
#     elif value == "semi-furnished":
#         return 1
#     return 0  # unfurnished

# # =========================================================
# # Routes
# # =========================================================
# @app.route("/")
# def index():
#     return render_template("index.html")

# @app.route("/predict", methods=["POST"])
# def predict():
#     try:
#         # Collect form data
#         d1 = int(request.form.get("area", 0))
#         d2 = int(request.form.get("bedrooms", 0))
#         d3 = int(request.form.get("bathrooms", 0))
#         d4 = int(request.form.get("stories", 0))
#         d5 = yes_no(request.form.get("mainroad"))
#         d6 = yes_no(request.form.get("guestroom"))
#         d7 = yes_no(request.form.get("basement"))
#         d8 = yes_no(request.form.get("hotwaterheating"))
#         d9 = yes_no(request.form.get("airconditioning"))
#         d10 = int(request.form.get("parking", 0))
#         d11 = yes_no(request.form.get("prefarea"))
#         d12 = furnishing_status(request.form.get("furnishingstatus"))

#         # Create input array
#         arr = np.array([[d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12]], dtype=float)
#         print("Input Array:", arr)

#         # Predict house price
#         if model:
#             prediction = model.predict(arr)[0]
#             prediction = round(prediction, 2)  # round to 2 decimal places
#         else:
#             prediction = 0.0

#         return render_template("result.html", prediction=prediction)

#     except Exception as e:
#         print("[EXCEPTION]", e, file=sys.stderr)
#         traceback.print_exc()
#         return f"An error occurred: {e}", 500

# # =========================================================
# # Run App
# # =========================================================
# if __name__ == "__main__":
#     app.run(debug=True)

# app.py
from flask import Flask, render_template, request
import pickle
import numpy as np
import sys, traceback
app = Flask(__name__)
try:
    with open(r"D:\Appro_Project_1(image_classification)\prediction\house_Prediction\model\house.pickle", "rb") as file:
        model = pickle.load(file)
        print("[INFO] Model loaded successfully.")
except Exception as e:
    print("[ERROR] Model loading failed:", e)
    model = None
def yes_no(value):
    """Convert yes/no to 1/0"""
    if not value:
        return 0
    return 1 if value.lower() == "yes" else 0
def furnishing_status(value):
    """Convert furnishingstatus string to numeric"""
    if not value:
        return 0
    value = value.lower()
    if value == "furnished":
        return 2
    elif value == "semi-furnished":
        return 1
    return 0  # unfurnished or missing
@app.route("/")
def index():
    return render_template("index.html")
@app.route("/predict", methods=["POST"])
def predict():
    try:
        d1 = float(request.form.get("area", 0))
        d2 = int(request.form.get("bedrooms", 0))
        d3 = int(request.form.get("bathrooms", 0))
        d4 = int(request.form.get("stories", 0))
        d5 = yes_no(request.form.get("mainroad"))
        d6 = yes_no(request.form.get("guestroom"))
        d7 = yes_no(request.form.get("basement"))
        d8 = yes_no(request.form.get("hotwaterheating"))
        d9 = yes_no(request.form.get("airconditioning"))
        d10 = int(request.form.get("parking", 0))
        d11 = yes_no(request.form.get("prefarea"))
        d12 = furnishing_status(request.form.get("furnishingstatus"))
        arr = np.array([[d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12]], dtype=float)
        print("Input Array:", arr)
        if model:
            prediction = model.predict(arr)[0]
            prediction = round(float(prediction), 2)  # ensure float, round to 2 decimals
        else:
            prediction = None
        return render_template("result.html", prediction=prediction)
    except Exception as e:
        print("[EXCEPTION]", e, file=sys.stderr)
        traceback.print_exc()
        return render_template("result.html", prediction=None, error=str(e))
if __name__ == "__main__":
    app.run(debug=True)
