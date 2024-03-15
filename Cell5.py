# Predict expenses for the test dataset
predictions = model.predict(X_test)

# Visualize results
plt.figure(figsize=(10, 6))
plt.scatter(y_test, predictions, color='blue')
plt.xlabel('Actual Expenses')
plt.ylabel('Predicted Expenses')
plt.title('Actual vs Predicted Expenses')
plt.show()
