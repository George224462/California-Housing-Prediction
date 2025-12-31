{
  "metadata": {
    "kernelspec": {
      "name": "xpython",
      "display_name": "Python 3.13 (XPython)",
      "language": "python"
    },
    "language_info": {
      "file_extension": ".py",
      "mimetype": "text/x-python",
      "name": "python",
      "version": "3.13.1"
    }
  },
  "nbformat_minor": 5,
  "nbformat": 4,
  "cells": [
    {
      "id": "9f0b4138-9508-49f7-b622-9f6d6851ab44",
      "cell_type": "code",
      "source": "import pandas as pd\nimport numpy as np\nfrom sklearn.datasets import fetch_california_housing\nfrom sklearn.model_selection import train_test_split\nfrom sklearn.preprocessing import StandardScaler\nfrom sklearn.linear_model import LinearRegression\nfrom sklearn.metrics import mean_squared_error, r2_score\n\n# 1. LOAD: Getting our \"LEGO bricks\"\nhousing = fetch_california_housing()\nX = pd.DataFrame(housing.data, columns=housing.feature_names)\ny = housing.target # Price in $100,000s\n\n# 2. SPLIT: Setting aside the \"Final Exam\" (X_test)\nX_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n\n# 3. SCALE: Making sure all numbers \"speak the same language\"\nscaler = StandardScaler()\nX_train_scaled = scaler.fit_transform(X_train)\nX_test_scaled = scaler.transform(X_test)\n\n# 4. TRAIN: Let the computer find the best line\nmodel = LinearRegression()\nmodel.fit(X_train_scaled, y_train)\n\n# 5. PREDICT & EVALUATE: How did we do?\npredictions = model.predict(X_test_scaled)\nmse = mean_squared_error(y_test, predictions)\nr2 = r2_score(y_test, predictions)\n\nprint(f\"Mean Squared Error: {mse:.4f}\")\nprint(f\"R-squared Score (Accuracy): {r2:.4f}\")",
      "metadata": {
        "trusted": true
      },
      "outputs": [
        {
          "ename": "<class 'ModuleNotFoundError'>",
          "evalue": "No module named 'pandas'",
          "traceback": [
            "\u001b[31m---------------------------------------------------------------------------\u001b[39m",
            "\u001b[31mModuleNotFoundError\u001b[39m                       Traceback (most recent call last)",
            "\u001b[36mCell\u001b[39m\u001b[36m \u001b[39m\u001b[32mIn[1]\u001b[39m\u001b[32m, line 1\u001b[39m\n\u001b[32m----> \u001b[39m\u001b[32m1\u001b[39m \u001b[38;5;28;01mimport\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mpandas\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mas\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mpd\u001b[39;00m\n\u001b[32m      2\u001b[39m \u001b[38;5;28;01mimport\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mnumpy\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mas\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01mnp\u001b[39;00m\n\u001b[32m      3\u001b[39m \u001b[38;5;28;01mfrom\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[34;01msklearn\u001b[39;00m\u001b[34;01m.\u001b[39;00m\u001b[34;01mdatasets\u001b[39;00m\u001b[38;5;250m \u001b[39m\u001b[38;5;28;01mimport\u001b[39;00m fetch_california_housing\n",
            "\u001b[31mModuleNotFoundError\u001b[39m: No module named 'pandas'"
          ],
          "output_type": "error"
        }
      ],
      "execution_count": 1
    },
    {
      "id": "97c87419-c353-4255-b0cf-2666e40bd85e",
      "cell_type": "code",
      "source": "",
      "metadata": {
        "trusted": true
      },
      "outputs": [],
      "execution_count": null
    }
  ]
}