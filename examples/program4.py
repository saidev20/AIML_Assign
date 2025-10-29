from sklearn.datasets import load_iris                            
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
iris = load_iris()
X = iris.data
y = iris.target
names = iris.target_names
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1)
knn = KNeighborsClassifier(n_neighbors=3)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)
correct = []
wrong = []
for i in range(len(y_test)):
    if y_test[i] == y_pred[i]:
        correct.append((i, y_test[i], y_pred[i]))
    else:
        wrong.append((i, y_test[i], y_pred[i]))
print("Correct Predictions:")
for idx, true, pred in correct:
    print(f"Index {idx}: True = {names[true]}, Predicted = {names[pred]}")
print("\nWrong Predictions:")
for idx, true, pred in wrong:
    print(f"Index {idx}: True = {names[true]}, Predicted = {names[pred]}")
print(f"\nTotal Correct: {len(correct)}")
print(f"Total Wrong: {len(wrong)}")


