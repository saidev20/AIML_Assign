from surprise import SVD, Dataset                         
from surprise.model_selection import train_test_split
from surprise import accuracy
data = Dataset.load_builtin('ml-100k')
train, test = train_test_split(data, test_size=0.2)
model = SVD()
model.fit(train)
pred = model.test(test)
rmse = accuracy.rmse(pred, verbose=False)
mae = accuracy.mae(pred, verbose=False)
print(f"\nRMSE={rmse:.4f}, MAE={mae:.4f}")
errs = sorted([(abs(p.r_ui - p.est), p) for p in pred], reverse=True)
print("\nWorst 5:")
for e, p in errs[:5]:
    print(f"U{p.uid}-I{p.iid} | T={p.r_ui} P={p.est:.3f} | Err={e:.3f}")
print("\nBest 5:")
for e, p in errs[-5:]:
    print(f"U{p.uid}-I{p.iid} | T={p.r_ui} P={p.est:.3f} | Err={e:.3f}")
print("\nSample 10:")
for p in pred[:10]:
    print(f"U{p.uid}, I{p.iid}, T={p.r_ui}, P={p.est:.3f}")
abs_errs = [abs(p.r_ui - p.est) for p in pred]
print("\nAvg Err=", sum(abs_errs)/len(abs_errs))
print("Max Err=", max(abs_errs))
print("Min Err=", min(abs_errs))
